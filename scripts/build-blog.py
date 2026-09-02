#!/usr/bin/env python3
"""
Genera el blog de Contaes y la pagina 404.

Todas las paginas comparten cascara (cabecera, pie, tokens), asi que se
escriben una sola vez aqui y el contenido de cada articulo vive en ARTICULOS.
Anadir un articulo = anadir una entrada a esa lista.

    python scripts/build-blog.py

Genera:
    404.html
    blog/index.html
    blog/<slug>.html   (uno por articulo)
    sitemap.xml        (portada + blog + articulos)

SEO: cada articulo lleva su propio title, description, canonical, OG, y
JSON-LD de tipo Article con BreadcrumbList. La cascara -marca, estilos,
barra y pie- viene de plantilla.py, para que el menu no se separe del
resto del sitio. El sitemap lo escribe build-sitio.py, que es el unico
que conoce todas las paginas.
"""

import io
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMINIO = "https://contaes.com"

# ─────────────────────────────────────────────────────────────────────────
# Los articulos. El cuerpo es HTML simple: h2, p, ul, blockquote.
# Regla de contenido: informacion util y honesta sobre el problema. Nada
# de cifras de clientes, casos de exito ni promesas sobre Contaes.
# ─────────────────────────────────────────────────────────────────────────
ARTICULOS = [
    {
        "slug": "cobrar-antes-sin-perder-clientes",
        "titulo": "Cobrar antes sin perder al cliente",
        "descripcion": "Gestionar deudas de clientes sin perder la relación: priorizar por antigüedad, pactar por escrito, avisar antes del vencimiento y saber retirarse a tiempo.",
        "fecha": "2026-09-02",
        "minutos": 7,
        "tema": "Tesorería",
        "acento": "verde",
        "entradilla": "La deuda no se cobra por importe, se cobra por fecha. Un impagado antiguo siempre sale más caro que uno grande.",
        "cuerpo": """
<h2>La deuda se mide en días, no en euros</h2><p>En el despacho veo todos los días empresas que solo persiguen las facturas grandes. Se olvidan de la de 300 euros de hace ocho meses. Mal hecho.</p><p>Una factura con tres meses de antigüedad tiene mucho menos recorrido que una de hace veinte días. Cada día que pasa, tu posición se debilita: el cliente se acostumbra a deberte, encuentra otro proveedor y pierde la vergüenza.</p><p>Lo pequeño olvidado se convierte en lo grande que un día no cobras.</p><ul><li>Lleva un listado de facturas por antigüedad, no por importe.</li><li>Ataca primero la más vieja, aunque sea ridícula.</li><li>Si un cliente te debe tres facturas de plazos distintos, empieza por la que venció antes.</li></ul><p>Da igual que sea un cliente excelente. Cuando no paga, deja de ser excelente: se convierte en un riesgo.</p><h2>Pacta por escrito, aunque te parezca feo</h2><p>"Llevamos diez años con esta forma de trabajar." Esa frase no vale para cobrar. Si no lo tienes escrito, el compromiso del cliente es débil.</p><p>En el contrato o en la hoja de encargo tiene que estar claro cuándo pagas y cómo pagas. No vale un "a 60 días" ambiguo. Hay que decir: la factura se paga a los sesenta días naturales desde su emisión, por transferencia, a la cuenta indicada.</p><p>Las condiciones deben estar cerradas antes de empezar a trabajar. Reabrir la conversación después de la entrega es ponerte en una posición incómoda.</p><p>Además, acostumbra a tus clientes a recibir un documento que lo confirme. La factura proforma o el presupuesto aceptado ya son un contrato. Que no haya sorpresas con el plazo.</p><blockquote>Una factura impagada no es un problema de dinero, es un problema de información. Te avisa de algo que está fallando en la relación.</blockquote><h2>El recordatorio antes del vencimiento: la mejor herramienta</h2><p>No tienes que esperar a que la factura venza para empezar a perseguirla. Envía un aviso dos o tres días antes. Un correo breve vale más que cualquier reclamación posterior.</p><p>Ese correo no es una amenaza. Es una cortesía profesional: "Te recuerdo que la factura X de importe Y vence el viernes. Si necesitas cualquier dato, dímelo".</p><p>Con eso consigues dos cosas. Que tu factura no pase desapercibida en el montón. Y que el cliente que no tiene intención de pagar se ponga nervioso antes de lo previsto.</p><ul><li>Establece una rutina: cada lunes, revisa los vencimientos de la semana siguiente.</li><li>Envía el recordatorio con tiempo para que te puedan responder.</li><li>Pide confirmación de recepción en el correo.</li></ul><p>Si el cliente te dice que no tiene efectivo, ya lo sabes antes de que venza. Has ganado semanas de margen.</p><h2>El cliente grande que paga tarde</h2><p>Todos tenemos un cliente gordo que se salta el plazo. La excusa es la misma: "Es el que da volumen". Y sí, da volumen, pero también te obliga a financiarle el negocio.</p><p>Que pague tarde no es gratis. Si tú pagas a tus proveedores a treinta días y tu cliente grande te paga a noventa, la diferencia la pones de tu bolsillo.</p><p>La solución no es no trabajar con él. Es cambiar las reglas del juego por escrito.</p><p>Primero, dentro de la empresa del cliente hay, al menos, dos personas: el que compra y el que paga. Habla con el que paga, no solo con el de compras. El comercial te dirá que todo va bien. El de administración te dirá la verdad.</p><p>Segundo, negocia algo a cambio del retraso. Por ejemplo, incluye en el contrato un calendario de pagos con cuotas o un plan de pago fraccionado. No aceptes que te diga "ya lo iremos viendo".</p><p>También puedes ofrecer descuento por pronto pago. En lugar de reclamar, premia al que cumple: un 2 % o un 3 % de descuento por pagar en menos plazo. Es rentable si el interés de tu banco te cobra más por descubrir el impago.</p><p>Y si el cliente grande abusa de forma sistemática, haz números. Con margen del 10 % y retrasos de noventa días, cada mes que tardas en cobrar te come el margen. A veces, no compensa.</p><h2>Saber cuándo dejar de servir</h2><p>Hay un momento en que la deuda deja de ser un problema puntual y se convierte en un hábito. Cuando eso pasa, tienes que tomar una decisión.</p><p>Si un cliente supera el plazo fijado en más del doble, y encima no responde a tus recordatorios, deja de servirle. Sin un pago al día o un plan de regularización firmado, cada nueva venta es una deuda más, no una venta.</p><p>Nadie quiere perder un cliente. Pero hay que preguntarse cuánto te cuesta conservarlo. Un cliente que paga tarde te obliga a pedir préstamos para pagar tus nóminas. Ese es el coste real.</p><p>Antes de cortar, haz un intento formal de cobro. Notifica al cliente, por escrito, que si no regulariza la situación, cancelarás los servicios pendientes. La mayoría de impagos puntuales se resuelven en esta fase.</p><p>Y si no se resuelve, déjalo. Tu tiempo también vale. Un cliente que no paga no es un cliente, es una factura con patas.</p><h2>La regla de oro</h2><p>No esperes a que la deuda sea vieja para actuar. No pienses que la factura pequeña desaparece sola. No confundas paciencia con debilidad.</p><p>Pacta desde el principio. Avisa antes de que venza. Clasifica por antigüedad. Y no sirvas a quien no paga.</p><p>Cobrar antes no es presionar al cliente. Es saber qué quieres y pedirlo con educación. El buen cliente no se va por eso. Al contrario, agradece trabajar con alguien que cuida su tesorería.</p>
"""
    },
    {
        "slug": "el-recuento-anual-llega-tarde",
        "titulo": "El recuento anual llega tarde",
        "descripcion": "Por qué contar el stock solo a cierre de año distorsiona tus márgenes. Inventario permanente y recuento cíclico para llevar la merma al día.",
        "fecha": "2026-09-02",
        "minutos": 7,
        "tema": "Operaciones",
        "acento": "cielo",
        "entradilla": "Cerrar el almacén una vez al año no te dice cuánto has perdido cada mes. Solo te dice que ya es tarde.",
        "cuerpo": """
<h2>En diciembre llega el susto</h2><p>En muchas pymes, el recuento del almacén se reserva para el final del año. Se cierra un día, se cuenta todo, se anotan diferencias y se ajusta el stock.</p><p>Ese recuento sirve, como mucho, para cuadrar una fotografía de un solo día. El resto del año, el sistema dice una cosa y la estantería dice otra. Tú vendes, compras y calculas márgenes sobre un número que no es el real.</p><p>Ese es el problema: no es un ajuste lo que necesitas. Es conocer tu negocio durante los doce meses.</p><h2>El margen que ves no es el margen que vives</h2><p>Pongamos un ejemplo sencillo. Compras un artículo por 10 euros y lo vendes por 15. La cuenta de resultados dirá que ganas 5 por cada venta. Pero dentro de esa compra, hay unidades que se rompen, que se pierden o que el transportista estropea. No las has vendido, no cobras por ellas, pero las pagaste.</p><p>Si no lo contabilizas en el momento, tu hoja de márgenes sigue diciendo que cada venta te deja 5 euros. La realidad es algo menos. Cuando haces el recuento anual, descubres que de 100 unidades que compraste, solo quedan 15 en lugar de las 20 que indicaba el sistema. Entonces haces un ajuste de 5 unidades que te resta beneficio de golpe. Pero ese coste no corresponde a diciembre: se ha ido generando mes a mes.</p><h2>Recuento anual: un día de caos</h2><p>No solo es un dato malo. El recuento físico anual tiene otra desventaja: paraliza el almacén.</p><ul><li>Los pedidos se retrasan porque no puedes tocar la mercancía.</li><li>El personal cuenta rápido y mal, sobre todo si hay prisa por cerrar.</li><li>Se corrigen diferencias sin investigar, porque no hay tiempo de buscar la causa.</li></ul><p>Así, acabas con un stock que parece cuadrar, pero nunca sabes por qué se descuadró. Y al año siguiente repetirás el mismo ritual.</p><h2>Inventario permanente: otra forma de trabajar</h2><p>Un inventario permanente no es un lujo. Significa que cada entrada y salida de mercancía se registra en el momento. Cada venta, cada compra, cada devolución, cada baja por rotura. Así el sistema siempre sabe lo que deberías tener.</p><p>¿Eres una pyme de cinco empleados? También lo necesitas. No necesitas un gran sistema. Puedes empezar con una hoja de cálculo bien llevada o con la opción de gestión de stock de tu herramienta de facturación.</p><p>Cuando alguien rompe una bombona de cristal, no basta con barrer los restos. Hay que dar de baja esa referencia en el mismo momento. Si no, estás contando una mentira dentro de tu propia contabilidad.</p><h2>Recuento cíclico: contar poco, pero contar siempre</h2><p>El recuento físico no desaparece. Lo que cambia es la frecuencia.</p><p>En lugar de contar todo en diciembre, se cuentan determinadas referencias cada semana o cada mes.</p><p>Por ejemplo, escoges 20 referencias al azar. Cuentas lo que hay, lo comparas con lo registrado y apuntas la diferencia. Si hay un error grande, investigas.</p><p>Las ventajas son claras:</p><ul><li>No detienes el almacén.</li><li>Detectas errores pronto, cuando aún puedes corregirlos.</li><li>Descubres malas prácticas: robos internos, proveedores que mandan menos, personal que no escanea mercancías.</li><li>Al cierre del año no hay sorpresas, porque ya has ido ajustando.</li></ul><p>Se puede hacer con la plantilla que tienes. No necesitas más recursos, sino más constancia.</p><h2>La merma no se espera: se registra cuando ocurre</h2><p>Una merma no es un descubrimiento. Es un evento que sucede en un momento concreto. Y si no lo apuntas en ese momento, contaminas todos los meses siguientes.</p><p>Piensa en un almacén donde se pierde una garrafa de aceite cada dos meses. Si lo anotas el día que pasa, cada mes su resultado refleja ese coste. Si lo esperas al recuento anual, tu resultado de enero, febrero, marzo y abril parece mejor del que es. O mides la merma cuando pasa, o la mides a ciegas.</p><h2>No se trata de contar más, sino de conocer antes</h2><p>El recuento anual tiene sentido para empresas con pocos movimientos o sin equipo. Pero si tu empresa tiene cinco empleados y cincuenta referencias que se mueven a diario, anotar solo en diciembre es tarde.</p><p>Convierte la toma de inventario en una rutina. No hace falta contarlo todo de golpe: cuenta cada referencia varias veces al año, priorizando las que más se mueven o más valen.</p><blockquote>El objetivo no es contar y cuadrar. Es entender qué pasa con tu mercancía mientras pasa.</blockquote><p>Ese es el cambio de mentalidad.</p>
"""
    },
    {
        "slug": "como-elegir-un-erp-sin-equivocarse",
        "titulo": "Cómo elegir un ERP sin equivocarse",
        "descripcion": "Guía práctica para elegir ERP sin equivocarse. Qué preguntar sobre soporte, salida de datos, histórico y plazos, y por qué la demo genérica no sirve.",
        "fecha": "2026-09-02",
        "minutos": 7,
        "tema": "Sistemas",
        "acento": "marigold",
        "entradilla": "Deja de escuchar al comercial y empieza a preguntar qué pasa si todo se rompe. Estas son las cuestiones que evitan el error caro.",
        "cuerpo": """
<h2>La demo es un escaparate, no una prueba</h2><p>La demo que te enseñan suele estar preparada con datos limpios y un operador experto detrás. El software se comporta bien porque la escena está pensada para mostrar fortalezas y ocultar aristas. El problema aparece cuando intentas hacer algo con tus propias reglas de negocio.</p><p>Por ejemplo, en tu empresa puede ser normal servir un pedido en dos envíos, trabajar con clientes que pagan a 60 días y un comercial que cobra comisión por la factura cobrada, no por la emitida. En la demo eso no se ve. Pide una prueba con un caso tuyo. Si el vendedor se pone nervioso o te promete verlo más adelante, date por avisado: más adelante significa una ampliación del proyecto y una factura nueva.</p><blockquote>Si no puedes probar la parte que te duele antes de comprar, tampoco podrás arreglarla después sin pagar más.</blockquote><h2>¿Quién responde cuando algo falla de verdad?</h2><p>Firmas el contrato con el fabricante del software, pero la implantación la hace una consultora que desaparece al terminar el proyecto. Seis meses después tienes una incidencia con un asiento de IVA y el soporte te abre un ticket que nadie lee. Antes de firmar, pregunta por el nombre de la persona que se sienta delante cuando las cosas se tuercen.</p><p>Busca una situación concreta: es lunes, no puedes validar una factura porque el sistema da un error, y el lunes toca presentar el modelo. ¿A quién llamas? ¿Cuánto tarda en responder mañana? ¿Qué nivel de acceso tiene esa persona a tu sistema? Si te contestan con frases del tipo tenemos un servicio de incidencias, no te quedas con la frase. Pide que te describan el recorrido escrito: tu llamada, el centro de soporte, y qué pasa si en dos horas no está resuelto.</p><h2>Si te vas, ¿con qué datos sales?</h2><p>Todo ERP se termina. Puede durar diez años, pero se termina. Cuando llegue el momento, los datos no son un capricho: son tus facturas, tu contabilidad, tu stock, la historia de tus clientes. Si no pactas la salida antes de entrar, te encuentras con que sacar la información cuesta un dinero o que te dan un montón de tablas que solo entienden ellos.</p><p>Pregunta en la fase comercial lo siguiente: si un año no os renovamos el mantenimiento, ¿qué formato nos das para llevarnos nuestra información? ¿Un Excel sencillo con las facturas? ¿Una copia de la base de datos con su diccionario de tablas? ¿O un volcado que luego hay que interpretar con herramientas que no tenemos? Haz que lo dejen escrito en el contrato, porque la venta de software no incluye la liberación de datos. Esa parte se negocia y se paga.</p><h2>Qué queda de tus años en el sistema</h2><p>Cuando cambias de ERP, te enfrentas a algo que pocos comerciales mencionan: el histórico. Tu asesor o tu gestoría necesitan poder consultar los cierres de los últimos ejercicios, localizar una factura de hace tres años o responder a una notificación de Hacienda sobre un período ya cerrado. No todo ese bloque se puede congelar y dejarlo en una carpeta.</p><p>Lo que funciona en la práctica es hablar antes con tu asesor fiscal y preguntarle qué datos necesita conservar como mínimo: asiento de apertura, listados de cierre, detalle de deudas con proveedores, movimientos de bancos. No intentes meter en el ERP nuevo los últimos diez años de albaranes. Mete solo lo que sea consultable y verificable, y guarda el resto en una copia a la que se pueda volver.</p><h2>La implantación vuelve a empezar cuando termina</h2><p>El comercial dibuja un calendario con semanas y fechas de entregas. Ese calendario suele terminar el día en que el sistema queda técnicamente instalado. Pero lo que tú necesitas es el día en que tu equipo deja de rellenar las mismas cosas en dos sitios distintos y la contabilidad cuadra con lo que dice el software.</p><p>Por eso, pide el plan de proyecto con responsables y entregables. Quién valida que la factura sale con el IVA correcto y que el cliente lo recibe en su correo. En qué momento se acepta un informe de impuestos. Cómo se prueba que una incidencia del mes anterior se refleja en la contabilidad sin duplicar asientos. El plazo de verdad no son las semanas de instalación: es el tiempo que pasa hasta que ya no tienes que comprobar en Excel si lo que ha hecho el sistema es correcto.</p><ul><li>Pide el nombre de la persona que responde en el día que se rompe el calendario.</li><li>Pide la lista de entregables que definen el final del proyecto, no una fecha.</li><li>Pide que te escriban cómo se queda delimitado el soporte cuando el sistema sea tuyo.</li></ul><h2>El contrato manda, pero la conversación manda más</h2><p>Al final, un ERP no es una herramienta cualquiera. Es un socio técnico que se sienta en la mesa de tu administración. Un mal socio se conoce cuando aparecen las obligaciones: un modelo, un pago a la Seguridad Social, una respuesta que hay que dar ante un requerimiento. Ese día descubres si compraste una solución o un problema.</p><p>No hace falta ser informático para elegir bien. Hace falta preguntar qué pasa cuando algo falla, y no quedarse con la respuesta que toca de memoria. La buena respuesta es concreta, no viene de un guion e incluye la palabra cómo, y no solo la palabra sí.</p>
"""
    },
    {
        "slug": "que-mira-hacienda-cuando-pide-los-libros",
        "titulo": "Qué mira Hacienda cuando pide los libros",
        "descripcion": "Resumen de qué revisa Hacienda al requerir la contabilidad: numeración, cuadre con modelos, gastos justificados y trazabilidad del apunte. Consejos para estar",
        "fecha": "2026-09-02",
        "minutos": 7,
        "tema": "Fiscalidad",
        "acento": "cielo",
        "entradilla": "Si Hacienda te pide los libros, no basta con tenerlos: tienes que saber cómo los va a leer.",
        "cuerpo": """
<h2>Primero: ¿qué son "los libros" para Hacienda?</h2><p>Cuando un inspector pide "los libros", no se conforma con el Libro Diario. Quiere ver toda la documentación que sostiene la contabilidad. Hablamos de facturas emitidas y recibidas, extractos bancarios, contratos, tickets, justificantes de pago, y cualquier papel que explique un movimiento.</p><p>A ti te suena a archivo. Para Hacienda es una cadena: cada apunte contable debe enlazar con un documento, y ese documento debe ser válido. La revisión no es aleatoria: busca huecos, saltos y contradicciones.</p><h2>La numeración: facturas sin saltos</h2><p>Lo primero que miran es si las facturas están correlativas. Emites la factura 12 y la siguiente es la 14. ¿Dónde está la 13? Puede que la anularas. Pero si no has guardado la factura anulada y su justificante, parecerá que ocultas una venta.</p><p>Lo mismo pasa con las recibidas: entra una factura de un proveedor y luego otra con número anterior. Si tu proveedor se ha equivocado de serie, mal asunto si no puedes explicarlo.</p><p>Un error común en las pymes es tener dos talonarios o usar el mismo número en el programa dos veces porque uno se borró. Si al imprimir la factura falló y la reimprimiste con otro número, la primera copia, aun rota, debe conservarse.</p><p>La regla es sencilla: toda la numeración, incluidos huecos y anulaciones, debe estar documentada. Si no, Hacienda puede presumir que hay ventas no declaradas que financian gastos personales.</p><h2>El cuadre entre libros y modelos</h2><p>Después mira si lo que declaraste en los modelos coincide con lo que reflejan tus libros. El ejemplo clásico es el IVA.</p><p>Si en el modelo 303 del primer trimestre declaraste 12.000 euros de base imponible de ventas, tu libro de facturas emitidas tiene que sumar esa misma cantidad. Y tu libro de gastos debe justificar las cuotas deducibles que te restaste.</p><p>No hace falta que todo cuadre a céntimo porque haya ajustes, pero debes poder explicar cada diferencia. Si aparece un gasto de 1.000 euros en el libro y en la declaración del IVA te dedujiste 210 euros, ¿qué factura es esa? Si no la encuentras, el gasto se puede caer entero.</p><p>También revisan el IRPF: los pagos a cuenta, las retenciones de empleados y profesionales. Es muy fácil desviarse un mes y no actualizar el libro. Cuando llega el requerimiento, cada falta de concordancia se convierte en una sospecha: cobras facturas que no declaras o pagas gastos personales desde la empresa.</p><h2>Gastos deducibles: la factura no basta</h2><p>Aquí la gente se confía. Creen que por tener una factura ya es deducible. Hacienda mira el contenido, no solo el papel.</p><p>Una factura de un restaurante a nombre de la empresa, con NIF y domicilio, puede no valer si es una comida de cumpleaños con amigos. ¿Cómo lo sabe el inspector? Porque tiene criterios: qué día es, cuántos asistentes pone en el ticket, si el gasto es recurrente, si está relacionado con clientes o proveedores reales.</p><p>Para que un gasto sea deducible tiene que estar justificado en cuanto a su necesidad para la actividad. No vale "era una comida con un posible cliente" si no hay un correo, un contrato o una agenda que lo respalde.</p><p>Otro ejemplo claro: el carburante. Hacienda admite el gasto de gasoil si el vehículo está afecto a la actividad. Pero si usas el mismo coche para todo, la deducción puede ser parcial. Si no llevas un registro de kilómetros o del uso, el inspector aplicará prudencia y te lo podrá quitar.</p><p>También vigilan las facturas de proveedores que están en paraísos fiscales o que son poco conocidos. No es que estén prohibidas, pero la carga de la prueba la tienes tú: tienes que demostrar que el servicio existió y que su precio era de mercado.</p><h2>El rastro de cada apunte hasta su documento</h2><p>Imagina que en tu libro contable hay un asiento: "Gastos de oficina" 300 euros. El inspector pide su justificación. Si tardas cuatro semanas en encontrar la factura, te lo anotará en el acta.</p><p>Peor si el apunte se generó porque el banco te pasó un recibo de un seguro y lo contabilizaste sin saber qué era. Cuando piden la póliza, no la encuentras, y el recibo no dice qué cubre. El gasto se convierte en no deducible porque no puedes acreditar su origen.</p><p>Hacienda no solo mira que exista un papel. Mira que el papel corresponda al asiento. Si el asiento dice "pago a proveedor" con 500 euros, y el extracto bancario dice 450 porque te hicieron un descuento, tiene que estar anotado ese descuento. Si no, no cuadra.</p><p>Los apuntes deben tener una trazabilidad completa: cuándo se registró, de qué factura viene, cómo se pagó, y si el pago fue en metálico, qué justificante hay. En operaciones de más de 3.000 euros, el pago en efectivo ya no es deducible. Esa norma sigue dando sorpresas a muchos.</p><h2>Antes de que llegue el requerimiento</h2><p>No esperes a la carta. Haz una revisión anual de tus libros aunque no tengas obligación de auditoría. Puedes hacerla en enero, antes de presentar el último trimestre.</p><p>Revisa que cada factura emitida tenga su número correlativo. Guarda las anuladas con su motivo. Comprueba que las facturas recibidas tienen NIF, domicilio, base e IVA bien desglosado. Si una no pasa el filtro, no la contabilices como deducible; o pide otra al proveedor antes de cerrar el ejercicio.</p><p>Concilia los extractos bancarios con tu libro de gastos. Una vez al mes basta. Cada movimiento del banco debe tener su asiento o su explicación. Si te sobra un recibo domiciliado sin identificar, es un foco de problema.</p><p>Digitaliza todo. No sirve de nada tener la contabilidad en un programa si el justificante está en una caja llena de papeles. Necesitas localizar cualquier factura en menos de cinco minutos. Escaneada y nombrada por fecha y proveedor, perfecto.</p><p>Aprovecha también para revisar si has incluido gastos personales entre los de la empresa. Es más frecuente de lo que parece: un viaje, una comida, un capricho con tarjeta de empresa. No pasa nada si lo detectas y lo sacas a tiempo. Pasa mucho si lo detecta Hacienda y te lo considera una retribución no declarada.</p><blockquote>La mejor respuesta a un requerimiento no es una defensa brillante: es llegar antes con los papeles en orden.</blockquote><p>Cuando recibas la notificación, respira y actúa con método. Reúne los libros obligatorios, las facturas, los extractos y los contratos. Mira si el requerimiento menciona períodos concretos o conceptos específicos. Si algo no cuadra, no intentes esconderlo: explícalo en un escrito con la documentación que lo aclare.</p><p>Y una última advertencia: la contabilidad no es un trámite. Es la memoria de tu empresa. Si la llevas con orden, no tendrás que sudar cuando Hacienda llame a la puerta.</p>
"""
    },
    {
        "slug": "facturar-mucho-y-ganar-poco",
        "titulo": "Facturar mucho y ganar poco",
        "descripcion": "Por qué subir la facturación no garantiza ganar dinero. Cómo calcular margen bruto, margen de contribución y umbral de rentabilidad con un ejemplo realista.",
        "fecha": "2026-09-02",
        "minutos": 7,
        "tema": "Gestión",
        "acento": "marigold",
        "entradilla": "Que este año factures más que el pasado no significa que vaya bien. Hay una distancia entre vender mucho y quedarte con algo.",
        "cuerpo": """
<h2>Ingresar no es ganar</h2><p>Un empresario me dijo una vez: "no entiendo nada, cada año vendemos más y no veo el dinero". Le pedí ver los números, no la facturación. La facturación es una foto de la actividad, no de la salud del negocio. Puedes mover mucho dinero y perder en cada operación.</p><p>La cuenta clásica es sencilla: lo que cobras menos lo que gastas. Si al final del año te queda algo, hay beneficio. Si no te queda, da igual lo que hayas facturado. Esa es la única pregunta que importa.</p><h2>Margen bruto: la primera prueba</h2><p>Los gastos no son todos iguales. Algunos cambian con cada venta: comprar mercancía, pagar a un subcontratista, el transporte de una entrega. Se llaman costes variables. Si vendes más, estos costes suben.</p><p>Piensa en un servicio que vendes por 100 euros. Para hacerlo necesitas materiales o trabajo externo por 70. Esos 70 son coste variable. Los otros 30 son tu margen bruto. Ese margen tiene que pagar todo lo demás y, si sobra algo, tu beneficio.</p><p>Si vendes un producto por menos de lo que te cuesta producirlo, cada pedido te acerca a la ruina. Puede sonar obvio, pero hay empresas que durante meses venden con margen negativo para ganar clientes. La facturación sube. El agujero también.</p><h2>Costes fijos: los que están aunque no vendas</h2><p>Luego están los costes fijos: el alquiler, los sueldos del personal estable, la luz, el teléfono, el software que usas. Estos existen aunque un mes no factures nada.</p><p>Cuando miras solo la facturación es fácil olvidarlos. Todo lo que entra parece ganancia. Pero primero hay que pagar las facturas de la casa, la nómina del administrativo, el seguro del local. De lo que queda, solo eso es tuyo.</p><h2>Margen de contribución: lo que de verdad aporta una venta</h2><p>Hay una manera más limpia de ver cada venta. El margen de contribución es lo que te queda de un ingreso después de pagar sus costes variables. Es el dinero que esa venta aporta para cubrir los costes fijos.</p><p>Por ejemplo, vendes un proyecto por 1.000 euros. Entre materiales y horas externas te gastas 600. Tu margen de contribución son 400 euros. Eso es lo que te ayuda a pagar el alquiler, la oficina y tus propias horas.</p><p>Si tienes cincuenta productos, no todos aportan lo mismo. Algunos tienen un margen del 40 %. Otros apenas del 5 %. Una empresa puede facturar mucho con los de margen pequeño y no darse cuenta hasta final de año.</p><h2>Umbral de rentabilidad: cuándo empiezas a ganar</h2><p>El umbral de rentabilidad es el punto donde lo que vendes cubre exactamente todos los costes. Ni ganas ni pierdes. A partir de ahí, empiezas a ganar.</p><p>Se calcula así: divide los costes fijos entre el margen de contribución de cada venta. Si tus costes fijos son 12.000 euros al mes y cada venta aporta un margen de 400, necesitas 30 ventas al mes para no perder dinero.</p><p>Ese número es tu suelo. Si haces 25 ventas, pierdes. Si haces 31, empiezas a ver beneficio. Muchas empresas crecen por debajo de su propio umbral sin saberlo. Suben las ventas, pero nunca pasan de la línea.</p><h2>Un ejemplo típico: crecer y perder dinero</h2><p>Imagina una empresa que presta servicios informáticos. Para crecer, acepta proyectos con descuentos. Cada proyecto exige contratar a un autónomo externo. La empresa factura 120 euros hora y paga 90 al autónomo. Margen de contribución: 30 euros por hora.</p><p>El dueño está contento porque factura más cada mes. Para atender tanto trabajo contrata a un administrativo. Eso añade 1.500 euros al mes de coste fijo. También cambia de local, otros 800 euros más.</p><p>Antes necesitaba un volumen de horas para cubrir sus costes. Ahora necesita más horas. Pero cada hora nueva deja menos margen porque ha bajado los precios para conseguirla. Resultado: factura el doble que hace dos años y pierde dinero cada mes.</p><p>Quizá pienses que esto no te pasa a ti. Pero hay una versión más sencilla: una tienda que vende más unidades con promociones. Un taller que factura más horas pero con más piezas caras de las que apenas saca margen. Un restaurante que llena el local con un menú de precio bajo que no cubre los costes.</p><h2>Vende, pero mira con lupa</h2><p>Si quieres saber si un negocio va bien, deja de mirar totales y mira líneas concretas. Pregúntate por cada producto o servicio:</p><ul><li>¿Cuánto me cuesta en materiales, subcontratación y comisiones?</li><li>¿Qué margen de contribución me deja?</li><li>¿Cuántas unidades necesito vender al mes para cubrir mis costes fijos?</li></ul><p>Hay clientes que dan un margen excelente y otros que solo quitan tiempo. Hay servicios que parecen estratégicos y no dejan un euro. Si no lo sabes, estás tomando decisiones a ciegas.</p><h2>La diferencia entre facturar y cobrar</h2><p>Otra trampa es confundir facturación con dinero en la cuenta. Puedes haber facturado mucho pero no haber cobrado. Si un cliente no paga, el beneficio existe en el papel, no en el banco.</p><p>El margen de contribución se calcula sobre el ingreso, no sobre el cobro. Por eso conviene vigilar también los impagos. Un beneficio que solo existe en facturas impagadas no paga nóminas.</p><h2>Entonces, ¿qué haces?</h2><p>Lo primero es poner en una hoja tus costes fijos mensuales. Lo segundo, calcular el margen de contribución de cada cosa que vendes. Lo tercero, averiguar cuántas ventas necesitas para cubrir los fijos.</p><p>Si descubres que estás por debajo, tienes dos caminos: subir precios o reducir costes. Ninguno es agradable, pero son los únicos que sostienen un negocio a largo plazo.</p><p>No hace falta ser un contable para entenderlo. Hace falta dejar de mirar la facturación como un trofeo y empezar a mirarla como un mapa. Un mapa no te dice dónde estás ganando ni dónde estás perdiendo. Eso te lo dice el margen.</p><blockquote><p>No hay negocio bueno con margen malo. Hay mucha facturación para poco beneficio, y tarde o temprano la facturación sube y el banco baja.</p></blockquote><p>La próxima vez que alguien diga "facturamos mucho", pregunta cuánto margen queda. Esa es la única cifra que pagará tus facturas y tu sueldo.</p>
"""
    },
    {
        "slug": "modelos-que-presenta-una-pyme-cada-ano",
        "titulo": "Los modelos que presenta una pyme cada año",
        "descripcion": "303, 111, 115, 130, 349, 347, 390, 190 y 200: qué es cada modelo, cuándo se presenta y de dónde salen los datos. Un calendario claro para empresarios que no.",
        "fecha": "2026-09-02",
        "minutos": 9,
        "tema": "Fiscalidad",
        "acento": "cielo",
        "entradilla": "Nadie monta una empresa para aprenderse los modelos de Hacienda. Pero conviene saber cuáles te tocan y de dónde sale cada número.",
        "cuerpo": """
<h2>Los trimestrales</h2>
<p>Son los que marcan el ritmo del año. Se presentan en los veinte primeros días de abril, julio y octubre, y el del cuarto trimestre en enero.</p>
<ul>
  <li><strong>Modelo 303: IVA.</strong> La diferencia entre el IVA que has repercutido en tus facturas y el que has soportado en las compras. Sale directo del libro de facturas emitidas y recibidas: si la contabilidad está al día, el 303 ya está hecho.</li>
  <li><strong>Modelo 111: retenciones de IRPF.</strong> Lo que has retenido a trabajadores y a profesionales que te facturan con retención. Sale de las nóminas y de las facturas recibidas de autónomos.</li>
  <li><strong>Modelo 115: retenciones por alquiler.</strong> Solo si alquilas local u oficina y practicas retención al arrendador.</li>
  <li><strong>Modelo 130: pago fraccionado de IRPF.</strong> Para autónomos en estimación directa. Una sociedad no lo presenta.</li>
  <li><strong>Modelo 349: operaciones intracomunitarias.</strong> Si compras o vendes a otros países de la UE. Su periodicidad depende del volumen.</li>
</ul>

<h2>Los anuales</h2>
<ul>
  <li><strong>Modelo 390: resumen anual de IVA.</strong> En enero. Es la suma de los cuatro 303, y por eso cuadra o no cuadra: si durante el año hubo correcciones que no se rehicieron, aquí salta.</li>
  <li><strong>Modelo 190: resumen anual de retenciones.</strong> También en enero, y hace el mismo papel respecto a los 111.</li>
  <li><strong>Modelo 347: operaciones con terceros.</strong> En febrero. Declara a quién le has comprado o vendido más de 3.005,06 € en el año. Es el que más discrepancias genera, porque la otra parte declara lo mismo desde su lado y los importes tienen que casar.</li>
  <li><strong>Modelo 200: Impuesto de Sociedades.</strong> Para ejercicios que cierran el 31 de diciembre, se presenta en julio.</li>
</ul>

<h2>Por qué casi todos los errores vienen del mismo sitio</h2>
<p>Los modelos no se rellenan: se calculan. Cada casilla sale de un dato que ya está en la contabilidad. Cuando algo falla, casi nunca es que alguien haya escrito mal un número en el formulario: es que el dato de origen estaba mal clasificado.</p>
<p>Los tres casos que más se repiten:</p>
<ul>
  <li>Una factura de proveedor clasificada en la cuenta equivocada, que mete un IVA soportado donde no toca.</li>
  <li>Un profesional al que se le paga sin practicar la retención que le corresponde.</li>
  <li>Una operación intracomunitaria tratada como nacional, que descuadra el 349 y arrastra al 303.</li>
</ul>

<h2>La consecuencia práctica</h2>
<p>Si la contabilidad está al día y bien clasificada, los modelos son casi automáticos. Si no lo está, cada trimestre se convierte en una semana de revisar hacia atrás. Ahí es donde se va el tiempo: no en presentar, en cuadrar antes de presentar.</p>
<p>Por eso tiene sentido que el sistema que lleva las facturas sea el mismo que prepara los modelos. Cada traspaso de datos entre programas (o de la empresa a la asesoría por correo) es una oportunidad de que algo se pierda o llegue tarde.</p>

<blockquote>Este artículo es una guía general. Los plazos y las obligaciones concretas dependen de tu situación: confírmalos siempre con tu asesor.</blockquote>
"""
    },
    {
        "slug": "cambiar-de-asesoria-sin-perder-el-historico",
        "titulo": "Cambiar de asesoría sin perder el histórico",
        "descripcion": "Qué documentación tienes derecho a llevarte, en qué momento del año conviene cambiar y cómo evitar quedarte sin poder consultar los años anteriores.",
        "fecha": "2026-09-02",
        "minutos": 6,
        "tema": "Asesoría",
        "acento": "marigold",
        "entradilla": "El miedo a cambiar de asesoría casi nunca es al asesor nuevo. Es a quedarse sin los papeles de los cinco años anteriores.",
        "cuerpo": """
<h2>Lo que es tuyo y te puedes llevar</h2>
<p>La documentación contable y fiscal de tu empresa es tuya, la tenga quien la tenga. Antes de cerrar la relación conviene pedir por escrito y comprobar que llega:</p>
<ul>
  <li>Los <strong>libros contables</strong> del ejercicio en curso y de los anteriores, en un formato que se pueda abrir sin el programa de la asesoría.</li>
  <li>Los <strong>modelos presentados</strong> con su justificante de presentación.</li>
  <li>El <strong>balance de sumas y saldos</strong> a la fecha del traspaso, con el detalle que compone cada saldo.</li>
  <li>Las <strong>cuentas anuales</strong> depositadas y los libros legalizados.</li>
  <li>Los <strong>datos maestros</strong>: clientes, proveedores y su histórico de operaciones.</li>
</ul>

<h2>El momento del año importa</h2>
<p>El cambio limpio es a cierre de ejercicio: los saldos están cerrados y el asesor nuevo arranca con un punto de partida sin ambigüedad. El segundo mejor momento es a cierre de trimestre, con los modelos ya presentados.</p>
<p>Cambiar a mitad de trimestre es posible, pero obliga a repartir la responsabilidad de un mismo periodo entre dos despachos, y ahí es donde se cuelan los huecos.</p>

<h2>Las tres preguntas que conviene hacer antes de firmar</h2>
<ul>
  <li><strong>¿Quién firma y presenta?</strong> Conviene saber el nombre de la persona colegiada que asume la responsabilidad, no solo el del despacho.</li>
  <li><strong>¿En qué formato me devolveréis los datos si algún día me voy?</strong> Si la respuesta es vaga, ya sabes cómo será la salida.</li>
  <li><strong>¿Qué pasa si Hacienda requiere algo de un año que llevabais vosotros?</strong> Debe estar claro por escrito quién responde y hasta cuándo.</li>
</ul>

<h2>El error más caro: no solapar</h2>
<p>Cortar con la asesoría antigua el mismo día que empieza la nueva deja un periodo sin nadie que responda. Merece la pena solapar unas semanas, aunque cueste, para que quien se va pueda aclarar dudas de lo que hizo.</p>
<p>Es el mismo principio que en una migración de sistema: la convivencia temporal no es un lujo, es lo que evita el agujero.</p>

<blockquote>Este artículo es orientativo y no sustituye al criterio de un profesional sobre tu caso concreto.</blockquote>
"""
    },
    {
        "slug": "migrar-de-odoo-sin-parar-la-empresa",
        "titulo": "Migrar de Odoo sin parar la empresa",
        "descripcion": "Qué mirar antes de cambiar de ERP: el traspaso de datos con histórico, el periodo de convivencia y el punto de retorno. Una guía práctica para pymes.",
        "fecha": "2026-09-02",
        "minutos": 7,
        "tema": "Migración",
        "acento": "marigold",
        "entradilla": "El día del cambio la empresa tiene que seguir facturando. Todo lo demás se puede planificar; eso no se puede parar.",
        "cuerpo": """
<h2>El error de plantearlo como un corte</h2>
<p>La mayoría de las migraciones se plantean como un salto: el viernes se apaga el sistema viejo, el lunes se enciende el nuevo. Suena limpio y casi nunca lo es. Los datos tardan más de lo previsto, aparecen casos que nadie contempló, y el lunes hay que facturar igual.</p>
<p>La alternativa es tratar la migración como un periodo, no como un instante. Durante unas semanas los dos sistemas coexisten: el antiguo en solo lectura, para consultar y comparar; el nuevo operando. Nadie se queda sin poder mirar un dato del año pasado.</p>

<h2>Los datos se traen con su histórico</h2>
<p>Hay una tentación grande al migrar: arrancar con saldos iniciales y olvidarse del pasado. Es rápido y es un error caro. En cuanto llega la primera reclamación de un cliente sobre una factura de hace dos años, alguien tiene que volver a levantar el sistema viejo.</p>
<p>Lo que conviene traer completo:</p>
<ul>
  <li><strong>Clientes y proveedores</strong> con sus datos fiscales y su histórico de operaciones.</li>
  <li><strong>Artículos</strong> con referencias, incluidas las referencias que usa cada cliente, que suelen vivir en la cabeza de comercial.</li>
  <li><strong>Saldos contables</strong> con el detalle que los compone, no solo el total.</li>
  <li><strong>Facturas emitidas y recibidas</strong> del ejercicio en curso y del anterior, como mínimo.</li>
</ul>

<h2>El punto de retorno se define antes, no a mitad</h2>
<p>Antes de empezar hay que escribir tres cosas: qué condiciones harían abortar la migración, quién toma esa decisión, y cuánto se tarda en volver atrás. Si esas tres respuestas no existen por escrito, la vuelta atrás se improvisa el peor día posible.</p>

<h2>El equipo practica antes, con datos reales</h2>
<p>Formar al equipo con datos de ejemplo no sirve de mucho. Las dudas reales aparecen con los casos reales: el cliente que factura a tres sedes, el artículo que se vende por unidades y se compra por cajas, el proyecto que se imputa a dos centros de coste.</p>
<p>Un entorno de pruebas cargado con una copia de los datos de verdad resuelve la mayoría de esas dudas antes de que cuesten dinero.</p>

<h2>Señales de que todavía no toca migrar</h2>
<p>No todo problema con un ERP se arregla cambiándolo. Si lo que falla es que nadie ha definido los procesos, el sistema nuevo va a heredar el mismo desorden en tres meses. Y si el equipo está en plena temporada alta, la migración va a competir con el trabajo real y va a perder.</p>
"""
    },
    {
        "slug": "senales-de-que-tu-erp-se-esta-degradando",
        "titulo": "Siete señales de que tu ERP se está degradando",
        "descripcion": "Los ERP no fallan de golpe: se degradan. Siete síntomas concretos que aparecen antes de que el sistema deje de ser fiable, y qué hacer con cada uno.",
        "fecha": "2026-09-02",
        "minutos": 6,
        "tema": "Diagnóstico",
        "acento": "coral",
        "entradilla": "Un ERP rara vez se cae. Lo que hace es dejar de ser fiable poco a poco, y eso no dispara ninguna alarma.",
        "cuerpo": """
<h2>1. Hay informes que solo sabe sacar una persona</h2>
<p>Cuando el cierre mensual depende de que alguien concreto esté disponible, el sistema ya tiene un problema de diseño. No es una cuestión de formación: es que el camino para llegar al dato no está donde debería.</p>

<h2>2. Nadie sabe explicar por qué está puesto un módulo</h2>
<p>Se instaló para un caso puntual hace tres años, ese caso ya no existe, y el módulo sigue ahí. Cada uno de esos módulos añade campos, permisos y comportamientos que alguien tendrá que entender el día que algo falle.</p>

<h2>3. El equipo lleva un Excel paralelo</h2>
<p>Es la señal más honesta de todas. Si alguien mantiene una hoja aparte, es que el sistema no le da lo que necesita. Merece la pena preguntar qué hay en esa hoja antes de pedirle que la deje.</p>

<h2>4. Aparecen facturas sin enviar y nadie se ha dado cuenta</h2>
<p>Los errores silenciosos son los peligrosos. Un envío que falla y no avisa, un proceso nocturno que dejó de ejecutarse, una cola que se llenó. El sistema sigue funcionando de cara al usuario mientras acumula deuda por detrás.</p>

<h2>5. Los datos maestros están duplicados</h2>
<p>El mismo cliente dado de alta tres veces con tres grafías. En cuanto eso pasa, cualquier informe agregado miente, y nadie sabe cuánto.</p>

<h2>6. Actualizar da miedo</h2>
<p>Si nadie se atreve a subir de versión porque no se sabe qué personalizaciones se romperán, el sistema ya está congelado. Y un sistema congelado acumula riesgo de seguridad además de deuda funcional.</p>

<h2>7. Cada cambio pequeño requiere un presupuesto</h2>
<p>Cuando añadir un campo o cambiar un informe pasa por un tercero y tarda semanas, la organización deja de pedir cambios. El sistema no mejora, y la gente se adapta trabajando fuera de él. Vuelve el punto 3.</p>

<h2>Qué hacer con esto</h2>
<p>Ninguna de estas señales, por sí sola, obliga a cambiar de sistema. Tres o cuatro juntas suelen significar que el coste de mantener ya supera al de sustituir. Antes de decidir, conviene poner número a dos cosas: cuántas horas al mes se van en trabajo manual que el sistema debería hacer, y cuánto se tarda hoy en responder a una pregunta que debería ser inmediata.</p>
"""
    },
    {
        "slug": "que-deberia-hacer-la-ia-en-un-erp",
        "titulo": "Qué debería hacer la IA en un ERP (y qué no)",
        "descripcion": "La IA en gestión empresarial es útil en dos sitios concretos: enseñar los datos sin menús y ejecutar tareas rutinarias con permiso. Dónde ayuda de verdad y.",
        "fecha": "2026-09-02",
        "minutos": 8,
        "tema": "Inteligencia artificial",
        "acento": "cielo",
        "entradilla": "El problema de la mayoría de los ERP no es que les falten datos. Es que hay que saber por dónde sacarlos.",
        "cuerpo": """
<h2>Donde la IA ayuda de verdad: llegar al dato</h2>
<p>Un ERP mediano tiene cientos de pantallas. La información está dentro, pero llegar a ella exige conocer la estructura del programa, no la del negocio. Quien pregunta «¿qué clientes me deben más de 60 días y además tienen pedidos abiertos?» está haciendo una pregunta de negocio, y tiene que traducirla a dos informes y un cruce manual.</p>
<p>Ahí es donde una IA cambia las cosas de verdad: recibe la pregunta en lenguaje natural, sabe qué tablas tocar, cruza lo que haga falta y devuelve la respuesta. No es magia, es quitar la traducción.</p>

<h2>El segundo sitio: el trabajo repetitivo</h2>
<p>Hay tareas que se hacen igual todos los meses y consumen horas: conciliar movimientos bancarios evidentes, mandar recordatorios de cobro, generar asientos periódicos, clasificar gastos recurrentes. Son trabajos donde el criterio ya está definido y lo único que falta es ejecutarlo.</p>

<h2>La regla que no se puede saltar: enseñar antes de hacer</h2>
<p>Aquí está la diferencia entre una herramienta útil y un riesgo. Cualquier acción que modifique datos (enviar, contabilizar, cambiar un estado) tiene que enseñarse antes de ejecutarse. Qué va a hacer, sobre qué registros y con qué efecto.</p>
<blockquote>Una IA que actúa sin enseñar lo que va a hacer no es automatización: es un error esperando a que alguien lo descubra en el cierre.</blockquote>

<h2>Donde la IA no debe entrar</h2>
<ul>
  <li><strong>Decisiones con criterio contable o fiscal.</strong> Puede preparar y proponer, pero la responsabilidad es de una persona.</li>
  <li><strong>Cierres y liquidaciones.</strong> Nada que se presente ante la administración debería salir sin revisión humana.</li>
  <li><strong>Inventar datos que no tiene.</strong> Si un dato no está, la respuesta correcta es «no lo tengo», no una estimación con aspecto de dato.</li>
</ul>

<h2>Cómo evaluarla antes de comprarla</h2>
<p>Tres preguntas sirven para separar lo real de la demo bonita:</p>
<ul>
  <li>¿Puede decir <em>de dónde</em> ha sacado cada cifra, con el registro concreto?</li>
  <li>¿Qué pasa cuando le preguntas algo que no puede responder?</li>
  <li>¿Qué acciones puede ejecutar sin confirmación, exactamente?</li>
</ul>
<p>Si a la tercera pregunta la respuesta no es una lista corta y clara, conviene desconfiar.</p>
"""
    },
]

