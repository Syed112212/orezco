#!/usr/bin/env python3
"""
Genera el blog de Contaes y la pagina 404.

Todas las paginas comparten cascara (cabecera, pie, tokens), asi que se
escriben una sola vez aqui y el contenido de cada articulo vive en ARTICULOS.
Anadir un articulo = anadir una entrada a esa lista.

    python scripts/build-blog.py

Genera:
    404.html
    blog/index.html
    blog/<slug>.html   (uno por articulo)
    sitemap.xml        (portada + blog + articulos)

SEO: cada articulo lleva su propio title, description, canonical, OG, y
JSON-LD de tipo Article con BreadcrumbList. El sitemap se regenera entero,
asi que no puede quedarse desincronizado.
"""

import io
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMINIO = "https://contaes.com"

# ─────────────────────────────────────────────────────────────────────────
# Los articulos. El cuerpo es HTML simple: h2, p, ul, blockquote.
# Regla de contenido: informacion util y honesta sobre el problema. Nada
# de cifras de clientes, casos de exito ni promesas sobre Contaes.
# ─────────────────────────────────────────────────────────────────────────
ARTICULOS = [
    {
        "slug": "modelos-que-presenta-una-pyme-cada-ano",
        "titulo": "Los modelos que presenta una pyme cada año",
        "descripcion": "303, 111, 115, 130, 349, 347, 390, 190 y 200: qué es cada modelo, cuándo se presenta y de dónde salen los datos. Un calendario claro para empresarios que no son fiscalistas.",
        "fecha": "2026-09-02",
        "minutos": 9,
        "tema": "Fiscalidad",
        "acento": "cielo",
        "entradilla": "Nadie monta una empresa para aprenderse los modelos de Hacienda. Pero conviene saber cuáles te tocan y de dónde sale cada número.",
        "cuerpo": """
<h2>Los trimestrales</h2>
<p>Son los que marcan el ritmo del año. Se presentan en los veinte primeros días de abril, julio y octubre, y el del cuarto trimestre en enero.</p>
<ul>
  <li><strong>Modelo 303 — IVA.</strong> La diferencia entre el IVA que has repercutido en tus facturas y el que has soportado en las compras. Sale directo del libro de facturas emitidas y recibidas: si la contabilidad está al día, el 303 ya está hecho.</li>
  <li><strong>Modelo 111 — retenciones de IRPF.</strong> Lo que has retenido a trabajadores y a profesionales que te facturan con retención. Sale de las nóminas y de las facturas recibidas de autónomos.</li>
  <li><strong>Modelo 115 — retenciones por alquiler.</strong> Solo si alquilas local u oficina y practicas retención al arrendador.</li>
  <li><strong>Modelo 130 — pago fraccionado de IRPF.</strong> Para autónomos en estimación directa. Una sociedad no lo presenta.</li>
  <li><strong>Modelo 349 — operaciones intracomunitarias.</strong> Si compras o vendes a otros países de la UE. Su periodicidad depende del volumen.</li>
</ul>

<h2>Los anuales</h2>
<ul>
  <li><strong>Modelo 390 — resumen anual de IVA.</strong> En enero. Es la suma de los cuatro 303, y por eso cuadra o no cuadra: si durante el año hubo correcciones que no se rehicieron, aquí salta.</li>
  <li><strong>Modelo 190 — resumen anual de retenciones.</strong> También en enero, y hace el mismo papel respecto a los 111.</li>
  <li><strong>Modelo 347 — operaciones con terceros.</strong> En febrero. Declara a quién le has comprado o vendido más de 3.005,06 € en el año. Es el que más discrepancias genera, porque la otra parte declara lo mismo desde su lado y los importes tienen que casar.</li>
  <li><strong>Modelo 200 — Impuesto de Sociedades.</strong> Para ejercicios que cierran el 31 de diciembre, se presenta en julio.</li>
</ul>

<h2>Por qué casi todos los errores vienen del mismo sitio</h2>
<p>Los modelos no se rellenan: se calculan. Cada casilla sale de un dato que ya está en la contabilidad. Cuando algo falla, casi nunca es que alguien haya escrito mal un número en el formulario — es que el dato de origen estaba mal clasificado.</p>
<p>Los tres casos que más se repiten:</p>
<ul>
  <li>Una factura de proveedor clasificada en la cuenta equivocada, que mete un IVA soportado donde no toca.</li>
  <li>Un profesional al que se le paga sin practicar la retención que le corresponde.</li>
  <li>Una operación intracomunitaria tratada como nacional, que descuadra el 349 y arrastra al 303.</li>
</ul>

<h2>La consecuencia práctica</h2>
<p>Si la contabilidad está al día y bien clasificada, los modelos son casi automáticos. Si no lo está, cada trimestre se convierte en una semana de revisar hacia atrás. Ahí es donde se va el tiempo: no en presentar, en cuadrar antes de presentar.</p>
<p>Por eso tiene sentido que el sistema que lleva las facturas sea el mismo que prepara los modelos. Cada traspaso de datos entre programas —o de la empresa a la asesoría por correo— es una oportunidad de que algo se pierda o llegue tarde.</p>

<blockquote>Este artículo es una guía general. Los plazos y las obligaciones concretas dependen de tu situación: confírmalos siempre con tu asesor.</blockquote>
"""
    },
    {
        "slug": "cambiar-de-asesoria-sin-perder-el-historico",
        "titulo": "Cambiar de asesoría sin perder el histórico",
        "descripcion": "Qué documentación tienes derecho a llevarte, en qué momento del año conviene cambiar y cómo evitar quedarte sin poder consultar los años anteriores.",
        "fecha": "2026-09-02",
        "minutos": 6,
        "tema": "Asesoría",
        "acento": "marigold",
        "entradilla": "El miedo a cambiar de asesoría casi nunca es al asesor nuevo. Es a quedarse sin los papeles de los cinco años anteriores.",
        "cuerpo": """
<h2>Lo que es tuyo y te puedes llevar</h2>
<p>La documentación contable y fiscal de tu empresa es tuya, la tenga quien la tenga. Antes de cerrar la relación conviene pedir por escrito y comprobar que llega:</p>
<ul>
  <li>Los <strong>libros contables</strong> del ejercicio en curso y de los anteriores, en un formato que se pueda abrir sin el programa de la asesoría.</li>
  <li>Los <strong>modelos presentados</strong> con su justificante de presentación.</li>
  <li>El <strong>balance de sumas y saldos</strong> a la fecha del traspaso, con el detalle que compone cada saldo.</li>
  <li>Las <strong>cuentas anuales</strong> depositadas y los libros legalizados.</li>
  <li>Los <strong>datos maestros</strong>: clientes, proveedores y su histórico de operaciones.</li>
</ul>

<h2>El momento del año importa</h2>
<p>El cambio limpio es a cierre de ejercicio: los saldos están cerrados y el asesor nuevo arranca con un punto de partida sin ambigüedad. El segundo mejor momento es a cierre de trimestre, con los modelos ya presentados.</p>
<p>Cambiar a mitad de trimestre es posible, pero obliga a repartir la responsabilidad de un mismo periodo entre dos despachos, y ahí es donde se cuelan los huecos.</p>

<h2>Las tres preguntas que conviene hacer antes de firmar</h2>
<ul>
  <li><strong>¿Quién firma y presenta?</strong> Conviene saber el nombre de la persona colegiada que asume la responsabilidad, no solo el del despacho.</li>
  <li><strong>¿En qué formato me devolveréis los datos si algún día me voy?</strong> Si la respuesta es vaga, ya sabes cómo será la salida.</li>
  <li><strong>¿Qué pasa si Hacienda requiere algo de un año que llevabais vosotros?</strong> Debe estar claro por escrito quién responde y hasta cuándo.</li>
</ul>

<h2>El error más caro: no solapar</h2>
<p>Cortar con la asesoría antigua el mismo día que empieza la nueva deja un periodo sin nadie que responda. Merece la pena solapar unas semanas, aunque cueste, para que quien se va pueda aclarar dudas de lo que hizo.</p>
<p>Es el mismo principio que en una migración de sistema: la convivencia temporal no es un lujo, es lo que evita el agujero.</p>

<blockquote>Este artículo es orientativo y no sustituye al criterio de un profesional sobre tu caso concreto.</blockquote>
"""
    },
    {
        "slug": "migrar-de-odoo-sin-parar-la-empresa",
        "titulo": "Migrar de Odoo sin parar la empresa",
        "descripcion": "Qué mirar antes de cambiar de ERP: el traspaso de datos con histórico, el periodo de convivencia y el punto de retorno. Una guía práctica para pymes.",
        "fecha": "2026-09-02",
        "minutos": 7,
        "tema": "Migración",
        "acento": "marigold",
        "entradilla": "El día del cambio la empresa tiene que seguir facturando. Todo lo demás se puede planificar; eso no se puede parar.",
        "cuerpo": """
<h2>El error de plantearlo como un corte</h2>
<p>La mayoría de las migraciones se plantean como un salto: el viernes se apaga el sistema viejo, el lunes se enciende el nuevo. Suena limpio y casi nunca lo es. Los datos tardan más de lo previsto, aparecen casos que nadie contempló, y el lunes hay que facturar igual.</p>
<p>La alternativa es tratar la migración como un periodo, no como un instante. Durante unas semanas los dos sistemas coexisten: el antiguo en solo lectura, para consultar y comparar; el nuevo operando. Nadie se queda sin poder mirar un dato del año pasado.</p>

<h2>Los datos se traen con su histórico</h2>
<p>Hay una tentación grande al migrar: arrancar con saldos iniciales y olvidarse del pasado. Es rápido y es un error caro. En cuanto llega la primera reclamación de un cliente sobre una factura de hace dos años, alguien tiene que volver a levantar el sistema viejo.</p>
<p>Lo que conviene traer completo:</p>
<ul>
  <li><strong>Clientes y proveedores</strong> con sus datos fiscales y su histórico de operaciones.</li>
  <li><strong>Artículos</strong> con referencias, incluidas las referencias que usa cada cliente, que suelen vivir en la cabeza de comercial.</li>
  <li><strong>Saldos contables</strong> con el detalle que los compone, no solo el total.</li>
  <li><strong>Facturas emitidas y recibidas</strong> del ejercicio en curso y del anterior, como mínimo.</li>
</ul>

<h2>El punto de retorno se define antes, no a mitad</h2>
<p>Antes de empezar hay que escribir tres cosas: qué condiciones harían abortar la migración, quién toma esa decisión, y cuánto se tarda en volver atrás. Si esas tres respuestas no existen por escrito, la vuelta atrás se improvisa el peor día posible.</p>

<h2>El equipo practica antes, con datos reales</h2>
<p>Formar al equipo con datos de ejemplo no sirve de mucho. Las dudas reales aparecen con los casos reales: el cliente que factura a tres sedes, el artículo que se vende por unidades y se compra por cajas, el proyecto que se imputa a dos centros de coste.</p>
<p>Un entorno de pruebas cargado con una copia de los datos de verdad resuelve la mayoría de esas dudas antes de que cuesten dinero.</p>

<h2>Señales de que todavía no toca migrar</h2>
<p>No todo problema con un ERP se arregla cambiándolo. Si lo que falla es que nadie ha definido los procesos, el sistema nuevo va a heredar el mismo desorden en tres meses. Y si el equipo está en plena temporada alta, la migración va a competir con el trabajo real y va a perder.</p>
"""
    },
    {
        "slug": "senales-de-que-tu-erp-se-esta-degradando",
        "titulo": "Siete señales de que tu ERP se está degradando",
        "descripcion": "Los ERP no fallan de golpe: se degradan. Siete síntomas concretos que aparecen antes de que el sistema deje de ser fiable, y qué hacer con cada uno.",
        "fecha": "2026-09-02",
        "minutos": 6,
        "tema": "Diagnóstico",
        "acento": "coral",
        "entradilla": "Un ERP rara vez se cae. Lo que hace es dejar de ser fiable poco a poco, y eso no dispara ninguna alarma.",
        "cuerpo": """
<h2>1. Hay informes que solo sabe sacar una persona</h2>
<p>Cuando el cierre mensual depende de que alguien concreto esté disponible, el sistema ya tiene un problema de diseño. No es una cuestión de formación: es que el camino para llegar al dato no está donde debería.</p>

<h2>2. Nadie sabe explicar por qué está puesto un módulo</h2>
<p>Se instaló para un caso puntual hace tres años, ese caso ya no existe, y el módulo sigue ahí. Cada uno de esos módulos añade campos, permisos y comportamientos que alguien tendrá que entender el día que algo falle.</p>

<h2>3. El equipo lleva un Excel paralelo</h2>
<p>Es la señal más honesta de todas. Si alguien mantiene una hoja aparte, es que el sistema no le da lo que necesita. Merece la pena preguntar qué hay en esa hoja antes de pedirle que la deje.</p>

<h2>4. Aparecen facturas sin enviar y nadie se ha dado cuenta</h2>
<p>Los errores silenciosos son los peligrosos. Un envío que falla y no avisa, un proceso nocturno que dejó de ejecutarse, una cola que se llenó. El sistema sigue funcionando de cara al usuario mientras acumula deuda por detrás.</p>

<h2>5. Los datos maestros están duplicados</h2>
<p>El mismo cliente dado de alta tres veces con tres grafías. En cuanto eso pasa, cualquier informe agregado miente, y nadie sabe cuánto.</p>

<h2>6. Actualizar da miedo</h2>
<p>Si nadie se atreve a subir de versión porque no se sabe qué personalizaciones se romperán, el sistema ya está congelado. Y un sistema congelado acumula riesgo de seguridad además de deuda funcional.</p>

<h2>7. Cada cambio pequeño requiere un presupuesto</h2>
<p>Cuando añadir un campo o cambiar un informe pasa por un tercero y tarda semanas, la organización deja de pedir cambios. El sistema no mejora, y la gente se adapta trabajando fuera de él. Vuelve el punto 3.</p>

<h2>Qué hacer con esto</h2>
<p>Ninguna de estas señales, por sí sola, obliga a cambiar de sistema. Tres o cuatro juntas suelen significar que el coste de mantener ya supera al de sustituir. Antes de decidir, conviene poner número a dos cosas: cuántas horas al mes se van en trabajo manual que el sistema debería hacer, y cuánto se tarda hoy en responder a una pregunta que debería ser inmediata.</p>
"""
    },
    {
        "slug": "que-deberia-hacer-la-ia-en-un-erp",
        "titulo": "Qué debería hacer la IA en un ERP (y qué no)",
        "descripcion": "La IA en gestión empresarial es útil en dos sitios concretos: enseñar los datos sin menús y ejecutar tareas rutinarias con permiso. Dónde ayuda de verdad y dónde es un riesgo.",
        "fecha": "2026-09-02",
        "minutos": 8,
        "tema": "Inteligencia artificial",
        "acento": "cielo",
        "entradilla": "El problema de la mayoría de los ERP no es que les falten datos. Es que hay que saber por dónde sacarlos.",
        "cuerpo": """
<h2>Donde la IA ayuda de verdad: llegar al dato</h2>
<p>Un ERP mediano tiene cientos de pantallas. La información está dentro, pero llegar a ella exige conocer la estructura del programa, no la del negocio. Quien pregunta «¿qué clientes me deben más de 60 días y además tienen pedidos abiertos?» está haciendo una pregunta de negocio, y tiene que traducirla a dos informes y un cruce manual.</p>
<p>Ahí es donde una IA cambia las cosas de verdad: recibe la pregunta en lenguaje natural, sabe qué tablas tocar, cruza lo que haga falta y devuelve la respuesta. No es magia, es quitar la traducción.</p>

<h2>El segundo sitio: el trabajo repetitivo</h2>
<p>Hay tareas que se hacen igual todos los meses y consumen horas: conciliar movimientos bancarios evidentes, mandar recordatorios de cobro, generar asientos periódicos, clasificar gastos recurrentes. Son trabajos donde el criterio ya está definido y lo único que falta es ejecutarlo.</p>

<h2>La regla que no se puede saltar: enseñar antes de hacer</h2>
<p>Aquí está la diferencia entre una herramienta útil y un riesgo. Cualquier acción que modifique datos —enviar, contabilizar, cambiar un estado— tiene que enseñarse antes de ejecutarse. Qué va a hacer, sobre qué registros y con qué efecto.</p>
<blockquote>Una IA que actúa sin enseñar lo que va a hacer no es automatización: es un error esperando a que alguien lo descubra en el cierre.</blockquote>

<h2>Donde la IA no debe entrar</h2>
<ul>
  <li><strong>Decisiones con criterio contable o fiscal.</strong> Puede preparar y proponer, pero la responsabilidad es de una persona.</li>
  <li><strong>Cierres y liquidaciones.</strong> Nada que se presente ante la administración debería salir sin revisión humana.</li>
  <li><strong>Inventar datos que no tiene.</strong> Si un dato no está, la respuesta correcta es «no lo tengo», no una estimación con aspecto de dato.</li>
</ul>

<h2>Cómo evaluarla antes de comprarla</h2>
<p>Tres preguntas sirven para separar lo real de la demo bonita:</p>
<ul>
  <li>¿Puede decir <em>de dónde</em> ha sacado cada cifra, con el registro concreto?</li>
  <li>¿Qué pasa cuando le preguntas algo que no puede responder?</li>
  <li>¿Qué acciones puede ejecutar sin confirmación, exactamente?</li>
</ul>
<p>Si a la tercera pregunta la respuesta no es una lista corta y clara, conviene desconfiar.</p>
"""
    },
]

