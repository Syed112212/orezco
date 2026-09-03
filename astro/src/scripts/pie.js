
/* -- Entrada al aparecer -------------------------------------
   La hoja de estilos no esconde nada por su cuenta: solo se oculta
   lo que este JavaScript marca, y siempre hay una red de seguridad
   que lo muestra pase lo que pase.                            */
(function(){
  var piezas=document.querySelectorAll(".revela");
  if(!piezas.length)return;
  function mostrar(e){e.classList.remove("espera");e.classList.add("visible");}
  if(window.matchMedia("(prefers-reduced-motion: reduce)").matches||!("IntersectionObserver" in window)){
    for(var i=0;i<piezas.length;i++)mostrar(piezas[i]);return;
  }
  var pendientes=[];
  for(var j=0;j<piezas.length;j++){
    if(piezas[j].getBoundingClientRect().top<window.innerHeight*0.92){mostrar(piezas[j]);}
    else{piezas[j].classList.add("espera");pendientes.push(piezas[j]);}
  }
  var obs=new IntersectionObserver(function(es){es.forEach(function(e){
    if(e.isIntersecting){mostrar(e.target);obs.unobserve(e.target);}
  });},{threshold:.05,rootMargin:"0px 0px -40px 0px"});
  for(var k=0;k<pendientes.length;k++)obs.observe(pendientes[k]);
  setTimeout(function(){
    for(var n=0;n<pendientes.length;n++)
      if(pendientes[n].classList.contains("espera"))mostrar(pendientes[n]);
  },2500);
})();

/* -- El menu: por areas en escritorio, plegable en movil ------
   Un solo mecanismo para los dos: el atributo data-abierta en el
   area. En escritorio el panel flota; en movil se despliega en su
   sitio. Cierra con Escape, al elegir enlace y al pulsar fuera.  */
(function(){
  var nav=document.querySelector(".nav");
  var boton=document.getElementById("menu-btn");
  var enlaces=document.getElementById("nav-links");
  if(!nav||!enlaces)return;
  var areas=[].slice.call(enlaces.querySelectorAll(".area"));

  function cierraAreas(salvo){
    areas.forEach(function(a){
      if(a===salvo)return;
      a.removeAttribute("data-abierta");
      a.querySelector("button").setAttribute("aria-expanded","false");
    });
  }
  areas.forEach(function(a){
    var b=a.querySelector("button");
    b.addEventListener("click",function(e){
      e.stopPropagation();
      var abre=!a.hasAttribute("data-abierta");
      cierraAreas(a);
      if(abre){a.setAttribute("data-abierta","");}else{a.removeAttribute("data-abierta");}
      b.setAttribute("aria-expanded",abre?"true":"false");
    });
    /* con raton basta pasar por encima; con teclado hace falta el click */
    a.addEventListener("mouseenter",function(){
      if(!window.matchMedia("(min-width: 981px)").matches)return;
      cierraAreas(a);a.setAttribute("data-abierta","");b.setAttribute("aria-expanded","true");
    });
    a.addEventListener("mouseleave",function(){
      if(!window.matchMedia("(min-width: 981px)").matches)return;
      a.removeAttribute("data-abierta");b.setAttribute("aria-expanded","false");
    });
  });

  function ponMovil(abierto){
    nav.classList.toggle("abierta",abierto);
    if(!boton)return;
    boton.setAttribute("aria-expanded",abierto?"true":"false");
    boton.setAttribute("aria-label",abierto?"Cerrar el menu":"Abrir el menu");
    if(!abierto)cierraAreas(null);
  }
  if(boton)boton.addEventListener("click",function(e){
    e.stopPropagation();ponMovil(!nav.classList.contains("abierta"));
  });
  enlaces.addEventListener("click",function(e){if(e.target.closest("a"))ponMovil(false);});
  document.addEventListener("keydown",function(e){
    if(e.key!=="Escape")return;
    cierraAreas(null);
    if(nav.classList.contains("abierta")){ponMovil(false);if(boton)boton.focus();}
  });
  document.addEventListener("click",function(e){
    if(!nav.contains(e.target)){cierraAreas(null);ponMovil(false);}
  });
})();
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
/* -- El fondo: laminas en un espacio con perspectiva ----------
   Proyeccion en perspectiva de toda la vida: una lamina a
   distancia z se ve a escala f/(f+z). Se pintan de la mas lejana
   a la mas cercana para que se tapen bien, y el desenfoque y la
   transparencia crecen con la distancia, que es lo que el ojo lee
   como profundidad.

   Las laminas se dibujan una vez en imagenes fuera de pantalla,
   con el desenfoque ya aplicado. Cada cuadro solo las coloca con
   su giro y su escala: repintar el desenfoque a cada cuadro
   costaria mas que todo lo demas junto.                          */