ACENTOS = {"marigold": "#ffb110", "coral": "#f64932", "cielo": "#62aef0",
           "verde": "#2FBF9B", "medianoche": "#02093a"}

import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import plantilla as P
import calendario_blog as CAL

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

MARCA_SVG = P.MARCA_SVG
MARCA_BLANCA = P.MARCA_BLANCA
cabecera = P.cabecera
pie = P.pie

# Lo unico que el blog no comparte: el articulo y su tarjeta.
ESTILOS_BLOG = '''
article.post{padding:44px 0 80px}
.post .meta{display:flex;gap:14px;align-items:center;flex-wrap:wrap;margin:18px 0 26px;font-size:14px;color:var(--piedra)}
.tema{border-radius:var(--r-pill);padding:3px 12px;font-size:13px;font-weight:500;color:#000}
.post .entradilla{font-family:var(--serif);font-size:21px;line-height:1.55;color:var(--grafito);margin-bottom:8px}
.post .cuerpo p{margin:0 0 16px;color:var(--grafito);font-size:17px;line-height:1.65}
.post .cuerpo strong{color:var(--tinta-fuerte);font-weight:600}
.post .cuerpo ul{margin:0 0 18px;padding-left:22px;color:var(--grafito);font-size:17px;line-height:1.65}
.post .cuerpo li{margin-bottom:8px}
.post .cuerpo blockquote{margin:24px 0;padding:20px 24px;background:var(--blanco);border:1px solid var(--borde);border-radius:var(--r-card);font-family:var(--serif);font-size:19px;line-height:1.5;color:var(--tinta-fuerte)}
.cierre-post{margin-top:44px;background:var(--blanco);border:1px solid var(--borde);border-radius:var(--r-card);padding:28px}
.cierre-post h3{margin-bottom:8px}
.cierre-post p{color:var(--grafito);margin-bottom:18px}
.post-card{background:var(--blanco);border:1px solid var(--borde);border-radius:var(--r-card);overflow:hidden;text-decoration:none;color:inherit;display:grid;transition:transform .22s ease,border-color .22s ease}
.post-card:hover{transform:translateY(-4px);border-color:rgba(0,0,0,.18)}
.post-card .franja{height:7px}
.post-card .dentro{padding:22px}
.post-card .tema{display:inline-block;margin-bottom:12px}
.post-card .post-tit{margin:0 0 8px;font-size:19px;font-weight:700;line-height:1.3;letter-spacing:0;color:var(--tinta-fuerte)}
.post-card p{font-size:15px;color:var(--grafito)}
.post-card .pie{margin-top:14px;font-size:13px;color:var(--piedra)}
'''


