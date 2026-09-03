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
    return tipo + " · " + so;
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
      ctx_pantalla: window.innerWidth + "×" + window.innerHeight,
      ctx_idioma: navigator.language || "",
      ctx_tiempo: minutos(Date.now() - arranque)
    };
    Object.keys(o.campana || {}).forEach(function (k) { v[k] = o.campana[k]; });
    f.querySelectorAll("[data-rastro]").forEach(function (c) {
      c.value = v[c.getAttribute("data-rastro")] || "";
    });
  });
})();
