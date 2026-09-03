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
import contenido_servicios as CS
import formulario as F
import dibujos as DIB
import diagramas_pagina as DP
import herramientas as H

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

DOMINIO = P.DOMINIO
COLORES = ["var(--verde)", "var(--cian)", "var(--azul-marca)", "var(--marigold)",
           "var(--cielo)", "var(--coral)", "var(--navy)", "var(--azul)"]


# ─────────────────────────────────────────────────────────────────────
# Datos estructurados. Solo lo que es cierto y esta en la pagina: sin
# valoraciones, sin precios y sin numero de opiniones inventados. Marcar
# lo que no existe es la forma mas rapida de que un buscador deje de
# fiarse tambien de lo que si.
# ─────────────────────────────────────────────────────────────────────
import json as _json


def _ld(datos):
    return ('<script type="application/ld+json">%s</script>'
            % _json.dumps(datos, ensure_ascii=False, separators=(",", ":")))


def ld_organizacion():
    return {
        "@type": "ProfessionalService",
        "@id": DOMINIO + "/#contaes",
        "name": "Contaes",
        "url": DOMINIO + "/",
        "areaServed": {"@type": "Country", "name": "España"},
        "knowsLanguage": "es",
        "description": ("Gestoría online para autónomos, startups y pymes: contabilidad, "
                        "impuestos, nóminas y contratos, con software propio incluido y "
                        "servicios de crecimiento."),
    }


def ld_migas(pasos):
    """pasos: [(ruta o None, nombre)] en orden."""
    items = []
    for i, (ruta, nombre) in enumerate(pasos, 1):
        item = {"@type": "ListItem", "position": i, "name": nombre}
        if ruta:
            item["item"] = DOMINIO + ruta
        items.append(item)
    return {"@type": "BreadcrumbList", "itemListElement": items}


def ld_servicio(nombre, descripcion, ruta, tipo="Service"):
    return {
        "@type": tipo,
        "name": nombre,
        "description": " ".join(descripcion.split())[:300],
        "url": DOMINIO + ruta,
        "provider": {"@id": DOMINIO + "/#contaes"},
        "areaServed": {"@type": "Country", "name": "España"},
    }


def ld_pagina(*bloques):
    return _ld({"@context": "https://schema.org", "@graph": list(bloques)})


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
    # Sin barrita de color arriba: no codificaba nada (ni orden, ni
    # categoria, ni estado) y la decoracion que no significa nada es lo
    # primero que hace que una pagina parezca hecha por una maquina.
    tarjetas = []
    for ruta, titulo, pie in entradas:
        tarjetas.append(
            '    <a class="tarjeta" href="%s%s">\n'
            '      <h2 class="tarjeta-tit">%s</h2>\n      <p>%s</p>\n'
            '      <span class="tarjeta-mas" aria-hidden="true">Ver</span>\n    </a>'
            % (base, ruta, titulo, pie))
    clase = "rejilla" if columnas == 3 else "rejilla-2"
    return '<div class="%s revela">\n%s\n  </div>' % (clase, "\n".join(tarjetas))


def prosa(secciones):
    trozos = []
    for h2, parrafos in secciones:
        trozos.append("<h2>%s</h2>" % h2)
        trozos.extend("<p>%s</p>" % t for t in parrafos)
    return "\n".join(trozos)


def lista_incluye(puntos):
    """Siete puntos sueltos en columna se leen como un parrafo largo. En
    rejilla se barren de un vistazo, que es para lo que estan."""
    filas = "".join(
        '    <li><span class="tic" aria-hidden="true"></span><span>%s</span></li>\n' % p
        for p in puntos)
    return '<ul class="incluye">\n%s  </ul>' % filas


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
    rastro = migas(("/", "Inicio"), ("/funcionalidades/", "Software"), (None, d["titulo"]))
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
  <div class="wrap estrecho">
%(dibujo)s
  </div>
</section>

<section class="seccion banda">
  <div class="wrap revela">
    <h2 style="margin-top:0">Qué incluye</h2>
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
        "enc": encabezado("Software" if es_modulo else "Lo que lo hace distinto",
                          d["titulo"] + ". <span style=\"color:var(--grafito);font-weight:500\">" + d["lema"] + "</span>",
                          d["entradilla"], rastro),
        "prosa": prosa(d["secciones"]),
        "aviso": aviso,
        "dibujo": DP.para("funcionalidades/" + slug),
        "incluye": lista_incluye(d["incluye"]),
        "conecta": conecta,
        "cierre": cierre(),
    }
    ld = ld_pagina(
        ld_organizacion(),
        ld_servicio(d["titulo"], d["entradilla"], "/funcionalidades/%s/" % slug,
                    tipo="SoftwareApplication" if es_modulo else "Service"),
        ld_migas([("/", "Inicio"), ("/funcionalidades/", "Software"), (None, d["titulo"])]))
    return P.pagina(
        "%s · El software · Contaes" % d["titulo"],
        d["entradilla"][:158],
        "%s/funcionalidades/%s/" % (DOMINIO, slug),
        cuerpo, extra_head=ld)


def pagina_funcionalidades():
    rastro = migas(("/", "Inicio"), (None, "Software"))
    cuerpo = '''%(enc)s

<section class="seccion">
  <div class="wrap estrecho prosa revela">
    <h2 style="margin-top:0">El mismo programa para los dos</h2>
    <p>Una gestoría normal usa su programa y tú usas el tuyo. Entre los dos hay un traspaso:
      tú mandas facturas, ellos las meten, y cada traspaso es una oportunidad de que algo se
      pierda o llegue tarde. Aquí no hay traspaso porque no hay dos programas.</p>
    <p>Eso tiene una consecuencia que se nota enseguida: tus libros están al día todos los
      días, no a final de trimestre. Puedes entrar a mirarlos sin pedírselos a nadie, y
      cuando toca presentar un modelo, los datos ya están donde tienen que estar.</p>

    <h2>Se activa lo que usas</h2>
    <p>Nadie necesita las ocho áreas. Un autónomo que factura servicios no quiere ver
      almacén; una empresa de distribución lo quiere lo primero. Se enciende lo que hace
      falta y lo demás no estorba en los menús.</p>
    <p>Lo que no cambia es el fondo: todo escribe en el mismo libro mayor. Por eso una
      factura emitida ya es un asiento, una compra recibida ya es existencias, y un informe
      no necesita que nadie exporte nada.</p>
  </div>
</section>

<section class="seccion">
  <div class="wrap">
    <h2 style="margin-top:0">La gestión del día a día</h2>
    <p class="cuerpo" style="margin-bottom:22px;max-width:60ch">Todo sobre el mismo libro mayor: lo que se registra en un sitio está disponible en los demás sin exportar nada. Se activa lo que necesites y se deja fuera lo que no.</p>
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
        "enc": encabezado("Software", "Un solo sitio para toda la gestión",
                          "El programa que usamos para llevarte la gestoría es el mismo al "
                          "que tú entras. Cada hecho se registra una vez y aparece donde hace "
                          "falta, sin exportar nada de un sitio a otro.", rastro),
        "modulos": rejilla_tarjetas([("funcionalidades/%s/" % s, n, d) for s, n, d in P.MODULOS], "/"),
        "capacidades": rejilla_tarjetas([("funcionalidades/%s/" % s, n, d) for s, n, d in P.CAPACIDADES], "/"),
        "cierre": cierre(),
    }
    return P.pagina("Producto · Contaes",
                    "Contabilidad, facturación, almacén, compras, ventas, proyectos e informes sobre el mismo libro mayor, con asesoría fiscal incluida.",
                    "%s/funcionalidades/" % DOMINIO, cuerpo)


# ─────────────────────────────────────────────────────────────────────
# Servicios: gestoria, crecimiento y publico
# ─────────────────────────────────────────────────────────────────────
AREAS = {
    "gestoria": ("Gestoría", "Gestoría", CS.GESTORIA, P.GESTORIA),
    "crecimiento": ("Crecimiento", "Crecimiento", CS.CRECIMIENTO, P.CRECIMIENTO),
    "para": ("Para quién", "Para quién es", CS.PARA, P.PUBLICO),
}


def pagina_servicio(area, slug, d):
    etiqueta, nombre_area, _datos, _mapa = AREAS[area]
    rastro = migas(("/", "Inicio"), ("/%s/" % area, nombre_area), (None, d["titulo"]))

    hermanas = [(s, n, p_) for s, n, p_ in AREAS[area][3] if s != slug][:3]
    otras = rejilla_tarjetas([("%s/%s/" % (area, s), n, p_) for s, n, p_ in hermanas], "/")

    cuerpo = '''%(enc)s

