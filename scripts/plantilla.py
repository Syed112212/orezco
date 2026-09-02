# -*- coding: utf-8 -*-
"""La cascara comun de todas las paginas generadas.

Aqui viven la marca, los estilos, la barra y el pie. Los generadores
(build-sitio.py y build-blog.py) importan de aqui para que el menu no se
separe entre secciones: si se anade una pagina, se anade en un sitio.

No incluye la portada: index.html se escribe a mano porque tiene piezas
propias (el fondo en canvas, la maqueta del asistente, la pila de
modulos) que no comparte nadie mas. Su barra se mantiene a la par a mano,
y check-design.py avisa si se separan.
"""

DOMINIO = "https://contaes.com"

# ─────────────────────────────────────────────────────────────────────
# El mapa del sitio. Es la unica fuente: barra, pie y sitemap salen de
# aqui, asi que no puede haber una pagina enlazada en un sitio y no en
# otro.
# ─────────────────────────────────────────────────────────────────────
GESTORIA = [
    ("contabilidad", "Contabilidad", "Los libros al día, no a final de trimestre"),
    ("fiscal", "Fiscal y modelos", "Preparados, firmados y presentados por un asesor"),
    ("laboral", "Laboral y nóminas", "Altas, contratos, nóminas y registro de jornada"),
    ("legal", "Legal", "Sociedades, contratos y protección de datos"),
]

CRECIMIENTO = [
    ("cfo", "CFO a tu lado", "Presupuesto, tesorería y márgenes, con criterio"),
    ("cmo", "CMO a tu lado", "Posicionamiento, captación y medir lo que trae clientes"),
    ("prospeccion", "Prospección comercial", "Encontrar clientes en vez de esperarlos"),
    ("bots", "Bot de llamadas y WhatsApp", "Atender cuando no hay nadie, y pasar a persona"),
    ("financiacion", "Financiación pública y privada", "Subvenciones, banca e inversión"),
    ("internacionalizacion", "Internacionalización", "Vender fuera con las cosas en orden"),
]

PUBLICO = [
    ("autonomos", "Autónomos", "Cuota, modelos, gastos y saber qué te queda"),
    ("startups", "Startups", "Libros que aguantan una due diligence"),
    ("pymes", "Pymes", "Cuando la empresa creció y la administración no"),
]

MODULOS = [
    ("contabilidad", "Contabilidad", "Asientos, plan contable, conciliación y cierre"),
    ("facturacion", "Facturación", "Emisión, rectificativas y seguimiento de cobro"),
    ("inventario", "Inventario", "Existencias, lotes y movimientos entre almacenes"),
    ("compras", "Compras", "Proveedores, pedidos y recepciones"),
    ("ventas", "Ventas y clientes", "Presupuestos, pedidos y la ficha de cada cuenta"),
    ("proyectos", "Proyectos", "Tareas, horas imputadas y rentabilidad"),
    ("personal", "Personal", "Plantilla, ausencias y gastos"),
    ("informes", "Informes", "Cuadros de mando sobre los datos en vivo"),
]

CAPACIDADES = [
    ("asesoria-fiscal", "Asesoría fiscal incluida", "Los modelos, preparados y presentados por un asesor"),
    ("asistente-ia", "Asistente con IA", "Preguntar en tu idioma en vez de buscar por menús"),
    ("escaner-facturas", "Escáner de facturas", "La factura del proveedor entra sin teclearla"),
    ("conciliacion-bancaria", "Conciliación bancaria", "El extracto contra los apuntes, cuadrado"),
    ("verifactu", "VeriFactu", "Qué es y a qué obliga tu sistema de facturación"),
]

SECTORES = [
    ("fabricacion", "Fabricación", "Escandallos, órdenes y coste real de producción"),
    ("distribucion", "Distribución y mayorista", "Muchas referencias, márgenes finos y stock que se mueve"),
    ("construccion", "Construcción", "Obra a obra: certificaciones, coste y desvío"),
    ("comercio", "Comercio y retail", "Tienda, almacén y contabilidad en el mismo sitio"),
    ("logistica", "Logística y transporte", "Rutas, portes y lo que cuesta cada servicio"),
    ("servicios", "Servicios profesionales", "Horas facturables, proyectos y rentabilidad"),
    ("instalaciones", "Instalaciones y mantenimiento", "Partes de trabajo, materiales y garantías"),
    ("agroalimentario", "Agroalimentario", "Lotes, trazabilidad y campañas"),
]

