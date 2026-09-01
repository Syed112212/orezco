# orezco.com

Sitio de Orezco. Ahora mismo, una pagina de espera estatica.

## Que hay

    index.html      pagina unica
    404.html        copia de index (Pages sirve esto en rutas no encontradas)
    assets/logo.svg logo reconstruido, monocromo, usa currentColor
    CNAME           dominio personalizado de GitHub Pages
    DESIGN.md       SSOT visual: color, tipografia, reglas del logo

Sin build, sin dependencias. HTML y CSS planos.

## Despliegue

GitHub Pages sirve la rama `main` desde la raiz. Cada push a `main` publica.

DNS en Hostinger apuntando a Pages:

    @    A      185.199.108.153 / .109.153 / .110.153 / .111.153
    www  CNAME  syed112212.github.io.

## Pendiente

- Sustituir `assets/logo.svg` por el original si aparece (el actual es reconstruccion).
- Definir sector, producto y publico. Hasta entonces la pagina no afirma nada.
- Decidir color de acento y tipografia definitiva.
- `<meta name="robots" content="noindex">` esta puesto a proposito. Quitarlo cuando
  haya contenido real que indexar.
