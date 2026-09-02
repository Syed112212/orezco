# -*- coding: utf-8 -*-
"""Diagramas animados que explican cada servicio sin leer.

Una pagina que solo tiene titulo, parrafo y lista obliga a leerlo todo
para entender que hace la cosa. Un dibujo que se mueve lo cuenta antes.

Reglas de estos dibujos:
  - Explican algo. No son adorno: cada uno muestra un flujo, una relacion
    o un antes y un despues que el texto tambien cuenta.
  - Usan el sistema visual del sitio y nada mas: lienzo calido, blanco,
    filete de 1px, el azul de accion y los tres acentos con cuentagotas.
  - Se paran con prefers-reduced-motion, y sin animacion siguen
    entendiendose: la animacion subraya, no informa.
  - Llevan su descripcion en texto para quien no los ve.

Son SVG en linea y no imagenes porque tienen que heredar los colores del
tema y escalar sin pesar nada.
"""

# ─────────────────────────────────────────────────────────────────────
# El CSS comun. Se inyecta una sola vez por pagina.
# ─────────────────────────────────────────────────────────────────────
ESTILOS = '''
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
.dibujo .et-p{font:400 11px/1 var(--sans);fill:var(--piedra)}
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
'''


def _marco(svg, pie, alto=200, ancho=860):
    return ('<figure class="dibujo revela">\n'
            '  <svg viewBox="0 0 %d %d" role="img" aria-label="%s">\n%s\n  </svg>\n'
            '  <figcaption>%s</figcaption>\n</figure>'
            % (ancho, alto, pie.replace('"', "'"), svg, pie))


# ─────────────────────────────────────────────────────────────────────
# 1. Un flujo de tres o cuatro pasos
# ─────────────────────────────────────────────────────────────────────
def flujo(pasos, pie):
    """pasos: [(titulo, linea corta)] de 3 o 4."""
    n = len(pasos)
    ancho_caja = 178 if n == 4 else 220
    hueco = (860 - 40 - ancho_caja * n) / (n - 1)
    piezas, centros = [], []
    for i, (titulo, sub) in enumerate(pasos):
        x = 20 + i * (ancho_caja + hueco)
        centros.append(x + ancho_caja / 2)
        piezas.append(
            '    <g class="paso-%d">\n'
            '      <rect class="caja" x="%.0f" y="52" width="%d" height="72" rx="10"/>\n'
            '      <rect class="caja-viva enciende" x="%.0f" y="52" width="%d" height="72" rx="10"/>\n'
            '      <text class="et" x="%.0f" y="84">%s</text>\n'
            '      <text class="et-p" x="%.0f" y="102">%s</text>\n'
            '    </g>' % (i + 1, x, ancho_caja, x, ancho_caja,
                          x + 16, titulo, x + 16, sub))
        if i < n - 1:
            x2 = x + ancho_caja
            piezas.append(
                '    <path class="linea" d="M%.0f 88 H%.0f" marker-end="url(#punta)"/>'
                % (x2 + 6, x2 + hueco - 8))

    saltos = "".join("--p%d:%.0fpx;" % (j, centros[j] - centros[0]) for j in range(1, n))
    piezas.append(
        '    <g class="viaja" style="%s">\n'
        '      <circle cx="%.0f" cy="30" r="7" fill="var(--azul)"/>\n'
        '    </g>' % (saltos, centros[0]))
    defs = ('    <defs><marker id="punta" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="6" '
            'markerHeight="6" orient="auto"><path d="M0 1 L7 4 L0 7" fill="none" '
            'stroke="var(--borde)" stroke-width="1.5"/></marker></defs>')
    return _marco(defs + "\n" + "\n".join(piezas), pie, alto=150)


# ─────────────────────────────────────────────────────────────────────
# 2. Papeles que caen y se convierten en apuntes
# ─────────────────────────────────────────────────────────────────────
def entrada_documentos(pie, etiquetas=("Factura", "Ticket", "Extracto"), destino="Apunte contable"):
    filas = []
    for i, e in enumerate(etiquetas):
        y = 30 + i * 52
        filas.append(
            '    <g class="cae%s">\n'
            '      <rect class="caja" x="24" y="%d" width="176" height="40" rx="8"/>\n'
            '      <rect x="40" y="%d" width="46" height="5" rx="2.5" fill="var(--azul)" opacity=".6"/>\n'
            '      <rect x="40" y="%d" width="120" height="4" rx="2" fill="rgba(0,0,0,.13)"/>\n'
            '      <text class="et-p" x="%d" y="%d">%s</text>\n'
            '    </g>' % ((" cae-%d" % (i + 2)) if i else "", y, y + 12, y + 24,
                          210, y + 25, e))
        filas.append('    <path class="linea traza" style="--largo:180" d="M206 %d C320 %d 400 %d 480 %d"/>'
                     % (y + 20, y + 20, 108, 108))

    filas.append(
        '    <g class="sella">\n'
        '      <rect class="caja-viva" x="490" y="62" width="346" height="92" rx="10"/>\n'
        '      <text class="et" x="512" y="92">%s</text>\n'
        '      <rect x="512" y="106" width="150" height="5" rx="2.5" fill="var(--azul)"/>\n'
        '      <rect x="512" y="120" width="220" height="4" rx="2" fill="rgba(0,0,0,.13)"/>\n'
        '      <rect x="512" y="132" width="180" height="4" rx="2" fill="rgba(0,0,0,.10)"/>\n'
        '    </g>' % destino)
    return _marco("\n".join(filas), pie, alto=200)


