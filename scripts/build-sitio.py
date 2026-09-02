# -*- coding: utf-8 -*-
"""Genera todas las paginas del sitio salvo la portada y el blog.

    python scripts/build-sitio.py

La portada (index.html) se escribe a mano: tiene piezas propias que no
comparte nadie. El blog lo genera build-blog.py. Todo lo demas -modulos,
sectores, glosario, calendario, legal- sale de aqui, a partir de
contenido.py, contenido_paginas.py y la cascara de plantilla.py.

El sitemap se escribe aqui y no en build-blog.py porque tiene que
incluirlo todo; si lo escribieran los dos, el ultimo en ejecutarse
borraria la mitad de las URLs.
"""
import importlib.util
import io
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)

import plantilla as P
import contenido as C
import contenido_paginas as CP

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

DOMINIO = P.DOMINIO
COLORES = ["var(--verde)", "var(--cian)", "var(--azul-marca)", "var(--marigold)",
           "var(--cielo)", "var(--coral)", "var(--navy)", "var(--azul)"]


# ─────────────────────────────────────────────────────────────────────
# Piezas comunes
# ─────────────────────────────────────────────────────────────────────
def migas(*pasos):
    """El rastro de navegacion. El ultimo paso no es enlace: es donde estas."""
    trozos = []
    for i, (ruta, nombre) in enumerate(pasos):
        if i == len(pasos) - 1 or ruta is None:
            trozos.append("<span>%s</span>" % nombre)
        else:
            trozos.append('<a href="%s">%s</a>' % (ruta, nombre))
    return '<p class="migas">%s</p>' % " &rsaquo; ".join(trozos)


def encabezado(etiqueta, titulo, entradilla, rastro=""):
    return '''<section class="encabezado">
  <div class="wrap estrecho">
    %s
    <p class="etiqueta">%s</p>
    <h1 style="margin-top:10px">%s</h1>
    <p class="editorial">%s</p>
  </div>
</section>''' % (rastro, etiqueta, titulo, entradilla)


def cierre(titulo="¿Te enseñamos cómo funciona?",
           texto="Una demo sobre tu caso concreto, no una presentación genérica. "
                 "Cuéntanos qué usáis ahora y qué es lo que peor lleváis."):
    return '''<section class="wrap estrecho">
  <div class="cierre revela">
    <h2>%s</h2>
    <p>%s</p>
    <a class="btn btn-azul" href="/demo/">Pedir una demo <span class="flecha" aria-hidden="true">&rarr;</span></a>
  </div>
</section>''' % (titulo, texto)


def rejilla_tarjetas(entradas, base, columnas=3):
    """entradas: [(ruta, titulo, pie)]"""
    tarjetas = []
    for i, (ruta, titulo, pie) in enumerate(entradas):
        tarjetas.append(
            '    <a class="tarjeta" href="%s%s">\n'
            '      <span class="franja" style="background:%s"></span>\n'
            '      <h3>%s</h3>\n      <p>%s</p>\n    </a>'
            % (base, ruta, COLORES[i % len(COLORES)], titulo, pie))
    clase = "rejilla" if columnas == 3 else "rejilla-2"
    return '<div class="%s revela">\n%s\n  </div>' % (clase, "\n".join(tarjetas))


def prosa(secciones):
    trozos = []
    for h2, parrafos in secciones:
        trozos.append("<h2>%s</h2>" % h2)
        trozos.extend("<p>%s</p>" % t for t in parrafos)
    return "\n".join(trozos)


def lista_incluye(puntos):
    filas = "".join('    <li><b>&#10003;</b><span>%s</span></li>\n' % p for p in puntos)
    return '<ul class="lista">\n%s  </ul>' % filas


def nombre_de(slug):
    if slug in C.MODULOS:
        return C.MODULOS[slug]["titulo"]
    if slug in C.CAPACIDADES:
        return C.CAPACIDADES[slug]["titulo"]
    return slug


# ─────────────────────────────────────────────────────────────────────
# Paginas de modulo y de capacidad
# ─────────────────────────────────────────────────────────────────────
def pagina_funcionalidad(slug, d, es_modulo):
    rastro = migas(("/", "Inicio"), ("/funcionalidades/", "Producto"), (None, d["titulo"]))
    conecta = "".join(
        '    <li><b>%s</b><span>%s</span></li>\n'
        % ('<a href="/funcionalidades/%s/" style="color:inherit">%s</a>' % (s, nombre_de(s)), por)
        for s, por in d.get("conecta", []))

    aviso = ('<div class="aviso">%s</div>' % d["aviso"]) if d.get("aviso") else ""

    cuerpo = '''%(enc)s

<section class="seccion">
  <div class="wrap estrecho prosa revela">
%(prosa)s
%(aviso)s
  </div>
</section>

<section class="seccion">
  <div class="wrap estrecho revela">
    <h2>Qué incluye</h2>
%(incluye)s
  </div>
</section>

<section class="seccion">
  <div class="wrap estrecho revela">
    <h2>Con qué se conecta</h2>
    <p class="cuerpo" style="margin-bottom:8px">Un módulo suelto no resuelve gran cosa. Lo que cambia el trabajo del día es que lo que entra por un sitio salga ya hecho por el otro.</p>
    <ul class="lista">
%(conecta)s    </ul>
  </div>
</section>

%(cierre)s''' % {
        "enc": encabezado("Producto" if es_modulo else "Lo que lo hace distinto",
                          d["titulo"] + ". <span style=\"color:var(--grafito);font-weight:500\">" + d["lema"] + "</span>",
                          d["entradilla"], rastro),
        "prosa": prosa(d["secciones"]),
        "aviso": aviso,
        "incluye": lista_incluye(d["incluye"]),
        "conecta": conecta,
        "cierre": cierre(),
    }
    return P.pagina(
        "%s — Contaes" % d["titulo"],
        d["entradilla"][:158],
        "%s/funcionalidades/%s/" % (DOMINIO, slug),
        cuerpo)


