# -*- coding: utf-8 -*-
"""Abre las paginas en un navegador de verdad y mide lo que solo se ve ahi.

    python scripts/check-render.py            todas las paginas
    python scripts/check-render.py index.html gestoria/index.html

check-design.py lee el CSS y check-voz.py lee el texto. Ninguno de los dos
ve lo que pasa cuando el navegador junta las dos cosas y monta la pagina.
Esto si:

  - Desbordamiento horizontal. El body recorta a lo ancho, asi que un
    desbordamiento no ensena barra: se mide el ancho real del documento.
  - Contenido invisible. Un elemento con opacidad cero que nunca vuelve.
    Paso de verdad, y lo encontro el cliente mirando la web.
  - Errores de JavaScript, ids repetidos, saltos de nivel de titulo,
    enlaces sin texto, campos sin etiqueta e imagenes sin alternativa.

Importante: NO se congelan las animaciones. Congelarlas en su estado final
hace la captura estable y esconde justo lo que nunca llega a empezar.
"""
import http.server
import io
import json
import os
import re
import shutil
import socketserver
import subprocess
import sys
import tempfile
import threading

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUERTO = 8811
ANCHOS = [(1360, 900, "escritorio"), (390, 900, "movil")]

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def busca_chrome():
    candidatos = [
        os.environ.get("CHROME"),
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        "/usr/bin/google-chrome", "/usr/bin/chromium-browser", "/usr/bin/chromium",
    ]
    for c in candidatos:
        if c and os.path.exists(c):
            return c
    for c in ("google-chrome", "chromium", "chrome"):
        r = shutil.which(c)
        if r:
            return r
    return None