ACENTOS = {"marigold": "#ffb110", "coral": "#f64932", "cielo": "#62aef0", "medianoche": "#02093a"}

MARCA_SVG = '''<svg class="marca-svg" viewBox="0 0 200 200" aria-hidden="true">
      <path class="mc-c" d="M 123.56 61.80 A 55.00 55.00 0 1 0 123.56 138.20" fill="none" stroke="#1E3A5F" stroke-width="27" stroke-linecap="round"/>
      <rect class="mc-b b1" x="113.0" y="59.5" width="74.0" height="19.0" rx="9.5" fill="#2FBF9B"/>
      <rect class="mc-b b2" x="113.0" y="90.5" width="74.0" height="19.0" rx="9.5" fill="#1F9EC4"/>
      <rect class="mc-b b3" x="113.0" y="121.5" width="62.0" height="19.0" rx="9.5" fill="#1E6FB8"/>
    </svg>'''

MARCA_BLANCA = MARCA_SVG.replace("#1E3A5F", "#ffffff").replace("#2FBF9B", "#ffffff").replace("#1F9EC4", "#ffffff").replace("#1E6FB8", "#ffffff")

ESTILOS = '''
:root{
  color-scheme:light;
  --papel:#f6f5f4;--blanco:#ffffff;--borde:rgba(0,0,0,.08);
  --tinta:rgba(0,0,0,.95);--tinta-fuerte:#000000;--grafito:#615d59;--piedra:#6a6a6a;--apagado:rgba(0,0,0,.54);
  --azul:#0075de;--azul-tinte:#e6f3fe;
  --marigold:#ffb110;--coral:#f64932;--cielo:#62aef0;--medianoche:#02093a;
  --navy:#1E3A5F;--verde:#2FBF9B;
  --ancho:1160px;--r-card:12px;--r-btn:8px;--r-pill:9999px;
  --sans:"Inter",ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  --serif:"Source Serif 4",ui-serif,Georgia,serif;
  --marca:"Quicksand",var(--sans);
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{margin:0;background:var(--papel);color:var(--tinta);font-family:var(--sans);font-size:16px;line-height:1.5;-webkit-font-smoothing:antialiased}
p{margin:0}
.wrap{max-width:var(--ancho);margin:0 auto;padding:0 24px}
.estrecho{max-width:720px}
h1{font-size:clamp(34px,5.6vw,60px);font-weight:600;line-height:1.08;letter-spacing:-.038em;margin:0;color:var(--tinta-fuerte)}
h2{font-size:clamp(23px,2.6vw,30px);font-weight:600;line-height:1.2;letter-spacing:-.02em;margin:38px 0 14px;color:var(--tinta-fuerte)}
h3{font-size:20px;font-weight:700;line-height:1.3;margin:0;color:var(--tinta-fuerte)}
.etiqueta{font-size:12px;font-weight:500;letter-spacing:.01em;color:var(--piedra);margin:0;text-transform:uppercase}
.wordmark{font-family:var(--marca);font-weight:600;letter-spacing:-.01em;color:var(--navy)}
.wordmark i{font-style:normal;color:var(--verde)}
.btn{display:inline-flex;align-items:center;gap:8px;font-size:15px;font-weight:500;line-height:1;padding:13px 20px;border-radius:var(--r-btn);text-decoration:none;border:1px solid transparent;transition:background .2s ease,transform .2s ease}
.btn-azul{background:var(--azul);color:#fff}
.btn-azul:hover,.btn-azul:focus-visible{background:#0064c0;transform:translateY(-1px)}
.nav{position:sticky;top:0;z-index:60;background:rgba(246,245,244,.86);backdrop-filter:blur(12px);box-shadow:0 .7px 1.462px rgba(0,0,0,.015),0 3px 9px rgba(0,0,0,.03)}
.nav-in{max-width:var(--ancho);margin:0 auto;padding:12px 24px;display:flex;align-items:center;gap:16px;min-height:64px}
.marca{display:flex;align-items:center;gap:9px;text-decoration:none}
.marca svg{width:32px;height:32px}
.marca span{font-size:21px}
.nav-links{display:flex;gap:4px;margin:0 auto}
.nav-links a{color:var(--apagado);font-size:15px;font-weight:500;text-decoration:none;padding:10px 14px;border-radius:var(--r-btn);transition:color .2s ease,background .2s ease}
.nav-links a:hover,.nav-links a:focus-visible{color:var(--tinta-fuerte);background:rgba(0,0,0,.04)}
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
.btn .flecha{display:inline-block;transition:transform .22s cubic-bezier(.22,1,.36,1)}
.btn:hover .flecha{transform:translateX(4px)}
.post-card{transform-style:preserve-3d}
.migas{font-size:14px;color:var(--piedra);margin-bottom:20px}
.migas a{color:var(--piedra);text-decoration:none}
.migas a:hover{color:var(--tinta-fuerte);text-decoration:underline}
.revela{opacity:0;transform:translateY(20px);transition:opacity .7s ease,transform .7s cubic-bezier(.22,1,.36,1)}
.revela.visible{opacity:1;transform:none}
article.post{padding:44px 0 80px}
.post .meta{display:flex;gap:14px;align-items:center;flex-wrap:wrap;margin:18px 0 26px;font-size:14px;color:var(--piedra)}
.tema{border-radius:var(--r-pill);padding:3px 12px;font-size:13px;font-weight:500;color:#000}
.post .entradilla{font-family:var(--serif);font-size:21px;line-height:1.55;color:var(--grafito);margin-bottom:8px}
.post .cuerpo p{margin:0 0 16px;color:var(--grafito);font-size:17px;line-height:1.65}
.post .cuerpo strong{color:var(--tinta-fuerte);font-weight:600}
.post .cuerpo ul{margin:0 0 18px;padding-left:22px;color:var(--grafito);font-size:17px;line-height:1.65}
.post .cuerpo li{margin-bottom:8px}
.post .cuerpo blockquote{margin:24px 0;padding:20px 24px;background:var(--blanco);border:1px solid var(--borde);border-radius:var(--r-card);font-family:var(--serif);font-size:19px;line-height:1.5;color:var(--tinta-fuerte)}
.cierre-post{margin-top:44px;background:var(--blanco);border:1px solid var(--borde);border-radius:var(--r-card);padding:28px}
.cierre-post h3{margin-bottom:8px}
.cierre-post p{color:var(--grafito);margin-bottom:18px}
.rejilla{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}
.post-card{background:var(--blanco);border:1px solid var(--borde);border-radius:var(--r-card);overflow:hidden;text-decoration:none;color:inherit;display:grid;transition:transform .22s ease,border-color .22s ease}
.post-card:hover{transform:translateY(-4px);border-color:rgba(0,0,0,.18)}
.post-card .franja{height:7px}
.post-card .dentro{padding:22px}
.post-card .tema{display:inline-block;margin-bottom:12px}
.post-card h3{margin-bottom:8px;font-size:19px}
.post-card p{font-size:15px;color:var(--grafito)}
.post-card .pie{margin-top:14px;font-size:13px;color:var(--piedra)}
footer{background:var(--medianoche);color:#c6cbe0;padding:44px 0;margin-top:0}
.foot-in{display:flex;gap:22px;align-items:center;flex-wrap:wrap;justify-content:space-between}
.foot-marca{display:flex;align-items:center;gap:9px}
.foot-marca svg{width:26px;height:26px}
.foot-marca .wordmark{font-size:18px;color:#fff}
.foot-marca .wordmark i{color:var(--verde)}
.foot-links{display:flex;gap:18px;flex-wrap:wrap}
.foot-links a{font-size:14px;color:#c6cbe0;text-decoration:none;transition:color .2s ease}
.foot-links a:hover{color:#fff}
footer small{font-size:14px;color:#8b93b5}
.skip{position:absolute;left:-9999px;top:0;z-index:100;background:var(--tinta-fuerte);color:#fff;padding:12px 18px;border-radius:0 0 var(--r-btn) 0;text-decoration:none}
.skip:focus{left:0}
:focus-visible{outline:2px solid var(--azul);outline-offset:3px}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}.revela{opacity:1;transform:none;transition:none}.marca-svg .mc-b{animation:none}*{transition-duration:.01ms!important}}
@media(max-width:900px){.rejilla{grid-template-columns:1fr}.nav-links{display:none}}
'''

