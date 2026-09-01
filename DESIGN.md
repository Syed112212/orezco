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
| `--pizarra` | `#6b6e78` | Apoyo, texto de párrafo secundario |
| `--ceniza` | `#6c6e74` | Etiquetas de categoría. Tipográficas, sin fondo ni borde |
| `--humo` | `#71747c` | Marcador de campo (placeholder) |
| `--sienna` | `#5d2a1a` | **Solo sobre melocotón.** Nunca como texto sobre blanco |
| `--hairline` | `#ececec` | Divisores y borde de campo |

**Dos reglas duras**: el melocotón aparece **una vez** en toda la página, y siempre sobre
blanco —nunca sobre una banda de color—. Y el sienna es la tinta del melocotón: fuera de
esa tarjeta no se usa.

El sistema es intencionadamente **casi acromático**. Meter azul, verde o morado lo rompe.

### Desviación consciente de la referencia: contraste

Los tres grises de texto **se han oscurecido respecto a la referencia**, porque los
originales no llegan al mínimo de WCAG AA (4.5:1 para texto normal):

| Token | Referencia | En uso | Antes | Ahora |
|---|---|---|---|---|
| `--pizarra` | `#777b86` | `#6b6e78` | 3.78:1 sobre tarjeta | **4.55:1** |
| `--ceniza` | `#979799` | `#6c6e74` | 2.92:1 sobre papel | **4.56:1** |
| `--humo` | `#a3a6af` | `#71747c` | 2.43:1 sobre campo | **4.68:1** |

El cambio es imperceptible a la vista y la diferencia de legibilidad es real. Todo lo
demás de la referencia se respeta al pie de la letra. `scripts/check-design.py` mide
estos contrastes en cada ejecución, así que si alguien devuelve los valores originales,
salta.

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

### Trampa: `filter` aplana el 3D

**Nunca poner `filter` (ni `opacity` < 1) en un elemento con `transform-style: preserve-3d`.**
Cualquier filtro fuerza `transform-style: flat` en los hijos, y el cubo pasa a verse como un
rombo plano. Pasó con un `drop-shadow` inocente en el cubo de la portada, y solo se ve
renderizando. Si hace falta sombra bajo un objeto 3D, va en un elemento hermano o en un
pseudoelemento del contenedor, nunca en el que lleva `preserve-3d`.

### Movimiento

Todo respeta `prefers-reduced-motion: reduce`: los giros se detienen y los relieves de hover
se anulan.

## Logo

Se genera con `python scripts/build-logo.py`. **No editar los SVG a mano**: se
sobrescriben. Si hay que cambiar la geometría, se cambian las constantes del script.

### Construcción

Hexágono de puntas verticales, radio 86 sobre lienzo de 200, esquinas redondeadas con
arcos reales de radio 24. Dividido por una Y invertida que lo hace leer como cubo
isométrico, con un destello de seis puntas centrado **alineado con las divisiones**, que
cruza las tres caras.

Todo se resuelve con **una máscara SVG**: el hexágono es sólido, y las divisiones y el
destello se restan. Los huecos son **transparentes de verdad**, no del color del fondo.

Eso es lo que arregla el defecto de la versión anterior, que pintaba las divisiones con
una variable `--mark-bg` y por tanto solo funcionaba sobre el fondo exacto para el que se
hizo: cargado como `<img>`, sobre una foto o en un bordado salía como un hexágono macizo.

### Variantes

| Fichero | Uso |
|---|---|
| `assets/logo.svg` | `currentColor`. Favicon y cualquier contexto que propague color |
| `assets/logo-tinta.svg` | Tinta fija `#17191c`, para consumidores que no propagan color |
| `assets/logo-blanco.svg` | Blanco, para fondos oscuros |
| `assets/mark-inline.svg` | Fragmento con `<mask>` + `<symbol id="mark">` para incrustar en HTML |

En la web va **incrustado**, no como `<img>`, para que herede `currentColor` del contenedor.

### Decisiones descartadas

- **Destello intercalado a 30°** de las divisiones: da nueve líneas y satura.
- **Destello en sólido**: al no cruzar ningún hueco se funde con el cuerpo y desaparece.

### Zona de protección

Margen libre alrededor del símbolo = 25% de su altura.

## Tokens

Los nombres del `:root` de `index.html` son **los canónicos de la referencia**
(`--color-ink-black`, `--surface-canvas`, `--radius-cards`…), con alias de trabajo derivados
de ellos. No renombrar: así el código y el sistema de diseño hablan el mismo idioma.

`tokens.json` guarda los mismos valores en formato DTCG, listo para alimentar Figma,
Tailwind o Style Dictionary. Si cambia un valor, cambia en los dos sitios.

## El verificador

`scripts/check-design.py` convierte las reglas duras de este documento en comprobaciones
ejecutables. Se ejecuta solo en cada push (`.github/workflows/check-design.yml`) y falla
la build si alguna se incumple:

1. **Nada de `filter`, `opacity` ni `mask` sobre `preserve-3d`** — la trampa que aplanó el cubo.
2. **Una sola tarjeta melocotón** por página.
3. **La serifa siempre en peso 400.**
4. **Sombra solo en artefactos flotantes.**
5. **Cuatro radios** y ni uno más.
6. **Ninguna variable CSS usada sin declarar.**
7. **Contraste WCAG AA** en los ocho emparejamientos reales de texto y fondo.
8. **`tokens.json` y el `:root` dicen lo mismo.**

Si cambias una regla en este documento, cámbiala también en el verificador. Si no, el
documento miente.

## Reglas de contenido

- **Nada inventado.** Sin cifras de clientes, testimonios, logotipos de empresas ni precios.
- El estado del producto se dice tal cual: **en desarrollo**, visible en la portada.
- La sección "Para quién es" incluye a propósito **un perfil al que no le sirve**.
- La copy actual es propuesta, pendiente de aprobar.