RECURSOS = [
    ("blog/", "Blog", "Artículos sobre gestión, fiscalidad y sistemas"),
    ("glosario/", "Glosario", "Los términos de contabilidad y fiscalidad, explicados"),
    ("calendario-fiscal/", "Calendario fiscal", "Qué modelo toca y cuándo"),
    ("preguntas/", "Preguntas frecuentes", "Lo que suelen preguntarnos"),
]

EMPRESA = [
    ("sobre/", "Sobre Contaes", "Qué estamos construyendo y por qué"),
    ("migracion/", "Migración", "Cómo se cambia de sistema sin parar"),
    ("seguridad/", "Seguridad y datos", "Dónde viven tus datos y qué derechos tienes"),
    ("precios/", "Precios", "Lo que sabemos hoy sobre el precio"),
    ("integraciones/", "Integraciones", "Con qué se conectará y con qué no"),
]

LEGAL = [
    ("legal/aviso-legal/", "Aviso legal"),
    ("legal/privacidad/", "Política de privacidad"),
    ("legal/cookies/", "Política de cookies"),
]

MARCA_SVG = '''<svg class="marca-svg" viewBox="0 0 200 200" aria-hidden="true">
      <path class="mc-c" d="M 123.56 61.80 A 55.00 55.00 0 1 0 123.56 138.20" fill="none" stroke="#1E3A5F" stroke-width="27" stroke-linecap="round"/>
      <rect class="mc-b b1" x="113.0" y="59.5" width="74.0" height="19.0" rx="9.5" fill="#2FBF9B"/>
      <rect class="mc-b b2" x="113.0" y="90.5" width="74.0" height="19.0" rx="9.5" fill="#1F9EC4"/>
      <rect class="mc-b b3" x="113.0" y="121.5" width="62.0" height="19.0" rx="9.5" fill="#1E6FB8"/>
    </svg>'''

MARCA_BLANCA = (MARCA_SVG.replace("#1E3A5F", "#ffffff").replace("#2FBF9B", "#ffffff")
                .replace("#1F9EC4", "#ffffff").replace("#1E6FB8", "#ffffff"))