REVELA_JS = '''<script>
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
document.getElementById("anio").textContent=new Date().getFullYear();
</script>'''


def cabecera(base=""):
    return f'''<a class="skip" href="#contenido">Saltar al contenido</a>
<nav class="nav" aria-label="Principal">
  <div class="nav-in">
    <a class="marca" href="{base}/">{MARCA_SVG}<span class="wordmark">cont<i>aes</i></span></a>
    <div class="nav-links">
      <a href="{base}/#ia">La IA</a>
      <a href="{base}/#modulos">Módulos</a>
      <a href="{base}/#migracion">Migración</a>
      <a href="{base}/blog/">Blog</a>
      <a href="{base}/#preguntas">Preguntas</a>
    </div>
    <a class="btn btn-azul" href="{base}/#contacto">Pedir una demo <span class="flecha" aria-hidden="true">&rarr;</span></a>
  </div>
</nav>'''


def pie(base=""):
    return f'''<footer>
  <div class="wrap foot-in">
    <div class="foot-marca">{MARCA_BLANCA}<span class="wordmark">cont<i>aes</i></span></div>
    <nav class="foot-links" aria-label="Pie">
      <a href="{base}/#ia">La IA</a>
      <a href="{base}/#modulos">Módulos</a>
      <a href="{base}/blog/">Blog</a>
      <a href="{base}/#preguntas">Preguntas</a>
      <a href="{base}/#contacto">Contacto</a>
    </nav>
    <small>&copy; <span id="anio">2026</span> Contaes</small>
  </div>
</footer>'''


