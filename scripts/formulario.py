# -*- coding: utf-8 -*-
"""El formulario, en un solo sitio: la portada y /demo/ usan este.

Dos decisiones que lo gobiernan:

1. Se rellena pinchando. Escribir en una web cuesta, y un campo de texto
   vacio delante es la forma mas rapida de perder a alguien. Solo se teclea
   lo que no se puede elegir de una lista: el nombre y la forma de
   contacto. Todo lo demas son opciones.

2. Lo que se pregunta sirve para preparar la llamada, no para rellenar un
   informe. Que eres, que necesitas, cuantos sois, que usas hoy y cuando
   quieres empezar. Con eso ya se puede hablar de un numero concreto en
   vez de un rango.

Un sitio estatico no puede guardar nada: hace falta algo que reciba el
envio. Se usa FormSubmit, que lo reenvia al buzon sin cuenta ni servidor
propio. Consecuencias que hay que asumir y contar: los envios pasan por un
tercero (aparece en la politica de privacidad) y el primer envio dispara
un correo de activacion al buzon.
"""

BUZON = "info@contaes.com"
ENDPOINT = "https://formsubmit.co/" + BUZON
GRACIAS = "https://contaes.com/gracias/"
TELEFONO = "+34 666 02 95 59"
TELEFONO_TEL = "+34666029559"

# El nombre del campo trampa lo fija FormSubmit: los robots rellenan todo
# lo que ven, las personas no ven este porque esta oculto.
TRAMPA = "_honey"

# ─────────────────────────────────────────────────────────────────────
# Lo que se pregunta. Cambiar aqui cambia la portada y /demo/ a la vez.
# ─────────────────────────────────────────────────────────────────────
PERFIL = [
    ("Autónomo", "Trabajo por mi cuenta"),
    ("Startup", "Empresa joven, buscando crecer"),
    ("Pyme", "Empresa con equipo"),
    ("Aún no tengo empresa", "Quiero montarla"),
]

EQUIPO = ["Solo yo", "2 a 5", "6 a 15", "16 a 50", "Más de 50"]

NECESITO = [
    ("La gestoría", [
        "Contabilidad",
        "Impuestos y modelos",
        "Nóminas y laboral",
        "Legal y contratos",
    ]),
    ("El software", [
        "Facturación",
        "Inventario y almacén",
        "Compras y proveedores",
        "Ventas y clientes",
        "Proyectos y horas",
        "Informes",
    ]),
    ("Crecer", [
        "Dirección financiera",
        "Marketing",
        "Captación de clientes",
        "Bot de llamadas y WhatsApp",
        "Financiación y subvenciones",
        "Vender fuera de España",
    ]),
]

AHORA = ["Una gestoría", "Hojas de cálculo", "Un ERP (Odoo, SAP, Sage...)",
         "Un programa de facturación", "Nada todavía"]

CUANDO = ["Cuanto antes", "Este trimestre", "Aún estoy mirando"]


def _grupo(nombre, campo, opciones, tipo="radio", pies=None):
    """Un bloque de opciones que se elige pinchando."""
    filas = []
    for i, o in enumerate(opciones):
        pie = ('<span class="op-pie">%s</span>' % pies[i]) if pies else ""
        filas.append(
            '        <label class="op">'
            '<input type="%s" name="%s" value="%s">'
            '<span class="op-cuerpo"><span class="op-tit">%s</span>%s</span>'
            '</label>' % (tipo, campo, o.replace('"', "'"), o, pie))
    return ('      <fieldset class="bloque">\n'
            '        <legend>%s</legend>\n%s\n      </fieldset>\n'
            % (nombre, "\n".join(filas)))


def campos_ocultos(asunto):
    return (
        '      <input type="hidden" name="_subject" value="%s">\n'
        '      <input type="hidden" name="_next" value="%s">\n'
        '      <input type="hidden" name="_template" value="table">\n'
        '      <input type="hidden" name="_captcha" value="false">\n'
        '      <input type="text" name="%s" tabindex="-1" autocomplete="off" aria-hidden="true"\n'
        '             style="position:absolute;left:-9999px;width:1px;height:1px;opacity:0">\n'
        % (asunto, GRACIAS, TRAMPA)
    )