ESTILOS = '''
:root{
  color-scheme:light;
  --papel:#f6f5f4;--blanco:#ffffff;--borde:rgba(0,0,0,.08);--niebla:#f8fafb;
  --tinta:rgba(0,0,0,.95);--tinta-fuerte:#000000;--grafito:#615d59;--piedra:#6a6a6a;--apagado:rgba(0,0,0,.54);
  --azul:#0075de;--azul-tinte:#e6f3fe;
  --marigold:#ffb110;--coral:#f64932;--cielo:#62aef0;--medianoche:#02093a;
  --navy:#1E3A5F;--verde:#2FBF9B;--cian:#1F9EC4;--azul-marca:#1E6FB8;
  --ancho:1160px;--r-card:12px;--r-btn:8px;--r-pill:9999px;--r-sm:4px;
  --sans:"Inter",ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  --serif:"Source Serif 4",ui-serif,Georgia,serif;
  --marca:"Quicksand",var(--sans);
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{margin:0;background:var(--papel);color:var(--tinta);font-family:var(--sans);font-size:16px;line-height:1.5;-webkit-font-smoothing:antialiased}
p{margin:0}
.wrap{max-width:var(--ancho);margin:0 auto;padding:0 24px}
.estrecho{max-width:760px}
h1{font-size:clamp(34px,5.2vw,56px);font-weight:600;line-height:1.1;letter-spacing:-.038em;margin:0;color:var(--tinta-fuerte);text-wrap:balance}
h2{font-size:clamp(23px,2.6vw,30px);font-weight:600;line-height:1.2;letter-spacing:-.02em;margin:38px 0 14px;color:var(--tinta-fuerte)}
h3{font-size:19px;font-weight:700;line-height:1.3;margin:0;color:var(--tinta-fuerte)}
.etiqueta{font-size:12px;font-weight:500;letter-spacing:.04em;color:var(--piedra);margin:0;text-transform:uppercase}
.wordmark{font-family:var(--marca);font-weight:600;letter-spacing:-.01em;color:var(--navy)}
.wordmark i{font-style:normal;color:var(--verde)}
.editorial{font-family:var(--serif);font-size:19px;line-height:1.6;color:var(--grafito)}
.cuerpo{color:var(--grafito)}
.btn{display:inline-flex;align-items:center;gap:8px;font-size:15px;font-weight:500;line-height:1;padding:13px 20px;border-radius:var(--r-btn);text-decoration:none;border:1px solid transparent;transition:background .2s ease,transform .2s ease}
.btn-azul{background:var(--azul);color:#fff;box-shadow:0 1px 2px rgba(0,0,0,.12)}
.btn-azul:hover,.btn-azul:focus-visible{background:#0064c0;transform:translateY(-1px)}
.btn-tinte{background:var(--azul-tinte);color:#005fb8}
.btn-tinte:hover,.btn-tinte:focus-visible{background:#d5eafd;transform:translateY(-1px)}
.btn .flecha{display:inline-block;transition:transform .22s cubic-bezier(.22,1,.36,1)}
.btn:hover .flecha,.btn:focus-visible .flecha{transform:translateX(4px)}

/* ── La barra, con el menu por areas ─────────────────────── */
.nav{position:sticky;top:0;z-index:60;background:rgba(246,245,244,.86);backdrop-filter:blur(12px);box-shadow:0 .7px 1.462px rgba(0,0,0,.015),0 3px 9px rgba(0,0,0,.03)}
.nav-in{max-width:var(--ancho);margin:0 auto;padding:12px 24px;display:flex;align-items:center;gap:12px;min-height:64px}
.marca{display:flex;align-items:center;gap:9px;text-decoration:none}
.marca svg{width:32px;height:32px}
.marca span{font-size:21px}
.nav-links{display:flex;gap:2px;align-items:center;margin:0 auto}
.nav-links > a,.area > button{
  display:inline-flex;align-items:center;gap:6px;
  color:var(--apagado);font-family:var(--sans);font-size:15px;font-weight:500;text-decoration:none;
  padding:10px 13px;border-radius:var(--r-btn);border:0;background:none;cursor:pointer;
  transition:color .2s ease,background .2s ease;
}
.nav-links > a:hover,.nav-links > a:focus-visible,.area > button:hover,.area[data-abierta] > button{color:var(--tinta-fuerte);background:rgba(0,0,0,.04)}
.area{position:relative}
.area .punta{width:8px;height:8px;border-right:1.5px solid currentColor;border-bottom:1.5px solid currentColor;transform:rotate(45deg) translateY(-2px);transition:transform .24s cubic-bezier(.22,1,.36,1)}
.area[data-abierta] .punta{transform:rotate(-135deg) translateY(-2px)}
.despliegue{
  position:absolute;top:calc(100% + 8px);left:50%;translate:-50% 0;z-index:70;
  background:var(--blanco);border:1px solid var(--borde);border-radius:var(--r-card);
  box-shadow:0 18px 44px rgba(18,32,54,.14);padding:12px;
  display:grid;gap:2px;min-width:320px;
  visibility:hidden;opacity:0;transform:translateY(-8px) scale(.985);
  transition:opacity .18s ease,transform .24s cubic-bezier(.22,1,.36,1),visibility 0s .18s;
}
.area[data-abierta] .despliegue{visibility:visible;opacity:1;transform:none;transition-delay:0s}
.despliegue.doble{grid-template-columns:repeat(2,minmax(0,1fr));min-width:600px}
.despliegue a{display:grid;gap:2px;padding:10px 12px;border-radius:var(--r-btn);text-decoration:none;transition:background .16s ease}
.despliegue a:hover,.despliegue a:focus-visible{background:var(--niebla)}
.despliegue a b{font-size:14.5px;font-weight:600;color:var(--tinta-fuerte)}
.despliegue a span{font-size:13px;color:var(--piedra);line-height:1.4}
.despliegue .titulo-grupo{grid-column:1/-1;padding:8px 12px 4px;font-size:11.5px;font-weight:600;letter-spacing:.05em;text-transform:uppercase;color:var(--piedra)}
.menu-btn{display:none;margin-left:auto;width:40px;height:40px;padding:0;align-items:center;justify-content:center;flex-direction:column;gap:5px;background:none;border:1px solid var(--borde);border-radius:var(--r-btn);cursor:pointer}
.mb-linea{display:block;width:17px;height:1.5px;background:var(--tinta-fuerte);transition:transform .26s cubic-bezier(.22,1,.36,1),opacity .18s ease}
.nav.abierta .mb-linea:nth-child(1){transform:translateY(6.5px) rotate(45deg)}
.nav.abierta .mb-linea:nth-child(2){opacity:0}
.nav.abierta .mb-linea:nth-child(3){transform:translateY(-6.5px) rotate(-45deg)}

/* la marca animada, igual que en la portada */
.marca-svg .mc-c{transform-origin:42% 50%;transition:transform .5s cubic-bezier(.22,1,.36,1)}
.marca-svg .mc-b{transform-origin:56% 50%;animation:barra 6s cubic-bezier(.22,1,.36,1) infinite;transition:transform .32s cubic-bezier(.22,1,.36,1)}
.marca-svg .b2{animation-delay:.12s}
.marca-svg .b3{animation-delay:.24s}
@keyframes barra{0%{transform:translateX(-14px) scaleX(.55);opacity:0}9%,52%{transform:none;opacity:1}62%{transform:translateX(7px)}72%,100%{transform:none;opacity:1}}
.marca:hover .mc-c{transform:rotate(-14deg)}
.marca:hover .mc-b{animation:none}
.marca:hover .b1{transform:translateX(9px)}
.marca:hover .b2{transform:translateX(5px)}
.marca:hover .b3{transform:translateX(12px)}

/* ── Piezas de pagina ────────────────────────────────────── */
.migas{font-size:14px;color:var(--piedra);margin-bottom:20px}
.migas a{color:var(--piedra);text-decoration:none}
.migas a:hover{color:var(--tinta-fuerte);text-decoration:underline}
.revela{opacity:0;transform:translateY(20px);transition:opacity .7s ease,transform .7s cubic-bezier(.22,1,.36,1)}
.revela.visible{opacity:1;transform:none}
.encabezado{padding:52px 0 30px}
.encabezado .editorial{margin-top:18px;max-width:60ch}
.seccion{padding:34px 0}
.rejilla{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}
.rejilla-2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px}
.tarjeta{background:var(--blanco);border:1px solid var(--borde);border-radius:var(--r-card);padding:22px;transition:transform .2s ease,border-color .2s ease}
.tarjeta:hover{transform:translateY(-3px);border-color:rgba(0,0,0,.16)}
.tarjeta h3,.tarjeta .tarjeta-tit{margin:0 0 7px}
/* Titulo de tarjeta: es un h2 porque va detras del h1 de la pagina,
   pero no debe verse como una cabecera de seccion. */
.tarjeta-tit{font-size:19px;font-weight:700;line-height:1.3;letter-spacing:0;color:var(--tinta-fuerte)}
.tarjeta p{font-size:15px;color:var(--grafito)}
a.tarjeta{text-decoration:none;color:inherit;display:grid;align-content:start;gap:7px}
/* La senal de que la tarjeta lleva a algun sitio. Aparece al pasar,
   asi que no compite con el texto cuando se esta leyendo. */
.tarjeta-mas{font-size:13.5px;font-weight:500;color:var(--azul);opacity:0;
  transform:translateX(-4px);transition:opacity .2s ease,transform .2s ease}
.tarjeta-mas::after{content:" \2192"}
a.tarjeta:hover .tarjeta-mas,a.tarjeta:focus-visible .tarjeta-mas{opacity:1;transform:none}
.lista{list-style:none;margin:0;padding:0}
.lista li{padding:14px 0;border-bottom:1px solid var(--borde);display:grid;grid-template-columns:auto 1fr;gap:14px;align-items:start;color:var(--grafito)}
.lista li:last-child{border-bottom:0}
.lista b{color:var(--azul);font-weight:500;font-size:15px}
.prosa p{margin:0 0 16px;color:var(--grafito);font-size:17px;line-height:1.65}
.prosa ul,.prosa ol{margin:0 0 18px;padding-left:22px;color:var(--grafito);font-size:17px;line-height:1.65}
.prosa li{margin-bottom:8px}
.prosa strong{color:var(--tinta-fuerte);font-weight:600}
.prosa a{color:var(--azul)}
.prosa h2{margin-top:34px}
.prosa h3{margin:26px 0 10px}
.aviso{margin:26px 0;padding:18px 22px;background:var(--blanco);border:1px solid var(--borde);border-left:3px solid var(--marigold);border-radius:var(--r-card);font-size:15.5px;color:var(--grafito)}
.aviso strong{color:var(--tinta-fuerte)}
.tabla{width:100%;border-collapse:collapse;font-size:15px}
.tabla th,.tabla td{text-align:left;padding:12px 14px;border-bottom:1px solid var(--borde);vertical-align:top}
.tabla th{font-size:12px;text-transform:uppercase;letter-spacing:.04em;color:var(--piedra);font-weight:600}
.tabla td:first-child{font-weight:600;color:var(--tinta-fuerte);white-space:nowrap}
.tabla-caja{overflow-x:auto;background:var(--blanco);border:1px solid var(--borde);border-radius:var(--r-card)}
.cierre{margin:56px 0 88px;background:var(--blanco);border:1px solid var(--borde);border-radius:var(--r-card);padding:30px;text-align:center}
.cierre h2{margin:0 0 10px}
.cierre p{color:var(--grafito);margin-bottom:20px;max-width:52ch;margin-left:auto;margin-right:auto}
footer{background:var(--medianoche);color:#c6cbe0;padding:52px 0 34px}
.foot-rejilla{display:grid;grid-template-columns:repeat(auto-fit,minmax(158px,1fr));gap:28px 24px;margin-bottom:34px}
.foot-rejilla > :first-child{grid-column:span 2;min-width:0}
.foot-titulo{font-size:12px;text-transform:uppercase;letter-spacing:.05em;color:#8b93b5;margin:0 0 12px;font-weight:600}
.foot-col a{display:block;font-size:14px;color:#c6cbe0;text-decoration:none;padding:4px 0;transition:color .2s ease}
.foot-col a:hover{color:#fff}
.foot-marca{display:flex;align-items:center;gap:9px;margin-bottom:12px}
.foot-marca svg{width:26px;height:26px}
.foot-marca .wordmark{font-size:18px;color:#fff}
.foot-marca .wordmark i{color:var(--verde)}
.foot-nota{font-size:14px;color:#8b93b5;max-width:34ch;line-height:1.55}
.foot-bajo{border-top:1px solid rgba(255,255,255,.1);padding-top:20px;display:flex;gap:18px;flex-wrap:wrap;justify-content:space-between;align-items:center}
.foot-bajo a{font-size:13.5px;color:#8b93b5;text-decoration:none}
.foot-bajo a:hover{color:#fff}
footer small{font-size:13.5px;color:#8b93b5}
.skip{position:absolute;left:-9999px;top:0;z-index:100;background:var(--tinta-fuerte);color:#fff;padding:12px 18px;border-radius:0 0 var(--r-btn) 0;text-decoration:none}
.skip:focus{left:0}
:focus-visible{outline:2px solid var(--azul);outline-offset:3px}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}.revela{opacity:1;transform:none;transition:none}.marca-svg .mc-b{animation:none}*{transition-duration:.01ms!important}}
@media(max-width:980px){
  .rejilla,.rejilla-2{grid-template-columns:1fr}
  .menu-btn{display:flex}
  /* El menu completo baja bajo la barra. Cerrado va con visibility:hidden
     y no solo con opacidad, para que el tabulador no entre en enlaces que
     no se ven. */
  .nav-links{
    position:absolute;left:0;right:0;top:100%;margin:0;
    flex-direction:column;align-items:stretch;gap:0;
    padding:10px 16px 18px;max-height:78vh;overflow-y:auto;
    background:var(--blanco);border-bottom:1px solid var(--borde);
    box-shadow:0 12px 24px rgba(0,0,0,.06);
    visibility:hidden;opacity:0;transform:translateY(-10px);
    transition:opacity .2s ease,transform .26s cubic-bezier(.22,1,.36,1),visibility 0s .2s;
  }
  .nav.abierta .nav-links{visibility:visible;opacity:1;transform:none;transition-delay:0s}
  .nav-links > a,.area > button{width:100%;justify-content:space-between;padding:13px 12px;font-size:16px}
  .despliegue{position:static;translate:none;transform:none;visibility:visible;opacity:1;
         min-width:0;box-shadow:none;border:0;border-left:2px solid var(--borde);
         border-radius:0;margin:0 0 8px 12px;padding:2px 0 2px 10px;display:none}
  .despliegue.doble{grid-template-columns:1fr;min-width:0}
  .area[data-abierta] .despliegue{display:grid}
  .despliegue a span{display:none}
}
'''