def pagina(titulo, descripcion, url, cuerpo, extra_head="", base=""):
    return f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo}</title>
<meta name="description" content="{descripcion}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#f6f5f4">
<link rel="icon" href="{base}/assets/logo.svg" type="image/svg+xml">
<meta property="og:site_name" content="Contaes">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{descripcion}">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_ES">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMINIO}/assets/og.png">
<meta name="twitter:card" content="summary_large_image">
{extra_head}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400..700&family=Quicksand:wght@600&family=Source+Serif+4:opsz,wght@8..60,400&display=swap">
<style>{ESTILOS}</style>
</head>
<body>
{cabecera(base)}
<main id="contenido">
{cuerpo}
</main>
{pie(base)}
{REVELA_JS}
</body>
</html>
'''


def construir_articulo(a):
    url = "%s/blog/%s.html" % (DOMINIO, a["slug"])
    color = ACENTOS[a["acento"]]
    ld = '''<script type="application/ld+json">
{
  "@context":"https://schema.org","@type":"Article",
  "headline":"%s","description":"%s",
  "datePublished":"%s","dateModified":"%s","inLanguage":"es",
  "mainEntityOfPage":{"@type":"WebPage","@id":"%s"},
  "author":{"@type":"Organization","name":"Contaes","url":"%s/"},
  "publisher":{"@type":"Organization","name":"Contaes","url":"%s/"}
}
</script>
<script type="application/ld+json">
{
  "@context":"https://schema.org","@type":"BreadcrumbList",
  "itemListElement":[
    {"@type":"ListItem","position":1,"name":"Inicio","item":"%s/"},
    {"@type":"ListItem","position":2,"name":"Blog","item":"%s/blog/"},
    {"@type":"ListItem","position":3,"name":"%s"}
  ]
}
</script>''' % (a["titulo"], a["descripcion"], a["fecha"], a["fecha"], url,
                DOMINIO, DOMINIO, DOMINIO, DOMINIO, a["titulo"])

    otros = [o for o in ARTICULOS if o["slug"] != a["slug"]][:2]
    tarjetas = "\n".join(
        '<a class="post-card" href="%s.html"><span class="franja" style="background:%s"></span>'
        '<span class="dentro"><span class="tema" style="background:%s">%s</span>'
        '<h3>%s</h3><p>%s</p></span></a>'
        % (o["slug"], ACENTOS[o["acento"]], ACENTOS[o["acento"]], o["tema"], o["titulo"], o["descripcion"][:110] + "…")
        for o in otros)

    cuerpo = f'''<article class="post">
  <div class="wrap estrecho">
    <p class="migas"><a href="/">Inicio</a> · <a href="/blog/">Blog</a></p>
    <span class="tema" style="background:{color}">{a["tema"]}</span>
    <h1 style="margin-top:14px">{a["titulo"]}</h1>
    <div class="meta"><time datetime="{a['fecha']}">2 de septiembre de 2026</time><span>·</span><span>{a["minutos"]} min de lectura</span></div>
    <p class="entradilla">{a["entradilla"]}</p>
    <div class="cuerpo">{a["cuerpo"]}</div>

    <div class="cierre-post revela">
      <h3>Contaes es un ERP con IA para pymes</h3>
      <p>Está en desarrollo. Si te interesa lo que cuenta este artículo, escríbenos y te avisamos cuando haya algo que enseñar.</p>
      <a class="btn btn-azul" href="/#contacto">Pedir una demo <span class="flecha" aria-hidden="true">&rarr;</span></a>
    </div>
  </div>

  <div class="wrap" style="margin-top:56px">
    <p class="etiqueta" style="margin-bottom:16px">Seguir leyendo</p>
    <div class="rejilla revela">{tarjetas}</div>
  </div>