# ═════════════════════════════════════════════════════════════════════
# De donde sale cada envio
# ═════════════════════════════════════════════════════════════════════
# Los rellena el navegador antes de enviar. Si el visitante lleva el
# JavaScript apagado se quedan vacios y el formulario funciona igual:
# el rastro es util, no imprescindible.
RASTRO = [
    ("Origen: primera pagina", "origen_primera"),
    ("Origen: quien le trajo", "origen_referente"),
    ("Origen: primera visita", "origen_fecha"),
    ("Campana: source", "utm_source"),
    ("Campana: medium", "utm_medium"),
    ("Campana: campaign", "utm_campaign"),
    ("Campana: term", "utm_term"),
    ("Campana: content", "utm_content"),
    ("Campana: gclid", "gclid"),
    ("Envio: pagina", "envio_pagina"),
    ("Envio: fecha", "envio_fecha"),
    ("Envio: paginas vistas", "envio_vistas"),
    ("Contexto: aparato", "ctx_aparato"),
    ("Contexto: pantalla", "ctx_pantalla"),
    ("Contexto: idioma", "ctx_idioma"),
    ("Contexto: tiempo de relleno", "ctx_tiempo"),
]


def campos_rastro():
    return "".join(
        '      <input type="hidden" name="%s" data-rastro="%s" value="">\n' % (n, clave)
        for n, clave in RASTRO)

def cuerpo(asunto):
    """El formulario entero, sin la etiqueta <form>."""
    partes = [campos_ocultos(asunto), campos_rastro()]

    partes.append(_grupo("¿Qué eres?", "Perfil", [p for p, _d in PERFIL],
                         pies=[d for _p, d in PERFIL]))
    partes.append(_grupo("¿Cuántos sois?", "Equipo", EQUIPO))

    # las necesidades van por areas, porque marcar quince casillas seguidas
    # cansa y agrupadas se leen de un vistazo
    bloques = []
    for area, opciones in NECESITO:
        filas = "\n".join(
            '          <label class="op op-chica"><input type="checkbox" name="Necesita: %s" '
            'value="%s"><span class="op-cuerpo"><span class="op-tit">%s</span></span></label>'
            % (area, o, o) for o in opciones)
        bloques.append('        <div class="sub">\n'
                       '          <p class="sub-tit">%s</p>\n%s\n        </div>' % (area, filas))
    partes.append('      <fieldset class="bloque">\n'
                  '        <legend>¿Con qué te podemos ayudar?</legend>\n'
                  '        <p class="bloque-pie">Marca lo que te suene. No hace falta acertar: '
                  'para eso está la llamada.</p>\n'
                  '        <div class="subs">\n%s\n        </div>\n      </fieldset>\n'
                  % "\n".join(bloques))

    partes.append(_grupo("¿Qué usas hoy?", "Sistema actual", AHORA))
    partes.append(_grupo("¿Para cuándo?", "Plazo", CUANDO))

    partes.append('''      <fieldset class="bloque">
        <legend>¿Cómo te llamamos?</legend>
        <div class="datos">
          <label class="dato"><span>Nombre</span>
            <input type="text" name="Nombre" autocomplete="name" required></label>
          <label class="dato"><span>Empresa <i>(opcional)</i></span>
            <input type="text" name="Empresa" autocomplete="organization"></label>
          <label class="dato"><span>Email</span>
            <input type="email" name="Email" autocomplete="email" required></label>
          <label class="dato"><span>Teléfono <i>(opcional)</i></span>
            <input type="tel" name="Teléfono" autocomplete="tel"></label>
        </div>
        <label class="dato dato-ancho"><span>¿Algo más que debamos saber? <i>(opcional)</i></span>
          <textarea name="Mensaje" rows="3"></textarea></label>
      </fieldset>
''')

    partes.append('''      <p class="form-nota">Al enviar aceptas que usemos estos datos para
        responderte. Nada más. Puedes leer el detalle en la
        <a href="/legal/privacidad/">política de privacidad</a>.</p>
      <div class="form-acciones">
        <button class="btn btn-azul" type="submit">Enviar
          <span class="flecha" aria-hidden="true">&rarr;</span></button>
        <span class="form-alt">o escríbenos a <a href="mailto:%s">%s</a>,
          o llama al <a href="tel:%s">%s</a></span>
      </div>
''' % (BUZON, BUZON, TELEFONO_TEL, TELEFONO))

    return "".join(partes)