PIE_JS = '''<script>
/* -- Entrada al aparecer ------------------------------------- */
(function(){
  var piezas=document.querySelectorAll(".revela");
  if(window.matchMedia("(prefers-reduced-motion: reduce)").matches||!("IntersectionObserver" in window)){
    for(var i=0;i<piezas.length;i++)piezas[i].classList.add("visible");return;
  }
  var obs=new IntersectionObserver(function(es){es.forEach(function(e){
    if(e.isIntersecting){e.target.classList.add("visible");obs.unobserve(e.target);}
  });},{threshold:.1,rootMargin:"0px 0px -50px 0px"});
  for(var j=0;j<piezas.length;j++)obs.observe(piezas[j]);
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
document.getElementById("anio").textContent=new Date().getFullYear();
</script>'''


def _panel(base, grupos, doble=False):
    """Un panel del menu. `grupos` son pares (titulo, [(ruta, nombre, pie)])."""
    filas = []
    for titulo, entradas in grupos:
        if titulo:
            filas.append('        <p class="titulo-grupo">%s</p>' % titulo)
        for ruta, nombre, pie_txt in entradas:
            filas.append('        <a href="%s/%s"><b>%s</b><span>%s</span></a>' % (base, ruta, nombre, pie_txt))
    return '      <div class="despliegue%s">\n%s\n      </div>' % (" doble" if doble else "", "\n".join(filas))