</article>'''

    return pagina("%s — Contaes" % a["titulo"], a["descripcion"], url, cuerpo, ld, base="")


def construir_indice():
    tarjetas = "\n".join(
        '<a class="post-card" href="%s.html"><span class="franja" style="background:%s"></span>'
        '<span class="dentro"><span class="tema" style="background:%s">%s</span>'
        '<h3>%s</h3><p>%s</p><p class="pie">%s min de lectura</p></span></a>'
        % (a["slug"], ACENTOS[a["acento"]], ACENTOS[a["acento"]], a["tema"], a["titulo"], a["descripcion"], a["minutos"])
        for a in ARTICULOS)

    cuerpo = f'''<section style="padding:56px 0 80px">
  <div class="wrap">
    <p class="migas"><a href="/">Inicio</a></p>
    <h1 style="max-width:16ch">Cómo se lleva un ERP sin que se te vaya de las manos</h1>
    <p class="entradilla" style="max-width:60ch;margin-top:18px;font-family:var(--serif);font-size:20px;line-height:1.55;color:var(--grafito)">
      Lo que aprendemos construyendo Contaes: migraciones, contabilidad, y qué puede hacer de verdad la IA en un sistema de gestión.
    </p>
    <div class="rejilla revela" style="margin-top:40px">{tarjetas}</div>
  </div>