def pagina_funcionalidades():
    rastro = migas(("/", "Inicio"), (None, "Producto"))
    cuerpo = '''%(enc)s

<section class="seccion">
  <div class="wrap">
    <h2 style="margin-top:0">Los ocho módulos</h2>
    <p class="cuerpo" style="margin-bottom:22px;max-width:60ch">Ocho áreas sobre el mismo libro mayor. Lo que se registra en una está disponible en las demás sin exportar nada.</p>
    %(modulos)s
  </div>
</section>

<section class="seccion">
  <div class="wrap">
    <h2>Lo que lo hace distinto</h2>
    <p class="cuerpo" style="margin-bottom:22px;max-width:60ch">Un ERP más no hacía falta. Lo que cambia el trabajo es que la contabilidad esté al día sola y que los modelos los presente alguien por ti.</p>
    %(capacidades)s
  </div>
</section>

%(cierre)s''' % {
        "enc": encabezado("Producto", "Ocho áreas, un solo sistema",
                          "Un ERP no es una suma de programas: es un sitio donde cada hecho se registra "
                          "una vez y aparece en todos los sitios donde hace falta.", rastro),
        "modulos": rejilla_tarjetas([("funcionalidades/%s/" % s, n, d) for s, n, d in P.MODULOS], "/"),
        "capacidades": rejilla_tarjetas([("funcionalidades/%s/" % s, n, d) for s, n, d in P.CAPACIDADES], "/"),
        "cierre": cierre(),
    }
    return P.pagina("Producto — Contaes",
                    "Los ocho módulos de Contaes y lo que lo hace distinto: asesoría fiscal incluida, asistente con IA, escáner de facturas y conciliación bancaria.",
                    "%s/funcionalidades/" % DOMINIO, cuerpo)


# ─────────────────────────────────────────────────────────────────────
# Sectores
# ─────────────────────────────────────────────────────────────────────
def pagina_sector(slug, d):
    rastro = migas(("/", "Inicio"), ("/sectores/", "Sectores"), (None, d["titulo"]))
    duele = "".join("    <li>%s</li>\n" % x for x in d["duele"])
    aporta = "".join('    <li><b>%s</b><span>%s</span></li>\n' % (t, x) for t, x in d["aporta"])
    modulos = rejilla_tarjetas(
        [("funcionalidades/%s/" % s, nombre_de(s),
          (C.MODULOS.get(s) or C.CAPACIDADES[s])["lema"]) for s in d["modulos"]], "/")

    cuerpo = '''%(enc)s

<section class="seccion">
  <div class="wrap estrecho revela prosa">
    <h2 style="margin-top:0">Lo que suele doler</h2>
    <ul>
%(duele)s    </ul>
  </div>
</section>

<section class="seccion">
  <div class="wrap estrecho revela">
    <h2>Qué cambia con Contaes</h2>
    <ul class="lista">
%(aporta)s    </ul>
  </div>
</section>

<section class="seccion">
  <div class="wrap revela">
    <h2>Los módulos que más se usan aquí</h2>
    <p class="cuerpo" style="margin-bottom:22px">Están todos disponibles; estos son los que llevan el peso en este sector.</p>
    %(modulos)s
  </div>
</section>

%(cierre)s''' % {
        "enc": encabezado("Sectores",
                          d["titulo"] + ". <span style=\"color:var(--grafito);font-weight:500\">" + d["lema"] + "</span>",
                          d["entradilla"], rastro),
        "duele": duele, "aporta": aporta, "modulos": modulos,
        "cierre": cierre("¿Se parece a lo vuestro?",
                         "En la primera llamada preferimos escuchar cómo trabajáis antes que enseñar pantallas. "
                         "Si no encajamos, se dice ahí."),
    }
    return P.pagina("ERP para %s — Contaes" % d["titulo"].lower(),
                    d["entradilla"][:158],
                    "%s/sectores/%s/" % (DOMINIO, slug), cuerpo)


def pagina_sectores():
    rastro = migas(("/", "Inicio"), (None, "Sectores"))
    cuerpo = '''%(enc)s

<section class="seccion">
  <div class="wrap">
    %(rejilla)s
  </div>
</section>

<section class="seccion">
  <div class="wrap estrecho prosa revela">
    <h2>Y si tu sector no está</h2>
    <p>Estas ocho fichas no son ocho productos distintos: es el mismo sistema contado desde el problema de cada uno. Si tu actividad no aparece, casi siempre es porque se parece a alguna de ellas.</p>
    <p>Lo que sí conviene decir claro: hay procesos muy particulares —fabricación compleja, normativa sectorial concreta— que hoy no cubrimos. Preferimos decirlo antes que después de la demo.</p>
  </div>
</section>

%(cierre)s''' % {
        "enc": encabezado("Sectores", "El mismo sistema, contado desde tu problema",
                          "Un ERP no se elige por la lista de funciones: se elige por si entiende cómo "
                          "trabaja tu negocio. Estas son las ocho formas de trabajar que tenemos más presentes.", rastro),
        "rejilla": rejilla_tarjetas([("sectores/%s/" % s, n, d) for s, n, d in P.SECTORES], "/"),
        "cierre": cierre(),
    }
    return P.pagina("Sectores — Contaes",
                    "Fabricación, distribución, construcción, comercio, logística, servicios, instalaciones y agroalimentario: el mismo ERP contado desde el problema de cada sector.",
                    "%s/sectores/" % DOMINIO, cuerpo)


