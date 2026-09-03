/* El año del pie ya no lo pone este script: Pie.astro lo calcula al
   generar la página, con new Date().getFullYear() en su cabecera, y no
   hay ningun #anio en el marcado para que esta linea lo actualizara. */

var SIN_MOVIMIENTO = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

/* ── Ocho losas 3D, una por modulo ─────────────────────────── */
(function () {
  var caja = document.getElementById("losas");
  var pie = document.getElementById("losas-pie");
  if (!caja || !pie) return;

  var TOTAL = 8, SEP = 15;
  for (var i = 0; i < TOTAL; i++) {
    var losa = document.createElement("div");
    losa.className = "losa";
    losa.setAttribute("data-losa", i + 1);
    losa.style.transform = "translateZ(" + (i * SEP) + "px)";
    caja.appendChild(losa);
  }

  var losas = caja.querySelectorAll(".losa");
  var cartas = document.querySelectorAll(".mod[data-losa]");
  var base = pie.textContent;

  function limpiar() {
    caja.classList.remove("hay-activa");
    for (var i = 0; i < losas.length; i++) {
      losas[i].classList.remove("activa");
      losas[i].style.transform = "translateZ(" + (i * SEP) + "px)";
    }
    pie.textContent = base;
  }

  function marcar(n, carta) {
    limpiar();
    var losa = caja.querySelector('.losa[data-losa="' + n + '"]');
    if (!losa) return;
    losa.classList.add("activa");
    caja.classList.add("hay-activa");
    losa.style.transform = "translateZ(" + ((n - 1) * SEP + 34) + "px)";
    var t = carta.querySelector("h3");
    if (t) pie.textContent = t.textContent;
  }

  for (var k = 0; k < cartas.length; k++) {
    (function (carta) {
      var n = carta.getAttribute("data-losa");
      carta.addEventListener("mouseenter", function () { marcar(n, carta); });
      carta.addEventListener("focusin", function () { marcar(n, carta); });
      carta.addEventListener("mouseleave", limpiar);
      carta.addEventListener("focusout", limpiar);
    })(cartas[k]);
  }
})();

/* ── Revelado al entrar en pantalla ──────────────────────────
   El contenido nunca depende de que esto funcione: la hoja de
   estilos no esconde nada por su cuenta. Aqui se marca lo que esta
   por debajo de la pantalla, se revela al llegar, y a los cuatro
   segundos se muestra lo que quede, sea cual sea el motivo.    */
(function () {
  var piezas = document.querySelectorAll(".revela, .cascada");
  if (!piezas.length) return;

  function mostrar(e) {
    e.classList.remove("espera");
    e.classList.add("visible");
  }
  if (SIN_MOVIMIENTO || !("IntersectionObserver" in window)) {
    for (var i = 0; i < piezas.length; i++) mostrar(piezas[i]);
    return;
  }

  var pendientes = [];
  for (var j = 0; j < piezas.length; j++) {
    // lo que ya se ve al cargar no se esconde nunca
    if (piezas[j].getBoundingClientRect().top < window.innerHeight * 0.92) {
      mostrar(piezas[j]);
    } else {
      piezas[j].classList.add("espera");
      pendientes.push(piezas[j]);
    }
  }

  var obs = new IntersectionObserver(function (entradas) {
    entradas.forEach(function (e) {
      if (e.isIntersecting) { mostrar(e.target); obs.unobserve(e.target); }
    });
  }, { threshold: 0.05, rootMargin: "0px 0px -40px 0px" });
  for (var k = 0; k < pendientes.length; k++) obs.observe(pendientes[k]);

  // red de seguridad: nada se queda escondido por un fallo de la animacion
  setTimeout(function () {
    for (var n = 0; n < pendientes.length; n++) {
      if (pendientes[n].classList.contains("espera")) mostrar(pendientes[n]);
    }
  }, 2500);
})();

/* -- Pausa de la cinta, tambien con teclado ------------------- */
(function () {
  var cinta = document.querySelector(".cinta");
  var boton = document.getElementById("cinta-pausa");
  if (!cinta || !boton) return;
  boton.addEventListener("click", function () {
    var parada = cinta.classList.toggle("parada");
    boton.setAttribute("aria-pressed", parada ? "true" : "false");
    boton.querySelector(".cp-texto").textContent = parada ? "Reanudar" : "Pausar";
    boton.querySelector(".cp-icono").textContent = parada ? "\u25B6" : "II";
  });
})();

/* -- Barra de navegacion que se compacta al bajar ------------- */
(function () {
  var nav = document.querySelector(".nav");
  if (!nav || SIN_MOVIMIENTO) return;
  var pedido = false;
  window.addEventListener("scroll", function () {
    if (pedido) return;
    pedido = true;
    requestAnimationFrame(function () {
      nav.classList.toggle("encogida", window.scrollY > 80);
      pedido = false;
    });
  }, { passive: true });
})();

/* -- Tarjetas que se inclinan siguiendo al raton ---------------
   Solo con puntero fino: en tactil no hay hover.               */
(function () {
  if (SIN_MOVIMIENTO || !window.matchMedia("(pointer: fine)").matches) return;
  var piezas = document.querySelectorAll(".inclina");
  for (var i = 0; i < piezas.length; i++) {
    (function (el) {
      el.addEventListener("mousemove", function (e) {
        var r = el.getBoundingClientRect();
        var x = (e.clientX - r.left) / r.width - 0.5;
        var y = (e.clientY - r.top) / r.height - 0.5;
        el.style.transform = "perspective(700px) rotateX(" + (-y * 7) + "deg) rotateY(" + (x * 9) + "deg) translateY(-4px)";
      });
      el.addEventListener("mouseleave", function () { el.style.transform = ""; });
    })(piezas[i]);
  }
})();

/* -- La conversacion de la maqueta se representa sola ----------
   Es una maqueta, no una conversacion real: la etiqueta bajo el
   marco lo dice. Va en bucle para quien llega tarde.            */
(function () {
  if (SIN_MOVIMIENTO) return;
  var chat = document.querySelector(".maqueta .chat");
  if (!chat) return;
  var burbujas = chat.querySelectorAll(".burbuja");
  var filas = document.querySelectorAll(".maqueta .tabla .fila");

  function ocultar(lista, eje) {
    for (var i = 0; i < lista.length; i++) {
      lista[i].style.opacity = "0";
      lista[i].style.transform = eje;
      lista[i].style.transition = "opacity .4s ease, transform .4s cubic-bezier(.22,1,.36,1)";
    }
  }
  function mostrar(lista, i, paso, luego) {
    if (i >= lista.length) { if (luego) luego(); return; }
    lista[i].style.opacity = "1";
    lista[i].style.transform = "none";
    setTimeout(function () { mostrar(lista, i + 1, paso, luego); }, paso);
  }
  function ciclo() {
    ocultar(burbujas, "translateY(10px)");
    ocultar(filas, "translateX(10px)");
    setTimeout(function () {
      mostrar(burbujas, 0, 850, function () {
        mostrar(filas, 0, 150, function () { setTimeout(ciclo, 6500); });
      });
    }, 400);
  }
  var obs = new IntersectionObserver(function (es) {
    es.forEach(function (e) { if (e.isIntersecting) { ciclo(); obs.disconnect(); } });
  }, { threshold: 0.3 });
  obs.observe(chat);
})();

/* ── Contacto ────────────────────────────────────────────────
   Unico valor que hay que rellenar. Vacio: se muestra la pildora
   informativa y el formulario queda oculto.                    */
