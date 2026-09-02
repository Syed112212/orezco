#!/usr/bin/env python3
"""
Verificador del sistema visual de Contaes.

Convierte las reglas duras de DESIGN.md en comprobaciones ejecutables. Cada
regla que aqui se comprueba esta escrita en DESIGN.md; si cambia una, cambian
las dos.

    python scripts/check-design.py

Sale con codigo 1 si alguna regla se incumple, para poder engancharlo a CI.
"""

import io
import os
import re
import sys

# La consola de Windows usa cp1252 por defecto y revienta con acentos.
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Se verifican tambien las plantillas que producen artefactos de produccion:
# og-template.html genera assets/og.png, y ya se aplano una vez por un filter
# sobre preserve-3d que nadie estaba mirando.
PAGINAS = ["index.html", "404.html", "scripts/og-template.html"]

fallos = []
avisos = []


def fallo(regla, detalle):
    fallos.append((regla, detalle))


def aviso(regla, detalle):
    avisos.append((regla, detalle))


def leer(nombre):
    with io.open(os.path.join(RAIZ, nombre), encoding="utf-8") as f:
        return f.read()


def css_de(html):
    m = re.search(r"<style>(.*?)</style>", html, re.S)
    css = m.group(1) if m else ""
    # Fuera comentarios: si no, un comentario delante de una regla se cuela
    # como parte del selector y produce falsos positivos.
    return re.sub(r"/\*.*?\*/", "", css, flags=re.S)


# ─────────────────────────────────────────────────────────────────────────
# 1. filter/opacity sobre preserve-3d aplana la escena
#    Es el bug que convirtio el cubo en un rombo. Nunca mas.
# ─────────────────────────────────────────────────────────────────────────
def regla_3d_sin_filtros(nombre, css):
    for bloque in re.findall(r"\{[^{}]*\}", css):
        if "preserve-3d" not in bloque:
            continue
        for prop in ("filter:", "backdrop-filter:", "mask:", "mix-blend-mode:"):
            if prop in bloque:
                fallo("3d-sin-filtros",
                      "%s: un bloque con preserve-3d declara '%s'. "
                      "Eso fuerza transform-style:flat en los hijos y aplana el objeto."
                      % (nombre, prop.rstrip(":")))
        m = re.search(r"opacity:\s*([\d.]+)", bloque)
        if m and float(m.group(1)) < 1:
            fallo("3d-sin-filtros",
                  "%s: un bloque con preserve-3d declara opacity:%s (<1), que tambien aplana."
                  % (nombre, m.group(1)))


# ─────────────────────────────────────────────────────────────────────────
# 2. Un unico boton cromatico: el azul de accion
#    Todo lo demas es fantasma, tinte o texto. El color vive en los paneles,
#    nunca en un segundo boton relleno.
# ─────────────────────────────────────────────────────────────────────────
AZULES_OK = {"#0075de", "#0064c0", "#e6f3fe", "#d5eafd", "#fff", "#ffffff", "transparent"}


def regla_un_solo_azul(nombre, css):
    for sel, bloque in re.findall(r"([^{}]+)\{([^{}]*)\}", css):
        if ".btn" not in sel:
            continue
        m = re.search(r"background:\s*([^;}]+)", bloque)
        if not m:
            continue
        v = m.group(1).strip().lower()
        if v.startswith("var(") or v.startswith("rgba"):
            continue
        if v not in AZULES_OK:
            fallo("un-solo-azul",
                  "%s: '%s' rellena un boton con '%s'. El unico relleno cromatico es el azul de accion."
                  % (nombre, sel.strip()[:40], v))


# ─────────────────────────────────────────────────────────────────────────
# 3. La serifa se queda en peso 400 a todos los tamanos
# ─────────────────────────────────────────────────────────────────────────
def regla_serifa_400_sin_uso(nombre, css):
    for sel, bloque in re.findall(r"([^{}]+)\{([^{}]*)\}", css):
        usa_serif = "var(--serif)" in bloque or "--font-signifier" in bloque or "Source Serif" in bloque
        if not usa_serif:
            continue
        for peso in re.findall(r"font-weight:\s*(\d+)", bloque):
            if peso != "400":
                fallo("serifa-400",
                      "%s: '%s' usa la serifa con font-weight:%s. Debe ser 400 siempre."
                      % (nombre, sel.strip()[:40], peso))


# ─────────────────────────────────────────────────────────────────────────
# 4. Solo los artefactos flotantes llevan sombra
# ─────────────────────────────────────────────────────────────────────────
# El anillo de foco de un campo es accesibilidad, no decoracion.
# El menu desplegable flota sobre el contenido, como la barra: la sombra
# es lo que lo separa de lo que tapa.
PERMITIDOS_SOMBRA = {".nav", ".nav-links", ".despliegue", ".maqueta", ".plano", ".btn-azul",
                     "input", "textarea", "input:focus", "textarea:focus"}


