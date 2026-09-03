# -*- coding: utf-8 -*-
"""Busca en el texto del sitio las marcas de escritura generada por IA.

    python scripts/check-voz.py

Basado en las senales que recoge Wikipedia en "Signs of AI writing",
traducidas al castellano. No detecta si un texto lo escribio una maquina:
detecta los tics que hacen que lo parezca, que es lo que molesta al leer.

Un tic suelto no dice nada. Lo que delata es el racimo: tres rayas, una
enumeracion de tres, dos gerundios de relleno y un "clave" en el mismo
parrafo. Por eso se puntua por cada mil palabras y se avisa por encima de
un umbral, en vez de perseguir apariciones sueltas.
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ─────────────────────────────────────────────────────────────────────
# Los tics, con su peso. El peso alto es para lo que casi nunca escribe
# una persona; el bajo, para lo que abusa la maquina pero existe.
# ─────────────────────────────────────────────────────────────────────
TICS = [
    ("raya de inciso", 2.0,
     r"[—–]",
     "La raya de inciso es correcta en castellano, pero la maquina la pone en "
     "todas partes. Casi siempre vale una coma, un punto o un parentesis."),

    ("no solo... sino", 3.0,
     r"\bno s[oó]lo\b[^.]{0,80}\bsino\b|\bno se trata de\b[^.]{0,60}\bsino\b|"
     r"\bmas que\b[^.]{0,40}\bes\b[^.]{0,30}\bque\b",
     "Paralelismo negativo. Suena a eslogan y no anade informacion."),

    ("gerundio de relleno", 2.5,
     r",\s*(permitiendo|garantizando|asegurando|logrando|facilitando|"
     r"consiguiendo|destacando|reflejando|contribuyendo|impulsando|"
     r"potenciando|optimizando|maximizando)\b",
     "Gerundio pegado al final para fingir profundidad. Se corta la frase "
     "o se dice que pasa de verdad."),

    ("palabra de folleto", 2.0,
     r"\b(clave|crucial|fundamental|esencial|vital|robusto|potente|"
     r"innovador|revolucionario|puntero|lider|integral|holistico|"
     r"sinergia|ecosistema digital|transformacion digital)\b",
     "Vocabulario de folleto. Casi siempre se puede decir lo mismo sin ello."),

    ("apertura de manual", 3.0,
     r"\b(hoy en d[ií]a|en el mundo actual|en la era digital|"
     r"a d[ií]a de hoy|en un mundo cada vez m[aá]s|cabe destacar|"
     r"es importante (?:destacar|se[nñ]alar|mencionar)|"
     r"vamos a (?:ver|analizar|explorar)|sin m[aá]s dilaci[oó]n)\b",
     "Arranque de manual. Se empieza por el asunto, no anunciandolo."),

    ("cierre generico", 3.0,
     r"\b(en (?:resumen|definitiva|conclusi[oó]n)|en s[ií]ntesis|"
     r"a modo de (?:resumen|conclusi[oó]n)|el futuro (?:pasa|es)|"
     r"un paso en la direcci[oó]n correcta)\b",
     "Cierre generico. Es mejor acabar en el ultimo dato concreto."),

    ("autoridad fingida", 2.5,
     r"\b(la (?:verdadera|autentica) (?:pregunta|clave)|en el fondo|"
     r"lo que de verdad importa|la clave est[aá] en|en esencia|"
     r"los expertos (?:coinciden|afirman)|seg[uú]n los expertos)\b",
     "Frase que finge revelar algo profundo antes de decir algo corriente."),

    ("negrita decorativa", 1.0,
     r"<strong>[^<]{1,28}</strong>\s*:",
     "Negrita con dos puntos al principio de cada punto de una lista: la "
     "lista con cabecera en negrita es de las marcas mas visibles."),
]

# "A, B y C" es castellano corriente y no delata nada. El tic no es usarla:
# es que casi todas las frases acaben en una. Se cuenta solo la variante
# larga, de sintagmas de dos o mas palabras, que es la que suena a relleno.
TRES = re.compile(r"\b\w+\s+\w+[^,.;:]{0,24},\s+\w+\s+\w+[^,.;:]{0,24}\s+y\s+\w+\s+\w+")

UMBRAL = 9.0          # puntos por cada mil palabras a partir de los cuales avisa
UMBRAL_FALLO = 16.0   # a partir de aqui, falla


def texto_de(html):
    """El texto propio de la pagina.

    Se quitan la barra y el pie: son identicos en las 65 paginas, asi que
    contarlos en todas las infla a todas por igual y no dice nada de
    ninguna.
    """
    s = re.sub(r"<(script|style)\b.*?</\1>", " ", html, flags=re.S | re.I)
    s = re.sub(r"<nav\b.*?</nav>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<footer\b.*?</footer>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    s = s.replace("&nbsp;", " ").replace("&amp;", "&").replace("&rsaquo;", ">")
    return re.sub(r"\s+", " ", s)


def analiza(nombre, html):
    visible = texto_de(html)
    palabras = len(visible.split())
    # Por debajo de doscientas palabras la puntuacion por mil se dispara: una
    # sola enumeracion en una pagina corta marca mas que diez en un articulo
    # largo, y eso no dice nada de como esta escrita.
    if palabras < 200:
        return None
    hallazgos, puntos = [], 0.0
    for etiqueta, peso, patron, _consejo in TICS:
        n = len(re.findall(patron, visible, re.I))
        if n:
            puntos += peso * n
            hallazgos.append((etiqueta, n))
    tres = len(TRES.findall(visible))
    # una enumeracion de tres cada tantas palabras es normal; el exceso no
    exceso = max(0, tres - palabras // 130)
    if exceso:
        puntos += 1.2 * exceso
        hallazgos.append(("enumeracion de tres", exceso))
    return {"nombre": nombre, "palabras": palabras,
            "puntos": puntos, "por_mil": puntos * 1000.0 / palabras,
            "hallazgos": hallazgos}


def paginas():
    saltar = {".git", "scripts", "assets", "node_modules"}
    for base, dirs, ficheros in os.walk(RAIZ):
        dirs[:] = [d for d in dirs if d not in saltar]
        for f in sorted(ficheros):
            if f.endswith(".html"):
                yield os.path.relpath(os.path.join(base, f), RAIZ).replace(os.sep, "/")


def main():
    resultados = []
    for rel in paginas():
        html = io.open(os.path.join(RAIZ, rel), encoding="utf-8", errors="replace").read()
        r = analiza(rel, html)
        if r:
            resultados.append(r)

    resultados.sort(key=lambda r: -r["por_mil"])
    malas = [r for r in resultados if r["por_mil"] >= UMBRAL]
    fallan = [r for r in resultados if r["por_mil"] >= UMBRAL_FALLO]

    print("Voz: marcas de escritura automatica")
    print("=" * 62)
    print("  %d paginas analizadas, %d palabras"
          % (len(resultados), sum(r["palabras"] for r in resultados)))
    media = (sum(r["por_mil"] for r in resultados) / len(resultados)) if resultados else 0
    print("  media: %.1f puntos por mil palabras (avisa en %.0f, falla en %.0f)"
          % (media, UMBRAL, UMBRAL_FALLO))

    if malas:
        print()
        print("  Paginas por encima del umbral:")
        for r in malas[:18]:
            detalle = ", ".join("%s x%d" % (e, n) for e, n in
                                sorted(r["hallazgos"], key=lambda x: -x[1])[:4])
            print("    %-52s %5.1f   %s" % (r["nombre"][:52], r["por_mil"], detalle))
        if len(malas) > 18:
            print("    ... y %d mas" % (len(malas) - 18))

    # que tic domina en todo el sitio
    total = {}
    for r in resultados:
        for e, n in r["hallazgos"]:
            total[e] = total.get(e, 0) + n
    if total:
        print()
        print("  Por tipo, en todo el sitio:")
        for e, n in sorted(total.items(), key=lambda x: -x[1]):
            print("    %-24s %5d" % (e, n))

    print("=" * 62)
    print("%d pagina(s) por encima del aviso, %d por encima del fallo"
          % (len(malas), len(fallan)))
    return 1 if fallan else 0


if __name__ == "__main__":
    sys.exit(main())
