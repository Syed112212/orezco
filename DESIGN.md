# Orezco — sistema visual

SSOT visual del proyecto. Cualquier cambio de color, tipografía, espaciado o componente
se decide aquí primero y se sincroniza en el mismo commit que el código.

**Dirección**: *analítica con serifa sobre papel cálido*. Lienzo blanco, titulares con
serifa en peso 400 a tamaños grandes, tarjetas de esquinas muy redondeadas, botones píldora,
y **un solo color** —un melocotón cálido— usado una vez por página. Adaptado del sistema de
Steep, que es la referencia que eligió el cliente.

Mundo visual único y deliberado (claro). No hay tema oscuro alternativo: todos los colores
se pintan explícitamente.

## Color

### Superficies

| Token | Hex | Uso |
|---|---|---|
| `--papel` | `#ffffff` | Lienzo. El blanco sobre el que se apoya todo |
| `--mist` | `#f2f2f3` | Tarjeta neutra: bloques de contenido, listas |
| `--niebla` | `#fafafb` | Banda de sección alterna. Rompe el blanco sin contraste |
| `--melocoton` | `#fbe1d1` | **Acento. Una tarjeta por página, ni una más** |

### Texto

| Token | Hex | Uso |
|---|---|---|
| `--tinta` | `#17191c` | Texto principal y relleno del botón. La única superficie oscura |
| `--pizarra` | `#777b86` | Apoyo, texto de párrafo secundario |
| `--ceniza` | `#979799` | Etiquetas de categoría. Tipográficas, sin fondo ni borde |
| `--humo` | `#a3a6af` | Marcador de campo (placeholder) |
| `--sienna` | `#5d2a1a` | **Solo sobre melocotón.** Nunca como texto sobre blanco |
| `--hairline` | `#ececec` | Divisores y borde de campo |

**Dos reglas duras**: el melocotón aparece **una vez** en toda la página, y siempre sobre
blanco —nunca sobre una banda de color—. Y el sienna es la tinta del melocotón: fuera de
esa tarjeta no se usa.

El sistema es intencionadamente **casi acromático**. Meter azul, verde o morado lo rompe.

## Tipografía

La referencia usa Signifier y Sohne, las dos de pago. Se sustituyen por equivalentes de
Google Fonts, que además son las que la propia referencia recomienda:

| Rol | Original | En uso | Ajustes |
|---|---|---|---|
| Display y titulares | Signifier | **Source Serif 4** 400 | `line-height: 1.3`, `-.025em` a 90px, `-.015em` a 44/64px |
| Cuerpo, UI, navegación | Sohne | **Inter** 400–500 | `-.009em` a 18–26px, 0 en cuerpo |

- **La serifa se queda en peso 400 a todos los tamaños.** Esa contención es la firma del
  sistema: nunca negrita, nunca semibold en la serifa.
- Una frase del titular va en **cursiva** a media oración. Es el gesto editorial de la
  referencia y se repite en cada `h2`.
- Inter usa pesos de medio paso —430, 450, 480— para la jerarquía del cuerpo antes de
  llegar a 500.

### Escala

| Rol | Tamaño | Interlineado |
|---|---|---|
| Display (portada) | 90px | 1.3 |
| Sección | 64px | 1.3 |
| Subtítulo | 20–22px | 1.35 |
| Cuerpo | 17px | 1.35 |
| Apoyo | 18px / peso 430 | 1.5 |
| Etiqueta | 14–15px | 1.5 |

## Ritmo y forma

| | |
|---|---|
| Ancho máximo | `1200px` |
| Separación entre secciones | `80px` |
| Relleno de tarjeta | `20px` |
| Base de espaciado | `4px` |

**Radios**: tarjetas `24px`, artefactos flotantes `20px`, campos `16px`, botones `9999px`.
Nada por debajo de 16px en tarjetas, y los botones son siempre píldora completa.

## Sombras

**Solo los artefactos flotantes llevan sombra.** Las tarjetas de contenido —neutras y la de
melocotón— van planas, sin sombra ni borde.

```
--sombra-flotante:
  rgba(4,23,43,.05) 0 0 0 1px,
  rgba(0,0,0,.1) 0 20px 25px -5px,
  rgba(0,0,0,.1) 0 8px 10px -6px;
```

## Botones

Píldora siempre, y **en pareja**: el relleno oscuro (`--tinta` sobre blanco) va acompañado
del fantasma (borde `--tinta`, fondo transparente) en la misma línea base. Los enlaces de
texto no van subrayados en reposo —la flecha `→` es la que indica que son enlaces—; el
subrayado aparece solo al pasar por encima.

## Los objetos 3D

No hay capturas de producto todavía, así que **el 3D ocupa el lugar de los artefactos
flotantes** de la referencia. Todo es CSS `transform-style: preserve-3d`, sin librerías.

### Cubo-logo (portada y 404)

El símbolo de la marca ya es un cubo isométrico, así que en 3D es un cubo real con el
destello de seis puntas en cada cara. Gira 360° en 24 s.

- Caras en `--papel` y `--mist` con arista `rgba(4,23,43,.1)`, y `backface-visibility:
  hidden`. Con caras translúcidas se transparentan los destellos traseros.

### Cubo de ocho piezas (módulos)

Ocho módulos, ocho vértices. Al pasar por una fila se ilumina su pieza en **melocotón con
borde sienna** y las otras siete bajan a opacidad `.3`. El pie escribe el nombre del módulo.
Funciona igual con teclado (`focusin`).

Es la excepción a la regla de "un melocotón por página": aquí es señal de estado, no una
tarjeta, y solo puede haber una pieza activa a la vez.

### Pila de migración

Dos planos flotantes en perspectiva —con la sombra del sistema—: el sistema antiguo detrás y
atenuado, Orezco delante. Al pasar por encima se separan.

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
- El estado del producto se dice tal cual: **en desarrollo**, visible en la portada.
- La sección "Para quién es" incluye a propósito **un perfil al que no le sirve**.
- La copy actual es propuesta, pendiente de aprobar.
