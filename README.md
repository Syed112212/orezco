# orezco.com

Web de Orezco, un ERP. Sitio estatico: HTML y CSS planos, sin build ni dependencias.

## Que hay

    index.html      landing completa
    404.html        pagina de error, mismo sistema visual
    assets/logo.svg logo monocromo, usa currentColor
    CNAME           dominio personalizado de GitHub Pages
    DESIGN.md       SSOT visual: color, tipografia, ritmo, componentes

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
- **Contacto**: el bloque de cierre tiene un hueco a la vista porque no hay buzon real.
  Hace falta email o formulario.
- **Logo**: `assets/logo.svg` es reconstruccion del PNG original, no el original.
- **Copy**: los textos son propuesta, pendientes de aprobar.
- **noindex**: puesto a proposito en index.html y 404.html. Quitarlo cuando la copy este
  aprobada y haya via de contacto.

## Reglas de contenido

Nada inventado. Sin cifras de clientes, sin testimonios, sin logotipos de empresas y sin
precios mientras no existan de verdad. El estado del producto se dice tal cual:
en desarrollo.