(function () {
  var lienzo = document.getElementById("fondo");
  if (!lienzo || !lienzo.getContext) return;
  var ctx = lienzo.getContext("2d");
  if (!ctx) return;

  var FOCO = 900;            // distancia focal, en pixeles del mundo
  var CERCA = 340;           // ninguna se acerca mas que esto
  var HONDO = 1700;          // la lamina mas lejana
  var CAPAS = 3;             // tres grados de desenfoque
  var TINTAS = [
    ["#2FBF9B", "#1F9EC4", "#eaf7f2"],   // el degradado de las barras del logo
    ["#1F9EC4", "#1E6FB8", "#e9f4f9"],
    ["#1E6FB8", "#1E3A5F", "#eaf1fa"],
    ["#ffb110", "#f2a10a", "#fff5e2"],   // el acento, en una de cada cinco
    ["#62aef0", "#1E6FB8", "#ecf4fd"]
  ];
  var ANCHO_L = 168, ALTO_L = 116, MARGEN = 26;  // la lamina, en su imagen

  var MINIMO_ENTRE_CUADROS = 1000 / 30;   // 30 por segundo basta para algo tan lento
  var quieto = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var estrecho = window.matchMedia("(max-width: 760px)").matches;
  var CUANTAS = estrecho ? 8 : 18;

  /* ---- las imagenes de las laminas, dibujadas una sola vez ---- */
  var sellos = [];
  function dibujaLamina(tinta, tipo, desenfoque) {
    var d = document.createElement("canvas");
    d.width = ANCHO_L + MARGEN * 2;
    d.height = ALTO_L + MARGEN * 2;
    var c = d.getContext("2d");
    var x = MARGEN, y = MARGEN, r = 11;

    function silueta() {
      c.beginPath();
      c.moveTo(x + r, y);
      c.arcTo(x + ANCHO_L, y, x + ANCHO_L, y + ALTO_L, r);
      c.arcTo(x + ANCHO_L, y + ALTO_L, x, y + ALTO_L, r);
      c.arcTo(x, y + ALTO_L, x, y, r);
      c.arcTo(x, y, x + ANCHO_L, y, r);
      c.closePath();
    }

    c.save();
    if (desenfoque > 0 && typeof c.filter === "string") c.filter = "blur(" + desenfoque + "px)";

    // sombra baja y muy abierta: separa el panel sin ensuciarlo
    c.shadowColor = "rgba(30,58,95,.13)";
    c.shadowBlur = 22;
    c.shadowOffsetY = 9;

    // el cristal: blanco arriba, tenido abajo
    var g = c.createLinearGradient(x, y, x + ANCHO_L * .5, y + ALTO_L);
    g.addColorStop(0, "rgba(255,255,255,.97)");
    g.addColorStop(1, tinta[2]);
    c.fillStyle = g;
    silueta();
    c.fill();
    c.shadowColor = "transparent";

    // el canto encendido: es lo que hace que parezca vidrio y no papel
    var bg = c.createLinearGradient(x, y, x + ANCHO_L, y + ALTO_L);
    bg.addColorStop(0, tinta[0]);
    bg.addColorStop(1, tinta[1]);
    c.strokeStyle = bg;
    c.globalAlpha = .42;
    c.lineWidth = 1.4;
    silueta();
    c.stroke();
    c.globalAlpha = 1;

    // el reflejo que cruza la esquina de arriba
    c.save();
    silueta();
    c.clip();
    var rf = c.createLinearGradient(x, y, x + ANCHO_L * .8, y + ALTO_L * .8);
    rf.addColorStop(0, "rgba(255,255,255,.85)");
    rf.addColorStop(.45, "rgba(255,255,255,0)");
    c.fillStyle = rf;
    c.fillRect(x, y, ANCHO_L, ALTO_L);
    c.restore();

    // el contenido, siempre en color de marca: nada de gris
    function barra(bx, by, an, al, alfa) {
      var b = c.createLinearGradient(bx, by, bx + an, by);
      b.addColorStop(0, tinta[0]);
      b.addColorStop(1, tinta[1]);
      c.fillStyle = b;
      c.globalAlpha = alfa;
      c.beginPath();
      var rr = Math.min(al / 2, 3);
      c.moveTo(bx + rr, by);
      c.arcTo(bx + an, by, bx + an, by + al, rr);
      c.arcTo(bx + an, by + al, bx, by + al, rr);
      c.arcTo(bx, by + al, bx, by, rr);
      c.arcTo(bx, by, bx + an, by, rr);
      c.closePath();
      c.fill();
      c.globalAlpha = 1;
    }

    if (tipo === 0) {                 // las tres barras del logo
      barra(x + 18, y + 26, 96, 9, .78);
      barra(x + 18, y + 46, 96, 9, .58);
      barra(x + 18, y + 66, 74, 9, .40);
      barra(x + 18, y + 88, 46, 6, .22);
    } else if (tipo === 1) {          // una tabla
      barra(x + 18, y + 20, 54, 7, .72);
      for (var j = 0; j < 4; j++) {
        barra(x + 18, y + 40 + j * 16, 78, 6, .30 - j * .05);
        barra(x + 106, y + 40 + j * 16, 44, 6, .18 - j * .03);
      }
    } else {                          // un cuadro de mando
      barra(x + 18, y + 20, 54, 7, .72);
      var altos = [20, 34, 27, 44, 37];
      for (var k = 0; k < altos.length; k++)
        barra(x + 20 + k * 26, y + ALTO_L - 18 - altos[k], 17, altos[k], .40 + k * .06);
    }
    c.restore();
    return d;
  }

  for (var capa = 0; capa < CAPAS; capa++) {
    var fila = [];
    for (var ti = 0; ti < TINTAS.length; ti++)
      for (var tipo = 0; tipo < 3; tipo++)
        fila.push(dibujaLamina(TINTAS[ti], tipo, capa * 1.6));
    sellos.push(fila);
  }

  /* ---- las laminas, repartidas por el espacio ---- */
  var laminas = [];
  for (var n = 0; n < CUANTAS; n++) {
    laminas.push({
      x: (Math.random() - .5) * 3000,
      y: (Math.random() - .5) * 1900,
      z: CERCA + Math.random() * HONDO,
      giro: Math.random() * Math.PI * 2,          // sobre su eje vertical
      vgiro: (.05 + Math.random() * .07) * (Math.random() < .5 ? -1 : 1),
      ladeo: (Math.random() - .5) * .34,          // inclinacion en el plano
      vladeo: (Math.random() - .5) * .05,
      sube: 9 + Math.random() * 13,               // pixeles por segundo
      sello: (Math.random() * 15) | 0
    });
  }
  laminas.sort(function (a, b) { return b.z - a.z; });

  /* ---- el bucle ---- */
  var an = 0, al = 0, dpr = 1;
  function mide() {
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    an = lienzo.clientWidth;
    al = lienzo.clientHeight;
    lienzo.width = Math.round(an * dpr);
    lienzo.height = Math.round(al * dpr);
  }
  mide();
  var remide;
  window.addEventListener("resize", function () {
    clearTimeout(remide);
    remide = setTimeout(mide, 180);
  }, { passive: true });

  function pinta(dt) {
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, an, al);
    var cx = an / 2, cy = al / 2;

    for (var i = 0; i < laminas.length; i++) {
      var l = laminas[i];
      if (dt) {
        l.y -= l.sube * dt;
        if (l.y < -1100) l.y = 1100;
        l.giro += l.vgiro * dt;
        l.ladeo += l.vladeo * dt * .12;
      }
      var k = FOCO / (FOCO + l.z);              // la escala por perspectiva
      var px = cx + l.x * k, py = cy + l.y * k;
      var tam = k * 1.05;
      if (px < -300 || px > an + 300 || py < -260 || py > al + 260) continue;

      // el giro sobre el eje vertical: la lamina se estrecha al ponerse de canto
      var canto = Math.cos(l.giro);
      var estrecha = Math.abs(canto);
      if (estrecha < .08) continue;             // de perfil no se ve

      var capa = l.z < 480 ? 0 : (l.z < 1000 ? 1 : 2);
      var img = sellos[capa][l.sello];
      // El texto vive en la columna central. Los paneles no se quitan de
      // enmedio -eso se notaria-, se apagan al acercarse a ella.
      var centrado = Math.abs(px - cx) / (an * .5);
      var paso = Math.min(1, Math.max(0, (centrado - .18) / .34));
      var aire = .22 + .78 * paso * paso;
      ctx.globalAlpha = (.42 - capa * .09) * Math.min(1, .35 + estrecha) * aire;
      ctx.setTransform(
        dpr * tam * estrecha * Math.cos(l.ladeo), dpr * tam * estrecha * Math.sin(l.ladeo),
        dpr * tam * -Math.sin(l.ladeo), dpr * tam * Math.cos(l.ladeo),
        dpr * px, dpr * py
      );
      ctx.drawImage(img, -img.width / 2, -img.height / 2);
    }
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.globalAlpha = 1;
  }

  if (quieto) { pinta(0); return; }             // un cuadro y quieta

  var antes = 0, vivo = true;
  document.addEventListener("visibilitychange", function () {
    vivo = !document.hidden;
    if (vivo) { antes = 0; requestAnimationFrame(cuadro); }
  });
  function cuadro(ahora) {
    if (!vivo) return;
    requestAnimationFrame(cuadro);
    // A treinta por segundo no se nota y se deja libre la mitad del hilo
    // principal, que es el que dibuja el texto.
    if (antes && ahora - antes < MINIMO_ENTRE_CUADROS) return;
    var dt = antes ? Math.min((ahora - antes) / 1000, .08) : 0;
    antes = ahora;
    pinta(dt);
  }
  requestAnimationFrame(cuadro);
})();
document.getElementById("anio").textContent=new Date().getFullYear();