SONDA = """
<script>
window.addEventListener("load", function () {
  var y = 0;
  var paso = setInterval(function () {
    y += window.innerHeight * 0.7;
    window.scrollTo(0, y);
    if (y > document.body.scrollHeight) {
      clearInterval(paso);
      window.scrollTo(0, 0);
      setTimeout(mide, 3200);
    }
  }, 70);

  function nombre(e) {
    var c = e.className;
    c = (c && c.baseVal !== undefined ? c.baseVal : c || "").toString().split(" ")[0];
    return e.tagName.toLowerCase() + (c ? "." + c : "");
  }

  function mide() {
    var r = {desborde: null, invisibles: [], ids: [], h1: 0, orden: [],
             vacios: [], campos: [], img: []};

    var de = document.documentElement;
    if (de.scrollWidth > de.clientWidth + 1) {
      var fuera = [];
      var todos = document.querySelectorAll("body, body *");
      for (var i = 0; i < todos.length; i++) {
        var e = todos[i], b = e.getBoundingClientRect();
        if (!b.width && !b.height) continue;
        if (b.right <= de.clientWidth + 1) continue;
        var recortado = false, p = e.parentElement;
        while (p) {
          if (getComputedStyle(p).overflowX !== "visible") { recortado = true; break; }
          p = p.parentElement;
        }
        if (!recortado) fuera.push(nombre(e) + " hasta " + Math.round(b.right));
      }
      r.desborde = de.scrollWidth + " > " + de.clientWidth +
                   (fuera.length ? " por " + fuera.slice(0, 3).join(", ") : "");
    }

    var leibles = document.querySelectorAll(
      "main h1,main h2,main h3,main p,main li,main article,main .tarjeta,main .mod,main .hito");
    for (var j = 0; j < leibles.length; j++) {
      var el = leibles[j], cs = getComputedStyle(el);
      if (cs.display === "none" || cs.visibility === "hidden") continue;
      var caja = el.getBoundingClientRect();
      if (!caja.width && !caja.height) continue;
      if (parseFloat(cs.opacity) >= 0.15) continue;
      // Invisible no basta: lo que importa es que nada lo vaya a cambiar.
      // Un elemento a mitad de su animacion de entrada esta invisible ahora
      // y visible en un segundo. Uno sin ninguna animacion viva se queda
      // asi para siempre, y ese es el fallo.
      var vivas = el.getAnimations ? el.getAnimations().filter(function (a) {
        return a.playState === "running" || a.playState === "pending";
      }) : [];
      var padre = el.parentElement, heredada = false;
      while (padre && !heredada) {
        if (padre.getAnimations && padre.getAnimations().some(function (a) {
              return a.playState === "running" || a.playState === "pending";
            })) heredada = true;
        padre = padre.parentElement;
      }
      if (!vivas.length && !heredada) {
        r.invisibles.push(nombre(el) + " [" + (el.textContent || "").trim().slice(0, 22) + "]");
      }
    }

    var vistos = {}, conId = document.querySelectorAll("[id]");
    for (var k = 0; k < conId.length; k++) {
      if (vistos[conId[k].id] && r.ids.indexOf(conId[k].id) < 0) r.ids.push(conId[k].id);
      vistos[conId[k].id] = 1;
    }

    var tit = document.querySelectorAll("main h1,main h2,main h3,main h4,main h5,main h6");
    var previo = 0;
    for (var m = 0; m < tit.length; m++) {
      var n = +tit[m].tagName[1];
      if (n === 1) r.h1++;
      if (previo && n > previo + 1)
        r.orden.push("h" + previo + " -> h" + n + ": " + tit[m].textContent.trim().slice(0, 26));
      previo = n;
    }

    var as = document.querySelectorAll("a");
    for (var q = 0; q < as.length; q++) {
      var texto = (as[q].textContent || "").trim() || as[q].getAttribute("aria-label") || "";
      if (!texto && !as[q].querySelector("img,svg")) r.vacios.push(as[q].getAttribute("href") || "?");
    }

    var campos = document.querySelectorAll("input:not([type=hidden]),textarea,select");
    for (var s = 0; s < campos.length; s++) {
      var c2 = campos[s];
      if (c2.getAttribute("aria-hidden") === "true") continue;
      var tiene = c2.closest("label") || (c2.id && document.querySelector('label[for="' + c2.id + '"]'))
                  || c2.getAttribute("aria-label") || c2.getAttribute("aria-labelledby");
      if (!tiene) r.campos.push(c2.name || c2.type);
    }

    var imgs = document.querySelectorAll("img");
    for (var v = 0; v < imgs.length; v++)
      if (imgs[v].getAttribute("alt") === null) r.img.push(imgs[v].src.slice(-32));

    console.log("RENDER " + JSON.stringify(r));
  }
});
</script>
"""


# Una pagina de cada clase. Abrir las ciento y pico en dos anchos son
# veinte minutos, y las paginas de la misma plantilla fallan igual: si se
# rompe una de servicio, se rompen las treinta.
MUESTRA = [
    "/index.html", "/404.html", "/demo/index.html", "/gracias/index.html",
    "/gestoria/index.html", "/gestoria/fiscal/index.html",
    "/crecimiento/index.html", "/crecimiento/financiacion/index.html",
    "/para/index.html", "/para/pymes/index.html",
    "/funcionalidades/index.html", "/funcionalidades/contabilidad/index.html",
    "/sectores/index.html", "/sectores/construccion/index.html",
    "/blog/index.html", "/glosario/index.html", "/calendario-fiscal/index.html",
    "/preguntas/index.html", "/precios/index.html", "/legal/privacidad/index.html",
]


def paginas_de(raiz, pedidas):
    if pedidas == ["--muestra"]:
        return [p for p in MUESTRA if os.path.exists(os.path.join(raiz, p.lstrip("/")))]
    if pedidas:
        return ["/" + p.lstrip("/").replace(os.sep, "/") for p in pedidas]
    saltar = {".git", "scripts", "assets", ".github"}
    salida = []
    for base, dirs, ficheros in os.walk(raiz):
        dirs[:] = [d for d in dirs if d not in saltar]
        for f in ficheros:
            if f.endswith(".html") and not f.startswith("google"):
                salida.append("/" + os.path.relpath(os.path.join(base, f), raiz).replace(os.sep, "/"))
    return sorted(salida)


