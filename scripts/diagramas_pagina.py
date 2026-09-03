# -*- coding: utf-8 -*-
"""Que dibujo lleva cada pagina.

Un diagrama por pagina, elegido porque explica lo que esa pagina cuenta.
Donde no hay nada que explicar visualmente, no se pone ninguno: un dibujo
de relleno estorba mas que la falta de dibujo.
"""
import dibujos as D

# ─────────────────────────────────────────────────────────────────────
# El flujo que define el servicio: el modelo lo prepara el programa, lo
# confirma el cliente, lo presenta un asesor, y el justificante vuelve.
# ─────────────────────────────────────────────────────────────────────
def flujo_modelo():
    return D.flujo(
        [("El programa lo prepara", "sobre tus propias facturas"),
         ("Tú lo confirmas", "un botón, cuando lo veas bien"),
         ("Un asesor lo revisa", "y lo firma con su nombre"),
         ("Presentado", "el justificante, en tu panel")],
        "Así se presenta un modelo 303. El programa lo calcula sobre los libros que ya "
        "están al día, tú confirmas, y una persona colegiada lo revisa, lo firma y lo "
        "presenta. El justificante vuelve a tu panel. Tú no entras en la sede de Hacienda.")


DIBUJOS = {
    # ── El software ──────────────────────────────────────────────
    "funcionalidades/contabilidad": lambda: D.entrada_documentos(
        "Cada documento que entra deja su apunte en el momento, con su cuenta y su tipo de "
        "IVA. No hay una fase posterior de ordenar papeles: el libro mayor se escribe solo "
        "según ocurren las cosas.",
        ("Factura emitida", "Factura de compra", "Movimiento del banco"),
        "Libro mayor"),
    "funcionalidades/facturacion": lambda: D.flujo(
        [("Presupuesto", "aceptado por el cliente"),
         ("Pedido", "hereda precios y condiciones"),
         ("Factura", "numerada, sin huecos"),
         ("Cobrada", "o vencida, y desde cuándo")],
        "El precio pactado no se vuelve a teclear en ningún paso, así que no se pierde por "
        "el camino. Y el estado de cobro es parte de la factura, no una hoja aparte."),
    "funcionalidades/compras": lambda: D.flujo(
        [("Pedido", "lo que pediste"),
         ("Recepción", "lo que llegó"),
         ("Factura", "lo que te cobran"),
         ("Asiento", "el gasto y su IVA")],
        "Los tres primeros pasos se comparan entre sí. Si lo recibido no cuadra con lo "
        "pedido, o lo facturado no cuadra con lo recibido, sale a la superficie en vez de "
        "esperar a que alguien lo note."),
    "funcionalidades/inventario": lambda: D.comparacion(
        ["El stock vive en una hoja aparte",
         "El recuento anual ajusta la diferencia",
         "El margen real se conoce en enero",
         "El lote se anota en una libreta"],
        ["Cada entrada y salida mueve valor",
         "Los recuentos son por ciclos, no anuales",
         "El margen se ve mientras vendes",
         "El lote se sigue en los dos sentidos"],
        "Un almacén descuadrado no es solo un problema de logística: las existencias son un "
        "activo, y su variación va directa a la cuenta de resultados."),
    "funcionalidades/ventas": lambda: D.flujo(
        [("Presupuesto", "con tu tarifa"),
         ("Pedido", "y su albarán"),
         ("Factura", "sin volver a teclear"),
         ("Ficha del cliente", "todo, en orden")],
        "Cuando llama un cliente, quien coge el teléfono tiene delante sus presupuestos, sus "
        "pedidos, sus facturas y lo que debe. Sin buscar en cuatro sitios."),
    "funcionalidades/proyectos": lambda: D.barras(
        [.42, .58, .71, .5, .84, .33],
        ["Obra A", "Obra B", "Obra C", "Obra D", "Obra E", "Obra F"],
        "El coste de cada proyecto se acumula mientras el proyecto vive, no al terminarlo. "
        "El desvío frente al presupuesto se ve cuando todavía se puede corregir.",
        resalta=[2, 4]),
    "funcionalidades/personal": lambda: D.flujo(
        [("Parte de horas", "desde el móvil"),
         ("Al proyecto", "que las consume"),
         ("A la nómina", "y su retención"),
         ("Al modelo 111", "cuadrado")],
        "Las horas se apuntan donde se trabajan y llegan solas al coste del proyecto y a la "
        "declaración de retenciones."),
    "funcionalidades/informes": lambda: D.barras(
        [.35, .48, .44, .62, .7, .58],
        ["Abr", "May", "Jun", "Jul", "Ago", "Sep"],
        "Los informes consultan el libro mayor directamente. No hay proceso nocturno ni "
        "copia intermedia, así que la cifra que ves es la que hay, y desde ella se puede "
        "bajar hasta el apunte que la compone."),
    "funcionalidades/asesoria-fiscal": flujo_modelo,
    "funcionalidades/asistente-ia": lambda: D.comparacion(
        ["Buscar el informe que responde",
         "Exportar a una hoja de cálculo",
         "Cruzar dos listados a mano",
         "Y volver a hacerlo el mes que viene"],
        ["Preguntar en tu idioma",
         "La respuesta, con su detalle detrás",
         "Comprobable hasta el documento",
         "Nada sale sin que lo apruebes"],
        "La IA hace lo repetitivo y una persona decide. Nada se envía ni se presenta sin "
        "aprobación, y si un dato no está, lo dice en vez de estimarlo."),
    "funcionalidades/escaner-facturas": lambda: D.entrada_documentos(
        "La factura llega en PDF, en foto o por correo. Se lee y se propone ya clasificada, "
        "con el documento original al lado para comprobarlo en segundos. Lo dudoso se marca "
        "en vez de rellenarse a ojo.",
        ("PDF por correo", "Foto del ticket", "Factura escaneada"),
        "Propuesta de asiento"),
    "funcionalidades/conciliacion-bancaria": lambda: D.emparejar(
        ["Transferencia 1.240,00", "Recibo 89,50", "Ingreso 3.100,00"],
        ["F-2026-0841 cobrada", "Cuota mensual", "F-2026-0855 cobrada"],
        "Lo evidente se casa solo. Lo interesante es lo que no casa: cobros parciales, "
        "transferencias agrupadas, comisiones que llevaban meses sin registrarse y cobros "
        "aplicados al cliente equivocado."),
    "funcionalidades/verifactu": lambda: D.flujo(
        [("Se emite", "numerada por serie"),
         ("Se encadena", "con la anterior"),
         ("Se conserva", "tal como se envió"),
         ("Se comprueba", "por su código")],
        "El encadenamiento es lo que hace detectable alterar una factura pasada. Por eso una "
        "factura emitida no se edita: se rectifica, y la rectificativa referencia a la original."),

    # ── La gestoría ──────────────────────────────────────────────
    "gestoria/contabilidad": lambda: D.comparacion(
        ["Guardas los papeles todo el trimestre",
         "Los mandas a la gestoría",
         "Recibes un PDF tres meses después",
         "Para entonces ya no decides nada"],
        ["El apunte nace donde ocurre el hecho",
         "Los libros están al día todos los días",
         "Entras y los miras cuando quieras",
         "Decides con datos de esta semana"],
        "La diferencia no es de precio: es de cuándo sabes las cosas. Una contabilidad a "
        "trimestre vencido sirve para declarar, no para dirigir."),
    "gestoria/fiscal": flujo_modelo,
    "gestoria/laboral": lambda: D.flujo(
        [("Alta y contrato", "en Seguridad Social"),
         ("Nómina mensual", "y su retención"),
         ("Registro de jornada", "que es obligatorio"),
         ("Modelo 111", "cuadrado con las nóminas")],
        "El coste real de una contratación no es el salario bruto. Antes de firmar te "
        "decimos qué sale de la cuenta cada mes, contando cotizaciones, pagas y vacaciones."),
    "gestoria/legal": lambda: D.comparacion(
        ["Un presupuesto aceptado por correo",
         "Condiciones que nadie escribió",
         "El pacto de socios, para más adelante",
         "Y el contrato se lee cuando hay lío"],
        ["Contrato con alcance y plazos",
         "Condiciones de venta por escrito",
         "Pacto firmado mientras todo va bien",
         "Revisado antes de firmar, no después"],
        "El enfoque es preventivo. Un contrato revisado antes cuesta una fracción del pleito "
        "que evita, y esa es toda la tesis."),

    # ── Crecimiento ──────────────────────────────────────────────
    "crecimiento/cfo": lambda: D.barras(
        [.28, .36, .33, .47, .55, .68],
        ["Abr", "May", "Jun", "Jul", "Ago", "Sep"],
        "La contabilidad cuenta lo que pasó. La dirección financiera usa esos mismos números "
        "para decidir lo que va a pasar: presupuesto, previsión de tesorería y margen por "
        "línea de negocio."),
    "crecimiento/cmo": lambda: D.flujo(
        [("Quién te compra", "y por qué"),
         ("Qué dices", "y dónde lo dices"),
         ("Quién llega", "y por qué canal"),
         ("Qué invertir", "en el siguiente euro")],
        "Se gasta en publicidad sin saber qué campaña trajo qué cliente. Medir la atribución "
        "es lo que convierte el gasto en inversión."),
    "crecimiento/prospeccion": lambda: D.barras(
        [1, .62, .34, .18, .09],
        ["Lista", "Contactados", "Responden", "Reunión", "Cliente"],
        "Prospectar es un embudo, no un envío masivo. Cada paso pierde gente, y por eso "
        "importa más a quién se escribe que a cuántos."),
    "crecimiento/bots": lambda: D.flujo(
        [("Entra la consulta", "llamada o WhatsApp"),
         ("El bot responde", "y dice que es un bot"),
         ("Si no llega", "pasa a una persona"),
         ("Queda registrado", "en la ficha del cliente")],
        "La regla que lo hace útil: el bot dice que es un bot y pasa a una persona sin "
        "pelear. Lo que se automatiza son las preguntas repetidas, no las conversaciones "
        "que necesitan confianza."),
    "crecimiento/financiacion": lambda: D.comparacion(
        ["Te enteras de la ayuda cuando cerró",
         "Pides la que no te encaja",
         "Falta un papel y se cae",
         "Te la conceden y no la justificas"],
        ["Buscamos la convocatoria que encaja",
         "Se prepara con tiempo",
         "La documentación, completa",
         "Y se justifica para no perderla"],
        "La mayoría de solicitudes se rechazan por defectos de forma o por pedir la ayuda "
        "equivocada. Las dos cosas se arreglan antes de presentar, no después."),
    "crecimiento/internacionalizacion": lambda: D.flujo(
        [("Dónde tributa", "cada operación"),
         ("Qué registros", "hacen falta"),
         ("Cómo se factura", "y con qué IVA"),
         ("Y el 349", "cuadrado")],
        "El error típico es vender fuera antes de tener claro dónde tributa cada operación. "
        "Esta parte la trabajamos con Filnet, una empresa hermana especializada en abrir "
        "mercados."),

    # ── Paginas sueltas ──────────────────────────────────────────
    "migracion": lambda: D.flujo(
        [("Se acuerda por escrito", "datos, plazos y vuelta atrás"),
         ("Se traen los datos", "con su histórico, no un saldo"),
         ("Conviven los dos", "el viejo, en solo lectura"),
         ("Se apaga el antiguo", "cuando lo nuevo cuadra")],
        "Los cuatro puntos se cierran antes de tocar nada. El tercero es el que más se salta "
        "y el que más caro sale: sin convivencia, los primeros meses son un agujero."),
    "precios": lambda: D.barras(
        [.3, .5, .68, .84, .95],
        ["Personas", "Servicios", "Módulos", "Documentos", "Migración"],
        "Las cinco cosas que mueven el presupuesto, en el orden en que suelen pesar. No hay "
        "tarifa publicada porque cobrar lo mismo a un autónomo con veinte facturas al año que "
        "a una empresa de treinta personas sería cobrarle de más a uno de los dos."),
    "seguridad": lambda: D.comparacion(
        ["Certificaciones que no tenemos",
         "Promesas de disponibilidad sin medir",
         "«Cifrado de nivel bancario»",
         "Y una página que no dice nada"],
        ["Cada apunte, con quién y cuándo",
         "Una factura emitida no se edita",
         "Tus datos, en formato estándar",
         "Y lo que falta, dicho por su nombre"],
        "Lo de la izquierda es lo que suele poner una página de seguridad. Lo de la derecha es "
        "lo que podemos sostener hoy, que es menos y es verdad."),
    "integraciones": lambda: D.flujo(
        [("Tu banco", "extracto, Norma 43"),
         ("Tu correo", "las facturas del proveedor"),
         ("Contaes", "todo en el mismo libro"),
         ("La Agencia Tributaria", "por donde salen los modelos")],
        "Lo que de verdad hace falta para llevar una gestoría entra y sale por aquí. El resto "
        "de conexiones se montan caso por caso, según con qué vendas y cobres."),
    "comparativa": lambda: D.comparacion(
        ["Tú haces de pegamento entre los dos",
         "Los datos viajan por correo",
         "Y lo que no mandas no se contabiliza"],
        ["No hay traspaso porque no hay dos",
         "El apunte nace donde ocurre el hecho",
         "Y quien lleva los libros los firma"],
        "La diferencia entre tener gestoría y programa por separado o juntos no está en las "
        "funciones: está en quién carga con el traspaso y qué se pierde por el camino."),

    # ── Sectores ─────────────────────────────────────────────────
    "sectores/fabricacion": lambda: D.flujo(
        [("Escandallo", "con el coste de hoy"),
         ("Orden de fabricación", "consume materia prima"),
         ("Producto terminado", "entra valorado"),
         ("Coste real", "no el estimado")],
        "El escandallo toma el precio actual del almacén, no el del día que se creó. Y las "
        "horas de taller se imputan a la orden, así que la mano de obra deja de repartirse "
        "a ojo."),
    "sectores/distribucion": lambda: D.comparacion(
        ["La tarifa del cliente, de memoria",
         "La rotura de stock se ve al servir",
         "El rappel del proveedor no baja el coste",
         "La deuda crece sin que nadie la mire"],
        ["El precio pactado se aplica solo",
         "El aviso llega antes de la rotura",
         "El coste real incluye el rappel",
         "La antigüedad de la deuda, a la vista"],
        "En distribución el margen por línea es pequeño, así que un error de precio o una "
        "rotura se comen el beneficio de varias operaciones buenas."),
    "sectores/construccion": lambda: D.barras(
        [.34, .52, .78, .46, .91, .27],
        ["Obra 1", "Obra 2", "Obra 3", "Obra 4", "Obra 5", "Obra 6"],
        "El resultado no es de la empresa: es de cada obra. Una empresa con cinco obras "
        "puede tener beneficio y estar perdiendo dinero en tres de ellas.",
        resalta=[2, 4]),
    "sectores/comercio": lambda: D.flujo(
        [("Venta en tienda", "o en la web"),
         ("Descuenta stock", "en el momento"),
         ("Asiento y IVA", "con su cuenta"),
         ("Margen por producto", "no solo la caja")],
        "El comercio pequeño suele tener tres verdades distintas del mismo negocio: lo que "
        "dice el TPV, lo que hay en la estantería y lo que llega a la contabilidad tres "
        "meses después."),
    "sectores/logistica": lambda: D.barras(
        [.62, .48, .81, .35, .7],
        ["Ruta A", "Ruta B", "Ruta C", "Ruta D", "Ruta E"],
        "Hay rutas que se mantienen porque nadie ha calculado que pierden dinero. Con "
        "combustible, horas y peajes imputados al servicio, el coste por ruta es un dato.",
        resalta=[2, 4]),
    "sectores/servicios": lambda: D.comparacion(
        ["Las horas se apuntan a fin de mes",
         "De memoria y a la baja",
         "El precio cerrado consume el doble",
         "Y se sabe al facturar"],
        ["Se apuntan sobre la tarea, al momento",
         "Desde el móvil, sin abrir nada",
         "El consumo, junto al presupuesto",
         "El desvío se ve mientras se puede"],
        "Cuando lo que vendes es tiempo, la rentabilidad es la diferencia entre las horas "
        "que cobras y las que dedicas. Muchos despachos solo miden la primera mitad."),
    "sectores/instalaciones": lambda: D.flujo(
        [("Aviso", "entra el parte"),
         ("Intervención", "material de la furgoneta"),
         ("Firma en destino", "horas y material"),
         ("Factura", "o garantía, si toca")],
        "El material que sale de la furgoneta descuenta stock, y la intervención sabe si "
        "está cubierta por garantía antes de facturarse, no después."),
    "sectores/agroalimentario": lambda: D.entrada_documentos(
        "La trazabilidad se recorre en los dos sentidos: desde el lote hacia los clientes "
        "que lo recibieron, y desde un cliente hacia la materia prima que entró. Es la "
        "diferencia entre una retirada quirúrgica y una retirada total.",
        ("Entrada de materia prima", "Lote de producción", "Salida al cliente"),
        "Trazabilidad completa"),

    # ── Para quién ───────────────────────────────────────────────
    "para/autonomos": lambda: D.flujo(
        [("Facturas", "las que emitas"),
         ("Gastos", "los que sí deducen"),
         ("Modelos", "303 y 130 o 111"),
         ("Lo que te queda", "de verdad, al mes")],
        "La pregunta que de verdad se hace un autónomo no es cuánto factura: es cuánto le "
        "queda después de cuota, impuestos y gastos. Eso es un número, y se puede ver."),
    "para/startups": lambda: D.comparacion(
        ["La contabilidad, como un trámite",
         "El pacto de socios, más adelante",
         "Los gastos de I+D, sin documentar",
         "Y llega el inversor a pedir números"],
        ["Libros que aguantan una revisión",
         "Pacto firmado desde el principio",
         "I+D documentado mientras se hace",
         "La due diligence no da sustos"],
        "Ordenar la casa después es caro y lento. Ordenarla desde el principio no cuesta "
        "casi nada y es lo que separa una ronda que avanza de una que se atasca."),
    "para/pymes": lambda: D.comparacion(
        ["Cuatro programas que no se hablan",
         "El Excel crítico que lleva una persona",
         "El margen se sabe a fin de año",
         "Y la gestoría va por detrás"],
        ["Un sistema, un libro mayor",
         "El dato se registra donde ocurre",
         "El margen, por línea y en vivo",
         "La gestoría, dentro y al día"],
        "El punto de dolor no es la falta de programas: es que la empresa creció y la "
        "administración se quedó como estaba."),
}


def para(clave):
    """El dibujo de una pagina, o cadena vacia si no lleva."""
    f = DIBUJOS.get(clave)
    return f() if f else ""