</section>'''

    ld = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Blog","name":"Blog de Contaes",
 "description":"Migraciones de ERP, contabilidad para pymes e inteligencia artificial aplicada a la gestión.",
 "url":"%s/blog/","inLanguage":"es",
 "publisher":{"@type":"Organization","name":"Contaes","url":"%s/"}}
</script>''' % (DOMINIO, DOMINIO)

    return pagina("Blog — Contaes", "Migraciones de ERP, contabilidad para pymes e inteligencia artificial aplicada a la gestión. Lo que aprendemos construyendo Contaes.",
                  "%s/blog/" % DOMINIO, cuerpo, ld, base="")


def construir_404():
    cuerpo = '''<section style="padding:96px 0 120px;text-align:center">
  <div class="wrap estrecho">
    <p class="etiqueta" style="margin-bottom:14px">Error 404</p>
    <h1>Esta página no existe</h1>
    <p style="margin:20px auto 28px;max-width:44ch;color:var(--grafito);font-size:17px">El enlace está roto o la página se movió de sitio.</p>
    <a class="btn btn-azul" href="/">Volver al inicio</a>
  </div>
</section>'''
    return pagina("Página no encontrada — Contaes", "La página que buscas no existe.",
                  "%s/404.html" % DOMINIO, cuerpo,
                  '<meta name="robots" content="noindex">', base="")