def form(asunto, clase="form"):
    return ('<form class="%s" id="form-contacto" action="%s" method="POST">\n%s    </form>'
            % (clase, ENDPOINT, cuerpo(asunto)))


ESTILOS = '''
/* ── El carril que contesta mientras rellenas ────────────────────── */
.form-avance{margin-bottom:22px}
.form-avance-barra{height:4px;border-radius:9999px;background:var(--borde);
  overflow:hidden}
.form-avance-barra i{display:block;height:100%;width:0;border-radius:9999px;
  background:var(--azul);transition:width .35s cubic-bezier(.4,0,.2,1)}
.form-avance-texto{margin:10px 0 0;font-size:13px;color:var(--piedra)}
.form-resumen{margin-bottom:22px;padding-bottom:20px;
  border-bottom:1px solid var(--borde)}
.form-resumen .etiqueta{margin-bottom:12px}
.form-resumen dl{margin:0;display:grid;gap:10px}
.form-resumen dt{font-size:12px;letter-spacing:.05em;text-transform:uppercase;
  color:var(--piedra);font-weight:600;margin-bottom:2px}
.form-resumen dd{margin:0;font-size:14px;line-height:1.45;
  color:var(--tinta-fuerte)}
.form-luego .pasos-lado li{padding-bottom:14px}
/* ── El formulario que se rellena pinchando ──────────────── */
.form{display:grid;gap:26px;max-width:720px;margin:0 auto;text-align:left}
.bloque{border:0;padding:0;margin:0;display:grid;gap:10px}
.bloque legend{font-size:17px;font-weight:600;color:var(--tinta-fuerte);padding:0;margin-bottom:2px}
.bloque-pie{font-size:14px;color:var(--piedra);margin:-4px 0 6px}
.bloque > .op,.bloque > label.op{margin:0}
.bloque{grid-auto-flow:row}
.bloque:has(.op:not(.op-chica)){grid-template-columns:repeat(auto-fit,minmax(190px,1fr))}
.bloque legend,.bloque-pie,.subs{grid-column:1/-1}

/* La opcion: una superficie que se pincha. Sin sombra, sin color de
   relleno hasta que se elige, y con la marca de elegido a la izquierda
   para que se lea de un vistazo cual esta activa. */
.op{
  position:relative;display:flex;gap:10px;align-items:flex-start;
  background:var(--blanco);border:1px solid var(--borde);border-radius:var(--r-btn);
  padding:12px 14px;cursor:pointer;
  transition:border-color .16s ease,background .16s ease,transform .16s ease;
}
.op:hover{border-color:rgba(0,0,0,.2)}
.op input{position:absolute;opacity:0;width:0;height:0}
.op-cuerpo{display:grid;gap:2px;min-width:0}
.op-tit{font-size:15px;font-weight:500;color:var(--tinta-fuerte);line-height:1.3}
.op-pie{font-size:13px;color:var(--piedra);line-height:1.35}
.op::before{
  content:"";flex:0 0 auto;width:17px;height:17px;margin-top:1px;
  border:1.5px solid rgba(0,0,0,.22);border-radius:50%;
  transition:border-color .16s ease,background .16s ease,box-shadow .16s ease;
}
.op:has(input[type=checkbox])::before{border-radius:var(--r-sm)}
.op:has(input:checked){border-color:var(--azul);background:var(--azul-tinte)}
.op:has(input:checked)::before{border-color:var(--azul);background:var(--azul)}
/* El punto del boton de opcion: hueco blanco por fuera, azul dentro. */
.op:has(input[type=radio]:checked)::before{box-shadow:inset 0 0 0 3px var(--blanco)}
/* La casilla marcada lleva su marca de verificacion, que se lee mucho
   mejor que un cuadrado de color a 17px. */
.op:has(input[type=checkbox]:checked)::before{
  background:var(--azul) no-repeat center/11px 11px;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 12'%3E%3Cpath d='M2 6.4 4.6 9 10 3.2' fill='none' stroke='%23fff' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E");
}
.op:has(input:focus-visible){outline:2px solid var(--azul);outline-offset:2px}
.op-chica{padding:10px 12px}
.op-chica .op-tit{font-size:14.5px}

.subs{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:18px}
.sub{display:grid;gap:7px;align-content:start}
.sub-tit{font-size:12px;font-weight:600;letter-spacing:.05em;text-transform:uppercase;color:var(--piedra);margin:0}

.datos{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.dato{display:grid;gap:6px;font-size:14px;color:var(--piedra)}
.dato i{font-style:normal;color:rgba(0,0,0,.34)}
.dato-ancho{margin-top:14px}
.dato input,.dato textarea{
  font:inherit;font-size:15px;color:var(--tinta);
  padding:11px 13px;background:var(--blanco);
  border:1px solid var(--borde);border-radius:var(--r-btn);resize:vertical;
  transition:border-color .16s ease,box-shadow .16s ease;
}
.dato input:focus,.dato textarea:focus{outline:0;border-color:var(--azul);box-shadow:0 0 0 3px var(--azul-tinte)}
.form-nota{font-size:13px;color:var(--piedra);line-height:1.5}
.form-nota a{color:var(--azul)}
.form-acciones{display:flex;gap:16px;align-items:center;flex-wrap:wrap}
.form-alt{font-size:14px;color:var(--piedra)}
.form-alt a{color:var(--azul)}
@media(max-width:640px){
  .datos{grid-template-columns:1fr}
  .bloque:has(.op:not(.op-chica)){grid-template-columns:1fr}
}
'''

