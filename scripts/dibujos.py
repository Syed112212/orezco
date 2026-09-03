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

/* ── El flujo: quien hace cada paso ──────────────────────────────────
   Era un SVG con cuatro cajas grises identicas y un punto azul flotando
   encima de la tercera. Dos problemas: no se veia quien hace que, que es
   lo unico que este dibujo tiene que contar, y en el movil el texto
   acababa en seis pixeles porque el SVG se escalaba entero. */
.flujo-caja{position:relative}
.flujo{list-style:none;margin:0;padding:0;display:grid;gap:14px}
.flujo-3{grid-template-columns:repeat(3,minmax(0,1fr))}
.flujo-4{grid-template-columns:repeat(4,minmax(0,1fr))}

/* El carril con el punto que lo recorre. Pasa por debajo de los nodos,
   asi que el punto va por la linea y no por encima de una caja. */
.fl-carril{position:absolute;left:6px;top:7px;height:2px;
  background:var(--borde);border-radius:2px}
.flujo-caja:has(.flujo-4) .fl-carril{right:calc((100% - 42px) / 4 - 6px)}
.flujo-caja:has(.flujo-3) .fl-carril{right:calc((100% - 28px) / 3 - 6px)}
.fl-carril i{position:absolute;top:-4px;left:-5px;width:10px;height:10px;
  border-radius:50%;background:var(--azul);
  animation:fl-viaja 6s cubic-bezier(.55,0,.45,1) infinite}
@keyframes fl-viaja{
  0%,4%{left:-5px;opacity:0}
  8%{opacity:1}
  26%,32%{left:calc(33.333% - 5px)}
  52%,58%{left:calc(66.666% - 5px)}
  78%,92%{left:calc(100% - 5px);opacity:1}
  98%,100%{left:calc(100% - 5px);opacity:0}
}
.flujo-3 .fl-carril i{animation-name:fl-viaja-3}
@keyframes fl-viaja-3{
  0%,4%{left:-5px;opacity:0}
  8%{opacity:1}
  34%,42%{left:calc(50% - 5px)}
  70%,92%{left:calc(100% - 5px);opacity:1}
  98%,100%{left:calc(100% - 5px);opacity:0}
}

.fl-paso{position:relative;padding-top:26px;display:flex;flex-direction:column}
.fl-nodo{position:absolute;top:2px;left:0;width:12px;height:12px;
  border-radius:50%;background:var(--blanco);
  border:2px solid var(--borde)}
.fl-paso:nth-child(1) .fl-nodo{border-color:var(--azul)}
.fl-paso:nth-child(2) .fl-nodo{border-color:var(--marigold)}
.fl-paso:nth-child(3) .fl-nodo{border-color:var(--medianoche)}
.fl-paso.es-final .fl-nodo{background:var(--medianoche);
  border-color:var(--medianoche)}
.fl-actor{margin:0 0 6px;font:600 11px/1.2 var(--sans);letter-spacing:.07em;
  text-transform:uppercase;color:var(--piedra)}
.fl-paso:nth-child(1) .fl-actor{color:var(--azul)}
.fl-paso:nth-child(2) .fl-actor{color:#a06c00}
.fl-paso:nth-child(3) .fl-actor{color:var(--medianoche)}
.fl-paso:nth-child(4) .fl-actor{color:var(--medianoche)}

.fl-tarjeta{flex:1;background:var(--papel);border:1px solid var(--borde);
  border-radius:12px;padding:14px 16px 16px}
.fl-paso.es-final .fl-tarjeta{background:var(--medianoche);
  border-color:var(--medianoche)}
.fl-tit{margin:0;font:600 15px/1.3 var(--sans);color:var(--tinta-fuerte)}
.fl-sub{margin:5px 0 0;font:400 13px/1.45 var(--sans);color:var(--piedra)}
.fl-paso.es-final .fl-tit{color:var(--blanco)}
.fl-paso.es-final .fl-sub{color:rgba(255,255,255,.72)}

@media(max-width:760px){
  .flujo,.flujo-3,.flujo-4{grid-template-columns:1fr;gap:10px}
  .fl-carril{left:5px;right:auto;top:8px;bottom:8px;width:2px;height:auto}
  .fl-carril i{animation:none;top:0;left:-4px}
  .flujo-caja:has(.flujo-4) .fl-carril,
  .flujo-caja:has(.flujo-3) .fl-carril{right:auto}
  .fl-paso{padding:0 0 0 26px}
  .fl-nodo{top:16px;left:0}
}
@media(prefers-reduced-motion:reduce){
  .fl-carril i{animation:none;left:calc(100% - 5px)}
}

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
def flujo(pasos, pie, actores=None):
    """pasos: [(titulo, linea corta)] de 3 o 4. actores: quien hace cada uno.

    Va en HTML y no en SVG a proposito. Estaba en SVG con las cajas
    puestas a mano en pixeles, y en el movil se escalaba entero: el texto
    acababa en seis pixeles. En HTML se apila solo.

    Cuando se pasan los actores, cada paso dice encima quien lo hace. En
    el flujo del modelo 303 eso es justo lo que hay que ver, porque lo
    que separa esto de un programa suelto es que en medio hay una persona
    colegiada que firma. Cuatro cajas iguales no lo cuentan.
    """
    n = len(pasos)
    actores = list(actores or [])
    piezas = []
    for i, (titulo, sub) in enumerate(pasos):
        quien = actores[i] if i < len(actores) else ""
        ultimo = " es-final" if i == n - 1 else ""
        piezas.append(
            '    <li class="fl-paso%s">\n'
            '      <span class="fl-nodo" aria-hidden="true"></span>\n'
            '%s'
            '      <div class="fl-tarjeta">\n'
            '        <p class="fl-tit">%s</p>\n'
            '        <p class="fl-sub">%s</p>\n'
            '      </div>\n'
            '    </li>'
            % (ultimo,
               ('      <p class="fl-actor">%s</p>\n' % quien) if quien else "",
               titulo, sub))

    # El carril va fuera de la lista. Un <span> suelto dentro de un <ol>
    # no es HTML valido, y ademas obligaba a contar los pasos desde el
    # segundo, que es como se descuadraron los colores.
    return ('<figure class="dibujo">\n'
            '  <div class="flujo-caja">\n'
            '    <span class="fl-carril" aria-hidden="true"><i></i></span>\n'
            '    <ol class="flujo flujo-%d">\n%s\n    </ol>\n'
            '  </div>\n'
            '  <figcaption>%s</figcaption>\n</figure>'
            % (n, "\n".join(piezas), pie))


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