def regla_sombra_solo_flotantes(nombre, css):
    for sel, bloque in re.findall(r"([^{}]+)\{([^{}]*)\}", css):
        if "box-shadow" not in bloque:
            continue
        if re.search(r"box-shadow:\s*none", bloque):
            continue
        # una sombra 'inset' no eleva nada: es una forma de dibujar dentro
        # del propio elemento, como el punto de un boton de opcion
        if re.search(r"box-shadow:\s*inset", bloque):
            continue
        selectores = {s.strip().split(":")[0].split(" ")[-1] for s in sel.split(",")}
        if not (selectores & PERMITIDOS_SOMBRA):
            aviso("sombra-solo-flotantes",
                  "%s: '%s' lleva box-shadow y no es un artefacto flotante."
                  % (nombre, sel.strip()[:40]))


# ─────────────────────────────────────────────────────────────────────────
# 5. Cuatro radios, y ni uno mas
# ─────────────────────────────────────────────────────────────────────────
RADIOS_OK = {"12px", "8px", "4px", "9999px", "0", "50%", "2px"}


def regla_radios(nombre, css):
    for valor in re.findall(r"border-radius:\s*([^;\}]+)", css):
        v = valor.strip()
        if "var(" in v or "calc(" in v:
            continue
        for parte in v.split():
            if parte not in RADIOS_OK:
                aviso("radios",
                      "%s: border-radius '%s' fuera del sistema (24/20/16/9999/2)." % (nombre, parte))


# ─────────────────────────────────────────────────────────────────────────
# 6. Ninguna variable CSS usada sin declarar
# ─────────────────────────────────────────────────────────────────────────
def regla_variables(nombre, css):
    declaradas = set(re.findall(r"(--[a-z0-9-]+)\s*:", css))
    usadas = set(re.findall(r"var\((--[a-z0-9-]+)", css))
    con_defecto = set(re.findall(r"var\((--[a-z0-9-]+)\s*,", css))
    # --i la fija el JS al generar las capas del logo 3D; --mark-bg y --l
    # son parametros de los simbolos. Ninguna es un olvido.
    huerfanas = usadas - declaradas - con_defecto - {"--i", "--mark-bg", "--l", "--lado"}
    for v in sorted(huerfanas):
        fallo("variables", "%s: se usa var(%s) pero no esta declarada." % (nombre, v))


# ─────────────────────────────────────────────────────────────────────────
# 7. Contraste de texto (WCAG AA: 4.5 para texto normal, 3.0 para grande)
# ─────────────────────────────────────────────────────────────────────────
def luminancia(hexcol):
    h = hexcol.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) / 255.0 for i in (0, 2, 4))
    def canal(c):
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = canal(r), canal(g), canal(b)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contraste(a, b):
    la, lb = luminancia(a), luminancia(b)
    claro, oscuro = max(la, lb), min(la, lb)
    return (claro + 0.05) / (oscuro + 0.05)


PARES = [
    ("texto principal sobre lienzo",  "#0d0d0d", "#f6f5f4", 4.5),
    ("cuerpo sobre lienzo",           "#615d59", "#f6f5f4", 4.5),
    ("cuerpo sobre tarjeta",          "#615d59", "#ffffff", 4.5),
    ("piedra sobre lienzo",           "#6a6a6a", "#f6f5f4", 4.5),
    ("blanco sobre azul de accion",   "#ffffff", "#0075de", 4.5),
    ("azul sobre tinte",              "#005fb8", "#e6f3fe", 4.5),
    ("negro sobre marigold",          "#000000", "#ffb110", 4.5),
    ("blanco sobre medianoche",       "#ffffff", "#02093a", 4.5),
    ("negro sobre coral",             "#000000", "#f64932", 4.5),
]


def regla_contraste():
    for etiqueta, fg, bg, minimo in PARES:
        r = contraste(fg, bg)
        if r < minimo:
            fallo("contraste",
                  "%s: %.2f:1, por debajo del minimo %.1f (%s sobre %s)."
                  % (etiqueta, r, minimo, fg, bg))
        elif r < minimo + 0.6:
            aviso("contraste", "%s: %.2f:1, justo por encima del minimo %.1f." % (etiqueta, r, minimo))


# ─────────────────────────────────────────────────────────────────────────
# 8. Coherencia entre tokens.json y el :root
# ─────────────────────────────────────────────────────────────────────────
def regla_tokens(css):
    import json
    ruta = os.path.join(RAIZ, "tokens.json")
    if not os.path.isfile(ruta):
        aviso("tokens", "no hay tokens.json.")
        return
    with io.open(ruta, encoding="utf-8") as f:
        t = json.load(f)
    for nombre, dato in t.get("color", {}).items():
        valor = dato["$value"].lower()
        var = "--color-%s" % nombre
        m = re.search(re.escape(var) + r"\s*:\s*([^;]+);", css)
        if not m:
            fallo("tokens", "%s esta en tokens.json pero no en el :root." % var)
        elif m.group(1).strip().lower() != valor:
            fallo("tokens", "%s vale '%s' en el CSS y '%s' en tokens.json."
                  % (var, m.group(1).strip(), valor))