JS = '''
/* -- El formulario ------------------------------------------
   Se envia solo, con su action y su method: sin JavaScript
   funciona igual. Esto solo desactiva el boton al enviar, para
   que nadie pulse dos veces, y avisa si no se ha marcado nada
   en las necesidades, que es lo unico que de verdad hace falta
   para preparar la llamada.                                 */
(function () {
  var f = document.getElementById("form-contacto");
  if (!f) return;
  f.addEventListener("submit", function (e) {
    var marcadas = f.querySelectorAll('input[type=checkbox]:checked').length;
    var aviso = f.querySelector(".form-aviso");
    if (!marcadas) {
      e.preventDefault();
      if (!aviso) {
        aviso = document.createElement("p");
        aviso.className = "form-aviso form-nota";
        aviso.style.color = "#b3261e";
        f.querySelector(".form-acciones").insertAdjacentElement("beforebegin", aviso);
      }
      aviso.textContent = "Marca al menos una cosa en la que podamos ayudarte.";
      var primera = f.querySelector('input[type=checkbox]');
      if (primera) primera.closest(".bloque").scrollIntoView({block: "center", behavior: "smooth"});
      return;
    }
    if (aviso) aviso.remove();
    var b = f.querySelector('button[type="submit"]');
    if (b) { b.disabled = true; b.textContent = "Enviando..."; }
  });
})();
'''

JS_LADO = '''
/* -- El carril del formulario -------------------------------
   Escribe al lado lo que se va marcando y cuanto queda. No es
   adorno: el formulario es largo y sin esto no sabes ni por
   donde vas ni que llevas dicho. Si esto no corre, el
   formulario sigue funcionando igual que siempre.          */
(function () {
  var f = document.getElementById("form-contacto");
  var caja = document.querySelector(".form-lado-caja");
  if (!f || !caja) return;

  var avance = caja.querySelector(".form-avance");
  var barra = caja.querySelector(".form-avance-barra i");
  var texto = caja.querySelector(".form-avance-texto");
  var resumen = caja.querySelector(".form-resumen");
  var lista = resumen ? resumen.querySelector("dl") : null;
  if (!avance || !resumen || !lista) return;

  /* Lo que se considera contestado, en el orden en que se pregunta. */
  var PASOS = [
    ["Perfil", "Qué eres"],
    ["Equipo", "Cuántos sois"],
    ["_necesita", "Te ayudamos con"],
    ["Sistema actual", "Usas hoy"],
    ["Plazo", "Para cuándo"],
    ["Nombre", "Nombre"],
    ["Email", "Email"]
  ];

  function marcado(nombre) {
    var e = f.querySelector('[name="' + nombre + '"]:checked');
    return e ? e.value : "";
  }

  function necesidades() {
    var v = [];
    f.querySelectorAll('input[type=checkbox]:checked').forEach(function (c) {
      if (c.name.indexOf("Necesita:") === 0) v.push(c.value);
    });
    return v;
  }

  function valor(clave) {
    if (clave === "_necesita") {
      var n = necesidades();
      if (!n.length) return "";
      return n.length > 3 ? n.slice(0, 3).join(", ") + " y " + (n.length - 3) + " más"
                          : n.join(", ");
    }
    var campo = f.querySelector('input[name="' + clave + '"]:not([type=radio])');
    if (campo) return campo.value.trim();
    return marcado(clave);
  }

  function pinta() {
    var hechos = 0, filas = "";
    PASOS.forEach(function (p) {
      var v = valor(p[0]);
      if (!v) return;
      hechos++;
      filas += "<div><dt>" + p[1] + "</dt><dd></dd></div>";
    });
    /* El texto se pone despues, con textContent, para que nada de lo
       que escriba el visitante llegue a interpretarse como HTML. */
    lista.innerHTML = filas;
    var dds = lista.querySelectorAll("dd"), i = 0;
    PASOS.forEach(function (p) {
      var v = valor(p[0]);
      if (v) dds[i++].textContent = v;
    });

    avance.hidden = false;
    barra.style.width = Math.round(hechos / PASOS.length * 100) + "%";
    texto.textContent = hechos === PASOS.length
      ? "Ya está: puedes enviarlo."
      : hechos + " de " + PASOS.length + " contestadas";
    resumen.hidden = hechos === 0;
  }

  f.addEventListener("change", pinta);
  f.addEventListener("input", pinta);
  pinta();
})();
'''

