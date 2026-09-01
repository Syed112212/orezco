# Orezco — sistema visual

SSOT visual del proyecto. Cualquier cambio de color, tipografia, espaciado o componente
se decide aqui primero y se sincroniza en el mismo commit que el codigo.

## Estado

Sistema **provisional**. Definido a partir del unico activo existente (el logo en
monocromo). Faltan por decidir: color de acento, tipografia definitiva del wordmark
y tono de marca. No hay identidad de marca formalizada todavia.

## Logo

- `assets/logo.svg` es una **reconstruccion vectorial** hecha a partir del PNG que
  entrego el usuario. Geometria: hexagono de puntas verticales con esquinas muy
  redondeadas, dividido por una Y invertida (lectura de cubo isometrico), con un
  destello de 6 puntas centrado que cruza las divisiones.
- Usa `currentColor` para el trazo, asi que hereda el color del contenedor.
- Las divisiones internas usan la variable `--logo-bg` (por defecto `#000`) y deben
  igualar el fondo sobre el que se coloca el logo.
- **Pendiente**: sustituir por el SVG original si existe. Comparar contra el PNG antes
  de dar por buena la reconstruccion.

### Zona de proteccion

Margen libre alrededor del simbolo = 25% de su altura. No colocar sobre fotografia
sin una capa de contraste por debajo.

## Color

| Token | Valor | Uso |
|---|---|---|
| `--bg` | `#000000` | Fondo. El negro es el fondo nativo de la marca |
| `--fg` | `#FFFFFF` | Logo, wordmark, texto principal |
| `--muted` | `rgba(255,255,255,.45)` | Texto secundario |
| `--logo-bg` | `#000000` | Divisiones internas del logo (= fondo) |

Sin color de acento. **Decision pendiente**: si Orezco necesita uno, elegirlo despues
de definir sector y publico, no antes.

## Tipografia

- Familia: **Poppins** (geometrica, sans, sustituta razonable del wordmark original).
  Fallback: `-apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif`.
- Wordmark: 600, `letter-spacing: .18em`, mayusculas.
- Texto secundario: 400, `letter-spacing: .32em`, mayusculas.
- Con tracking amplio hay que compensar con `text-indent` del mismo valor, si no el
  bloque queda descentrado hacia la izquierda.

## Escala y layout

- Espaciado y tamanos con `clamp()` — el sitio no tiene breakpoints, escala continua.
- Centrado absoluto, una sola columna.

## Movimiento

- Una unica entrada: fade + 14px hacia arriba, 900ms, `cubic-bezier(.2,.7,.3,1)`.
- Respeta `prefers-reduced-motion: reduce`.

## Reglas de contenido

- **Nada inventado.** La pagina no afirma que hace Orezco, no lista servicios, no da
  cifras ni promete fechas, porque nada de eso esta definido.
- No se publica email de contacto hasta que exista un buzon real (la cuenta no tiene
  plan de correo).