def cabecera(base=""):
    modulos = [("funcionalidades/%s/" % s, n, d) for s, n, d in MODULOS]
    capacidades = [("funcionalidades/%s/" % s, n, d) for s, n, d in CAPACIDADES]
    return '''<a class="skip" href="#contenido">Saltar al contenido</a>
<nav class="nav" aria-label="Principal">
  <div class="nav-in">
    <a class="marca" href="%(base)s/">%(marca)s<span class="wordmark">cont<i>aes</i></span></a>
    <div class="nav-links" id="nav-links">
      <div class="area">
        <button type="button" aria-expanded="false">Gestoría <span class="punta" aria-hidden="true"></span></button>
%(panel_gestoria)s
      </div>
      <div class="area">
        <button type="button" aria-expanded="false">Crecimiento <span class="punta" aria-hidden="true"></span></button>
%(panel_crecimiento)s
      </div>
      <div class="area">
        <button type="button" aria-expanded="false">Software <span class="punta" aria-hidden="true"></span></button>
%(panel_software)s
      </div>
      <div class="area">
        <button type="button" aria-expanded="false">Para quién <span class="punta" aria-hidden="true"></span></button>
%(panel_publico)s
      </div>
      <div class="area">
        <button type="button" aria-expanded="false">Recursos <span class="punta" aria-hidden="true"></span></button>
%(panel_recursos)s
      </div>
      <a href="%(base)s/precios/">Precios</a>
    </div>
    <button type="button" class="menu-btn" id="menu-btn" aria-expanded="false" aria-controls="nav-links" aria-label="Abrir el menu">
      <span class="mb-linea"></span><span class="mb-linea"></span><span class="mb-linea"></span>
    </button>
    <a class="btn btn-azul" href="%(base)s/demo/">Hablemos <span class="flecha" aria-hidden="true">&rarr;</span></a>
  </div>
</nav>''' % {
        "base": base,
        "marca": MARCA_SVG,
        "panel_gestoria": _panel(base, [("", [("gestoria/%s/" % s, n, d) for s, n, d in GESTORIA])]),
        "panel_crecimiento": _panel(base, [("", [("crecimiento/%s/" % s, n, d) for s, n, d in CRECIMIENTO])], doble=True),
        "panel_software": _panel(base, [("Los ocho módulos", modulos), ("Lo que lo hace distinto", capacidades)], doble=True),
        "panel_publico": _panel(base, [("Por tipo de empresa", [("para/%s/" % s, n, d) for s, n, d in PUBLICO]),
                                       ("Por sector", [("sectores/%s/" % s, n, d) for s, n, d in SECTORES])], doble=True),
        "panel_recursos": _panel(base, [("", [(r, n, d) for r, n, d in RECURSOS])]),
    }