<section class="seccion">
  <div class="wrap estrecho prosa revela">
%(prosa)s
  </div>
</section>

<section class="seccion">
  <div class="wrap estrecho">
%(dibujo)s
  </div>
</section>

<section class="seccion banda">
  <div class="wrap revela">
    <h2 style="margin-top:0">Qué incluye</h2>
%(incluye)s
  </div>
</section>

<section class="seccion">
  <div class="wrap">
    <div class="panel medianoche revela">
      <p class="etiqueta" style="color:#8b93b5;margin-bottom:12px">Con franqueza</p>
      <h2 style="margin:0 0 14px;max-width:20ch">Para quién no es</h2>
      <p class="cuerpo" style="max-width:64ch;font-size:17px">%(limites)s</p>
    </div>
  </div>
</section>

<section class="seccion">
  <div class="wrap revela">
    <p class="etiqueta" style="margin-bottom:10px">Del mismo bloque</p>
    <h2 style="margin-top:0">También te puede interesar</h2>
    %(otras)s
  </div>
</section>

%(cierre)s''' % {
        "enc": encabezado(etiqueta,
                          d["titulo"] + ". <span style=\"color:var(--grafito);font-weight:500\">"
                          + d["lema"] + "</span>",
                          d["entradilla"], rastro),
        "prosa": prosa(d["secciones"]),
        "dibujo": DP.para("%s/%s" % (area, slug)),
        "incluye": lista_incluye(d["incluye"]),
        "limites": d["limites"],
        "otras": otras,
        "cierre": cierre(),
    }
    # El titulo lleva el area: hay una pagina de Contabilidad en la
    # gestoria y otra en el software, y con el mismo titulo Google no
    # sabe cual ensenar para la misma busqueda.
    ld = ld_pagina(
        ld_organizacion(),
        ld_servicio(d["titulo"], d["entradilla"], "/%s/%s/" % (area, slug)),
        ld_migas([("/", "Inicio"), ("/%s/" % area, nombre_area), (None, d["titulo"])]))
    return P.pagina("%s · %s · Contaes" % (d["titulo"], nombre_area),
                    " ".join(d["entradilla"].split())[:158],
                    "%s/%s/%s/" % (DOMINIO, area, slug), cuerpo, extra_head=ld)


def pagina_area(area, titulo, entradilla, intro=(), dibujo="", preguntas=()):
    etiqueta, nombre_area, datos, mapa = AREAS[area]
    rastro = migas(("/", "Inicio"), (None, nombre_area))

    bloque_intro = ""
    if intro:
        bloque_intro = ('''<section class="seccion">
  <div class="wrap estrecho prosa revela">
%s
  </div>
</section>

''' % prosa(intro))

    bloque_dibujo = ""
    if dibujo:
        bloque_dibujo = ('''<section class="seccion">
  <div class="wrap estrecho">
%s
  </div>
</section>

''' % dibujo)

    bloque_preguntas = ""
    if preguntas:
        items = "".join(
            '    <details class="tarjeta revela" style="margin-bottom:12px">\n'
            '      <summary style="cursor:pointer;font-weight:600;font-size:17px;'
            'color:var(--tinta-fuerte)">%s</summary>\n'
            '      <p style="margin-top:12px;color:var(--grafito)">%s</p>\n    </details>\n'
            % (q, r) for q, r in preguntas)
        bloque_preguntas = ('''<section class="seccion">
  <div class="wrap estrecho">
    <h2 style="margin-top:0">Lo que suelen preguntarnos de esto</h2>
%s  </div>
</section>

''' % items)

    cuerpo = '''%(enc)s

%(intro)s<section class="seccion">
  <div class="wrap">
    %(rejilla)s
  </div>
</section>

