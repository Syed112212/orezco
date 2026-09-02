# Contaes — sistema visual

SSOT visual del proyecto. Cualquier cambio de color, tipografía, espaciado o componente
se decide aquí primero y se sincroniza en el mismo commit que el código.

**Dirección**: *cuaderno de papel cálido bajo luz de tarde*, tomada de la referencia Notion
que eligió el cliente. Lienzo cálido en vez de blanco, tarjetas con filete de 1px y **sin
sombra**, un único azul para la acción, y un reparto de acentos que pinta paneles enteros
como si fueran notas adhesivas.

La paleta de la marca —el navy y el verde del logo— entra en ese reparto, no lo sustituye.

Mundo visual único y deliberado (claro). No hay tema oscuro alternativo.

## Color

### Superficies

| Token | Hex | Uso |
|---|---|---|
| `--papel` | `#f6f5f4` | **Lienzo.** Cálido, no blanco. Es la firma del sistema |
| `--blanco` | `#ffffff` | Tarjetas. El blanco es lo que va *encima* de la página |
| `--borde` | `rgba(0,0,0,.08)` | Filete de 1px. **Nunca sombra en una tarjeta de contenido** |

### Texto

La jerarquía se construye con **alfa sobre el mismo negro**, no añadiendo colores.

| Token | Valor | Uso |
|---|---|---|
| `--tinta` | `rgba(0,0,0,.95)` | Texto general |
| `--tinta-fuerte` | `#000000` | Titulares |
| `--grafito` | `#615d59` | Cuerpo, con matiz cálido que armoniza con el lienzo |
| `--piedra` | `#6a6a6a` | Apoyo. **Oscurecido**: el `#757575` de la referencia no llega a AA |
| `--apagado` | `rgba(0,0,0,.54)` | Enlaces de navegación en reposo |

### Acción y acentos

| Token | Hex | Uso |
|---|---|---|
| `--azul` | `#0075de` | **El único relleno cromático.** Un botón por pantalla |
| `--azul-tinte` | `#e6f3fe` | Fondo del botón secundario. Su texto va en `#005fb8`, no en `#0075de` |
| `--marigold` | `#ffb110` | Panel de acento, píldora del titular |
| `--coral` | `#f64932` | Panel de acento. **Texto negro encima**, el blanco no llega a AA |
| `--cielo` | `#62aef0` | Panel de acento |
| `--medianoche` | `#02093a` | Panel oscuro y pie. Isla oscura, no un tema |

### Marca

`--navy #1E3A5F`, `--verde #2FBF9B`, `--cian #1F9EC4`, `--azul-marca #1E6FB8`,
`--canto #132741` (el canto de las extrusiones 3D). Salen del logo y viven en el logo, el
wordmark y las extrusiones.

### Desviaciones conscientes de la referencia

Tres colores se han oscurecido porque los originales no llegan a WCAG AA:

| Token | Referencia | En uso | Antes | Ahora |
|---|---|---|---|---|
| `--piedra` | `#757575` | `#6a6a6a` | 4.23:1 | **4.97:1** |
| texto sobre tinte | `#0075de` | `#005fb8` | 4.05:1 | **5.59:1** |
| texto sobre coral | `#ffffff` | `#000000` | 3.55:1 | **5.92:1** |

`scripts/check-design.py` los mide en cada ejecución: si alguien devuelve los originales,
salta.

## Tipografía

| Rol | Original | En uso |
|---|---|---|
| Interfaz y titulares | NotionInter | **Inter** 400/500/600/700 |
| Voz editorial | Lyon Text | **Source Serif 4** 400, solo a 18–21px |
| Wordmark | — | **Quicksand** 600, con las letras «es» en verde |

- **Tracking negativo agresivo en los tamaños grandes**: `-.048em` a 84px, `-.035em` a
  54px. Es lo que hace que el titular lea compacto y seguro en vez de aireado.
- La serifa es un **acento**, no una jerarquía paralela: entradillas y pies, nunca UI.

## Ritmo y forma

Base 4px. Ancho 1160px. Secciones a 80px. Relleno de tarjeta 24px.

**Cuatro radios y ni uno más**: tarjetas `12px`, botones `8px`, pequeños `4px`,
píldoras `9999px`. Nada por encima de 12px en contenido rectangular.

## Sombras

**Ninguna tarjeta de contenido lleva sombra.** Solo tres cosas:
la barra de navegación, la maqueta de producto, y el anillo de foco de los campos —que es
accesibilidad, no decoración.

## Los objetos 3D y la animación

Todo es CSS `transform-style: preserve-3d`, **sin librerías**.

- **Logo extruido**: 14 copias del símbolo desplazadas en Z, las de atrás en `--canto`.
  Sigue al ratón, y solo con puntero fino: en táctil no hay hover.
- **Ocho losas** apiladas, una por módulo. Al pasar por una fila, su losa sube y se pinta.
- **Dos planos de migración** que se separan al pasar por encima.
- **Entrada escalonada** de la portada, **revelado al hacer scroll** con
  `IntersectionObserver`, y motas flotantes.

Sin `IntersectionObserver` todo se muestra de golpe: **el contenido nunca depende de que la
animación funcione**. Y todo se apaga con `prefers-reduced-motion: reduce`.

### Trampa: `filter` aplana el 3D

**Nunca poner `filter` ni `opacity` < 1 en un elemento con `preserve-3d`.** Fuerza
`transform-style: flat` en los hijos y el objeto se ve plano. Ya pasó dos veces. El
verificador lo detecta.

## Logo

Se genera con `python scripts/build-logo.py`. **No editar los SVG a mano.**

Símbolo: una C abierta hacia la derecha y, dentro de la abertura, tres barras que completan
una E. Leen «C» + «E» y a la vez sugieren las líneas de un libro de cuentas. Las barras
suben de azul a verde: es el único degradado de la marca.

| Fichero | Uso |
|---|---|
| `assets/logo.svg` | Principal, a color |
| `assets/logo-navy.svg` | Una sola tinta |
| `assets/logo-blanco.svg` | Fondos oscuros |
| `assets/mark-inline.svg` | Fragmento con los tres símbolos para incrustar |

Los colores son **una estimación tomada del PNG original**. Si aparecen los valores exactos
de marca, se cambian en el script y se regenera todo.

## El blog

Se genera con `python scripts/build-blog.py`. Índice, artículos, 404 y sitemap salen de una
sola fuente, así que no pueden desincronizarse. **Añadir un artículo es añadir una entrada a
`ARTICULOS`**, no copiar una plantilla.

Cada artículo lleva canonical, OG, JSON-LD de `Article` y `BreadcrumbList`.

## El verificador

`scripts/check-design.py` convierte estas reglas en pruebas y corre en CI. Si cambias una
regla aquí, cámbiala también allí. Si no, este documento miente.

## Reglas de contenido

- **Nada inventado.** Sin cifras de clientes, testimonios, logotipos ni precios.
- El estado se dice tal cual: **en desarrollo**, visible en la portada.
- La maqueta de conversación de la portada lleva **aviso visible** de que es ilustrativa.
- La sección «Para quién es» incluye a propósito **un perfil al que no le sirve**.
- Los artículos del blog informan sobre el problema; **no prometen nada sobre Contaes**.
- La copy es propuesta, pendiente de aprobar.