def pagina(titulo, descripcion, url, cuerpo, extra_head="", base=""):
    return P.pagina(titulo, descripcion, url, cuerpo,
                    extra_head=extra_head, base=base, extra_css=ESTILOS_BLOG)


def construir_articulo(a):
    url = "%s/blog/%s.html" % (DOMINIO, a["slug"])
    color = ACENTOS[a["acento"]]
    ld = '''<script type="application/ld+json">
{
  "@context":"https://schema.org","@type":"Article",
  "headline":"%s","description":"%s",
  "datePublished":"%s","dateModified":"%s","inLanguage":"es",
  "mainEntityOfPage":{"@type":"WebPage","@id":"%s"},
  "author":{"@type":"Organization","name":"Contaes","url":"%s/"},
  "publisher":{"@type":"Organization","name":"Contaes","url":"%s/"}
}
</script>
<script type="application/ld+json">
{
  "@context":"https://schema.org","@type":"BreadcrumbList",
  "itemListElement":[
    {"@type":"ListItem","position":1,"name":"Inicio","item":"%s/"},
    {"@type":"ListItem","position":2,"name":"Blog","item":"%s/blog/"},
    {"@type":"ListItem","position":3,"name":"%s"}
  ]
}
</script>''' % (a["titulo"], a["descripcion"], a["fecha"], a["fecha"], url,
                DOMINIO, DOMINIO, DOMINIO, DOMINIO, a["titulo"])

    otros = [o for o in ARTICULOS if o["slug"] != a["slug"]][:2]
    tarjetas = "\n".join(
        '<a class="post-card" href="%s.html"><span class="franja" style="background:%s"></span>'
        '<span class="dentro"><span class="tema" style="background:%s">%s</span>'
        '<h2 class="post-tit">%s</h2><p>%s</p></span></a>'
        % (o["slug"], ACENTOS[o["acento"]], ACENTOS[o["acento"]], o["tema"], o["titulo"], o["descripcion"][:110] + "…")
        for o in otros)

    cuerpo = f'''<article class="post">
  <div class="wrap estrecho">
    <p class="migas"><a href="/">Inicio</a> · <a href="/blog/">Blog</a></p>
    <span class="tema" style="background:{color}">{a["tema"]}</span>
    <h1 style="margin-top:14px">{a["titulo"]}</h1>
    <div class="meta"><time datetime="{a['fecha']}">2 de septiembre de 2026</time><span>·</span><span>{a["minutos"]} min de lectura</span></div>
    <p class="entradilla">{a["entradilla"]}</p>
    <div class="cuerpo">{a["cuerpo"]}</div>

    <div class="cierre-post revela">
      <h3>Contaes es un ERP con IA para pymes</h3>
      <p>Está en desarrollo. Si te interesa lo que cuenta este artículo, escríbenos y te avisamos cuando haya algo que enseñar.</p>
      <a class="btn btn-azul" href="/#contacto">Pedir una demo <span class="flecha" aria-hidden="true">&rarr;</span></a>
    </div>
  </div>

  <div class="wrap" style="margin-top:56px">
    <p class="etiqueta" style="margin-bottom:16px">Seguir leyendo</p>
    <div class="rejilla revela">{tarjetas}</div>
  </div>
</article>'''

    return pagina("%s · Contaes" % a["titulo"], a["descripcion"], url, cuerpo, ld, base="")