%(dibujo)s%(preguntas)s%(cierre)s''' % {
        "enc": encabezado(etiqueta, titulo, entradilla, rastro),
        "intro": bloque_intro,
        "rejilla": rejilla_tarjetas([("%s/%s/" % (area, s), n, p_) for s, n, p_ in mapa], "/"),
        "dibujo": bloque_dibujo,
        "preguntas": bloque_preguntas,
        "cierre": cierre(),
    }
    return P.pagina("%s · Contaes" % titulo,
                    " ".join(entradilla.split())[:158],
                    "%s/%s/" % (DOMINIO, area), cuerpo)


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
  <div class="wrap estrecho">
%(dibujo)s
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
  <div class="wrap estrecho">
    <h2 style="margin-top:0">Lo que preguntamos en la primera llamada</h2>
    <p class="cuerpo" style="margin-bottom:18px">Tres preguntas de este sector. Si las
      respuestas te incomodan, probablemente tengamos de qué hablar.</p>
%(preguntas)s
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
        "preguntas": "".join(
            '    <details class="tarjeta revela" style="margin-bottom:12px">\n'
            '      <summary style="cursor:pointer;font-weight:600;font-size:17px;'
            'color:var(--tinta-fuerte)">%s</summary>\n'
            '      <p style="margin-top:12px;color:var(--grafito)">%s</p>\n    </details>\n'
            % (q, r) for q, r in d.get("preguntas", [])),
        "dibujo": DP.para("sectores/%s" % slug),
        "cierre": cierre("¿Se parece a lo vuestro?",
                         "En la primera llamada preferimos escuchar cómo trabajáis antes que enseñar pantallas. "
                         "Si no encajamos, se dice ahí."),
    }
    ld = ld_pagina(
        ld_organizacion(),
        ld_servicio("Gestoría y software para %s" % d["titulo"].lower(),
                    d["entradilla"], "/sectores/%s/" % slug),
        ld_migas([("/", "Inicio"), ("/sectores/", "Sectores"), (None, d["titulo"])]))
    return P.pagina("Gestoría y software para %s · Contaes" % d["titulo"].lower(),
                    d["entradilla"][:158],
                    "%s/sectores/%s/" % (DOMINIO, slug), cuerpo, extra_head=ld)


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
    <h2>Por qué el sector cambia tanto las cosas</h2>
    <p>Un ERP no se elige por la lista de funciones: se elige por si entiende cómo trabaja tu
      negocio. Y lo que hace difícil a cada negocio no es lo mismo.</p>
    <p>En fabricación el problema es el coste: transformar materiales y horas en producto sin
      saber cuánto cuesta esa transformación convierte el margen en una opinión. En
      distribución es el volumen: márgenes finos donde un error de precio se come el beneficio
      de varias operaciones buenas. En construcción es la obra: el resultado no es de la
      empresa, es de cada obra, y una empresa con cinco puede tener beneficio y estar
      perdiendo dinero en tres.</p>
    <p>En servicios profesionales el problema es el tiempo, que se apunta tarde y a la baja.
      En comercio, que el TPV, el almacén y la contabilidad cuentan tres verdades distintas
      del mismo negocio. Y en alimentación, la trazabilidad, que no es una mejora sino una
      obligación legal.</p>

    <h2>Lo que no cambia</h2>
    <p>Debajo de todos ellos hay lo mismo: un libro mayor, unas existencias valoradas, unos
      clientes que pagan tarde y unos modelos que presentar. Por eso no son ocho productos:
      es el mismo sistema, con el peso puesto en sitios distintos.</p>

    <h2>Y si tu sector no está</h2>
    <p>Estas ocho fichas no son ocho productos distintos: es el mismo sistema contado desde el problema de cada uno. Si tu actividad no aparece, casi siempre es porque se parece a alguna de ellas.</p>
    <p>Lo que sí conviene decir claro: hay procesos muy particulares (fabricación compleja, normativa sectorial concreta) que hoy no cubrimos. Preferimos decirlo antes que después de la demo.</p>
  </div>
</section>

%(cierre)s''' % {
        "enc": encabezado("Sectores", "El mismo sistema, contado desde tu problema",
                          "Un ERP no se elige por la lista de funciones: se elige por si entiende cómo "
                          "trabaja tu negocio. Estas son las ocho formas de trabajar que tenemos más presentes.", rastro),
        "rejilla": rejilla_tarjetas([("sectores/%s/" % s, n, d) for s, n, d in P.SECTORES], "/"),
        "cierre": cierre(),
    }
    return P.pagina("Sectores · Contaes",
                    "Fabricación, distribución, construcción, comercio, logística, servicios, instalaciones y agroalimentario: el mismo ERP contado desde el problema de cada sector.",
                    "%s/sectores/" % DOMINIO, cuerpo)


# ─────────────────────────────────────────────────────────────────────
# Glosario, calendario, preguntas
# ─────────────────────────────────────────────────────────────────────
TABLA_COMPARATIVA = """    <div class="tabla-caja">
      <table class="tabla comparativa">
        <thead><tr><th scope="col"></th><th scope="col">Gestoría y programa aparte</th><th scope="col">Solo software</th><th scope="col" class="col-nuestra">Las dos juntas</th></tr></thead>
        <tbody>
        <tr><th scope="row">Quién lleva los libros</th><td>Tu gestoría, con lo que le mandas cada trimestre</td><td>Tú o alguien de tu equipo, en el programa</td><td>Nosotros, en el mismo programa al que tú entras</td></tr>
        <tr><th scope="row">Cuándo están al día</th><td>A trimestre vencido, cuando se cierra</td><td>Depende de lo constante que seas</td><td>Todos los días, porque el apunte nace con el hecho</td></tr>
        <tr><th scope="row">Quién presenta los modelos</th><td>Tu gestoría, con su firma</td><td>Tú, o los pasas a una gestoría</td><td>Un asesor colegiado, con su firma</td></tr>
        <tr><th scope="row">Qué pasa si algo descuadra</th><td>Se ve al cerrar el trimestre</td><td>Se ve si lo miras</td><td>Se avisa antes de presentar</td></tr>
        <tr><th scope="row">Coste</th><td>Cuota de gestoría más licencia del programa</td><td>Solo licencia, más tu tiempo</td><td>Una cuota, según lo que uses</td></tr>
        <tr><th scope="row">Dónde está el riesgo</th><td>En el traspaso: lo que no mandas, no se contabiliza</td><td>En que la responsabilidad fiscal acaba siendo tuya</td><td>En depender de un solo proveedor para las dos cosas</td></tr>
        </tbody>
      </table>
    </div>"""

CUANDO_COMPARATIVA = """      <div class="cuando">
        <h3>Gestoría de siempre y programa aparte</h3>
        <p><b>Encaja</b> Cuando ya tienes una relación buena con tu gestoría y un sistema que os funciona a los dos. Si el traspaso trimestral no te duele, cambiarlo por cambiarlo no tiene sentido.</p>
        <p class="cuando-no"><b>No encaja</b> Deja de encajar cuando empiezas a tomar decisiones que necesitan datos de este mes y los que tienes son de hace tres.</p>
      </div>
      <div class="cuando">
        <h3>Solo software, tú lo llevas</h3>
        <p><b>Encaja</b> Cuando tienes a alguien dentro que sabe contabilidad y prefieres el control. Sale más barato en cuota y da más autonomía.</p>
        <p class="cuando-no"><b>No encaja</b> Deja de encajar cuando esa persona se va de vacaciones, o cuando llega un requerimiento y descubres que la responsabilidad ante Hacienda es tuya.</p>
      </div>
      <div class="cuando">
        <h3>Las dos cosas juntas</h3>
        <p><b>Encaja</b> Cuando quieres los libros al día sin llevarlos tú, y que quien los lleva sea quien firma lo que se presenta. No hay traspaso porque no hay dos sistemas.</p>
        <p class="cuando-no"><b>No encaja</b> No encaja si prefieres tener la contabilidad y el software con proveedores distintos para no depender de uno solo. Es una preferencia legítima y no vamos a discutirla.</p>
      </div>"""