def pie(base=""):
    def col(titulo, entradas):
        enlaces = "".join('      <a href="%s/%s">%s</a>\n' % (base, r, n) for r, n in entradas)
        # Etiqueta de un grupo de enlaces, no titulo de contenido: iba como
        # <h4> justo detras de un <h1> y rompia el orden de titulos de la
        # pagina para quien navega con lector de pantalla.
        return ('    <nav class="foot-col" aria-label="%s">\n'
                '      <p class="foot-titulo">%s</p>\n%s    </nav>' % (titulo, titulo, enlaces))

    return '''<footer>
  <div class="wrap">
  <div class="foot-rejilla">
    <div class="foot-col">
      <div class="foot-marca">%(marca)s<span class="wordmark">cont<i>aes</i></span></div>
      <p class="foot-nota">Un ERP con IA y una asesoría detrás. La IA mantiene la contabilidad al día y prepara los modelos; un asesor los revisa, los firma y los presenta.</p>
    </div>
%(producto)s
%(sectores)s
%(recursos)s
%(recursos2)s
%(empresa)s
  </div>
  <div class="foot-bajo">
    <small>&copy; <span id="anio">2026</span> Contaes &middot; En desarrollo</small>
    <nav aria-label="Legal" style="display:flex;gap:18px;flex-wrap:wrap">
%(legal)s
    </nav>
  </div>
  </div>
</footer>''' % {
        "marca": MARCA_BLANCA,
        "producto": col("Gestoría", [("gestoria/%s/" % s, n) for s, n, _ in GESTORIA]
                        + [("funcionalidades/", "El software")]),
        "sectores": col("Crecimiento", [("crecimiento/%s/" % s, n) for s, n, _ in CRECIMIENTO]),
        "recursos": col("Para quién", [("para/%s/" % s, n) for s, n, _ in PUBLICO]
                        + [("sectores/", "Por sector")]),
        "recursos2": col("Recursos", [(r, n) for r, n, _ in RECURSOS]),
        "empresa": col("Empresa", [(r, n) for r, n, _ in EMPRESA]),
        "legal": "".join('      <a href="%s/%s">%s</a>\n' % (base, r, n) for r, n in LEGAL),
    }