# ─────────────────────────────────────────────────────────────────────
# Glosario, calendario, preguntas
# ─────────────────────────────────────────────────────────────────────
def pagina_glosario():
    rastro = migas(("/", "Inicio"), ("/#", "Recursos"), (None, "Glosario"))
    terminos = sorted(CP.GLOSARIO, key=lambda x: x[0].lower())
    filas = "".join(
        '    <div class="tarjeta revela" id="%s">\n'
        '      <p class="etiqueta" style="margin-bottom:8px">%s</p>\n'
        '      <h3>%s</h3>\n      <p style="margin-top:8px">%s</p>\n    </div>\n'
        % (t.lower().replace(" ", "-").replace("ó", "o").replace("í", "i").replace("á", "a"), fam, t, txt)
        for t, fam, txt in terminos)
    ld = ('<script type="application/ld+json">{"@context":"https://schema.org",'
          '"@type":"DefinedTermSet","name":"Glosario de contabilidad y fiscalidad",'
          '"url":"%s/glosario/"}</script>' % DOMINIO)
    cuerpo = '''%(enc)s

<section class="seccion">
  <div class="wrap" style="display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:16px">
%(filas)s  </div>
</section>

%(cierre)s''' % {
        "enc": encabezado("Recursos", "Glosario de contabilidad y fiscalidad",
                          "Los términos que aparecen en cualquier conversación con una asesoría, "
                          "explicados sin dar por sabido nada.", rastro),
        "filas": filas,
        "cierre": cierre("¿Te lo explicamos sobre tus propios números?",
                         "Un glosario sirve para entender el vocabulario. Para saber qué te toca a ti "
                         "hace falta mirar tu caso."),
    }
    return P.pagina("Glosario de contabilidad y fiscalidad — Contaes",
                    "Asiento, base imponible, devengo, IVA repercutido, modelos 303, 111, 130, 347, VeriFactu y más de veinte términos explicados en claro.",
                    "%s/glosario/" % DOMINIO, cuerpo, extra_head=ld)


def pagina_calendario():
    rastro = migas(("/", "Inicio"), ("/#", "Recursos"), (None, "Calendario fiscal"))
    bloques = []
    for mes, modelos in CP.CALENDARIO:
        filas = "".join('        <tr><td>Modelo %s</td><td>%s</td></tr>\n' % (m, d) for m, d in modelos)
        bloques.append(
            '  <div class="revela" style="margin-bottom:26px">\n'
            '    <h2 style="margin:0 0 12px">%s</h2>\n'
            '    <div class="tabla-caja"><table class="tabla">\n'
            '      <thead><tr><th>Modelo</th><th>Qué se presenta</th></tr></thead>\n'
            '      <tbody>\n%s      </tbody>\n    </table></div>\n  </div>' % (mes, filas))

    cuerpo = '''%(enc)s

<section class="seccion">
  <div class="wrap estrecho">
%(bloques)s
    <div class="aviso">
      <strong>Cómo leer este calendario.</strong> %(nota)s Confirma siempre tu caso con tu asesor
      o en la sede electrónica de la Agencia Tributaria: los plazos concretos de cada año se publican allí.
    </div>
  </div>
</section>

%(cierre)s''' % {
        "enc": encabezado("Recursos", "Qué modelo toca y cuándo",
                          "El año fiscal de una pyme española cabe en cinco meses del calendario. "
                          "Estos son los modelos que marcan el ritmo.", rastro),
        "bloques": "\n".join(bloques),
        "nota": CP.CALENDARIO_NOTA,
        "cierre": cierre("Y si no quieres acordarte de nada de esto",
                         "Es exactamente para lo que existe Contaes: la contabilidad al día y los "
                         "modelos presentados por un asesor."),
    }
    return P.pagina("Calendario fiscal para pymes y autónomos — Contaes",
                    "Modelos 303, 111, 115, 130, 349, 347, 390, 190 y 200: qué se presenta en cada mes del año y de dónde salen los datos.",
                    "%s/calendario-fiscal/" % DOMINIO, cuerpo)


def pagina_preguntas():
    rastro = migas(("/", "Inicio"), ("/#", "Recursos"), (None, "Preguntas"))
    items = "".join(
        '    <details class="tarjeta revela" style="margin-bottom:12px">\n'
        '      <summary style="cursor:pointer;font-weight:600;font-size:17px;color:var(--tinta-fuerte)">%s</summary>\n'
        '      <p style="margin-top:12px">%s</p>\n    </details>\n' % (q, r)
        for q, r in CP.PREGUNTAS)
    import json
    ld = ('<script type="application/ld+json">%s</script>' % json.dumps({
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": r}} for q, r in CP.PREGUNTAS],
    }, ensure_ascii=False))
    cuerpo = '''%(enc)s

<section class="seccion">
  <div class="wrap estrecho">
%(items)s  </div>
</section>

%(cierre)s''' % {
        "enc": encabezado("Recursos", "Lo que suelen preguntarnos",
                          "Incluidas las incómodas: si está disponible, cuánto cuesta y quién responde "
                          "ante Hacienda.", rastro),
        "items": items, "cierre": cierre(),
    }
    return P.pagina("Preguntas frecuentes — Contaes",
                    "Si está disponible, qué hace la IA y qué no, quién firma los modelos, cómo se migra desde otro ERP y cuánto costará.",
                    "%s/preguntas/" % DOMINIO, cuerpo, extra_head=ld)