# ─────────────────────────────────────────────────────────────────────
# 3. Dos columnas que se emparejan
# ─────────────────────────────────────────────────────────────────────
def emparejar(izq, der, pie, titulo_izq="Banco", titulo_der="Tus apuntes"):
    filas = ['    <text class="et-p" x="24" y="24">%s</text>' % titulo_izq,
             '    <text class="et-p" x="520" y="24">%s</text>' % titulo_der]
    for i in range(max(len(izq), len(der))):
        y = 40 + i * 48
        if i < len(izq):
            filas.append('    <rect class="caja" x="24" y="%d" width="290" height="36" rx="8"/>' % y)
            filas.append('    <text class="et" x="42" y="%d">%s</text>' % (y + 23, izq[i]))
        if i < len(der):
            filas.append('    <rect class="caja" x="520" y="%d" width="316" height="36" rx="8"/>' % y)
            filas.append('    <text class="et" x="538" y="%d">%s</text>' % (y + 23, der[i]))
        if i < min(len(izq), len(der)):
            filas.append(
                '    <g class="casa%s">\n'
                '      <path class="linea" style="stroke:var(--azul);stroke-width:1.5" '
                'd="M320 %d H514"/>\n'
                '      <circle cx="417" cy="%d" r="10" fill="var(--azul-tinte)" '
                'stroke="var(--azul)" stroke-width="1.2"/>\n'
                '      <path d="M412 %d l4 4 6.5 -7" fill="none" stroke="var(--azul)" '
                'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>\n'
                '    </g>' % ((" casa-%d" % (i + 1)) if i else "", y + 18, y + 18, y + 17))
    return _marco("\n".join(filas), pie, alto=40 + max(len(izq), len(der)) * 48 + 12)


# ─────────────────────────────────────────────────────────────────────
# 4. Barras que crecen: un cuadro de mando
# ─────────────────────────────────────────────────────────────────────
def barras(valores, etiquetas, pie, resalta=None):
    filas = ['    <path class="linea" d="M24 156 H836"/>']
    ancho = 60
    hueco = (812 - ancho * len(valores)) / (len(valores) - 1)
    for i, v in enumerate(valores):
        x = 24 + i * (ancho + hueco)
        alto = int(112 * v)
        color = "var(--azul)" if (resalta is None or i in resalta) else "rgba(0,117,222,.28)"
        filas.append(
            '    <rect class="crece%s" x="%.0f" y="%d" width="%d" height="%d" rx="5" fill="%s"/>'
            % ((" crece-%d" % (i + 1)) if i else "", x, 156 - alto, ancho, alto, color))
        filas.append('    <text class="et-p" x="%.0f" y="174" text-anchor="middle">%s</text>'
                     % (x + ancho / 2, etiquetas[i]))
    return _marco("\n".join(filas), pie, alto=186)


# ─────────────────────────────────────────────────────────────────────
# 5. Antes y despues
# ─────────────────────────────────────────────────────────────────────
def comparacion(antes, despues, pie, tit_antes="Como suele ir", tit_despues="Como va aquí"):
    def columna(x, titulo, puntos, vivo):
        piezas = ['    <text class="et-p" x="%d" y="22">%s</text>' % (x + 18, titulo)]
        clase = "caja-viva" if vivo else "caja"
        piezas.append('    <rect class="%s" x="%d" y="32" width="394" height="%d" rx="10"/>'
                      % (clase, x, 22 + len(puntos) * 34))
        for i, p in enumerate(puntos):
            y = 62 + i * 34
            marca = ("var(--azul)" if vivo else "rgba(0,0,0,.22)")
            piezas.append('    <circle cx="%d" cy="%d" r="4" fill="%s"/>' % (x + 22, y - 5, marca))
            piezas.append('    <text class="et" x="%d" y="%d">%s</text>' % (x + 36, y, p))
        return "\n".join(piezas)

    alto = 32 + 22 + max(len(antes), len(despues)) * 34 + 16
    return _marco(columna(24, tit_antes, antes, False) + "\n" +
                  columna(442, tit_despues, despues, True), pie, alto=alto)