def construir_indice():
    tarjetas = "\n".join(
        '<a class="post-card" href="%s.html"><span class="franja" style="background:%s"></span>'
        '<span class="dentro"><span class="tema" style="background:%s">%s</span>'
        '<h2 class="post-tit">%s</h2><p>%s</p><p class="pie">%s min de lectura</p></span></a>'
        % (a["slug"], ACENTOS[a["acento"]], ACENTOS[a["acento"]], a["tema"], a["titulo"], a["descripcion"], a["minutos"])
        for a in ARTICULOS)

    cuerpo = f'''<section style="padding:56px 0 80px">
  <div class="wrap">
    <p class="migas"><a href="/">Inicio</a></p>
    <h1 style="max-width:16ch">Cómo se lleva un ERP sin que se te vaya de las manos</h1>
    <p class="entradilla" style="max-width:60ch;margin-top:18px;font-family:var(--serif);font-size:20px;line-height:1.55;color:var(--grafito)">
      Lo que aprendemos construyendo Contaes: migraciones, contabilidad, y qué puede hacer de verdad la IA en un sistema de gestión.
    </p>
    <div class="rejilla revela" style="margin-top:40px">{tarjetas}</div>
  </div>
</section>'''

    ld = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Blog","name":"Blog de Contaes",
 "description":"Migraciones de ERP, contabilidad para pymes e inteligencia artificial aplicada a la gestión.",
 "url":"%s/blog/","inLanguage":"es",
 "publisher":{"@type":"Organization","name":"Contaes","url":"%s/"}}