# ─────────────────────────────────────────────────────────────────────
# Empresa: sobre, migracion, seguridad, precios, integraciones
# ─────────────────────────────────────────────────────────────────────
def pagina_simple(slug, etiqueta, titulo, entradilla, secciones, meta,
                  rastro_nombre=None, extra="", cierre_txt=None):
    rastro = migas(("/", "Inicio"), (None, rastro_nombre or titulo))
    cuerpo = '''%(enc)s

<section class="seccion">
  <div class="wrap estrecho prosa revela">
%(prosa)s
  </div>
</section>
%(extra)s
%(cierre)s''' % {
        "enc": encabezado(etiqueta, titulo, entradilla, rastro),
        "prosa": prosa(secciones), "extra": extra,
        "cierre": cierre(*cierre_txt) if cierre_txt else cierre(),
    }
    return P.pagina("%s — Contaes" % titulo, meta, "%s/%s" % (DOMINIO, slug), cuerpo)


def pagina_precios():
    rastro = migas(("/", "Inicio"), (None, "Precios"))
    factores = [
        ("Cuánta gente lo usa", "no es lo mismo una administración de dos personas que un equipo de treinta con acceso desde obra o desde tienda."),
        ("Qué módulos se activan", "quien solo necesita contabilidad y facturación no debería pagar por inventario y proyectos."),
        ("Si incluye la asesoría", "es la parte con coste de personas detrás: alguien colegiado revisa, firma y presenta. Eso tiene un precio distinto al del software."),
        ("El volumen de documentos", "leer y clasificar facturas tiene un coste por documento; una empresa con cien facturas al mes no es como una con tres mil."),
        ("La migración", "traerse el histórico de otro sistema es un trabajo con principio y final, y se presupuesta aparte."),
    ]
    filas = "".join('    <li><b>%s</b><span>%s</span></li>\n' % (t, d) for t, d in factores)
    cuerpo = '''%(enc)s

<section class="seccion">
  <div class="wrap estrecho">
    <div class="aviso">
      <strong>Todavía no hay tarifa pública.</strong> El producto está en desarrollo, y publicar
      un precio ahora sería inventarlo. Preferimos decir esto que poner tres columnas con cifras
      que no podríamos sostener.
    </div>
  </div>
</section>

<section class="seccion">
  <div class="wrap estrecho revela">
    <h2 style="margin-top:0">De qué dependerá</h2>
    <p class="cuerpo" style="margin-bottom:8px">Lo que sí sabemos es qué mueve el precio. Son cinco cosas:</p>
    <ul class="lista">
%(filas)s    </ul>
  </div>
</section>

<section class="seccion">
  <div class="wrap estrecho prosa revela">
    <h2>Lo que no vamos a hacer</h2>
    <p>No va a haber un plan gratuito que sirva de poco para que acabes pagando el de arriba. No va a haber un precio de entrada que suba al año siguiente sin avisar. Y el presupuesto de migración no va a aparecer después de firmar.</p>
    <p>Cuando haya tarifa, estará en esta página.</p>
  </div>
</section>

%(cierre)s''' % {
        "enc": encabezado("Precios", "Lo que sabemos hoy sobre el precio",
                          "Contaes está en desarrollo. Esta página dice lo que hay: todavía no hay "
                          "tarifa, y sí sabemos de qué dependerá.", rastro),
        "filas": filas,
        "cierre": cierre("¿Quieres saber qué supondría en tu caso?",
                         "Cuéntanos cuánta gente sois, qué usáis hoy y cuántas facturas movéis al mes. "
                         "Con eso se puede hablar de números con sentido."),
    }
    return P.pagina("Precios — Contaes",
                    "Todavía no hay tarifa pública porque el producto está en desarrollo. Esto es de qué dependerá el precio y qué no vamos a hacer.",
                    "%s/precios/" % DOMINIO, cuerpo)


def pagina_integraciones():
    rastro = migas(("/", "Inicio"), (None, "Integraciones"))
    previstas = [
        ("Bancos", "importación de extractos para la conciliación, empezando por los formatos estándar (Norma 43) y las conexiones abiertas por PSD2."),
        ("Agencia Tributaria", "presentación de modelos a través de la sede electrónica, que es por donde pasa el servicio de asesoría."),
        ("Correo", "una dirección del sistema a la que reenviar facturas de proveedor para que entren por el escáner."),
        ("Tiendas en línea", "pedidos y clientes desde las plataformas más habituales, para que la venta no se teclee dos veces."),
        ("Pasarelas de pago", "conciliación de los cobros con sus liquidaciones, que es donde se pierden las comisiones."),
        ("Exportación abierta", "poder sacar tus datos en formatos estándar. No es una integración: es un derecho."),
    ]
    filas = "".join('    <li><b>%s</b><span>%s</span></li>\n' % (t, d) for t, d in previstas)
    cuerpo = '''%(enc)s

<section class="seccion">
  <div class="wrap estrecho">
    <div class="aviso">
      <strong>Ninguna de estas integraciones está disponible todavía.</strong> Esto es la hoja de
      ruta, no un catálogo. Poner logotipos de servicios con los que aún no conectamos sería
      dar a entender algo que no es cierto.
    </div>
  </div>
</section>

<section class="seccion">
  <div class="wrap estrecho revela">
    <h2 style="margin-top:0">Lo que está previsto</h2>
    <ul class="lista">
%(filas)s    </ul>
  </div>
</section>

<section class="seccion">
  <div class="wrap estrecho prosa revela">
    <h2>Por qué no habrá cien integraciones</h2>
    <p>Un catálogo largo de conectores suele esconder que la mayoría hacen poco: mueven un dato de un sitio a otro y dejan el trabajo de cuadrar para la persona.</p>
    <p>La razón de ser de Contaes es que las cosas estén dentro y no conectadas por fuera. Cada integración que hagamos es una que no ha hecho falta construir dentro, y eso es una decisión, no una victoria.</p>
    <h2>Si necesitas una concreta</h2>
    <p>Dínoslo en la primera llamada. Saber con qué tenéis que hablar es parte de decidir si encajamos.</p>
  </div>
</section>

%(cierre)s''' % {
        "enc": encabezado("Integraciones", "Con qué se conectará, y con qué no",
                          "Hoja de ruta de integraciones. Todavía no hay ninguna disponible: "
                          "el producto está en desarrollo.", rastro),
        "filas": filas, "cierre": cierre(),
    }
    return P.pagina("Integraciones — Contaes",
                    "Hoja de ruta de integraciones de Contaes: bancos, Agencia Tributaria, correo, tiendas en línea y pasarelas de pago. Ninguna disponible todavía.",
                    "%s/integraciones/" % DOMINIO, cuerpo)


