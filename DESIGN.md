# Orezco — sistema visual

SSOT visual del proyecto. Cualquier cambio de color, tipografía, espaciado o componente
se decide aquí primero y se sincroniza en el mismo commit que el código.

**Dirección**: *instrumento de precisión, medianoche*. Lienzo casi negro, tipografía blanca
con tracking apretado, bordes hairline en lugar de sombras, y **un único acento cromático**
—lima ácido— que funciona como linterna: pequeño, de alto contraste y reservado a la acción.
Adaptado del sistema de Linear, que es la referencia que eligió el cliente.

Mundo visual único y deliberado (oscuro). No hay tema claro alternativo: todos los colores
se pintan explícitamente.

## Color

### Superficies

| Token | Hex | Uso |
|---|---|---|
| `--void` | `#08090a` | Lienzo. El fondo por defecto de todo |
| `--carbon` | `#0f1011` | Tarjetas y barras. Un escalón por encima del lienzo |
| `--obsidian` | `#161718` | Paneles elevados, caras del cubo |
| `--slate` | `#23252a` | Relleno interactivo, borde de tarjeta |

### Bordes

| Token | Hex | Uso |
|---|---|---|
| `--graphite` | `#23252a` | Hairline base: divisores, contorno de tarjeta |
| `--smoke` | `#383b3f` | Hairline de más contraste: separadores, aristas del cubo |

**La elevación se consigue con bordes, no con sombras.** La jerarquía sale de la progresión
de superficies `#08090a → #0f1011 → #161718 → #23252a` y del contorno. La única sombra real
del sistema es la del botón lima.

### Texto

| Token | Hex | Uso |
|---|---|---|
| `--paper` | `#ffffff` | Titulares, máximo contraste |
| `--mist` | `#d0d6e0` | Cuerpo, texto de botón |
| `--fog` | `#8a8f98` | Terciario, descripciones, marcador de campo |
| `--ash` | `#62666d` | Apagado, metadatos |

Nada de texto cromático en el cuerpo: todo vive en la escala de grises.

### Acentos

| Token | Hex | Uso |
|---|---|---|
| `--lima` | `#e4f222` | **Única acción cromática.** Una por pantalla. Nunca decorativa |
| `--pulso` | `#27a644` | Apoyo: etiquetas de la lista de migración. **Nunca como acción** |

**Regla dura**: el lima es el botón principal y nada más. Si aparece dos veces en la misma
pantalla, sobra una.

## Tipografía

| Rol | Familia | Ajustes |
|---|---|---|
| Interfaz y titulares | **Inter** | pesos 300 / 400 / 510 / 590. Nunca 700+ |
| Metadatos técnicos | **JetBrains Mono** | 400, `letter-spacing: -.013em` |

- `font-feature-settings: "cv01" on, "ss03" on, "zero" on` en `body`. Estas alternativas de
  glifo son parte de la identidad — sin ellas la tipografía pierde carácter.
- **Tracking apretado, no negociable**: `-.022em` de 48px para arriba, `-.011em` a 15–16px.
- El mono es solo para números de módulo, códigos y metadatos. **Nunca para titulares ni copy.**

### Escala

| Rol | Tamaño | Peso | Interlineado |
|---|---|---|---|
| Display (portada) | 72px | 510 | 1.0 |
| Sección | 48px | 510 | 1.0 |
| Subtítulo de tarjeta | 17px | 510 | 1.4 |
| Cuerpo | 16px | 400 | 1.5 |
| Pequeño | 13–15px | 400 | 1.5 |
| Etiqueta | 12px | 400 | 1.4 |

## Ritmo y forma

| | |
|---|---|
| Ancho máximo | `1200px` |
| Separación entre secciones | `96px` |
| Relleno de tarjeta | `24px` |
| Separación entre elementos | `8px` |
| Base de espaciado | `4px` |

**Tres radios y nada más**: tarjetas `12px`, botones e inputs `6px`, píldoras `9999px`.
Etiquetas `4px`. Nunca por encima de 12px en tarjetas.

## Los objetos 3D

No hay capturas de producto todavía, así que **el 3D ocupa ese lugar**: es el artefacto
visual de la página, no un adorno. Todo es CSS `transform-style: preserve-3d`, sin librerías.

### Cubo-logo (portada y 404)

El símbolo de la marca ya es un cubo isométrico, así que en 3D se convierte en un cubo real
con el destello de seis puntas en cada cara. Gira 360° en 24 s.

- Caras **opacas** (`#161718`, `#0d0e10` en los lados, `#212326` arriba) más
  `backface-visibility: hidden`. Con caras translúcidas se transparentan los destellos
  traseros y el cubo se ensucia.
- Aristas en `--smoke`: el volumen se define con hairlines, igual que el resto del sistema.

### Cubo de ocho piezas (módulos)

Ocho módulos, ocho vértices de un cubo. Al pasar por una fila de módulo se ilumina su pieza
en lima y las otras siete bajan a opacidad `.25`. El pie del cubo escribe el nombre del
módulo activo. Funciona igual con teclado (`focusin`).

Es la única excepción a la regla del lima: aquí es señal de estado, no acción, y solo puede
haber una pieza activa a la vez.

### Pila de migración

Dos planos en perspectiva: el sistema antiguo detrás y atenuado, Orezco delante. Al pasar
por encima se separan. Representa la convivencia de los dos sistemas durante el traspaso.

### Movimiento

Todo respeta `prefers-reduced-motion: reduce`: los giros se detienen y los relieves de hover
se anulan.

## Logo

- `assets/logo.svg` es una **reconstrucción vectorial** del PNG original, no el original.
- Usa `currentColor`. Las divisiones internas leen `--mark-bg`, que **debe igualar el fondo**
  sobre el que se coloca.
- **Pendiente**: sustituir por el SVG original si aparece.

## Reglas de contenido

- **Nada inventado.** Sin cifras de clientes, testimonios, logotipos de empresas ni precios.
  Nada de eso existe todavía.
- El estado del producto se dice tal cual: **en desarrollo**, en una etiqueta visible.
- Sin tira de logos de clientes, aunque la referencia la lleve: no hay clientes que enseñar.
- La copy actual es propuesta, pendiente de aprobar.
