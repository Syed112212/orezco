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
    ("herramientas/", "Calculadoras", "Coste de contratar, punto de equilibrio, IVA"),
    ("glosario/", "Glosario", "Los términos de contabilidad y fiscalidad, explicados"),
    ("calendario-fiscal/", "Calendario fiscal", "Qué modelo toca y cuándo"),
    ("preguntas/", "Preguntas frecuentes", "Lo que suelen preguntarnos"),
]

EMPRESA = [
    ("sobre/", "Sobre Contaes", "Qué estamos construyendo y por qué"),
    ("comparativa/", "Cómo se compara", "Frente a una gestoría con programa aparte"),
    ("migracion/", "Migración", "Cómo se cambia de sistema sin parar"),
    ("seguridad/", "Seguridad y datos", "Dónde viven tus datos y qué derechos tienes"),
    ("precios/", "Precios", "Lo que sabemos hoy sobre el precio"),
    ("formulario/", "Cuéntanos tu caso", "El formulario, en una página aparte"),
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

import dibujos as _D
import formulario as _F

ESTILOS = '''
:root{
  color-scheme:light;
  --papel:#f6f5f4;--blanco:#ffffff;--borde:rgba(0,0,0,.08);--niebla:#f8fafb;
  --tinta:rgba(0,0,0,.95);--tinta-fuerte:#000000;--grafito:#615d59;--piedra:#636363;--apagado:rgba(0,0,0,.54);
  --azul:#006bcb;--azul-tinte:#e6f3fe;
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

/* Un bloque de texto que no tiene indice al lado no se centra: se alinea
   con el titular y con todo lo demas de la pagina. Centrado en una
   columna de 760px dentro de una de 1160 quedaba flotando en el medio,
   con hueco a los dos lados y sin alinearse con nada. */
.seccion > .wrap.estrecho{max-width:var(--ancho)}
.seccion > .wrap.estrecho > *{max-width:76ch}
.seccion > .wrap.estrecho > .dibujo,
.seccion > .wrap.estrecho > .incluye{max-width:none}

/* ── La pagina del formulario ────────────────────────────────────────
   El formulario a la izquierda y, al lado, lo que pasa despues de darle
   a enviar. Es la duda que tiene todo el que deja su telefono en una
   web, asi que va junto al boton y no tres secciones mas abajo. */
.formulario-rejilla{display:grid;grid-template-columns:minmax(0,1fr) 300px;
  gap:clamp(24px,4vw,56px);align-items:start}
.form-lado{position:sticky;top:92px}
.form-lado-caja{background:var(--blanco);border:1px solid var(--borde);
  border-radius:12px;padding:24px}
.pasos-lado{margin:0;padding:0;list-style:none;counter-reset:paso}
.pasos-lado li{position:relative;padding:0 0 18px 0;font-size:14px;
  line-height:1.5;color:var(--grafito)}
.pasos-lado li:last-child{padding-bottom:0}
.pasos-lado b{display:block;color:var(--tinta-fuerte);font-weight:600;
  font-size:15px;margin-bottom:3px}
.form-lado-nota{margin:20px 0 0;padding-top:16px;font-size:13px;
  line-height:1.5;color:var(--piedra);border-top:1px solid var(--borde)}
@media(max-width:900px){
  .formulario-rejilla{grid-template-columns:1fr;gap:22px}
  .form-lado{position:static;order:-1}
}

/* ── Encabezado y lectura a dos columnas ─────────────────────────────
   Una columna de 760px centrada en una pantalla de 1400 deja media
   pagina vacia a cada lado y hace que la pagina parezca un documento
   sin maquetar. El titular ocupa su lado y la entradilla el suyo. */
.enc-rejilla{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);
  gap:clamp(26px,4.5vw,68px);align-items:start}
.enc-rejilla h1{margin:10px 0 0}
.enc-lado{padding-top:6px}
.enc-lado .editorial{margin-top:0;max-width:46ch}
.enc-corto{margin:20px 0 0;padding:0;list-style:none;
  border-top:1px solid var(--borde)}
.enc-corto li{display:flex;gap:12px;padding:11px 0;font-size:15px;
  line-height:1.45;color:var(--grafito);border-bottom:1px solid var(--borde)}
.enc-corto b{color:var(--tinta-fuerte);font-weight:600;flex:0 0 auto;min-width:88px}

/* La lectura con su indice al lado. Son las secciones reales de la
   pagina, asi que ademas de llenar el hueco sirven para saltar. */
.lectura{display:grid;grid-template-columns:190px minmax(0,1fr);
  gap:clamp(22px,4vw,60px);align-items:start}
.indice{position:sticky;top:92px}
.indice p{margin:0 0 12px;font-size:12px;letter-spacing:.08em;
  text-transform:uppercase;color:var(--piedra);font-weight:600}
.indice ol{margin:0;padding:0;list-style:none;
  border-left:1px solid var(--borde)}
.indice li{margin:0}
.indice a{display:block;padding:7px 0 7px 14px;margin-left:-1px;
  border-left:2px solid transparent;color:var(--grafito);
  font-size:14px;line-height:1.4;text-decoration:none}
.indice a:hover,.indice a:focus-visible{color:var(--tinta-fuerte);
  border-left-color:var(--azul)}
.lectura .prosa > h2:first-child{margin-top:0}

@media(max-width:900px){
  .enc-rejilla{grid-template-columns:1fr;gap:18px;align-items:start}
  .enc-lado{padding-bottom:0}
  .lectura{grid-template-columns:1fr;gap:18px}
  .indice{position:static}
  .indice ol{display:flex;flex-wrap:wrap;gap:6px;border-left:0}
  .indice a{padding:6px 12px;border:1px solid var(--borde);
    border-radius:9999px;margin-left:0;font-size:13px}
  .indice a:hover,.indice a:focus-visible{border-color:var(--azul)}
}

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
.despliegue a{display:flex;gap:11px;align-items:flex-start;padding:9px 12px;border-radius:var(--r-btn);text-decoration:none;transition:background .16s ease}
.op-ico{flex:0 0 auto;width:19px;height:19px;margin-top:1px;fill:none;stroke:var(--piedra);
  stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round;transition:stroke .16s ease}
.despliegue a:hover .op-ico,.despliegue a:focus-visible .op-ico{stroke:var(--azul)}
.ml-texto{display:grid;gap:2px;min-width:0}
/* La linea entre grupos dice donde acaba un area y empieza otra, que en
   un panel de veinte enlaces no se ve solo con el espacio. */
.despliegue.doble .titulo-grupo:not(:first-child){
  border-top:1px solid var(--borde);margin-top:8px;padding-top:14px;
}
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
.revela.espera{opacity:0;transform:translateY(20px);transition:opacity .7s ease,transform .7s cubic-bezier(.22,1,.36,1)}
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
/* ── El aviso de cookies ─────────────────────────────────────────────
   Abajo y estrecho, no una cortina que tape la pagina. Las dos opciones
   pesan lo mismo: un "rechazar" escondido no es un consentimiento. */
.cookies{position:fixed;left:16px;right:16px;bottom:16px;z-index:80;
  max-width:640px;margin:0 auto;background:var(--blanco);
  border:1px solid var(--borde);border-radius:12px;
  box-shadow:0 12px 32px rgba(0,0,0,.12);padding:18px 20px}
.cookies[hidden]{display:none}
.cookies-in{display:flex;gap:16px;align-items:center;flex-wrap:wrap}
.cookies-txt{margin:0;flex:1 1 260px;font-size:14px;line-height:1.5;
  color:var(--grafito)}
.cookies-txt b{color:var(--tinta-fuerte)}
.cookies-btns{display:flex;gap:8px;flex:0 0 auto}
.cookies-btns .btn{padding:9px 16px;font-size:14px}
@media(max-width:560px){
  .cookies-btns{width:100%;}
  .cookies-btns .btn{flex:1}
}

/*@FORM_CSS@*/

/* -- El fondo -------------------------------------------------
   Un lienzo pegado a la ventana; el contenido pasa por encima. La
   barra NO entra en la regla de apilado: ya es sticky con z-index
   60 en su bloque, y repetir 'position' aqui se lo quitaba.      */
.fondo{
  position:fixed;inset:0;z-index:0;pointer-events:none;display:block;
  width:100%;height:100%;
}
main,footer{position:relative;z-index:1}
/* En una pagina interior el fondo se aparta mas: ahi se viene a leer,
   y un fondo que compite con un parrafo largo cansa. */
body:not(.portada) .fondo{opacity:.55}
/* ── Que incluye ─────────────────────────────────────────────
   En rejilla y no en columna: siete puntos sueltos apilados se
   leen como un parrafo largo, que es justo lo que no son.      */
.incluye{list-style:none;margin:0;padding:0;
  display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:2px 34px}
.incluye li{
  display:grid;grid-template-columns:auto 1fr;gap:13px;align-items:start;
  padding:15px 0;border-bottom:1px solid var(--borde);color:var(--grafito);font-size:16px;
}
.tic{
  width:19px;height:19px;margin-top:2px;border-radius:50%;background:var(--azul-tinte);
  position:relative;
}
.tic::after{
  content:"";position:absolute;left:5.5px;top:5px;width:5px;height:8px;
  border:solid var(--azul);border-width:0 1.8px 1.8px 0;transform:rotate(45deg);
}
/* La banda clara separa esta seccion de las de alrededor sin
   necesidad de una tarjeta. */
.banda{background:var(--niebla);border-top:1px solid var(--borde);
       border-bottom:1px solid var(--borde);margin:14px 0}
.panel{border-radius:var(--r-card);padding:clamp(26px,4vw,44px);position:relative;overflow:hidden}
.panel.medianoche{background:var(--medianoche);color:#fff}
.panel.medianoche .cuerpo{color:#c6cbe0}
.panel.medianoche h2{color:#fff}
.panel .tarjeta,.panel .tarjeta h3{color:var(--tinta-fuerte)}
.panel .tarjeta .cuerpo,.panel .tarjeta p{color:var(--grafito)}

/*@DIBUJO_CSS@*/

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
/*@COOKIES_JS@*/
/*@FORM_JS@*/
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
</script>'''


# ─────────────────────────────────────────────────────────────────────
# Los iconos del menu. Trazos, no dibujos: heredan el color del texto
# y no compiten con el. Cada uno se parece a lo que nombra.
# ─────────────────────────────────────────────────────────────────────
TRAZOS = {
    "contabilidad": "M4 5h16v14H4z M4 10h16 M9 10v9",
    "fiscal": "M6 3h9l4 4v14H6z M14 3v5h5 M9 13h6 M9 17h4",
    "laboral": "M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8z M4 20a8 8 0 0 1 16 0",
    "legal": "M12 3v18 M5 8h14 M5 8l-2 6a3 3 0 0 0 6 0z M19 8l2 6a3 3 0 0 1-6 0z",
    "facturacion": "M6 3h12v18l-3-2-3 2-3-2-3 2z M9 8h6 M9 12h6",
    "inventario": "M3 8l9-5 9 5v8l-9 5-9-5z M3 8l9 5 9-5 M12 13v8",
    "compras": "M4 5h2l2 10h10l2-7H7 M9 19a1 1 0 1 0 0 2 1 1 0 0 0 0-2z M17 19a1 1 0 1 0 0 2 1 1 0 0 0 0-2z",
    "ventas": "M4 19V9 M10 19V5 M16 19v-7 M4 19h16",
    "proyectos": "M4 6h16 M4 11h10 M4 16h13 M18 14l2 2 3-4",
    "personal": "M9 11a3 3 0 1 0 0-6 3 3 0 0 0 0 6z M2 20a7 7 0 0 1 14 0 M17 6a3 3 0 0 1 0 6 M17 14a6 6 0 0 1 5 6",
    "informes": "M4 20h16 M7 16v-5 M12 16V6 M17 16v-8",
    "asesoria-fiscal": "M4 4h12l4 4v12H4z M14 4v5h5 M8 14l2.5 2.5L16 11",
    "asistente-ia": "M12 3l1.8 4.2L18 9l-4.2 1.8L12 15l-1.8-4.2L6 9l4.2-1.8z M18 15l.9 2.1L21 18l-2.1.9L18 21l-.9-2.1L15 18l2.1-.9z",
    "escaner-facturas": "M4 8V5h3 M20 8V5h-3 M4 16v3h3 M20 16v3h-3 M8 12h8",
    "conciliacion-bancaria": "M4 7h7 M4 17h7 M13 7h7 M13 17h7 M9 5l2 2-2 2 M15 15l-2 2 2 2",
    "verifactu": "M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z M9 12l2 2 4-4",
    "cfo": "M4 19h16 M7 16v-4 M12 16V7 M17 16v-6 M12 7l5-3",
    "cmo": "M3 10v4h4l5 4V6L7 10z M16 9a4 4 0 0 1 0 6 M19 6a8 8 0 0 1 0 12",
    "prospeccion": "M11 17a6 6 0 1 0 0-12 6 6 0 0 0 0 12z M15.5 15.5L21 21",
    "bots": "M12 3v3 M6 6h12v10H6z M9 10h.01 M15 10h.01 M9 19l3-3 3 3",
    "financiacion": "M12 3v18 M16 7a4 4 0 0 0-8 0c0 4 8 2 8 6a4 4 0 0 1-8 0",
    "internacionalizacion": "M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18z M3 12h18 M12 3a14 14 0 0 1 0 18 M12 3a14 14 0 0 0 0 18",
    "autonomos": "M12 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8z M5 21a7 7 0 0 1 14 0",
    "startups": "M12 3c3 2 5 5.5 5 9l-5 4-5-4c0-3.5 2-7 5-9z M12 12a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3z M9 17l-2 4 5-2 5 2-2-4",
    "pymes": "M3 21h18 M5 21V8l7-5 7 5v13 M10 21v-6h4v6",
    "blog/": "M5 4h14v16H5z M9 8h6 M9 12h6 M9 16h3",
    "glosario/": "M4 5a2 2 0 0 1 2-2h13v18H6a2 2 0 0 1-2-2z M8 8h7 M8 12h5",
    "calendario-fiscal/": "M4 6h16v14H4z M4 10h16 M8 3v4 M16 3v4 M9 14h2 M14 14h2",
    "herramientas/": "M4 4h16v16H4z M8 8h8 M8 12h2 M12 12h2 M16 12h.01 M8 16h2 M12 16h2 M16 16h.01",
    "preguntas/": "M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18z M9.5 9a2.6 2.6 0 0 1 5 1c0 1.7-2.5 2-2.5 3.5 M12 17h.01",
}



# El CSS y el JS del formulario viven en formulario.py y solo ahi. Aqui
# se sustituye una marca: interpolar con % reventaria en el primer 50%
# del CSS, que esta lleno de ellos.
ESTILOS = ESTILOS.replace("/*@FORM_CSS@*/", _F.ESTILOS.strip())
ESTILOS = ESTILOS.replace("/*@DIBUJO_CSS@*/", _D.ESTILOS.strip())
_PIE_FORM = "\n\n".join(
    x.strip() for x in (_F.JS, _F.JS_LADO, _F.JS_RASTRO))
PIE_JS = PIE_JS.replace("/*@FORM_JS@*/", _PIE_FORM)

def _icono(ruta):
    clave = ruta.rstrip("/").split("/")[-1]
    d = TRAZOS.get(clave) or TRAZOS.get(ruta) or "M5 5h14v14H5z"
    return ('<svg class="op-ico" viewBox="0 0 24 24" aria-hidden="true">'
            '<path d="%s"/></svg>' % d)


def _panel(base, grupos, doble=False):
    """Un panel del menu. `grupos` son pares (titulo, [(ruta, nombre, pie)])."""
    filas = []
    for titulo, entradas in grupos:
        if titulo:
            filas.append('        <p class="titulo-grupo">%s</p>' % titulo)
        for ruta, nombre, pie_txt in entradas:
            filas.append('        <a href="%s/%s">%s<span class="ml-texto">'
                         '<b>%s</b><span>%s</span></span></a>'
                         % (base, ruta, _icono(ruta), nombre, pie_txt))
    return '      <div class="despliegue%s">\n%s\n      </div>' % (" doble" if doble else "", "\n".join(filas))


def cabecera(base=""):
    modulos = [("funcionalidades/%s/" % s, n, d) for s, n, d in MODULOS]
    capacidades = [("funcionalidades/%s/" % s, n, d) for s, n, d in CAPACIDADES]
    return '''<a class="skip" href="#contenido">Saltar al contenido</a>
<!-- El mismo fondo que la portada: laminas flotando en un espacio con
     perspectiva. Aqui va mas tenue, porque en una pagina interior se
     viene a leer. -->
<canvas class="fondo" id="fondo" aria-hidden="true"></canvas>
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
        "panel_software": _panel(base, [("La gestión del día a día", modulos), ("Lo que lo hace distinto", capacidades)], doble=True),
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
      <p class="foot-nota">La gestoría de siempre, con el software dentro y gente que te ayuda a crecer. Contabilidad, impuestos, nóminas y contratos, más dirección financiera, captación de clientes, financiación y salida al exterior.</p>
    </div>
%(producto)s
%(sectores)s
%(recursos)s
%(recursos2)s
%(empresa)s
  </div>
  <div class="foot-bajo">
    <small>&copy; <span id="anio">2026</span> Contaes &middot; Gestoría online para autónomos, startups y pymes</small>
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
        "recursos2": col("Recursos", [(r, n) for r, n, _ in RECURSOS]
                         + [("recursos/", "Ver todo")]),
        "empresa": col("Empresa", [(r, n) for r, n, _ in EMPRESA]),
        "legal": "".join('      <a href="%s/%s">%s</a>\n' % (base, r, n) for r, n in LEGAL),
    }


def version_hoja():
    """Huella corta de la hoja comun, para el parametro de cache.

    Sin ella, un cambio de estilos no le llegaria a quien ya tuvo la
    pagina abierta: el navegador seguiria sirviendo la hoja vieja."""
    import hashlib
    return hashlib.sha1(ESTILOS.encode("utf-8")).hexdigest()[:8]


def escribe_hoja(raiz):
    """Deja la hoja comun en assets/contaes.css."""
    import os
    destino = os.path.join(raiz, "assets", "contaes.css")
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with open(destino, "w", encoding="utf-8") as f:
        f.write("/* La hoja comun del sitio. La genera plantilla.py: no se edita a mano. */" + chr(10))
        f.write(ESTILOS)
    return destino



# La etiqueta de Google y el aviso de cookies. Con nombre propio porque
# la portada, que se escribe a mano, tiene que llevarlas iguales y las
# coge de aqui en vez de tener su copia.
JS_COOKIES = '''/* -- El aviso de cookies ------------------------------------
   Sale solo si no hay respuesta guardada. Las dos opciones
   valen lo mismo y la respuesta se recuerda en el navegador,
   no en una cookie: para preguntar por cookies no hace falta
   escribir una.                                            */
(function () {
  var caja = document.getElementById("cookies");
  if (!caja) return;
  var LLAVE = "contaes:cookies";
  var guardado = null;
  try { guardado = localStorage.getItem(LLAVE); } catch (e) {}
  if (guardado) return;
  caja.hidden = false;

  caja.addEventListener("click", function (e) {
    var b = e.target.closest("[data-cookies]");
    if (!b) return;
    var si = b.getAttribute("data-cookies") === "si";
    try { localStorage.setItem(LLAVE, si ? "si" : "no"); } catch (e2) {}
    if (si && typeof gtag === "function") {
      gtag("consent", "update", {
        ad_storage: "granted",
        ad_user_data: "granted",
        ad_personalization: "granted",
        analytics_storage: "granted"
      });
    }
    caja.hidden = true;
  });
})();
'''

TAG_GOOGLE = """<!-- El consentimiento va PRIMERO: hasta que alguien acepta, la etiqueta
     de Google no puede escribir ni leer nada. Es lo que exige el
     articulo 22.2 de la LSSI y lo que promete nuestra pagina de
     cookies. -->
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('consent', 'default', {
    'ad_storage': 'denied',
    'ad_user_data': 'denied',
    'ad_personalization': 'denied',
    'analytics_storage': 'denied',
    'functionality_storage': 'granted',
    'security_storage': 'granted',
    'wait_for_update': 500
  });
  try {
    if (localStorage.getItem('contaes:cookies') === 'si') {
      gtag('consent', 'update', {
        'ad_storage': 'granted',
        'ad_user_data': 'granted',
        'ad_personalization': 'granted',
        'analytics_storage': 'granted'
      });
    }
  } catch (e) {}
</script>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-18427533910"></script>
<script>
  gtag('js', new Date());
  gtag('config', 'AW-18427533910');
</script>
"""

AVISO_COOKIES = """<div class="cookies" id="cookies" hidden>
  <div class="cookies-in">
    <p class="cookies-txt"><b>Cookies de publicidad.</b> Medimos si nuestros anuncios
      traen a alguien. Si dices que no, la web funciona igual y no se escribe nada.
      El detalle esta en la <a href="/legal/cookies/">politica de cookies</a>.</p>
    <div class="cookies-btns">
      <button type="button" class="btn btn-tinte" data-cookies="no">Solo lo necesario</button>
      <button type="button" class="btn btn-azul" data-cookies="si">Aceptar</button>
    </div>
  </div>
</div>"""


def pagina(titulo, descripcion, url, cuerpo, extra_head="", base="", noindex=False, extra_css=""):
    return '''<!doctype html>
<html lang="es">
<head>
%(tag_google)s<meta charset="utf-8">
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
<link rel="stylesheet" href="%(base)s/assets/contaes.css?v=%(version)s">
%(estilos_extra)s
</head>
<body>
%(cabecera)s
<main id="contenido">
%(cuerpo)s
</main>
%(pie)s

%(aviso_cookies)s
%(js)s
</body>
</html>
''' % {
        "titulo": titulo, "desc": descripcion, "url": url, "base": base,
        "robots": '<meta name="robots" content="noindex, follow">\n' if noindex else "",
        "dominio": DOMINIO, "extra": extra_head,
        "version": version_hoja(),
        "estilos_extra": ("<style>%s</style>" % extra_css) if extra_css else "",
        "cabecera": cabecera(base), "cuerpo": cuerpo, "pie": pie(base), "js": PIE_JS,
        "tag_google": TAG_GOOGLE, "aviso_cookies": AVISO_COOKIES,
    }


# El aviso de cookies va en todas las paginas y la portada lo coge de
# aqui, igual que la etiqueta de Google.
PIE_JS = PIE_JS.replace("/*@COOKIES_JS@*/", JS_COOKIES.strip())