CSS_COMPARATIVA = """
/* ── Comparativa ─────────────────────────────────────────────
   La columna propia se marca, pero no se maquilla: si las otras
   dos salieran mal en todas las filas, nadie se creeria la tabla. */
.comparativa th[scope="col"]{font-size:13px;color:var(--tinta-fuerte);text-transform:none;
  letter-spacing:0;font-weight:600;vertical-align:bottom}
.comparativa th[scope="row"]{font-size:14px;font-weight:600;color:var(--tinta-fuerte);
  white-space:normal;width:9rem;text-transform:none;letter-spacing:0}
.comparativa td{font-size:14.5px;color:var(--grafito);vertical-align:top}
.comparativa .col-nuestra{color:var(--azul)}
.comparativa tbody td:last-child{background:var(--azul-tinte)}
.comparativa thead th:last-child{background:var(--azul-tinte)}
.cuando{padding:22px 0;border-top:1px solid var(--borde)}
.cuando h3{margin-bottom:10px}
.cuando p{color:var(--grafito);margin-bottom:8px;max-width:66ch}
.cuando b{color:var(--tinta-fuerte);font-weight:600}
.cuando-no b{color:var(--piedra)}
"""


def pagina_comparativa():
    """Las tres maneras de llevar esto, comparadas sin maquillar."""
    rastro = migas(("/", "Inicio"), (None, "Cómo se compara"))
    cuerpo = '''%(enc)s

<section class="seccion">
  <div class="wrap estrecho prosa revela">
    <h2 style="margin-top:0">La decisión no es entre marcas</h2>
    <p>Quien busca gestoría no compara empresas: compara maneras de llevarlo. O sigues con la
      gestoría de siempre y un programa aparte, o te compras un software y lo lleva alguien de
      tu equipo, o juntas las dos cosas. Esa es la decisión.</p>
    <p>Ninguna de las tres es mala en abstracto. Cada una tiene un caso en el que es la
      correcta, y esta página dice cuál es, incluida la nuestra y cuándo no lo es.</p>
  </div>
</section>

<section class="seccion">
  <div class="wrap">
%(tabla)s
  </div>
</section>

<section class="seccion">
  <div class="wrap estrecho">
    <h2 style="margin-top:0">Cuándo encaja cada una</h2>
%(cuando)s
  </div>
</section>

<section class="seccion">
  <div class="wrap estrecho">
%(dibujo)s
  </div>
</section>

<section class="seccion">
  <div class="wrap estrecho prosa revela">
    <h2>Lo que no cambia elijas lo que elijas</h2>
    <p>Los libros tienen que estar bien, los modelos hay que presentarlos en plazo y alguien
      tiene que responder si Hacienda pregunta. Las tres opciones resuelven eso; lo que cambia
      es quién carga con qué y cuándo te enteras de las cosas.</p>
    <p>Y una cosa que conviene mirar en cualquiera de las tres: cómo se sale. Pregunta en qué
      formato te devuelven tus datos si algún día te vas. Si la respuesta es vaga, ya sabes
      cómo será la salida.</p>
  </div>
</section>

%(cierre)s

<style>%(css)s</style>''' % {
        "enc": encabezado("Cómo se compara", "Tres maneras de llevar la gestión",
                          "Gestoría de siempre con un programa aparte, software que llevas tú, "
                          "o las dos cosas juntas. Qué cambia en cada una y cuándo conviene, "
                          "también cuándo no conviene la nuestra.", rastro),
        "tabla": TABLA_COMPARATIVA,
        "cuando": CUANDO_COMPARATIVA,
        "dibujo": DP.para("comparativa"),
        "cierre": cierre("¿Cuál te encaja a ti?",
                         "En la primera llamada te decimos cuál de las tres tiene más sentido "
                         "en tu caso, aunque no sea la nuestra."),
        "css": CSS_COMPARATIVA,
    }
    return P.pagina("Gestoría online, software o las dos cosas · Contaes",
                    "Gestoría de siempre con programa aparte, software que llevas tú, o las dos "
                    "juntas. Qué cambia, cuándo encaja cada una y cuándo no.",
                    "%s/comparativa/" % DOMINIO, cuerpo)


def pagina_recursos():
    """La entrada a todo lo que se puede leer sin hablar con nadie."""
    rastro = migas(("/", "Inicio"), (None, "Recursos"))
    tarjetas = rejilla_tarjetas([(r, n, d) for r, n, d in P.RECURSOS], "/")
    cuerpo = '''%(enc)s

<section class="seccion">
  <div class="wrap">
    %(tarjetas)s
  </div>
</section>

<section class="seccion">
  <div class="wrap estrecho prosa revela">
    <h2>Por qué publicamos esto</h2>
    <p>Una gestoría vive de que sus clientes no tengan que entender de contabilidad. Publicar
      cómo funciona parece ir en contra de eso, y no lo va: quien entiende lo que le estamos
      haciendo pregunta mejor, decide antes y discute los números en vez de asentir.</p>
    <p>Además hay una parte egoísta que conviene decir: si algo de lo que lees aquí te sirve
      para arreglarlo tú solo, tampoco pasa nada. Preferimos que nos llames cuando de verdad
      haga falta a que nos llames por algo que podías resolver leyendo diez minutos.</p>

    <h2>Lo que no vas a encontrar</h2>
    <p>Ni plantillas descargables a cambio de tu correo, ni informes con cifras de sector que
      nadie puede comprobar, ni artículos escritos para colocar una palabra en un buscador.
      Cada pieza responde una pregunta entera o no está.</p>
    <p>Tampoco cifras concretas de tipos, plazos ni umbrales: la normativa cambia y un número
      mal puesto en una web hace daño meses después. Cuando hace falta un número, el artículo
      te dice dónde mirarlo.</p>
  </div>
</section>

%(cierre)s''' % {
        "enc": encabezado("Recursos", "Para leer antes de llamar a nadie",
                          "Artículos, un glosario, el calendario de modelos, calculadoras y "
                          "las preguntas que más nos hacen. Todo abierto, sin pedir el correo "
                          "a cambio.", rastro),
        "tarjetas": tarjetas,
        "cierre": cierre(),
    }
    return P.pagina("Recursos · Contaes",
                    "Blog, glosario de contabilidad y fiscalidad, calendario de modelos, "
                    "calculadoras y preguntas frecuentes. Abierto y sin registro.",
                    "%s/recursos/" % DOMINIO, cuerpo)


def pagina_herramientas():
    """Cuatro cuentas que se hacen mal en una servilleta."""
    rastro = migas(("/", "Inicio"), ("/#", "Recursos"), (None, "Herramientas"))
    cuerpo = '''%(enc)s

<section class="seccion">
  <div class="wrap estrecho">
%(indice)s
  </div>
</section>

%(calculadoras)s

%(cierre)s

<style>%(css)s</style>
<script>%(js)s</script>''' % {
        "enc": encabezado("Recursos", "Cuatro cuentas que conviene hacer bien",
                          "Se calculan en tu navegador y no se envía nada a ninguna parte. "
                          "Ninguna trae tipos ni porcentajes puestos por nosotros: los pones "
                          "tú, porque cambian y dependen de tu caso.", rastro),
        "indice": H.indice(),
        "calculadoras": H.cuerpo(),
        "cierre": cierre("¿Y si lo miramos con tus números?",
                         "Estas cuentas son la versión rápida. La de verdad sale de tus libros, "
                         "y para eso hace falta media hora de conversación."),
        "css": H.ESTILOS,
        "js": H.js(),
    }
    return P.pagina("Calculadoras para tu empresa · Contaes",
                    "Coste real de una contratación, punto de equilibrio, lo que cuesta cobrar "
                    "tarde y el IVA de una factura. Se calculan en tu navegador.",
                    "%s/herramientas/" % DOMINIO, cuerpo)


