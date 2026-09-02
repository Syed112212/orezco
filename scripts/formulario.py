# -*- coding: utf-8 -*-
"""El formulario, en un solo sitio.

Un sitio estatico no puede guardar nada por si mismo: hace falta algo que
reciba el envio. Aqui se usa FormSubmit, que reenvia cada formulario al
buzon indicado sin necesidad de cuenta ni de servidor propio.

Dos consecuencias que hay que asumir y contar:
  1. Los envios pasan por un tercero, asi que aparece en la politica de
     privacidad como encargado del tratamiento.
  2. El primer envio dispara un correo de activacion al buzon. Hasta que
     alguien pulse ese enlace, no llega nada. Y para que ese correo
     llegue, el dominio necesita registros MX.

Si algun dia hay servidor propio, solo cambia DESTINO y ENDPOINT.
"""

BUZON = "info@contaes.com"
ENDPOINT = "https://formsubmit.co/" + BUZON
GRACIAS = "https://contaes.com/gracias/"

# El nombre del campo trampa lo fija FormSubmit: los robots rellenan todo
# lo que ven, las personas no ven este porque esta oculto.
TRAMPA = "_honey"


def campos_ocultos(asunto):
    return (
        '        <input type="hidden" name="_subject" value="%s">\n'
        '        <input type="hidden" name="_next" value="%s">\n'
        '        <input type="hidden" name="_template" value="table">\n'
        '        <input type="hidden" name="_captcha" value="false">\n'
        '        <input type="text" name="%s" tabindex="-1" autocomplete="off" aria-hidden="true"\n'
        '               style="position:absolute;left:-9999px;width:1px;height:1px;opacity:0">\n'
        % (asunto, GRACIAS, TRAMPA)
    )


def nota_legal(sangria="        "):
    return (
        '%s<p class="form-nota">Al enviar aceptas que usemos estos datos para responderte. '
        'Nada mas. Puedes leer el detalle en la <a href="/legal/privacidad/">política de '
        'privacidad</a>.</p>\n' % sangria
    )