JS_RASTRO = '''
/* -- De donde sale cada envio -------------------------------
   Rellena los campos ocultos del formulario antes de mandarlo.
   El primer contacto se guarda la primera vez que alguien
   entra y se conserva aunque despues navegue diez paginas: sin
   eso, todo lead parece venir de la pagina del formulario.
   Si esto no corre, los campos van vacios y el formulario
   funciona igual.                                          */
(function () {
  var LLAVE = "contaes:origen";
  var PROPIAS = /(^|\.)contaes\.com$/i;

  function guardado() {
    try { return JSON.parse(localStorage.getItem(LLAVE) || "null"); }
    catch (e) { return null; }
  }

  function deQuien() {
    var r = document.referrer;
    if (!r) return "directo o guardado en favoritos";
    try {
      var h = new URL(r).hostname;
      return PROPIAS.test(h) ? "" : h;
    } catch (e) { return ""; }
  }

  /* El primer contacto: se escribe una vez y no se toca mas. */
  var o = guardado();
  if (!o) {
    var q = new URLSearchParams(location.search), campana = {};
    ["utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content",
     "gclid"].forEach(function (k) { if (q.get(k)) campana[k] = q.get(k); });
    o = {
      primera: location.pathname,
      referente: deQuien(),
      fecha: new Date().toISOString().slice(0, 16).replace("T", " "),
      campana: campana,
      vistas: 0
    };
  }
  o.vistas = (o.vistas || 0) + 1;
  try { localStorage.setItem(LLAVE, JSON.stringify(o)); } catch (e) {}

  var f = document.getElementById("form-contacto");
  if (!f) return;
  var arranque = Date.now();

  function aparato() {
    var a = navigator.userAgent;
    var tipo = /Mobi|Android/i.test(a) ? "movil"
             : /iPad|Tablet/i.test(a) ? "tableta" : "ordenador";
    var so = /Windows/.test(a) ? "Windows" : /Mac OS X/.test(a) ? "Mac"
           : /Android/.test(a) ? "Android"
           : /iPhone|iPad|iPod/.test(a) ? "iOS"
           : /Linux/.test(a) ? "Linux" : "otro";
    return tipo + " \u00b7 " + so;
  }

  function minutos(ms) {
    var s = Math.round(ms / 1000);
    return s < 90 ? s + " s" : Math.round(s / 60) + " min";
  }

  f.addEventListener("submit", function () {
    var v = {
      origen_primera: o.primera,
      origen_referente: o.referente,
      origen_fecha: o.fecha,
      envio_pagina: location.pathname,
      envio_fecha: new Date().toLocaleString("es-ES", {timeZone: "Europe/Madrid"}),
      envio_vistas: String(o.vistas),
      ctx_aparato: aparato(),
      ctx_pantalla: window.innerWidth + "\u00d7" + window.innerHeight,
      ctx_idioma: navigator.language || "",
      ctx_tiempo: minutos(Date.now() - arranque)
    };
    Object.keys(o.campana || {}).forEach(function (k) { v[k] = o.campana[k]; });
    f.querySelectorAll("[data-rastro]").forEach(function (c) {
      c.value = v[c.getAttribute("data-rastro")] || "";
    });
  });
})();
'''
