#!/usr/bin/env python3
"""
Verificador del sistema visual de Orezco.

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
# 2. El melocoton es una tarjeta por pagina
# ─────────────────────────────────────────────────────────────────────────
def regla_melocoton_unico(nombre, html):
    usos = len(re.findall(r'class="[^"]*\bacento-card\b', html))
    if usos > 1:
        fallo("melocoton-unico",
              "%s: hay %d tarjetas melocoton. DESIGN.md permite una por pagina." % (nombre, usos))


# ─────────────────────────────────────────────────────────────────────────
# 3. La serifa se queda en peso 400 a todos los tamanos
# ─────────────────────────────────────────────────────────────────────────
def regla_serifa_400(nombre, css):
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
PERMITIDOS_SOMBRA = {".artefacto", ".plano", ".modulos-marco"}


def regla_sombra_solo_flotantes(nombre, css):
    for sel, bloque in re.findall(r"([^{}]+)\{([^{}]*)\}", css):
        if "box-shadow" not in bloque:
            continue
        if re.search(r"box-shadow:\s*none", bloque):
            continue
        selectores = {s.strip().split(":")[0].split(" ")[-1] for s in sel.split(",")}
        if not (selectores & PERMITIDOS_SOMBRA):
            aviso("sombra-solo-flotantes",
                  "%s: '%s' lleva box-shadow y no es un artefacto flotante."
                  % (nombre, sel.strip()[:40]))


# ─────────────────────────────────────────────────────────────────────────
# 5. Cuatro radios, y ni uno mas
# ─────────────────────────────────────────────────────────────────────────
RADIOS_OK = {"24px", "20px", "16px", "9999px", "2px", "0", "4px", "50%"}


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
    huerfanas = usadas - declaradas - con_defecto
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
    ("texto principal sobre papel",   "#17191c", "#ffffff", 4.5),
    ("apoyo sobre papel",             "#6b6e78", "#ffffff", 4.5),
    ("apoyo sobre banda",             "#6b6e78", "#fafafb", 4.5),
    ("apoyo sobre tarjeta neutra",    "#6b6e78", "#f2f2f3", 4.5),
    ("etiqueta sobre papel",          "#6c6e74", "#ffffff", 4.5),
    ("etiqueta sobre banda",          "#6c6e74", "#fafafb", 4.5),
    ("etiqueta sobre tarjeta neutra", "#6c6e74", "#f2f2f3", 4.5),
    ("marcador de campo sobre campo blanco", "#71747c", "#ffffff", 4.5),
    ("sienna sobre melocoton",        "#5d2a1a", "#fbe1d1", 4.5),
    ("papel sobre boton relleno",     "#ffffff", "#17191c", 4.5),
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
def main():
    index = leer("index.html")
    css_index = css_de(index)

    for nombre in PAGINAS:
        html = leer(nombre)
        css = css_de(html)
        regla_3d_sin_filtros(nombre, css)
        regla_melocoton_unico(nombre, html)
        regla_serifa_400(nombre, css)
        regla_sombra_solo_flotantes(nombre, css)
        regla_radios(nombre, css)
        regla_variables(nombre, css)

    regla_contraste()
    regla_tokens(css_index)

    print("Verificacion del sistema visual de Orezco")
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