def pagina_glosario():
    rastro = migas(("/", "Inicio"), ("/#", "Recursos"), (None, "Glosario"))
    terminos = sorted(CP.GLOSARIO, key=lambda x: x[0].lower())
    filas = "".join(
        '    <div class="tarjeta revela" id="%s">\n'
        '      <p class="etiqueta" style="margin-bottom:8px">%s</p>\n'
        '      <h2 class="tarjeta-tit">%s</h2>\n      <p style="margin-top:8px">%s</p>\n    </div>\n'
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
    return P.pagina("Glosario de contabilidad y fiscalidad · Contaes",
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
    return P.pagina("Calendario fiscal para pymes y autónomos · Contaes",
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
    return P.pagina("Preguntas frecuentes · Contaes",
                    "Si está disponible, qué hace la IA y qué no, quién firma los modelos, cómo se migra desde otro ERP y cuánto costará.",
                    "%s/preguntas/" % DOMINIO, cuerpo, extra_head=ld)


# ─────────────────────────────────────────────────────────────────────
# Empresa: sobre, migracion, seguridad, precios, integraciones
# ─────────────────────────────────────────────────────────────────────
def envuelve_dibujo(dibujo):
    """El dibujo en su seccion, o nada si esa pagina no lleva.

    Un dibujo de relleno estorba mas que la falta de dibujo, asi que las
    paginas legales y las de agradecimiento no llevan ninguno."""
    if not dibujo:
        return ""
    return ('<section class="seccion">' + chr(10)
            + '  <div class="wrap estrecho">' + chr(10)
            + dibujo + chr(10)
            + '  </div>' + chr(10) + '</section>' + chr(10) + chr(10))


def pagina_simple(slug, etiqueta, titulo, entradilla, secciones, meta,
                  rastro_nombre=None, extra="", cierre_txt=None):
    dibujo = DP.para(slug.rstrip("/"))
    rastro = migas(("/", "Inicio"), (None, rastro_nombre or titulo))
    cuerpo = '''%(enc)s

<section class="seccion">
  <div class="wrap estrecho prosa revela">
%(prosa)s
  </div>
</section>

%(dibujo)s%(extra)s
%(cierre)s''' % {
        "enc": encabezado(etiqueta, titulo, entradilla, rastro),
        "prosa": prosa(secciones),
        "dibujo": envuelve_dibujo(dibujo),
        "extra": extra,
        "cierre": cierre(*cierre_txt) if cierre_txt else cierre(),
    }
    return P.pagina("%s · Contaes" % titulo, meta, "%s/%s" % (DOMINIO, slug), cuerpo)


def pagina_precios():
    rastro = migas(("/", "Inicio"), (None, "Precios"))
    factores = [
        ("Cuánta gente lo usa", "no es lo mismo una administración de dos personas que un equipo de treinta con acceso desde obra o desde tienda."),
        ("Qué módulos del software usas", "quien solo necesita contabilidad y facturación no debería pagar por inventario y proyectos."),
        ("Qué servicios contratas", "no es lo mismo la gestoría sola que sumarle dirección financiera, captación de clientes o la búsqueda de financiación. Se contrata por partes."),
        ("El volumen de documentos", "leer y clasificar facturas tiene un coste por documento; una empresa con cien facturas al mes no es como una con tres mil."),
        ("La migración", "traerse el histórico de otro sistema es un trabajo con principio y final, y se presupuesta aparte."),
    ]
    filas = "".join('    <li><b>%s</b><span>%s</span></li>\n' % (t, d) for t, d in factores)
    cuerpo = '''%(enc)s

<section class="seccion">
  <div class="wrap estrecho">
    <div class="aviso">
      <strong>No publicamos tarifa, y te decimos por qué.</strong> Una gestoría que cobra lo
      mismo a un autónomo con veinte facturas al año que a una empresa de treinta personas con
      almacén está cobrando de más a uno de los dos. El presupuesto sale de cinco cosas
      concretas, y las tienes aquí abajo.
    </div>
  </div>
</section>

<section class="seccion">
  <div class="wrap estrecho revela">
    <h2 style="margin-top:0">Las cinco cosas que mueven el precio</h2>
    <p class="cuerpo" style="margin-bottom:8px">Ninguna sorpresa: son las mismas que te preguntaría cualquier gestoría seria antes de darte un número.</p>
    <ul class="lista">
%(filas)s    </ul>
  </div>
</section>

<section class="seccion">
  <div class="wrap estrecho">
%(dibujo)s
  </div>
</section>

<section class="seccion">
  <div class="wrap estrecho prosa revela">
    <h2>Lo que no vamos a hacer</h2>
    <p>No hay plan gratuito que sirva de poco para que acabes pagando el de arriba. No hay precio de entrada que suba al año siguiente sin avisar. Y el presupuesto de migración se cierra antes de firmar, no después.</p>
    <p>Tampoco hay permanencia escondida en una cláusula. Si un día te vas, te llevas tus datos en un formato que se abre sin nuestro programa.</p>
  </div>
</section>

%(cierre)s''' % {
        "enc": encabezado("Precios", "De qué depende lo que pagas",
                          "Cada empresa paga por lo que usa. Aquí está de qué depende el presupuesto, "
                          "para que sepas qué te van a preguntar antes de la llamada.", rastro),
        "filas": filas,
        "dibujo": DP.para("precios"),
        "cierre": cierre("¿Cuánto te saldría a ti?",
                         "Cuéntanos cuánta gente sois, qué usáis hoy y cuántas facturas movéis al mes. "
                         "Con eso te damos un número, no un rango."),
    }
    return P.pagina("Precios · Contaes",
                    "De qué depende el presupuesto de una gestoría online: personas, servicios contratados, volumen de documentos y migración. Y lo que no vamos a hacer.",
                    "%s/precios/" % DOMINIO, cuerpo)


def pagina_integraciones():
    rastro = migas(("/", "Inicio"), (None, "Integraciones"))
    previstas = [
        ("Tu banco", "el extracto entra para conciliar. Formato estándar Norma 43, que exporta cualquier banco español, y las conexiones abiertas por PSD2 donde están disponibles."),
        ("La Agencia Tributaria", "por ahí pasan los modelos. Es la parte del servicio que hace una persona colegiada con su firma."),
        ("Tu correo", "una dirección a la que reenviar las facturas de proveedor. Entran por el escáner y salen clasificadas."),
        ("Tu tienda o tu TPV", "si vendes online o en local, los pedidos pueden entrar sin teclearse. Se monta caso por caso según con qué vendas."),
        ("Tus pasarelas de cobro", "para cuadrar lo cobrado con lo liquidado, que es donde se pierden las comisiones sin que nadie las registre."),
        ("La puerta de salida", "poder sacar tus datos en formatos estándar. No es una integración: es la condición para poder irte, y por tanto para poder confiar."),
    ]
    filas = "".join('    <li><b>%s</b><span>%s</span></li>\n' % (t, d) for t, d in previstas)
    cuerpo = '''%(enc)s

<section class="seccion">
  <div class="wrap estrecho">
    <div class="aviso">
      <strong>Aquí no vas a ver un muro de logotipos.</strong> Un catálogo largo de conectores
      suele esconder que la mayoría hacen poco: mueven un dato de un sitio a otro y dejan el
      trabajo de cuadrar para una persona. Preferimos contarte con qué trabajamos de verdad y
      preguntarte qué necesitas tú.
    </div>
  </div>
</section>

<section class="seccion">
  <div class="wrap estrecho revela">
    <h2 style="margin-top:0">Lo que entra y sale del sistema</h2>
    <ul class="lista">
%(filas)s    </ul>
  </div>
</section>

<section class="seccion">
  <div class="wrap estrecho">
%(dibujo)s
  </div>
</section>

<section class="seccion">
  <div class="wrap estrecho prosa revela">
    <h2>Por qué no hay cien integraciones</h2>
    <p>La razón de ser de Contaes es que las cosas estén dentro y no conectadas por fuera. Cada integración que montamos es una que no ha hecho falta construir dentro, y eso es una decisión, no una victoria.</p>
    <h2>Si necesitas una concreta</h2>
    <p>Dínoslo en la primera llamada. Saber con qué tenéis que hablar los sistemas es parte de decidir si encajamos, y a veces la respuesta honesta es que hoy no llegamos.</p>
  </div>
</section>

%(cierre)s''' % {
        "enc": encabezado("Integraciones", "Con qué trabajamos, y qué te vamos a preguntar",
                          "Lo que hace falta para llevar una gestoría entra por aquí: el banco, la sede de la Agencia Tributaria y el correo por el que llegan las facturas.", rastro),
        "filas": filas, "dibujo": DP.para("integraciones"), "cierre": cierre(),
    }
    return P.pagina("Integraciones · Contaes",
                    "Con qué trabaja Contaes: tu banco por Norma 43, la sede de la Agencia Tributaria, el correo de facturas, tu tienda y tus pasarelas de cobro.",
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

%(formulario)s

  </div>
</section>''' % {
        "enc": encabezado("Hablemos", "¿Te enseñamos cómo funciona?",
                          "Una demo sobre tu caso concreto, no una presentación genérica. "
                          "Cuéntanos qué usáis ahora y qué es lo que peor lleváis.", rastro),
        "filas": filas,
        "formulario": F.form("Contaes: peticion desde /demo/"),
    }
    return P.pagina("Pedir una demo · Contaes",
                    "Una demo sobre vuestro caso concreto. Si no encajamos, se dice en la primera llamada.",
                    "%s/demo/" % DOMINIO, cuerpo)



def pagina_gracias():
    """Donde aterriza quien acaba de enviar el formulario. Sin indexar:
    no tiene sentido llegar aqui desde un buscador."""
    cuerpo = '''<section class="encabezado">
  <div class="wrap estrecho" style="text-align:center;padding:60px 0 20px">
    <p class="etiqueta">Recibido</p>
    <h1 style="margin-top:10px">Gracias. Te contestamos pronto.</h1>
    <p class="editorial" style="margin:18px auto 0;max-width:52ch">
      Hemos recibido lo que nos has contado. Lo leemos nosotros, no un formulario
      automatico, asi que la respuesta tarda lo que tarda una persona en leerlo.
    </p>
    <div style="margin-top:30px;display:flex;gap:10px;justify-content:center;flex-wrap:wrap">
      <a class="btn btn-azul" href="/">Volver al inicio <span class="flecha" aria-hidden="true">&rarr;</span></a>
      <a class="btn btn-tinte" href="/blog/">Leer el blog</a>
    </div>
  </div>
</section>

<section class="seccion">
  <div class="wrap estrecho revela">
    <h2 style="margin-top:0">Mientras tanto</h2>
    <p class="cuerpo" style="margin-bottom:22px">Si quieres ir haciendote una idea, estas tres paginas son las que mas cuentan.</p>
    <div class="rejilla">
      <a class="tarjeta" href="/funcionalidades/asesoria-fiscal/"><h2 class="tarjeta-tit">Asesoria fiscal incluida</h2><p>Lo que de verdad separa a Contaes de un ERP normal.</p></a>
      <a class="tarjeta" href="/migracion/"><h2 class="tarjeta-tit">Migracion</h2><p>Como se cambia de sistema sin parar la empresa.</p></a>
      <a class="tarjeta" href="/preguntas/"><h2 class="tarjeta-tit">Preguntas</h2><p>Incluidas las incomodas.</p></a>
    </div>
  </div>
</section>'''
    return P.pagina("Gracias · Contaes",
                    "Hemos recibido tu mensaje. Te contestamos pronto.",
                    "%s/gracias/" % DOMINIO, cuerpo, noindex=True)


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
                 "Este sitio informa sobre los servicios de Contaes. No permite contratar en línea ni "
                 "realizar pagos: la contratación se formaliza aparte, y aquí solo se recogen "
                 "solicitudes de contacto.",
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
                 "El formulario se envía a través de FormSubmit (formsubmit.co), un servicio que "
                 "recibe el envío y lo reenvía a nuestro buzón. Es decir, tus datos pasan por ese "
                 "servicio antes de llegarnos: lo decimos porque es tu derecho saberlo. Si prefieres "
                 "evitarlo, escríbenos directamente a %s." % d["correo"],
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
                 " (como la dirección IP) para servir las páginas y protegerse de abusos. Las tipografías "
                 "se cargan desde Google Fonts, lo que implica una conexión a servidores de Google. El "
                 "formulario se procesa a través de FormSubmit, que actúa como encargado del tratamiento "
                 "para hacernos llegar tu mensaje.",
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
                 "Tu navegador guarda además datos técnicos propios (caché, preferencias) que no son "
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
        salidas[ruta + "index.html"] = P.pagina("%s · Contaes" % titulo, meta,
                                                "%s/%s" % (DOMINIO, ruta), cuerpo)
    return salidas


# ─────────────────────────────────────────────────────────────────────
# Sitemap y robots
# ─────────────────────────────────────────────────────────────────────
def articulos_del_blog():
    """Solo los que ya estan publicados: el sitemap no puede anunciar
    paginas que aun no existen."""
    import calendario_blog as CAL
    ruta = os.path.join(AQUI, "build-blog.py")
    spec = importlib.util.spec_from_file_location("build_blog", ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    publicados, _total = CAL.reparte(mod.ARTICULOS)
    return [a["slug"] for a in publicados]


def construir_sitemap(rutas):
    """El sitemap, con la fecha real de cada fichero.

    La fecha sale de cuando se escribio el HTML, no de una constante: un
    lastmod inventado es peor que no ponerlo, porque el buscador aprende
    que no puede fiarse y deja de mirarlo."""
    import datetime
    filas = []
    for r in rutas:
        u = "%s/%s" % (DOMINIO, r) if r else "%s/" % DOMINIO
        prioridad = "1.0" if not r else ("0.8" if r.count("/") <= 1 else "0.6")
        fichero = os.path.join(RAIZ, r.replace("/", os.sep) + ("index.html" if r.endswith("/") or not r else ""))
        fecha = ""
        if os.path.exists(fichero):
            marca = datetime.date.fromtimestamp(os.path.getmtime(fichero))
            fecha = "\n    <lastmod>%s</lastmod>" % marca.isoformat()
        filas.append("  <url>\n    <loc>%s</loc>%s\n    <changefreq>%s</changefreq>"
                     "\n    <priority>%s</priority>\n  </url>"
                     % (u, fecha, "weekly" if not r else "monthly", prioridad))
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s\n</urlset>\n'
            % "\n".join(filas))


# ─────────────────────────────────────────────────────────────────────
def main():
    P.escribe_hoja(RAIZ)
    salidas = {}

    salidas["funcionalidades/index.html"] = pagina_funcionalidades()
    for slug, d in C.MODULOS.items():
        salidas["funcionalidades/%s/index.html" % slug] = pagina_funcionalidad(slug, d, True)
    for slug, d in C.CAPACIDADES.items():
        salidas["funcionalidades/%s/index.html" % slug] = pagina_funcionalidad(slug, d, False)

    for area in AREAS:
        _e, _n, datos, mapa = AREAS[area]
        for slug, _nombre, _pie in mapa:
            salidas["%s/%s/index.html" % (area, slug)] = pagina_servicio(area, slug, datos[slug])

    salidas["gestoria/index.html"] = pagina_area(
        "gestoria", "La gestoría, hecha como debería estar hecha",
        "Contabilidad, impuestos, nóminas y contratos. Lo de siempre, pero con los libros "
        "al día todos los días y no a final de trimestre, y con el software incluido en "
        "vez de aparte.",
        intro=[
            ("Qué cambia respecto a la gestoría de siempre", [
                "El reparto habitual es este: tú guardas papeles durante tres meses, los mandas, "
                "y recibes unos números cuando ya no puedes hacer nada con ellos. No es culpa de "
                "nadie: es que el despacho no tiene tus datos hasta que se los das.",
                "Aquí el programa es el mismo para los dos. Cada factura que emites y cada gasto "
                "que entra deja su apunte en el momento, así que a final de trimestre no hay nada "
                "que reconstruir. Y tú entras a mirar tus libros cuando quieras, sin pedirlos.",
            ]),
            ("Quién firma lo que se presenta", [
                "La parte automática prepara. La responsabilidad ante la Administración es de una "
                "persona colegiada que revisa, firma y presenta. No es un matiz: es la diferencia "
                "entre un servicio profesional y una herramienta que te deja solo ante un "
                "requerimiento.",
                "Y antes de presentar te avisamos de lo que descuadra. Un gasto sin factura "
                "válida, un tipo de IVA que no cuadra con lo declarado, una operación "
                "intracomunitaria tratada como nacional. Se corrige antes, no en una "
                "regularización.",
            ]),
            ("Cómo se cambia desde otra gestoría", [
                "La documentación contable de tu empresa es tuya, la tenga quien la tenga. Antes "
                "de cerrar la relación anterior conviene pedir por escrito los libros, los modelos "
                "presentados con su justificante, el balance de sumas y saldos y los datos de "
                "clientes y proveedores con su histórico.",
                "El momento limpio es a cierre de ejercicio; el segundo mejor, a cierre de "
                "trimestre con los modelos ya presentados. Y conviene solapar unas semanas, "
                "para que quien se va pueda aclarar dudas de lo que hizo.",
            ]),
        ],
        dibujo=DP.flujo_modelo(),
        preguntas=[
            ("¿Tengo que cambiar de programa para que llevéis la contabilidad?",
             "Si vienes de otro sistema, se traen los datos con su histórico y hay un periodo en "
             "que los dos conviven, con el antiguo en solo lectura para consultar y comparar. No "
             "se apaga nada hasta que lo nuevo está funcionando y cuadrado."),
            ("¿Puedo ver mis libros cuando quiera o me los mandáis?",
             "Entras y los miras. Esa es media razón de que el software vaya dentro: si tienes que "
             "pedir tus propios números, la contabilidad no está al día, está archivada."),
            ("¿Qué pasa si Hacienda me requiere algo de un año anterior?",
             "Lo miramos caso por caso antes de comprometernos a nada. Si el periodo lo llevó otro "
             "despacho, hay que ver qué documentación hay y qué se presentó, y decirte con "
             "franqueza qué se puede hacer."),
        ])

    salidas["crecimiento/index.html"] = pagina_area(
        "crecimiento", "Lo que una gestoría normal no te da",
        "Una gestoría te mantiene en regla. Esto es lo que hace falta además para crecer: "
        "dirección financiera, marketing, clientes nuevos, financiación y salir fuera. Con "
        "las mismas personas que ya conocen tus números.",
        intro=[
            ("Por qué esto va con la gestoría y no aparte", [
                "Un consultor externo empieza siempre por lo mismo: pedirte los números y "
                "entenderlos. Eso son semanas que pagas antes de que nadie te diga nada útil, y "
                "se repite con cada consultor que contratas.",
                "Quien ya lleva tu contabilidad no tiene que empezar por ahí. Sabe qué margen "
                "tiene cada línea, quién te paga tarde y cuánta caja te queda, porque son los "
                "mismos datos que usa para presentar tus modelos.",
            ]),
            ("Se contrata por partes", [
                "Nadie necesita las seis cosas a la vez. Lo normal es empezar por una: la "
                "dirección financiera cuando las decisiones ya no caben en la cabeza del dueño, "
                "la financiación cuando hay una inversión delante, la prospección cuando el boca "
                "a boca deja de traer suficiente.",
                "En la primera llamada preferimos decirte cuál de las seis te haría falta ahora "
                "y cuáles pueden esperar, aunque eso signifique venderte menos.",
            ]),
        ],
        preguntas=[
            ("¿Hay que tener la gestoría con vosotros para contratar esto?",
             "No es obligatorio, pero funciona mucho mejor. La ventaja de que lo lleve quien ya "
             "tiene tus números es justo esa: que no hay que empezar por explicárselos."),
            ("¿Esto sustituye a contratar a alguien en plantilla?",
             "Durante un tiempo, sí. Cuando la empresa da para tener un director financiero o un "
             "responsable de marketing a jornada completa, lo suyo es contratarlo, y te lo diremos."),
            ("¿Qué pasa si no funciona?",
             "Se ve pronto, porque estos servicios se miden. Si a los pocos meses no ha movido "
             "nada, lo honesto es decirlo y parar, no renovar por inercia."),
        ])

    salidas["para/index.html"] = pagina_area(
        "para", "Autónomos, startups y pymes",
        "No necesitan lo mismo. Un autónomo quiere saber qué le queda al mes; una startup, "
        "unos libros que aguanten una ronda; una pyme, que la administración crezca al ritmo "
        "de la empresa.",
        intro=[
            ("Lo que cambia según en cuál estés", [
                "Un autónomo tiene un problema de tiempo y de dudas: qué se deduce y qué no, qué "
                "modelo le toca, y cuánto le queda de verdad después de cuota e impuestos. Casi "
                "todo lo demás sobra.",
                "Una startup tiene un problema de forma: la contabilidad como trámite funciona "
                "hasta el día que un inversor pide números, y entonces los libros tienen que "
                "aguantar una revisión. Ordenarlo después es caro y lento.",
                "Una pyme tiene un problema de escala: la empresa creció y la administración se "
                "quedó como estaba. Cuatro programas que no se hablan, un Excel crítico que lleva "
                "una persona, y el margen real conocido a fin de año.",
            ]),
            ("Y lo que no cambia", [
                "Los libros al día, los modelos presentados por alguien que firma con su nombre, "
                "y poder mirar tus propios números cuando quieras. Eso es igual para los tres.",
            ]),
        ],
        preguntas=[
            ("Soy autónomo sin empleados, ¿me hace falta esto?",
             "Depende del volumen. Si tienes pocas facturas y ningún gasto que dudar, "
             "probablemente puedas apañarte solo, y te lo diremos. Tiene sentido cuando un error "
             "cuesta más que la cuota, o cuando el tiempo en papeles es tiempo sin facturar."),
            ("Acabo de montar la empresa y aún no facturo, ¿espero?",
             "Casi todo puede esperar, sí. Lo que no conviene dejar para después es el pacto de "
             "socios y la forma jurídica, porque cambiarlos más tarde sí cuesta."),
            ("¿Se puede empezar por poco e ir sumando?",
             "Es lo normal. Casi todo el mundo empieza por la gestoría y añade lo demás cuando "
             "aparece la necesidad, no al revés."),
        ])

    salidas["sectores/index.html"] = pagina_sectores()
    for slug, d in C.SECTORES.items():
        salidas["sectores/%s/index.html" % slug] = pagina_sector(slug, d)

    salidas["glosario/index.html"] = pagina_glosario()
    salidas["herramientas/index.html"] = pagina_herramientas()
    salidas["recursos/index.html"] = pagina_recursos()
    salidas["comparativa/index.html"] = pagina_comparativa()
    salidas["calendario-fiscal/index.html"] = pagina_calendario()
    salidas["preguntas/index.html"] = pagina_preguntas()
    salidas["precios/index.html"] = pagina_precios()
    salidas["integraciones/index.html"] = pagina_integraciones()
    salidas["demo/index.html"] = pagina_demo()
    salidas["gracias/index.html"] = pagina_gracias()

    salidas["sobre/index.html"] = pagina_simple(
        "sobre/", "Empresa", "Qué estamos construyendo",
        "Contaes es una gestoría online con el software dentro y gente que te ayuda a "
        "crecer. Esta página cuenta por qué existe y con qué criterio se trabaja.",
        [("El hueco que intenta llenar", [
            "Una pyme española con quince personas tiene hoy dos cosas separadas: un programa donde mete los datos y una asesoría a la que se los manda. En medio hay un mes de correos, una hoja de cálculo y la pregunta de siempre.",
            "Ese hueco no es un problema de software. Es un problema de reparto: el programa no se responsabiliza de lo que se presenta, y la asesoría no tiene los datos al día. Contaes existe para que las dos cosas estén del mismo lado.",
        ]),
         ("Con qué criterio se construye", [
             "Que el dato se registre una vez, donde ocurre el hecho. Que cualquier cifra se pueda seguir hasta el documento que la origina. Que lo que sale de la empresa (un correo, un modelo) lo apruebe una persona. Y que la responsabilidad ante la Administración sea de alguien colegiado, no de un algoritmo.",
             "También hay un criterio sobre lo que no se hace: no competir en número de funciones, no llenar el catálogo de integraciones que hacen poco y no prometer autonomía donde debería haber criterio profesional.",
         ]),
         ("Cómo se cobra y por qué importa decirlo", [
             "Una gestoría cobra una cuota y, cuando pasa algo fuera de lo normal, un extra. El "
             "problema no es el extra: es enterarse del extra después. Nosotros preferimos "
             "decir el precio de lo excepcional antes de que ocurra, aunque eso obligue a tener "
             "conversaciones incómodas el primer día.",
             "Y no cobramos por cosas que no cuestan trabajo. Enviarte tus propios datos no es "
             "un servicio: es tuyo. Que puedas sacarlos en un formato que se abre sin nuestro "
             "programa es la condición para poder irte, y por tanto la condición para confiar.",
         ]),
         ("Qué pasa cuando nos equivocamos", [
             "Va a pasar. Una gestoría que lleva cientos de empresas comete errores, y quien "
             "diga lo contrario no ha llevado ninguna. Lo que se puede prometer no es la "
             "perfección: es que el error se cuente en cuanto se detecta, que se diga qué "
             "consecuencias tiene y que se arregle sin cobrar por arreglarlo.",
             "El seguro de responsabilidad civil profesional cubre lo que tiene que cubrir. "
             "Pero lo que de verdad marca la diferencia es enterarse por nosotros y no por una "
             "carta de Hacienda.",
         ]),
         ("Qué encontrarás y qué no", [
             "Esta web no tiene testimonios, ni logotipos de clientes, ni cifras de usuarios. No porque no haya trabajo detrás, sino porque esas tres cosas son las más fáciles de inflar y las que menos dicen. Una gestoría que empieza la relación exagerando empieza mal.",
             "Lo que sí encontrarás es lo que hacemos, lo que no hacemos y de qué depende el precio. Con eso se puede decidir.",
         ])],
        "Contaes es una gestoría online para autónomos, startups y pymes, con software propio y servicios de crecimiento. Por qué existe y con qué criterio trabajamos.",
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
             "No tenemos certificaciones que enseñar: ni ISO 27001, ni un informe SOC 2. Podríamos no mencionarlo y casi nadie preguntaría, pero un proveedor que lleva tu contabilidad y presume de lo que no tiene es exactamente el que no quieres. Cuando existan compromisos concretos y verificables sobre alojamiento, cifrado, copias de seguridad y tiempos de recuperación, estarán aquí con su nombre y su fecha.",
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
    for area in ("gestoria", "crecimiento", "para"):
        rutas += ["%s/" % area] + ["%s/%s/" % (area, s) for s, _n, _p in AREAS[area][3]]
    rutas += ["sectores/"] + ["sectores/%s/" % s for s in C.SECTORES]
    rutas += ["comparativa/", "recursos/", "herramientas/", "glosario/", "calendario-fiscal/", "preguntas/", "precios/",
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