def construir_sitemap():
    urls = ["%s/" % DOMINIO, "%s/blog/" % DOMINIO]
    urls += ["%s/blog/%s.html" % (DOMINIO, a["slug"]) for a in ARTICULOS]
    filas = "\n".join(
        "  <url>\n    <loc>%s</loc>\n    <changefreq>%s</changefreq>\n    <priority>%s</priority>\n  </url>"
        % (u, "weekly" if u.endswith("/") else "monthly", "1.0" if u == urls[0] else "0.7")
        for u in urls)
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s\n</urlset>\n' % filas


def main():
    os.makedirs(os.path.join(RAIZ, "blog"), exist_ok=True)

    salidas = {"404.html": construir_404(),
               os.path.join("blog", "index.html"): construir_indice(),
               "sitemap.xml": construir_sitemap()}
    for a in ARTICULOS:
        salidas[os.path.join("blog", a["slug"] + ".html")] = construir_articulo(a)

    for ruta, contenido in sorted(salidas.items()):
        with io.open(os.path.join(RAIZ, ruta), "w", encoding="utf-8") as f:
            f.write(contenido)
        print("  %-52s %6d bytes" % (ruta.replace(os.sep, "/"), len(contenido)))

    print()
    print("  %d articulos, %d URLs en el sitemap" % (len(ARTICULOS), len(ARTICULOS) + 2))


if __name__ == "__main__":
    main()