def main():
    chrome = busca_chrome()
    if not chrome:
        print("No hay Chrome disponible: no se puede comprobar el renderizado.")
        return 0

    objetivo = paginas_de(RAIZ, sys.argv[1:])
    copia = tempfile.mkdtemp(prefix="contaes-render-")
    try:
        shutil.copytree(RAIZ, copia, dirs_exist_ok=True,
                        ignore=shutil.ignore_patterns(".git", "scripts", ".github", "*.md"))
        for base, _d, ficheros in os.walk(copia):
            for f in ficheros:
                if f.endswith(".html"):
                    r = os.path.join(base, f)
                    s = io.open(r, encoding="utf-8", errors="replace").read()
                    io.open(r, "w", encoding="utf-8").write(s.replace("</body>", SONDA + "</body>"))

        class Silencioso(http.server.SimpleHTTPRequestHandler):
            def __init__(self, *a, **kw):
                super().__init__(*a, directory=copia, **kw)

            def log_message(self, *a):
                pass

        srv = socketserver.TCPServer(("127.0.0.1", PUERTO), Silencioso)
        threading.Thread(target=srv.serve_forever, daemon=True).start()

        fallos, avisos = [], []
        for ancho, alto, etiqueta in ANCHOS:
            for pag in objetivo:
                p = subprocess.run(
                    [chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                     "--no-sandbox", "--enable-logging=stderr", "--v=0",
                     "--virtual-time-budget=22000", "--window-size=%d,%d" % (ancho, alto),
                     "--dump-dom", "http://127.0.0.1:%d%s" % (PUERTO, pag)],
                    capture_output=True, text=True, errors="replace")
                err = p.stderr or ""
                donde = "%s (%s)" % (pag, etiqueta)

                for l in err.splitlines():
                    if "Uncaught" in l or "SyntaxError" in l:
                        fallos.append((donde, "JavaScript: " + l.split("] ", 1)[-1][:90]))
                        break

                datos = None
                for l in err.splitlines():
                    m = re.search(r"RENDER (\{.*\})", l)
                    if m:
                        try:
                            datos = json.loads(m.group(1))
                        except Exception:
                            pass
                if datos is None:
                    continue

                if datos["desborde"]:
                    fallos.append((donde, "se sale a lo ancho: " + datos["desborde"][:90]))
                if datos["invisibles"]:
                    fallos.append((donde, "contenido invisible: %d (%s)"
                                   % (len(datos["invisibles"]), datos["invisibles"][0][:50])))
                if datos["ids"]:
                    fallos.append((donde, "ids repetidos: " + ", ".join(datos["ids"][:3])))
                if datos["h1"] != 1:
                    avisos.append((donde, "h1 = %d" % datos["h1"]))
                if datos["orden"]:
                    avisos.append((donde, "salto de titulo: " + datos["orden"][0]))
                if datos["vacios"]:
                    avisos.append((donde, "enlaces sin texto: %d" % len(datos["vacios"])))
                if datos["campos"]:
                    avisos.append((donde, "campos sin etiqueta: " + ", ".join(datos["campos"][:3])))
                if datos["img"]:
                    avisos.append((donde, "imagenes sin alt: %d" % len(datos["img"])))

        srv.shutdown()
    finally:
        shutil.rmtree(copia, ignore_errors=True)

    print("Renderizado: lo que solo se ve en un navegador")
    print("=" * 62)
    print("  %d paginas x %d anchos" % (len(objetivo), len(ANCHOS)))
    for d, m in fallos:
        print("FALLO  %-34s %s" % (d[:34], m))
    for d, m in avisos[:20]:
        print("aviso  %-34s %s" % (d[:34], m))
    if len(avisos) > 20:
        print("       ... y %d avisos mas" % (len(avisos) - 20))
    print("=" * 62)
    print("%d fallo(s), %d aviso(s)" % (len(fallos), len(avisos)))
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