def pagina_demo():
    rastro = migas(("/", "Inicio"), (None, "Pedir una demo"))
    garantias = [
        ("Si no encajamos, te lo decimos", "en la primera llamada. No en la tercera."),
        ("Punto de retorno por escrito", "antes de tocar nada, si llegáramos a trabajar juntos."),
        ("La llamada no cuesta nada", "y no hay nada que firmar para tenerla."),
    ]
    filas = "".join('    <li><b>%s</b><span>%s</span></li>\n' % (t, d) for t, d in garantias)
    cuerpo = '''%(enc)s

<section class="seccion">
  <div class="wrap estrecho revela">
    <ul class="lista" style="margin-bottom:30px">
%(filas)s    </ul>

    <form class="tarjeta" id="form-demo" style="display:grid;gap:16px;padding:26px" hidden>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px">
        <label style="display:grid;gap:6px;font-size:14px;color:var(--piedra)">Nombre
          <input name="nombre" required style="font:inherit;padding:11px 13px;border:1px solid var(--borde);border-radius:var(--r-btn);background:var(--blanco);color:var(--tinta)">
        </label>
        <label style="display:grid;gap:6px;font-size:14px;color:var(--piedra)">Empresa
          <input name="empresa" style="font:inherit;padding:11px 13px;border:1px solid var(--borde);border-radius:var(--r-btn);background:var(--blanco);color:var(--tinta)">
        </label>
        <label style="display:grid;gap:6px;font-size:14px;color:var(--piedra)">Email
          <input name="email" type="email" required style="font:inherit;padding:11px 13px;border:1px solid var(--borde);border-radius:var(--r-btn);background:var(--blanco);color:var(--tinta)">
        </label>
        <label style="display:grid;gap:6px;font-size:14px;color:var(--piedra)">Qué usáis ahora
          <input name="sistema" style="font:inherit;padding:11px 13px;border:1px solid var(--borde);border-radius:var(--r-btn);background:var(--blanco);color:var(--tinta)">
        </label>
      </div>
      <label style="display:grid;gap:6px;font-size:14px;color:var(--piedra)">Qué es lo que peor lleváis
        <textarea name="mensaje" rows="4" style="font:inherit;padding:11px 13px;border:1px solid var(--borde);border-radius:var(--r-btn);background:var(--blanco);color:var(--tinta);resize:vertical"></textarea>
      </label>
      <p style="font-size:13px;color:var(--piedra)">Al enviar se abrirá tu programa de correo con el mensaje preparado. Tus datos se usan solo para responderte; puedes leer cómo en la <a href="/legal/privacidad/" style="color:var(--azul)">política de privacidad</a>.</p>
      <div><button class="btn btn-azul" type="submit">Enviar <span class="flecha" aria-hidden="true">&rarr;</span></button></div>
    </form>

    <p id="demo-directo" class="cuerpo">Escríbenos a <a href="mailto:info@contaes.com" style="color:var(--azul)">info@contaes.com</a> contándonos qué usáis hoy y qué es lo que peor lleváis.</p>
  </div>
</section>

<script>
/* El formulario solo aparece si hay JavaScript: sin el, prepararlo no
   serviria de nada y el correo directo funciona igual. */
(function(){
  var f=document.getElementById("form-demo"); if(!f)return;
  f.hidden=false;
  f.addEventListener("submit",function(e){
    e.preventDefault();
    var d=new FormData(f), l=[];
    d.forEach(function(v,k){ if(String(v).trim()) l.push(k+": "+v); });
    window.location.href="mailto:info@contaes.com"
      +"?subject="+encodeURIComponent("Demo de Contaes")
      +"&body="+encodeURIComponent(l.join("\\n"));
  });
})();
</script>''' % {
        "enc": encabezado("Hablemos", "¿Te enseñamos cómo funciona?",
                          "Una demo sobre tu caso concreto, no una presentación genérica. "
                          "Cuéntanos qué usáis ahora y qué es lo que peor lleváis.", rastro),
        "filas": filas,
    }
    return P.pagina("Pedir una demo — Contaes",
                    "Una demo sobre vuestro caso concreto. Si no encajamos, se dice en la primera llamada.",
                    "%s/demo/" % DOMINIO, cuerpo)


# ─────────────────────────────────────────────────────────────────────
# Legal
# ─────────────────────────────────────────────────────────────────────
def _falta(clave):
    v = CP.DATOS_EMPRESA[clave]
    if v == CP.PENDIENTE:
        return '<mark style="background:#ffe9a8;padding:1px 6px;border-radius:4px">[PENDIENTE: %s]</mark>' % clave.replace("_", " ")
    return v


