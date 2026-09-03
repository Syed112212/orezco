# -*- coding: utf-8 -*-
"""Pone al dia la barra, el pie y su CSS en index.html.

    python scripts/sync-portada.py

La portada se escribe a mano porque tiene piezas que no comparte nadie
-el fondo en canvas, la maqueta del asistente, la pila de modulos-, pero
su menu tiene que ser el mismo que el de las otras 37 paginas. Antes era
una copia, y una copia se separa: se anade una pagina al menu, se
regenera el sitio y la portada se queda con el menu de ayer.

Esto lo resuelve reescribiendo esos trozos desde plantilla.py cada vez.
Se puede ejecutar tantas veces como haga falta: siempre deja lo mismo.
"""
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)
import plantilla as P

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ABRE_CSS = "/* === barra y pie: los reescribe scripts/sync-portada.py === */"
CIERRA_CSS = "/* === fin de barra y pie === */"


def trozo_de_estilos(desde, hasta):
    m = re.search(re.escape(desde) + r"(.*?)" + re.escape(hasta), P.ESTILOS, re.S)
    assert m, "no encontrado el trozo '%s' en plantilla.ESTILOS" % desde[:30]
    return m.group(0)[:-len(hasta)].rstrip() if hasta else m.group(0)


def main():
    ruta = os.path.join(RAIZ, "index.html")
    t = io.open(ruta, encoding="utf-8").read()
    antes = t

    # ── el marcado ───────────────────────────────────────────────────
    # El lienzo del fondo viene dentro de la cabecera comun. Si ya hay uno
    # de una pasada anterior hay que quitarlo antes: dos elementos con el
    # mismo id son HTML invalido, y el JavaScript solo encuentra el primero.
    t = re.sub(r"<!-- El mismo fondo que la portada.*?\n", "", t, flags=re.S)
    t = t.replace('<canvas class="fondo" id="fondo" aria-hidden="true"></canvas>\n', "")

    m = re.search(r'<nav class="nav" aria-label="Principal">.*?\n</nav>', t, re.S)
    assert m, "no encontrada la barra en index.html"
    t = t[:m.start()] + P.cabecera("").split("\n", 1)[1] + t[m.end():]

    m = re.search(r"<footer>.*?\n</footer>", t, re.S)
    assert m, "no encontrado el pie en index.html"
    t = t[:m.start()] + P.pie("") + t[m.end():]

    # El CSS ya no se copia: la portada enlaza assets/contaes.css como
    # el resto del sitio. Copiarlo es lo que provoco tres veces el mismo
    # fallo mudo, una clase declarada dos veces.
    version = 'href="/assets/contaes.css?v=%s"' % P.version_hoja()
    t = re.sub(r'href="/assets/contaes\.css\?v=[a-f0-9]*"', version, t)

    # ── el JS del menu ───────────────────────────────────────────────
    nuevo_js = re.search(r"(/\* -- El menu: por areas en escritorio.*?\n\}\)\(\);\n)", P.PIE_JS, re.S).group(1)
    m = re.search(r"/\* -- El menu: por areas en escritorio.*?\n\}\)\(\);\n", t, re.S)
    assert m, "no encontrado el JS del menu en index.html"
    t = t[:m.start()] + nuevo_js + t[m.end():]

    io.open(ruta, "w", encoding="utf-8").write(t)
    print("  index.html: barra, pie y su CSS al dia" + ("" if t != antes else " (ya estaban)"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
