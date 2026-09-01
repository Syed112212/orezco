# Orezco — sistema visual

SSOT visual del proyecto. Cualquier cambio de color, tipografía, espaciado o componente
se decide aquí primero y se sincroniza en el mismo commit que el código.

**Dirección**: *broadsheet editorial en sala verde*. La página se lee como un periódico
financiero impreso llevado a pantalla: titulares monumentales con serifa, micro-etiquetas
en versalitas, y un único verde saturado que funciona como rotulador sobre un lienzo por lo
demás monocromo. Es un mundo visual único y deliberado — no hay tema oscuro alternativo,
todos los colores se pintan explícitamente.

Referencia de partida: `styles.refero.design/style/1a519123-071a-449f-b5df-0def73ed7f35`

## Color

| Token | Hex | Nombre | Uso |
|---|---|---|---|
| `--verde` | `#2bee4b` | Rotulador | **Único acento vivo.** Relleno de CTA, subrayado de navegación activa, banda de pie |
| `--musgo` | `#93b799` | Musgo | Apoyo. Sombras del CTA, numeración, detalle. **Nunca como color de acción** |
| `--eco` | `#c4e4c9` | Eco | Apoyo claro. Separadores y bordes de retícula |
| `--tinta` | `#000000` | Tinta | Texto corrido sobre claro |
| `--prensa` | `#121613` | Negro prensa | Titulares, fondo de secciones oscuras y pie. Negro con sesgo verde frío |
| `--pizarra` | `#232924` | Pizarra | Superficie secundaria dentro de lo oscuro |
| `--gris` | `#516254` | Gris papel | Pies, texto auxiliar, etiquetas apagadas |
| `--salvia` | `#c8d2c8` | Salvia | Texto claro sobre superficie oscura |
| `--hueso` | `#fafffa` | Blanco hueso | Lienzo. Casi blanco con tinte verde, para que lea como papel y no como pantalla |

**Regla dura**: el verde `#2bee4b` es un rotulador, no un color de relleno. Si aparece en
más de dos sitios por pantalla, algo está mal.

## Tipografía

La referencia usa TWK Lausanne, PP Mondwest y Editorial New — las tres de pago. Se
sustituyen por equivalentes de Google Fonts, que es además lo que la propia referencia
recomienda como fallback:

| Rol | Original | En uso | Ajustes |
|---|---|---|---|
| Display | PP Mondwest | **Instrument Serif** 400 | `line-height: .9`, `letter-spacing: -.04em` |
| Editorial | Editorial New | **Newsreader** 300 | `line-height: 1.32`, `letter-spacing: -.015em` |
| UI / texto | TWK Lausanne | **Inter** 400/500/600 | micro-etiquetas 11px / 600 / `+.01em` mayúsculas |

- Escala: cuarta justa (1.333) desde 18px base.
- El titular de portada va en Instrument Serif con interlineado 0.9 y tracking −0.04em.
  **Ese tracking apretado es lo que hace que el titular lea como tinta impresa** — si se
  afloja, se pierde la dirección entera.
- Las micro-etiquetas en versalitas son estructura, no decoración: marcan de qué habla
  cada sección.

## Ritmo y forma

| | |
|---|---|
| Ancho máximo | `1400px` |
| Separación entre secciones | `80px` |
| Separación entre elementos | `20px` |
| Radio de botones | `5px` |
| Radio de píldoras | `10px` |
| Radio de imágenes y retículas | `14px` |

Densidad **espaciosa**. El aire es parte de la dirección, no un descuido.

## Componentes

- **CTA primario**: relleno `--verde`, texto `--prensa`, sombra verde tintada con
  `--musgo`. Es el único elemento con sombra en toda la página.
- **Retículas**: se dibujan con `gap: 1px` sobre fondo `--eco`, no con bordes por celda.
  Así las hairlines no se duplican.
- **Banda verde**: franja a sangre entre el cierre y el pie. Enumera las áreas del
  producto en versalitas.

## Logo

- `assets/logo.svg` es una **reconstrucción vectorial** del PNG original. Geometría:
  hexágono de puntas verticales con esquinas muy redondeadas, dividido por una Y invertida
  (lectura de cubo isométrico), con un destello de 6 puntas centrado.
- Usa `currentColor`, así que hereda el color del contenedor.
- Las divisiones internas leen la variable `--mark-bg`, que **debe igualar el fondo** sobre
  el que se coloca. Está definida en `.nav` (hueso), `.dark` y `footer` (prensa).
- **Pendiente**: sustituir por el SVG original si aparece.

### Zona de protección

Margen libre alrededor del símbolo = 25% de su altura.

## Reglas de contenido

- **Nada inventado.** La página no da cifras de clientes, ni testimonios, ni logotipos de
  empresas, ni precios. Nada de eso existe todavía y publicarlo sería falso.
- El estado del producto se dice tal cual: **en desarrollo**.
- El bloque de contacto lleva un hueco marcado a la vista porque no hay buzón real — la
  cuenta no tiene plan de correo. Se rellena cuando lo haya.
- `<meta name="robots" content="noindex">` está puesto a propósito. Quitarlo cuando la
  copy esté aprobada y haya vía de contacto.
