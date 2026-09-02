# -*- coding: utf-8 -*-
"""Pone al dia la barra, el pie y su CSS en index.html.

    python scripts/sync-portada.py

La portada se escribe a mano porque tiene piezas que no comparte nadie
-el fondo en canvas, la maqueta del asistente, la pila de modulos-, pero
su menu tiene que ser el mismo que el de las otras 37 paginas. Antes era
una copia, y una copia se separa: se anade una pagina al menu, se
regenera el sitio y la portada se queda con el menu de ayer.

Esto lo resuelve reescribiendo esos trozos desde plantilla.py cada vez.
Se puede ejecutar tantas veces como haga falta: siempre deja lo mismo.
"""
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)
import plantilla as P

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ABRE_CSS = "/* === barra y pie: los reescribe scripts/sync-portada.py === */"
CIERRA_CSS = "/* === fin de barra y pie === */"


def trozo_de_estilos(desde, hasta):
    m = re.search(re.escape(desde) + r"(.*?)" + re.escape(hasta), P.ESTILOS, re.S)
    assert m, "no encontrado el trozo '%s' en plantilla.ESTILOS" % desde[:30]
    return m.group(0)[:-len(hasta)].rstrip() if hasta else m.group(0)


def main():
    ruta = os.path.join(RAIZ, "index.html")
    t = io.open(ruta, encoding="utf-8").read()
    antes = t

    # ── el marcado ───────────────────────────────────────────────────
    m = re.search(r'<nav class="nav" aria-label="Principal">.*?\n</nav>', t, re.S)
    assert m, "no encontrada la barra en index.html"
    t = t[:m.start()] + P.cabecera("").split("\n", 1)[1] + t[m.end():]

    m = re.search(r"<footer>.*?\n</footer>", t, re.S)
    assert m, "no encontrado el pie en index.html"
    t = t[:m.start()] + P.pie("") + t[m.end():]

    # ── el CSS, entre marcas ─────────────────────────────────────────
    barra = trozo_de_estilos("/* ── La barra, con el menu por areas", "\n\n/* la marca animada")
    pie_css = re.search(r"footer\{background:var\(--medianoche\).*?footer small\{[^\n]*\}", P.ESTILOS, re.S).group(0)
    bloque = "%s\n%s\n\n%s\n%s\n" % (ABRE_CSS, barra, pie_css, CIERRA_CSS)

    if ABRE_CSS in t:
        i = t.index(ABRE_CSS)
        j = t.index(CIERRA_CSS) + len(CIERRA_CSS) + 1
        t = t[:i] + bloque + t[j:]
    else:
        # primera vez: se coloca donde estaba el CSS de la barra copiado
        m = re.search(r"/\* La barra y su menu por areas:.*?\n(?=/\* la marca animada)", t, re.S)
        assert m, "no encontrado el CSS de la barra en index.html"
        t = t[:m.start()] + bloque + "\n" + t[m.end():]
        # y el del pie, que estaba en otro sitio
        m = re.search(r"footer\{background:var\(--medianoche\).*?footer small\{[^\n]*\}\n", t, re.S)
        if m and m.start() > t.index(ABRE_CSS) + len(bloque):
            t = t[:m.start()] + t[m.end():]

    # ── el JS del menu ───────────────────────────────────────────────
    nuevo_js = re.search(r"(/\* -- El menu: por areas en escritorio.*?\n\}\)\(\);\n)", P.PIE_JS, re.S).group(1)
    m = re.search(r"/\* -- El menu: por areas en escritorio.*?\n\}\)\(\);\n", t, re.S)
    assert m, "no encontrado el JS del menu en index.html"
    t = t[:m.start()] + nuevo_js + t[m.end():]

    io.open(ruta, "w", encoding="utf-8").write(t)
    print("  index.html: barra, pie y su CSS al dia" + ("" if t != antes else " (ya estaban)"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