# ─────────────────────────────────────────────────────────────────────────
def regla_herencia_en_tarjetas(nombre, css):
    """Un panel de fondo oscuro aclara su texto. Si dentro hay tarjetas de
    fondo claro, ese color se hereda y queda gris claro sobre blanco: no se
    lee. Cada hoja que aclare texto de panel tiene que devolverlo en la
    tarjeta."""
    aclara = re.findall(
        r"\.panel\.([a-z-]+)\s+\.cuerpo\s*\{[^}]*color\s*:\s*"
        r"(?:#[0-9a-fA-F]{3,6}|rgba?\([^)]*\))", css)
    if not aclara:
        return
    if not re.search(r"\.panel\s+\.tarjeta[^{]*\{[^}]*color\s*:", css):
        fallo("herencia-en-tarjetas",
              "%s: los paneles '%s' cambian el color del texto y ninguna regla lo "
              "devuelve dentro de .tarjeta; quedaria ilegible sobre el fondo claro"
              % (nombre, "', '".join(sorted(set(aclara)))))


def regla_barra_intacta(nombre, css):
    """La barra se queda arriba y por encima de todo. Cualquier regla
    posterior que vuelva a declarar su 'position' o su 'z-index' se lo
    quita en silencio: el fallo solo se ve al desplazar la pagina, nunca
    leyendo el codigo."""
    tocan = []
    for sel, bloque in re.findall(r"([^{}]+)\{([^{}]*)\}", css):
        partes = [s.strip() for s in sel.split(",")]
        if not any(s == ".nav" for s in partes):
            continue
        if re.search(r"(^|;)\s*(position|z-index)\s*:", bloque):
            tocan.append(sel.strip()[:46])
    if len(tocan) > 1:
        fallo("barra-intacta",
              "%s: '%s' vuelve a declarar position/z-index de .nav; se pierde el "
              "sticky y la barra queda por debajo del contenido"
              % (nombre, tocan[-1]))


# Clases del menu. Si alguna se declara dos veces en la misma hoja, la
# segunda gana y el menu se rompe sin que nada falle: paso con .panel, que
# era a la vez el desplegable y el panel de acento de la portada.
CLASES_UNICAS = [".nav-in", ".nav-links", ".despliegue", ".menu-btn", ".area"]


def sin_medias(css):
    """El CSS sin los bloques @media. Redeclarar una clase dentro de una
    consulta es lo normal -es como se adapta a la pantalla-; declararla
    dos veces fuera es el fallo que buscamos."""
    fuera, i = [], 0
    while i < len(css):
        j = css.find("@media", i)
        if j < 0:
            fuera.append(css[i:])
            break
        fuera.append(css[i:j])
        k = css.find("{", j)
        if k < 0:
            break
        hondo, k = 1, k + 1
        while k < len(css) and hondo:
            if css[k] == "{":
                hondo += 1
            elif css[k] == "}":
                hondo -= 1
            k += 1
        i = k
    return "".join(fuera)


def regla_clases_del_menu(nombre, css):
    """Una clase del menu declarada dos veces con 'position' o 'display' es
    un fallo mudo: la segunda gana y el menu se descoloca sin que nada
    proteste. Paso con .panel, que era a la vez el desplegable del menu y
    el panel de acento de la portada.

    No cuenta lo que va dentro de un @media -adaptar a la pantalla es su
    trabajo-, ni las reglas que solo tocan la clase de pasada, como una
    transicion compartida entre varios selectores."""
    for clase in CLASES_UNICAS:
        veces = 0
        for sel, bloque in re.findall(r"([^{}]+)\{([^{}]*)\}", sin_medias(css)):
            if clase not in [s.strip() for s in sel.split(",")]:
                continue
            if re.search(r"(^|;)\s*(position|display)\s*:", bloque):
                veces += 1
        if veces > 1:
            fallo("clases-del-menu",
                  "%s: '%s' fija position o display %d veces fuera de cualquier @media; "
                  "la segunda gana y descoloca el menu sin dar ningun error"
                  % (nombre, clase, veces))

def main():
    index = leer("index.html")
    css_index = css_de(index)

    for nombre in PAGINAS:
        html = leer(nombre)
        css = css_de(html)
        regla_3d_sin_filtros(nombre, css)
        regla_un_solo_azul(nombre, css)
        regla_sombra_solo_flotantes(nombre, css)
        regla_radios(nombre, css)
        regla_variables(nombre, css)
        regla_herencia_en_tarjetas(nombre, css)
        regla_barra_intacta(nombre, css)
        regla_clases_del_menu(nombre, css)

    regla_contraste()

    print("Verificacion del sistema visual de Contaes")
    print("=" * 46)
    if not fallos and not avisos:
        print("Todo correcto.")
    for regla, detalle in fallos:
        print("FALLO  [%s] %s" % (regla, detalle))
    for regla, detalle in avisos:
        print("aviso  [%s] %s" % (regla, detalle))
    print("=" * 46)
    print("%d fallo(s), %d aviso(s)" % (len(fallos), len(avisos)))
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