</script>''' % (DOMINIO, DOMINIO)

    return pagina("Blog · Contaes", "Migraciones de ERP, contabilidad para pymes e inteligencia artificial aplicada a la gestión. Lo que aprendemos construyendo Contaes.",
                  "%s/blog/" % DOMINIO, cuerpo, ld, base="")


def construir_404():
    cuerpo = '''<section style="padding:96px 0 120px;text-align:center">
  <div class="wrap estrecho">
    <p class="etiqueta" style="margin-bottom:14px">Error 404</p>
    <h1>Esta página no existe</h1>
    <p style="margin:20px auto 28px;max-width:44ch;color:var(--grafito);font-size:17px">El enlace está roto o la página se movió de sitio.</p>
    <a class="btn btn-azul" href="/">Volver al inicio</a>
  </div>
</section>'''
    return pagina("Página no encontrada · Contaes", "La página que buscas no existe.",
                  "%s/404.html" % DOMINIO, cuerpo,
                  '<meta name="robots" content="noindex">', base="")


def main():
    os.makedirs(os.path.join(RAIZ, "blog"), exist_ok=True)

    # Solo se escriben los que ya toca publicar. El resto espera su turno:
    # un blog que suelta ciento ochenta articulos el mismo dia se delata.
    global ARTICULOS
    ARTICULOS, escritos = CAL.reparte(ARTICULOS)

    salidas = {"404.html": construir_404(),
               os.path.join("blog", "index.html"): construir_indice(),
               }
    for a in ARTICULOS:
        salidas[os.path.join("blog", a["slug"] + ".html")] = construir_articulo(a)

    for ruta, contenido in sorted(salidas.items()):
        with io.open(os.path.join(RAIZ, ruta), "w", encoding="utf-8") as f:
            f.write(contenido)
        print("  %-52s %6d bytes" % (ruta.replace(os.sep, "/"), len(contenido)))

    print()
    print(CAL.resumen(escritos, len(ARTICULOS)))
    print("  El sitemap lo escribe build-sitio.py")


if __name__ == "__main__":
    main()