def paginas_legales():
    d = CP.DATOS_EMPRESA
    aviso_datos = ('<div class="aviso"><strong>Esta página está incompleta.</strong> Faltan los datos '
                   'identificativos del titular del sitio, que la Ley de Servicios de la Sociedad de la '
                   'Información obliga a publicar. Están marcados abajo.</div>')

    legal = {
        "legal/aviso-legal/": (
            "Aviso legal",
            "Quién es responsable de este sitio, en cumplimiento del artículo 10 de la Ley 34/2002.",
            [("Titular del sitio", [
                "Razón social: %s" % _falta("razon_social"),
                "NIF: %s" % _falta("nif"),
                "Domicilio: %s" % _falta("domicilio"),
                "Correo de contacto: %s" % d["correo"],
                "Datos registrales: %s" % _falta("registro"),
            ]),
             ("Objeto", [
                 "Este sitio informa sobre Contaes, un producto en desarrollo. No permite contratar nada ni "
                 "realizar pagos: su única función es informar y recoger solicitudes de contacto.",
             ]),
             ("Uso del sitio", [
                 "El acceso es libre y gratuito. Quien lo usa se compromete a no emplearlo para actividades "
                 "contrarias a la ley ni a intentar dañar su funcionamiento.",
             ]),
             ("Propiedad intelectual", [
                 "Los textos, el diseño y las marcas de este sitio pertenecen a su titular, salvo lo "
                 "expresamente indicado. La normativa fiscal citada es de dominio público; su redacción "
                 "y ordenación en estas páginas, no.",
             ]),
             ("Responsabilidad sobre el contenido fiscal", [
                 "Las páginas sobre modelos, plazos y obligaciones tienen carácter general e informativo. "
                 "No son asesoramiento fiscal ni sustituyen al criterio de un profesional sobre un caso "
                 "concreto. La normativa cambia; confirma siempre tu situación con tu asesor o en la sede "
                 "electrónica de la Agencia Tributaria.",
             ]),
             ("Legislación aplicable", [
                 "Esta relación se rige por la legislación española.",
             ])]),
        "legal/privacidad/": (
            "Política de privacidad",
            "Qué datos recogemos, para qué, cuánto tiempo y qué derechos tienes.",
            [("Quién trata tus datos", [
                "Responsable: %s, NIF %s, con domicilio en %s. Puedes escribir a %s para cualquier "
                "cuestión relacionada con tus datos."
                % (_falta("razon_social"), _falta("nif"), _falta("domicilio"), d["correo"]),
            ]),
             ("Qué datos recogemos y por qué", [
                 "Solo los que nos envías tú al pedir una demo o escribirnos: nombre, empresa, correo "
                 "electrónico, el sistema que usáis hoy y lo que nos cuentes en el mensaje.",
                 "El formulario de este sitio no envía nada a ningún servidor nuestro: abre tu programa "
                 "de correo con el mensaje preparado. Es decir, los datos viajan por tu correo, y nosotros "
                 "los recibimos como recibiríamos cualquier email.",
                 "La finalidad es responderte y, si procede, preparar una demostración. No los usamos "
                 "para nada más ni los cedemos a terceros.",
             ]),
             ("Base legal", [
                 "El tratamiento se basa en tu consentimiento al escribirnos y en el interés legítimo de "
                 "atender la solicitud que nos haces (artículo 6.1.a y 6.1.f del Reglamento General de "
                 "Protección de Datos).",
             ]),
             ("Cuánto tiempo los guardamos", [
                 "El tiempo necesario para atender tu solicitud y, después, el que exijan las obligaciones "
                 "legales que pudieran aplicar. Si nos pides que borremos tu mensaje, lo borramos.",
             ]),
             ("Tus derechos", [
                 "Puedes pedir acceso a tus datos, su rectificación o su supresión; limitar u oponerte a su "
                 "tratamiento; y solicitar su portabilidad. Basta con escribir a %s." % d["correo"],
                 "Si crees que no hemos atendido bien tu solicitud, puedes reclamar ante la Agencia "
                 "Española de Protección de Datos (www.aepd.es).",
             ]),
             ("Encargados y transferencias", [
                 "Este sitio está alojado en GitHub Pages, que registra datos técnicos de la conexión "
                 "—como la dirección IP— para servir las páginas y protegerse de abusos. Las tipografías "
                 "se cargan desde Google Fonts, lo que implica una conexión a servidores de Google.",
                 "Ambos servicios pueden implicar transferencias internacionales de datos amparadas en los "
                 "mecanismos previstos por el Reglamento General de Protección de Datos.",
             ])]),
        "legal/cookies/": (
            "Política de cookies",
            "Este sitio no usa cookies de seguimiento ni de publicidad.",
            [("Qué cookies usa este sitio", [
                "Ninguna propia. No hay analítica, ni píxeles de publicidad, ni cookies de seguimiento. "
                "No hay banner de consentimiento porque no hay nada que consentir.",
            ]),
             ("Servicios de terceros", [
                 "El sitio se sirve desde GitHub Pages y carga las tipografías desde Google Fonts. Esas "
                 "conexiones no instalan cookies de seguimiento en tu navegador, pero sí implican que esos "
                 "servicios reciben datos técnicos de la conexión, como tu dirección IP.",
                 "Tu navegador guarda además datos técnicos propios —caché, preferencias— que no son "
                 "cookies nuestras y que puedes borrar desde su configuración.",
             ]),
             ("Si esto cambia", [
                 "Si en algún momento añadimos analítica o cualquier otra herramienta que use cookies, "
                 "esta página se actualizará y aparecerá el aviso de consentimiento correspondiente antes "
                 "de instalar nada.",
             ])]),
    }

    salidas = {}
    for ruta, (titulo, meta, secciones) in legal.items():
        hay_pendiente = any(CP.PENDIENTE in " ".join(ps) or "PENDIENTE" in " ".join(ps)
                            for _, ps in secciones)
        rastro = migas(("/", "Inicio"), (None, titulo))
        extra = aviso_datos if ruta != "legal/cookies/" else ""
        cuerpo = '''%(enc)s

<section class="seccion">
  <div class="wrap estrecho">%(aviso)s</div>
  <div class="wrap estrecho prosa revela">
%(prosa)s
    <p style="font-size:14px;color:var(--piedra);margin-top:34px">Última revisión: septiembre de 2026.</p>
  </div>
</section>''' % {
            "enc": encabezado("Legal", titulo, meta, rastro),
            "aviso": extra,
            "prosa": prosa(secciones),
        }
        salidas[ruta + "index.html"] = P.pagina("%s — Contaes" % titulo, meta,
                                                "%s/%s" % (DOMINIO, ruta), cuerpo)
    return salidas