def pagina(titulo, descripcion, url, cuerpo, extra_head="", base="", noindex=False, extra_css=""):
    return '''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(titulo)s</title>
<meta name="description" content="%(desc)s">
<link rel="canonical" href="%(url)s">
%(robots)s<meta name="theme-color" content="#f6f5f4">
<link rel="icon" href="%(base)s/assets/logo.svg" type="image/svg+xml">
<meta property="og:site_name" content="Contaes">
<meta property="og:title" content="%(titulo)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_ES">
<meta property="og:url" content="%(url)s">
<meta property="og:image" content="%(dominio)s/assets/og.png">
<meta name="twitter:card" content="summary_large_image">
%(extra)s
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400..700&family=Quicksand:wght@600&family=Source+Serif+4:opsz,wght@8..60,400&display=swap">
<style>%(estilos)s</style>
</head>
<body>
%(cabecera)s
<main id="contenido">
%(cuerpo)s
</main>
%(pie)s
%(js)s
</body>
</html>
''' % {
        "titulo": titulo, "desc": descripcion, "url": url, "base": base,
        "robots": '<meta name="robots" content="noindex, follow">\n' if noindex else "",
        "dominio": DOMINIO, "extra": extra_head, "estilos": ESTILOS + extra_css,
        "cabecera": cabecera(base), "cuerpo": cuerpo, "pie": pie(base), "js": PIE_JS,
    }
