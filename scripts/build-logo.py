#!/usr/bin/env python3
"""
Genera el logo de Contaes.

El simbolo es una C abierta hacia la derecha y, dentro de esa abertura, tres
barras horizontales apiladas que completan una E. Juntas leen "C" + "E" -- las
iniciales -- y a la vez sugieren las lineas de un libro de cuentas.

La C va en navy. Las tres barras suben de azul a verde de abajo arriba: es el
unico degradado de la marca y solo vive en el simbolo.

    python scripts/build-logo.py

Los colores son una estimacion tomada del PNG original. Si aparecen los valores
exactos de marca, se cambian aqui y se regenera todo. No editar los SVG a mano.
"""

import io
import math
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(RAIZ, "assets")

# ── Paleta de marca ──────────────────────────────────────────────────────
NAVY = "#1E3A5F"
VERDE = "#2FBF9B"   # barra superior, y las letras "es" del wordmark
CIAN = "#1F9EC4"    # barra central
AZUL = "#1E6FB8"    # barra inferior
CANTO = "#132741"   # canto de la extrusion 3D: navy dos pasos mas oscuro

# ── Geometria, sobre lienzo 200x200 ──────────────────────────────────────
CX, CY = 84.0, 100.0    # centro de la C
RADIO = 55.0            # radio medio del anillo
GROSOR = 27.0           # grosor del trazo
ABERTURA = 44.0         # semiangulo del hueco, en grados, mirando a la derecha

BARRA_ALTO = 19.0
BARRA_X = 113.0         # borde izquierdo de las barras
BARRAS = [              # (ancho, desplazamiento vertical respecto al centro)
    (74.0, -31.0),
    (74.0, 0.0),
    (62.0, 31.0),
]


def punto(grados, r):
    a = math.radians(grados)
    return (CX + r * math.cos(a), CY - r * math.sin(a))


def arco_c():
    """La C: arranca en el borde superior del hueco y da toda la vuelta por la
    izquierda hasta el borde inferior.

    large-arc-flag = 1 porque recorre mas de media circunferencia.
    sweep-flag = 0 para ir en sentido antihorario, es decir por la izquierda.
    """
    ini = punto(ABERTURA, RADIO)
    fin = punto(-ABERTURA, RADIO)
    return "M %.2f %.2f A %.2f %.2f 0 1 0 %.2f %.2f" % (
        ini[0], ini[1], RADIO, RADIO, fin[0], fin[1])


def cuerpo(navy, barras):
    trozos = [
        '<path d="%s" fill="none" stroke="%s" stroke-width="%.0f" stroke-linecap="round"/>'
        % (arco_c(), navy, GROSOR)
    ]
    for (ancho, dy), color in zip(BARRAS, barras):
        y = CY + dy - BARRA_ALTO / 2
        trozos.append(
            '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="%s"/>'
            % (BARRA_X, y, ancho, BARRA_ALTO, BARRA_ALTO / 2, color))
    return "\n    ".join(trozos)


def svg(navy=NAVY, barras=(VERDE, CIAN, AZUL)):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" role="img" aria-label="Contaes">
  <title>Contaes</title>
  <g>
    {cuerpo(navy, barras)}
  </g>
</svg>
'''


def simbolo():
    """Fragmento para incrustar en HTML.

    Va inline y no como <img> para poder recolorearlo desde CSS: el pie va
    sobre fondo oscuro y necesita la version en blanco.
    """
    return f'''<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <symbol id="mark" viewBox="0 0 200 200">
    {cuerpo(NAVY, (VERDE, CIAN, AZUL))}
  </symbol>
  <symbol id="mark-blanco" viewBox="0 0 200 200">
    {cuerpo("#ffffff", ("#ffffff", "#ffffff", "#ffffff"))}
  </symbol>
  <symbol id="mark-canto" viewBox="0 0 200 200">
    {cuerpo(CANTO, (CANTO, CANTO, CANTO))}
  </symbol>
</svg>
'''


def main():
    os.makedirs(ASSETS, exist_ok=True)
    salidas = {
        "logo.svg": svg(),                                                    # principal, a color
        "logo-navy.svg": svg(NAVY, (NAVY, NAVY, NAVY)),                       # una sola tinta
        "logo-blanco.svg": svg("#ffffff", ("#ffffff", "#ffffff", "#ffffff")),  # fondos oscuros
    }
    for nombre, contenido in salidas.items():
        with io.open(os.path.join(ASSETS, nombre), "w", encoding="utf-8") as f:
            f.write(contenido)
        print("  %-18s %5d bytes" % (nombre, len(contenido)))

    frag = simbolo()
    with io.open(os.path.join(ASSETS, "mark-inline.svg"), "w", encoding="utf-8") as f:
        f.write(frag)
    print("  %-18s %5d bytes  (fragmento para inline)" % ("mark-inline.svg", len(frag)))

    print()
    print("  paleta:  navy %s | verde %s | cian %s | azul %s" % (NAVY, VERDE, CIAN, AZUL))


if __name__ == "__main__":
    main()
