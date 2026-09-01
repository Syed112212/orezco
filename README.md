# orezco.com

Web de Orezco, un ERP. Sitio estatico: HTML y CSS planos, sin build ni dependencias.

## Que hay

    index.html      landing completa
    404.html        pagina de error, mismo sistema visual
    assets/logo.svg logo monocromo, usa currentColor
    assets/og.png   imagen 1200x630 para compartir enlaces (generada, ver abajo)
    robots.txt      permite indexar, apunta al sitemap
    sitemap.xml     una sola URL
    CNAME           dominio personalizado de GitHub Pages
    DESIGN.md       SSOT visual: color, tipografia, ritmo, componentes

## Imagen para compartir

`assets/og.png` se genera con Chrome headless a partir de una plantilla HTML. Para
regenerarla tras un cambio de marca:

    chrome --headless=new --disable-gpu --hide-scrollbars --virtual-time-budget=10000       --force-device-scale-factor=1 --window-size=1200,630       --screenshot=assets/og.png file:///ruta/og.html

## Diseno

Direccion "broadsheet editorial en sala verde": titulares monumentales con serifa,
micro-etiquetas en versalitas y un unico verde (#2bee4b) usado como rotulador.
Mundo visual unico y deliberado, sin tema oscuro alternativo.

Todo el sistema esta en DESIGN.md. **Leerlo antes de tocar cualquier estilo.**

## Despliegue

GitHub Pages sirve la rama `main` desde la raiz. Cada push a `main` publica.

DNS en Hostinger apuntando a Pages:

    @    A      185.199.108.153 / .109.153 / .110.153 / .111.153
    www  CNAME  syed112212.github.io.

Script para aplicarlo: `~/.claude/scripts/hostinger-dns-orezco.sh {pages|rollback|show}`

## Pendiente

- **DNS**: el dominio sigue apuntando al aparcamiento de Hostinger.
- **Contacto**: el formulario esta construido y probado, pero inactivo. Para activarlo,
  poner la direccion en la constante `CONTACTO` del script al final de `index.html`:

      var CONTACTO = "hola@orezco.com";

  Vacia -> se muestra la pildora "canal disponible en breve" y el formulario queda oculto.
  Con valor -> aparece el formulario, que compone un mailto con los campos rellenados, y
  el enlace directo a esa direccion. No hace falta backend.

  La API de Hostinger NO gestiona correo (todos los endpoints de email dan 404), asi que
  el buzon hay que crearlo a mano en hPanel. Plan mas barato: Starter Business Email,
  7,08 USD el primer ano y 19,08 despues.
- **Logo**: `assets/logo.svg` es reconstruccion del PNG original, no el original.
- **Copy**: los textos son propuesta, pendientes de aprobar.
- **noindex**: puesto a proposito en index.html y 404.html. Quitarlo cuando la copy este
  aprobada y haya via de contacto.

## Reglas de contenido

Nada inventado. Sin cifras de clientes, sin testimonios, sin logotipos de empresas y sin
precios mientras no existan de verdad. El estado del producto se dice tal cual:
en desarrollo.