# ─────────────────────────────────────────────────────────────────────
# Sitemap y robots
# ─────────────────────────────────────────────────────────────────────
def articulos_del_blog():
    ruta = os.path.join(AQUI, "build-blog.py")
    spec = importlib.util.spec_from_file_location("build_blog", ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return [a["slug"] for a in mod.ARTICULOS]


def construir_sitemap(rutas):
    filas = []
    for r in rutas:
        u = "%s/%s" % (DOMINIO, r) if r else "%s/" % DOMINIO
        prioridad = "1.0" if not r else ("0.8" if r.count("/") <= 1 else "0.6")
        filas.append("  <url>\n    <loc>%s</loc>\n    <changefreq>%s</changefreq>"
                     "\n    <priority>%s</priority>\n  </url>"
                     % (u, "weekly" if not r else "monthly", prioridad))
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s\n</urlset>\n'
            % "\n".join(filas))


# ─────────────────────────────────────────────────────────────────────
def main():
    salidas = {}

    salidas["funcionalidades/index.html"] = pagina_funcionalidades()
    for slug, d in C.MODULOS.items():
        salidas["funcionalidades/%s/index.html" % slug] = pagina_funcionalidad(slug, d, True)
    for slug, d in C.CAPACIDADES.items():
        salidas["funcionalidades/%s/index.html" % slug] = pagina_funcionalidad(slug, d, False)

    salidas["sectores/index.html"] = pagina_sectores()
    for slug, d in C.SECTORES.items():
        salidas["sectores/%s/index.html" % slug] = pagina_sector(slug, d)

    salidas["glosario/index.html"] = pagina_glosario()
    salidas["calendario-fiscal/index.html"] = pagina_calendario()
    salidas["preguntas/index.html"] = pagina_preguntas()
    salidas["precios/index.html"] = pagina_precios()
    salidas["integraciones/index.html"] = pagina_integraciones()
    salidas["demo/index.html"] = pagina_demo()

    salidas["sobre/index.html"] = pagina_simple(
        "sobre/", "Empresa", "Qué estamos construyendo",
        "Contaes es un ERP para pymes con una asesoría fiscal dentro. Está en desarrollo, "
        "y esta página cuenta por qué y con qué criterio.",
        [("El hueco que intenta llenar", [
            "Una pyme española con quince personas tiene hoy dos cosas separadas: un programa donde mete los datos y una asesoría a la que se los manda. En medio hay un mes de correos, una hoja de cálculo y la pregunta de siempre.",
            "Ese hueco no es un problema de software. Es un problema de reparto: el programa no se responsabiliza de lo que se presenta, y la asesoría no tiene los datos al día. Contaes existe para que las dos cosas estén del mismo lado.",
        ]),
         ("Con qué criterio se construye", [
             "Que el dato se registre una vez, donde ocurre el hecho. Que cualquier cifra se pueda seguir hasta el documento que la origina. Que lo que sale de la empresa —un correo, un modelo— lo apruebe una persona. Y que la responsabilidad ante la Administración sea de alguien colegiado, no de un algoritmo.",
             "También hay un criterio sobre lo que no se hace: no competir en número de funciones, no llenar el catálogo de integraciones que hacen poco y no prometer autonomía donde debería haber criterio profesional.",
         ]),
         ("En qué punto está", [
             "En desarrollo. No hay versión disponible, ni prueba gratuita, ni tarifa. Esta web no tiene testimonios, ni logotipos de clientes, ni cifras de usuarios, porque no los hay: ponerlos sería mentir, y un producto de contabilidad que empieza mintiendo empieza mal.",
             "Lo que sí se puede hacer hoy es contarnos cómo trabajáis. Eso decide qué se construye antes.",
         ])],
        "Contaes es un ERP para pymes con asesoría fiscal dentro, en desarrollo. Por qué existe, con qué criterio se construye y en qué punto está.",
        rastro_nombre="Sobre Contaes")

    salidas["migracion/index.html"] = pagina_simple(
        "migracion/", "Empresa", "Cambiar sin parar la empresa",
        "Nadie cambia de ERP porque le apetezca. Se cambia cuando el que hay cuesta más de "
        "mantener que de sustituir, y aun así da vértigo, porque durante la migración la "
        "empresa tiene que seguir facturando.",
        [("Los cuatro puntos que se acuerdan antes de tocar nada", [
            "<strong>Datos.</strong> Clientes, proveedores, artículos y saldos se traen con su histórico, no como un saldo inicial suelto. Un saldo sin historia detrás es un número que nadie puede defender ante una inspección.",
            "<strong>Convivencia.</strong> Un periodo en que el sistema antiguo sigue vivo en solo lectura, para consultar y comparar. No es un lujo: es lo que evita el agujero de los primeros meses.",
            "<strong>Reversión.</strong> Un punto de retorno definido antes de empezar, no improvisado a mitad. Si a las tres semanas algo no funciona, tiene que estar escrito qué se hace.",
            "<strong>Formación.</strong> El equipo trabaja en un entorno de pruebas con datos reales antes del cambio. Aprender con la empresa en marcha es la forma más cara de aprender.",
        ]),
         ("Cuándo conviene cambiar", [
             "El cambio limpio es a cierre de ejercicio: los saldos están cerrados y el sistema nuevo arranca con un punto de partida sin ambigüedad. El segundo mejor momento es a cierre de trimestre, con los modelos ya presentados.",
             "Cambiar a mitad de trimestre es posible, pero reparte la responsabilidad de un mismo periodo entre dos sistemas, y ahí es donde se cuelan los huecos.",
         ]),
         ("De dónde se suele venir", [
             "De un ERP genérico que lleva años acumulando módulos que nadie sabe explicar. De una hoja de cálculo que creció hasta ser crítica. De un programa de facturación que hace su parte pero no habla con la contabilidad. Y, muchas veces, de las tres cosas a la vez.",
             "Ninguno de esos casos es excepcional. Lo excepcional sería encontrarse una empresa cuyo sistema hace exactamente lo que necesita.",
         ])],
        "Cómo se cambia de ERP sin parar la empresa: datos con histórico, convivencia de los dos sistemas, punto de retorno por escrito y formación antes del cambio.")

    salidas["seguridad/index.html"] = pagina_simple(
        "seguridad/", "Empresa", "Seguridad y datos",
        "Un sistema que lleva tu contabilidad tiene tus datos más sensibles. Esta página dice "
        "qué compromisos asumimos y, con la misma claridad, qué no podemos afirmar todavía.",
        [("Lo que sí podemos decir hoy", [
            "Los datos de una empresa son suyos. Poder sacarlos en un formato estándar y abrirlos sin nuestro programa no es una función avanzada: es la condición para poder irse, y por tanto la condición para confiar.",
            "Cada apunte guarda quién lo hizo y cuándo. Una factura emitida no se edita ni se borra: se rectifica. Esto no es solo una exigencia normativa, es lo que hace que los libros sirvan de prueba.",
            "El tratamiento de datos personales se rige por el Reglamento General de Protección de Datos. Puedes leer qué recogemos hoy en la <a href=\"/legal/privacidad/\">política de privacidad</a>: en este momento, solo lo que nos escribes tú.",
        ]),
         ("Lo que todavía no podemos afirmar", [
             "El producto está en desarrollo. No tenemos certificaciones que enseñar —ni ISO 27001, ni un informe SOC 2— porque no se certifica lo que aún se está construyendo, y presumir de una que no se tiene es exactamente el tipo de cosa que descalifica a un proveedor de contabilidad.",
             "Cuando existan compromisos concretos y verificables sobre alojamiento, cifrado, copias de seguridad y tiempos de recuperación, estarán aquí con nombre y fecha. Hasta entonces, esta página dice lo que hay.",
         ]),
         ("Este sitio web", [
             "La web que estás leyendo se sirve desde GitHub Pages sobre HTTPS. No usa cookies de seguimiento ni analítica: no hay banner de consentimiento porque no hay nada que consentir. El detalle está en la <a href=\"/legal/cookies/\">política de cookies</a>.",
             "El formulario no envía datos a ningún servidor nuestro: abre tu programa de correo con el mensaje preparado.",
         ])],
        "Qué compromisos asumimos sobre tus datos y qué no podemos afirmar todavía. Sin certificaciones que no tenemos.",
        rastro_nombre="Seguridad y datos")

    salidas.update(paginas_legales())

    # ── sitemap con todo ─────────────────────────────────────────────
    rutas = [""]
    rutas += ["funcionalidades/"] + ["funcionalidades/%s/" % s for s in
                                     list(C.MODULOS) + list(C.CAPACIDADES)]
    rutas += ["sectores/"] + ["sectores/%s/" % s for s in C.SECTORES]
    rutas += ["glosario/", "calendario-fiscal/", "preguntas/", "precios/",
              "integraciones/", "demo/", "sobre/", "migracion/", "seguridad/"]
    rutas += [r for r, _ in P.LEGAL]
    rutas += ["blog/"] + ["blog/%s.html" % s for s in articulos_del_blog()]
    salidas["sitemap.xml"] = construir_sitemap(rutas)
    salidas["robots.txt"] = "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % DOMINIO

    # ── escribir ─────────────────────────────────────────────────────
    for ruta, contenido in sorted(salidas.items()):
        destino = os.path.join(RAIZ, ruta.replace("/", os.sep))
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        with io.open(destino, "w", encoding="utf-8") as f:
            f.write(contenido)
    print("  %d ficheros generados" % len(salidas))
    print("  %d URLs en el sitemap" % len(rutas))

    faltan = [k for k, v in CP.DATOS_EMPRESA.items() if v == CP.PENDIENTE]
    if faltan:
        print()
        print("  AVISO: las paginas legales estan incompletas.")
        print("  Falta rellenar en scripts/contenido_paginas.py -> DATOS_EMPRESA:")
        for k in faltan:
            print("    - %s" % k.replace("_", " "))
    return 0


if __name__ == "__main__":
    sys.exit(main())
