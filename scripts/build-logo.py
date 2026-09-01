#!/usr/bin/env python3
"""
Genera el logo definitivo de Orezco.

El simbolo es un hexagono de puntas verticales con esquinas muy redondeadas,
dividido por una Y invertida que lo hace leer como un cubo isometrico, con un
destello de seis puntas centrado que cruza las divisiones.

Construccion: una mascara SVG. El hexagono es solido, las divisiones se restan
como huecos y el destello se vuelve a sumar encima. Asi los huecos son
**transparentes de verdad**, no del color del fondo, y el logo funciona sobre
cualquier superficie: blanco, tinta, una foto o un bordado.

    python scripts/build-logo.py
"""

import io
import math
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(RAIZ, "assets")

LIENZO = 200.0
C = LIENZO / 2          # centro
R = 86.0                # radio a los vertices
REDONDEO = 24.0         # radio de las esquinas
CORTE = 13.0            # grosor de las divisiones del cubo
DESTELLO = 15.0         # grosor de los brazos del destello
BRAZO = 52.0            # longitud de cada brazo desde el centro


def vertice(grados):
    a = math.radians(grados)
    return (C + R * math.cos(a), C - R * math.sin(a))


# Hexagono de punta arriba: vertice superior, luego cada 60 grados.
ANGULOS = [90, 30, -30, -90, -150, 150]
VERTICES = [vertice(g) for g in ANGULOS]


def hexagono_redondeado(puntos, r):
    """Camino SVG del poligono con las esquinas redondeadas por arcos reales."""
    n = len(puntos)
    trozos = []
    for i in range(n):
        prev = puntos[(i - 1) % n]
        act = puntos[i]
        sig = puntos[(i + 1) % n]

        def acortar(desde, hacia, dist):
            dx, dy = hacia[0] - desde[0], hacia[1] - desde[1]
            largo = math.hypot(dx, dy)
            k = dist / largo
            return (desde[0] + dx * k, desde[1] + dy * k)

        entrada = acortar(act, prev, r)   # punto sobre la arista que llega
        salida = acortar(act, sig, r)     # punto sobre la arista que sale

        if i == 0:
            trozos.append("M %.2f %.2f" % entrada)
        else:
            trozos.append("L %.2f %.2f" % entrada)
        # Arco de esquina. Los vertices se recorren en sentido horario en
        # coordenadas de pantalla (la y crece hacia abajo), asi que el arco
        # convexo necesita sweep-flag = 1. Con 0 las esquinas se meten hacia
        # dentro y el hexagono sale festoneado.
        trozos.append("A %.2f %.2f 0 0 1 %.2f %.2f" % (r, r, salida[0], salida[1]))
    trozos.append("Z")
    return " ".join(trozos)


def hacia(grados, dist):
    a = math.radians(grados)
    return (C + dist * math.cos(a), C - dist * math.sin(a))


CAMINO_HEX = hexagono_redondeado(VERTICES, REDONDEO)

# Divisiones del cubo: Y invertida. Del centro hacia las dos esquinas
# superiores y hacia la punta inferior. Se quedan algo cortas del borde para
# que el hueco no muerda el contorno.
DIVISIONES = [(150, R - 6), (30, R - 6), (-90, R - 6)]

# Destello: tres rectas por el centro, seis brazos, ALINEADOS con las
# divisiones. Se resta igual que ellas, asi que queda grabado en el cubo y
# cruza las tres caras. Es la lectura del logo original.
#
# Probadas tres variantes y descartadas dos: intercalar los brazos a 30 grados
# da nueve lineas y satura; dibujar el destello en solido lo hace invisible,
# porque al no cruzar ningun hueco se funde con el cuerpo.
EJES = [(90, -90), (30, -150), (150, -30)]


def svg(color="currentColor", ident="orezco"):
    div = "".join(
        '<path d="M %.2f %.2f L %.2f %.2f"/>' % (C, C, *hacia(g, d))
        for g, d in DIVISIONES
    )
    chispa = "".join(
        '<path d="M %.2f %.2f L %.2f %.2f"/>' % (*hacia(a, BRAZO), *hacia(b, BRAZO))
        for a, b in EJES
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" role="img" aria-label="Orezco">
  <title>Orezco</title>
  <mask id="{ident}" maskUnits="userSpaceOnUse" x="0" y="0" width="200" height="200">
    <!-- solido: el cuerpo del hexagono -->
    <path d="{CAMINO_HEX}" fill="#fff"/>
    <!-- hueco: las divisiones que lo hacen leer como cubo -->
    <g stroke="#000" stroke-width="{CORTE:.0f}" stroke-linecap="round" fill="none">{div}</g>
    <!-- hueco tambien: el destello queda grabado y cruza las tres caras -->
    <g stroke="#000" stroke-width="{DESTELLO:.0f}" stroke-linecap="round" fill="none">{chispa}</g>
  </mask>
  <rect width="200" height="200" fill="{color}" mask="url(#{ident})"/>
</svg>
'''


def simbolo():
    """Fragmento para inline en HTML: la mascara en defs y un symbol que la usa.

    Va inline y no como <img> porque asi hereda currentColor del contenedor.
    """
    div = "".join(
        '<path d="M %.2f %.2f L %.2f %.2f"/>' % (C, C, *hacia(g, d))
        for g, d in DIVISIONES
    )
    chispa = "".join(
        '<path d="M %.2f %.2f L %.2f %.2f"/>' % (*hacia(a, BRAZO), *hacia(b, BRAZO))
        for a, b in EJES
    )
    return f'''<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <defs>
    <mask id="orezco-mask" maskUnits="userSpaceOnUse" x="0" y="0" width="200" height="200">
      <path d="{CAMINO_HEX}" fill="#fff"/>
      <g stroke="#000" stroke-width="{CORTE:.0f}" stroke-linecap="round" fill="none">{div}</g>
      <g stroke="#000" stroke-width="{DESTELLO:.0f}" stroke-linecap="round" fill="none">{chispa}</g>
    </mask>
  </defs>
  <symbol id="mark" viewBox="0 0 200 200">
    <rect width="200" height="200" fill="currentColor" mask="url(#orezco-mask)"/>
  </symbol>
</svg>'''


def main():
    os.makedirs(ASSETS, exist_ok=True)
    salidas = {
        # Hereda el color del contenedor. Es el que usa la web.
        "logo.svg": svg("currentColor", "orezco"),
        # Tinta fija, para cuando el consumidor no propaga currentColor.
        "logo-tinta.svg": svg("#17191c", "orezco-tinta"),
        # Blanco, para fondos oscuros.
        "logo-blanco.svg": svg("#ffffff", "orezco-blanco"),
    }
    for nombre, contenido in salidas.items():
        ruta = os.path.join(ASSETS, nombre)
        with io.open(ruta, "w", encoding="utf-8") as f:
            f.write(contenido)
        print("  %-18s %5d bytes" % (nombre, len(contenido)))

    frag = os.path.join(ASSETS, "mark-inline.svg")
    with io.open(frag, "w", encoding="utf-8") as f:
        f.write(simbolo())
    print("  %-18s %5d bytes  (fragmento para inline)" % ("mark-inline.svg", len(simbolo())))

    print()
    print("  vertices del hexagono:")
    for g, (x, y) in zip(ANGULOS, VERTICES):
        print("    %4d grados -> (%6.2f, %6.2f)" % (g, x, y))


if __name__ == "__main__":
    main()
