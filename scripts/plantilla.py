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
/* ── Diagramas ───────────────────────────────────────────── */
.dibujo{
  background:var(--blanco);border:1px solid var(--borde);border-radius:var(--r-card);
  padding:26px 24px 20px;margin:0;overflow:hidden;
}
.dibujo svg{width:100%;height:auto;display:block}
.dibujo figcaption{
  margin-top:16px;font-size:14px;color:var(--piedra);line-height:1.5;
  padding-top:14px;border-top:1px solid var(--borde);
}
.dibujo .et{font:500 13px/1 var(--sans);fill:var(--tinta-fuerte)}
.dibujo .et-p{font:400 11.5px/1 var(--sans);fill:var(--piedra)}
.dibujo .caja{fill:var(--papel);stroke:var(--borde)}
.dibujo .caja-viva{fill:var(--azul-tinte);stroke:rgba(0,117,222,.3)}
.dibujo .linea{stroke:var(--borde);stroke-width:1.5;fill:none}
.dibujo .barra{fill:var(--azul)}

/* el punto que recorre el flujo: es lo que convierte cuatro cajas en un
   proceso con direccion */
.viaja{animation:viaja 5.2s cubic-bezier(.5,0,.5,1) infinite}
@keyframes viaja{
  0%,6%    {transform:translateX(0);opacity:0}
  10%      {opacity:1}
  28%,34%  {transform:translateX(var(--p1))}
  52%,58%  {transform:translateX(var(--p2))}
  76%,88%  {transform:translateX(var(--p3));opacity:1}
  96%,100% {transform:translateX(var(--p3));opacity:0}
}
/* cada caja se enciende cuando el punto llega a ella */
.enciende{animation:enciende-caja 5.2s linear infinite}
@keyframes enciende-caja{0%,100%{opacity:0}}
.paso-1 .enciende{animation-delay:0s}
.paso-2 .enciende{animation-delay:1.35s}
.paso-3 .enciende{animation-delay:2.7s}
.paso-4 .enciende{animation-delay:4s}

/* la linea que se dibuja sola */
.traza{stroke-dasharray:var(--largo);stroke-dashoffset:var(--largo);
       animation:traza 3.4s cubic-bezier(.4,0,.2,1) infinite}
@keyframes traza{0%{stroke-dashoffset:var(--largo)}45%,80%{stroke-dashoffset:0}100%{stroke-dashoffset:0;opacity:0}}

/* algo que cae en su sitio */
.cae{animation:cae 4.4s cubic-bezier(.3,1.3,.5,1) infinite}
@keyframes cae{0%,10%{transform:translateY(-22px);opacity:0}24%,86%{transform:none;opacity:1}96%,100%{opacity:0}}
.cae-2{animation-delay:.5s}
.cae-3{animation-delay:1s}
.cae-4{animation-delay:1.5s}

/* el sello que aparece al final */
.sella{animation:sella 4.4s cubic-bezier(.2,1.6,.4,1) infinite;transform-origin:center}
@keyframes sella{0%,54%{transform:scale(1.7) rotate(-8deg);opacity:0}64%,88%{transform:none;opacity:1}96%,100%{opacity:0}}

/* la barra que crece */
.crece{transform-origin:center bottom;animation:crece 3.8s cubic-bezier(.3,1,.4,1) infinite}
@keyframes crece{0%,8%{transform:scaleY(.06)}40%,84%{transform:scaleY(1)}96%,100%{transform:scaleY(1);opacity:.35}}
.crece-2{animation-delay:.12s}
.crece-3{animation-delay:.24s}
.crece-4{animation-delay:.36s}
.crece-5{animation-delay:.48s}
.crece-6{animation-delay:.6s}

/* dos columnas que se emparejan */
.casa{animation:casa 4.6s ease-in-out infinite}
@keyframes casa{0%,14%{opacity:0}26%,86%{opacity:1}96%,100%{opacity:0}}
.casa-2{animation-delay:.55s}
.casa-3{animation-delay:1.1s}

@media(prefers-reduced-motion:reduce){
  .viaja,.enciende,.traza,.cae,.sella,.crece,.casa{animation:none}
  .enciende{opacity:1}
  .traza{stroke-dashoffset:0}
  .viaja{opacity:1;transform:translateX(var(--p3))}
}
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
