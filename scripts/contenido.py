# -*- coding: utf-8 -*-
"""El texto del sitio. Solo datos: la maquetacion vive en build-sitio.py.

Regla que gobierna todo este fichero: aqui no se inventa nada. Contaes
esta en desarrollo, asi que no hay clientes, ni cifras, ni opiniones, ni
precios, ni logotipos, ni casos de exito. Lo que se cuenta es lo que el
producto hace o hara, y lo que la ley obliga; cuando algo esta previsto y
no hecho, se dice con esas palabras.
"""

# ═════════════════════════════════════════════════════════════════════
# Los ocho modulos
# clave: (titulo, entradilla, [(h2, [parrafos])], [(que incluye)], [(se conecta con, por que)])
# ═════════════════════════════════════════════════════════════════════
MODULOS = {
    "contabilidad": {
        "titulo": "Contabilidad",
        "lema": "El libro mayor como fuente única de verdad",
        "entradilla": "Todo lo que pasa en la empresa acaba siendo un apunte. Si el apunte nace donde ocurre el hecho (la factura, el cobro, el movimiento de almacén) la contabilidad deja de ser una tarea aparte.",
        "secciones": [
            ("Por qué la contabilidad va primero", [
                "En muchos negocios la contabilidad es lo último: se factura durante el mes, se guardan los papeles y a final de trimestre alguien los ordena. Ese orden invierte el problema. Cuando el asiento se genera en el momento del hecho, no hay nada que reconstruir después.",
                "Contaes parte del libro mayor. Cada factura emitida, cada compra, cada nómina y cada movimiento bancario deja su apunte en el momento en que ocurre, con su cuenta y su tipo de IVA. Lo que ves en un informe y lo que declaras en un modelo salen del mismo sitio.",
            ]),
            ("Plan contable y cuentas", [
                "El plan general contable español viene cargado, con la posibilidad de abrir subcuentas por cliente, proveedor o centro de coste. Las cuentas que no se usan no estorban: la búsqueda va por nombre, no por número, así que no hace falta memorizar el código.",
                "Cada cuenta guarda su histórico completo. Entrar en una cuenta y ver los apuntes que la componen (con el documento original a un clic) es lo que convierte un balance en algo que se puede auditar.",
            ]),
            ("El cierre", [
                "El cierre de ejercicio deja de ser una campaña si durante el año no se ha acumulado deuda: amortizaciones calculadas, periodificaciones puestas, saldos de clientes y proveedores cuadrados con sus documentos.",
                "El sistema señala lo que falta antes de cerrar: asientos descuadrados, cuentas con saldo anómalo, facturas sin contabilizar y diferencias entre el libro de IVA y el resumen anual.",
            ]),
        ],
        "incluye": [
            "Plan general contable español, con subcuentas por tercero o centro de coste",
            "Asientos automáticos desde facturas, compras, nóminas y banco",
            "Libro diario, libro mayor y balance de sumas y saldos",
            "Balance de situación y cuenta de pérdidas y ganancias",
            "Amortizaciones y periodificaciones",
            "Libros registro de IVA, emitidas y recibidas",
            "Trazabilidad de cada apunte hasta su documento original",
        ],
        "conecta": [
            ("facturacion", "cada factura emitida genera su asiento con el IVA repercutido que le corresponde"),
            ("compras", "la factura del proveedor entra con su cuenta de gasto y su IVA soportado"),
            ("conciliacion-bancaria", "el extracto se casa con los apuntes en vez de teclearse aparte"),
            ("asesoria-fiscal", "los modelos se calculan sobre estos libros, no sobre una copia"),
        ],
    },
    "facturacion": {
        "titulo": "Facturación",
        "lema": "De la emisión al cobro, con la trazabilidad que exige la administración",
        "entradilla": "Facturar es fácil. Lo difícil es que la factura quede bien numerada, bien contabilizada, bien enviada y bien cobrada, y saber en cualquier momento cuál de esas cuatro cosas falta.",
        "secciones": [
            ("La factura como documento con obligaciones", [
                "Una factura no es un PDF bonito: es un documento con requisitos legales de contenido, numeración correlativa sin huecos, conservación durante años y, desde la entrada en vigor de VeriFactu, requisitos técnicas sobre el sistema que la emite.",
                "Contaes numera de forma correlativa por serie, impide huecos, guarda el histórico de cada documento y conserva la factura tal y como se envió, no como quedaría si se regenerase hoy.",
            ]),
            ("Rectificar sin ensuciar", [
                "Una factura emitida no se borra ni se edita: se rectifica. La rectificativa referencia a la original, invierte lo que corresponde y deja el rastro que un inspector espera encontrar.",
                "El sistema no permite modificar una factura ya contabilizada. Puede parecer incómodo la primera vez; es exactamente lo que evita la conversación de «este número no cuadra con el del año pasado».",
            ]),
            ("El seguimiento del cobro", [
                "La parte que más dinero mueve no es emitir: es cobrar. Cada factura lleva su estado (emitida, vencida, cobrada parcialmente, cobrada) y su antigüedad.",
                "Desde ahí se puede pedir al asistente que ordene lo pendiente por antigüedad, que prepare los recordatorios de las que pasan de un plazo o que enseñe qué cliente concentra el riesgo. La decisión de enviar sigue siendo tuya.",
            ]),
        ],
        "incluye": [
            "Series y numeración correlativa, sin huecos",
            "Facturas rectificativas enlazadas a la original",
            "Facturación recurrente para servicios periódicos",
            "Estados de cobro y antigüedad de la deuda",
            "Recordatorios de cobro preparados por el asistente",
            "Envío por correo con registro de lo enviado",
            "Conservación del documento tal como se emitió",
        ],
        "conecta": [
            ("contabilidad", "el asiento de la venta y el IVA repercutido salen solos"),
            ("ventas", "el presupuesto aceptado se convierte en pedido y el pedido en factura"),
            ("verifactu", "los requisitos del sistema de facturación afectan directamente a este módulo"),
            ("asesoria-fiscal", "el libro de emitidas es la mitad del modelo 303"),
        ],
    },
    "inventario": {
        "titulo": "Inventario",
        "lema": "Lo que hay, dónde está y desde cuándo",
        "entradilla": "Un almacén descuadrado no es solo un problema de logística: es un problema contable, porque las existencias son un activo y su variación va a la cuenta de resultados.",
        "secciones": [
            ("Existencias que cuadran con la contabilidad", [
                "En muchos negocios el stock vive en una hoja de cálculo y la contabilidad en otro sitio, y a fin de año se hace un recuento para ajustar la diferencia. Ese ajuste es una confesión: durante doce meses nadie sabía el margen real.",
                "Aquí cada entrada y cada salida mueve existencias y valor a la vez. El inventario permanente no es una función avanzada, es lo normal.",
            ]),
            ("Lotes, caducidades y trazabilidad", [
                "Cuando el sector lo exige (alimentación, farmacia, componentes con garantía) el lote deja de ser opcional. Saber a qué clientes fue un lote concreto es la diferencia entre una retirada quirúrgica y una retirada total.",
                "El movimiento guarda de dónde vino y a dónde fue, así que la trazabilidad se puede recorrer en los dos sentidos.",
            ]),
            ("Varios almacenes", [
                "Almacén central, tienda, furgoneta de un técnico o material en depósito en casa del cliente son sitios distintos con el mismo artículo. Tratarlos como uno solo es lo que produce el clásico «en el sistema hay diez y en la estantería hay tres».",
            ]),
        ],
        "incluye": [
            "Inventario permanente, valorado",
            "Varios almacenes y ubicaciones",
            "Lotes, números de serie y caducidades",
            "Movimientos entre almacenes con su rastro",
            "Regularizaciones con motivo y responsable",
            "Stock mínimo y aviso de reposición",
            "Valoración de existencias para el cierre",
        ],
        "conecta": [
            ("compras", "la recepción de mercancía entra en existencias en el momento"),
            ("ventas", "la salida descuenta stock y avisa si no hay"),
            ("contabilidad", "la variación de existencias llega al resultado sin ajustes de última hora"),
        ],
    },
    "compras": {
        "titulo": "Compras",
        "lema": "Del presupuesto a la factura sin volver a teclear nada",
        "entradilla": "El circuito de compra es donde más se pierde: se pide por teléfono, llega la mercancía, la factura aparece semanas después y nadie recuerda si el precio era el acordado.",
        "secciones": [
            ("El circuito completo", [
                "Petición, pedido al proveedor, recepción y factura son cuatro momentos distintos del mismo hecho. Cuando cada uno vive en un sitio, cuadrarlos es trabajo manual; cuando están enlazados, el sistema puede avisar solo de las diferencias.",
                "Contaes compara el pedido con lo recibido y lo recibido con lo facturado. Lo que no cuadra sale a la superficie en vez de esperar a que alguien lo note.",
            ]),
            ("La factura del proveedor sin teclear", [
                "La mayoría de facturas de proveedor llegan en PDF por correo. El escáner las lee, extrae proveedor, fecha, base, IVA y líneas, y las propone ya clasificadas. Quien las revisa confirma o corrige.",
                "Corregir es más rápido que teclear, y además enseña: lo que se corrige una vez se propone mejor la siguiente para ese proveedor.",
            ]),
            ("Proveedores y condiciones", [
                "Cada proveedor guarda sus condiciones, sus plazos de pago y su histórico completo. Saber cuánto se le ha comprado en el año no debería requerir una consulta especial: es la primera pantalla de su ficha.",
            ]),
        ],
        "incluye": [
            "Pedidos a proveedor y recepciones parciales",
            "Cotejo entre pedido, recepción y factura",
            "Escáner de facturas de proveedor",
            "Clasificación contable propuesta y editable",
            "Condiciones y plazos de pago por proveedor",
            "Histórico de compras por proveedor y por artículo",
            "Previsión de pagos a partir de los vencimientos",
        ],
        "conecta": [
            ("inventario", "lo recibido entra en existencias en el momento de la recepción"),
            ("contabilidad", "el gasto y el IVA soportado quedan asentados con su cuenta"),
            ("escaner-facturas", "es el módulo que más se apoya en la lectura automática"),
        ],
    },
    "ventas": {
        "titulo": "Ventas y clientes",
        "lema": "El histórico completo de cada cuenta en una sola ficha",
        "entradilla": "No hace falta un CRM aparte para saber qué le has vendido a un cliente, qué te debe y qué le presupuestaste hace tres meses. Hace falta que esté en el mismo sitio que la factura.",
        "secciones": [
            ("La ficha del cliente", [
                "Presupuestos, pedidos, albaranes, facturas, cobros, incidencias y contactos, en orden cronológico. Cuando llama un cliente, la persona que coge el teléfono debería tener eso delante sin buscar en cuatro sistemas.",
            ]),
            ("Del presupuesto a la factura", [
                "El presupuesto aceptado se convierte en pedido; el pedido servido en albarán; el albarán en factura. Cada paso hereda del anterior, así que un precio pactado no se pierde por el camino ni se vuelve a teclear.",
                "Los presupuestos que caducan sin respuesta no desaparecen: quedan como lo que son, oportunidades perdidas que conviene mirar de vez en cuando.",
            ]),
            ("Márgenes reales", [
                "Vender mucho y ganar poco es un problema que se ve tarde si el coste no está en el mismo sistema. Con el inventario valorado y las compras dentro, el margen por artículo y por cliente sale sin cálculos aparte.",
            ]),
        ],
        "incluye": [
            "Ficha de cliente con histórico completo",
            "Presupuestos, pedidos y albaranes enlazados",
            "Tarifas y descuentos por cliente",
            "Margen por artículo, por pedido y por cliente",
            "Estado de cobro visible desde la ficha",
            "Contactos y notas de la relación",
        ],
        "conecta": [
            ("facturacion", "el pedido servido se convierte en factura sin volver a introducir nada"),
            ("inventario", "la salida descuenta existencias y avisa de roturas de stock"),
            ("proyectos", "cuando la venta es un proyecto, las horas y el material van contra él"),
        ],
    },
    "proyectos": {
        "titulo": "Proyectos",
        "lema": "Saber lo que cuesta un proyecto mientras se hace",
        "entradilla": "El proyecto que sale mal casi nunca sorprende al final: sorprende porque nadie miró a mitad. Imputar horas y materiales sobre la marcha convierte la rentabilidad en algo que se puede corregir a tiempo.",
        "secciones": [
            ("Coste real, no estimado", [
                "Un proyecto acumula horas de personas, materiales de almacén, compras específicas y gastos. Si las cuatro cosas se imputan donde corresponde, el coste es un dato, no una impresión.",
                "El presupuesto inicial queda al lado del coste acumulado, así que el desvío se ve mientras aún se puede hacer algo.",
            ]),
            ("Horas que sí se apuntan", [
                "La imputación de horas fracasa cuando es incómoda. El parte se rellena desde el móvil, sobre las tareas que la persona ya tiene asignadas, y admite corrección posterior.",
            ]),
            ("Certificaciones y facturación por hitos", [
                "En obra y en servicios largos no se factura al final: se certifica por avance. El proyecto lleva sus hitos y lo que queda por certificar, que es la mitad de la previsión de tesorería.",
            ]),
        ],
        "incluye": [
            "Presupuesto por proyecto y por partida",
            "Imputación de horas, materiales y compras",
            "Coste acumulado y desvío frente al presupuesto",
            "Hitos, certificaciones y facturación por avance",
            "Rentabilidad por proyecto y por responsable",
            "Partes de trabajo desde el móvil",
        ],
        "conecta": [
            ("personal", "las horas del equipo se imputan al proyecto en el que se trabajan"),
            ("compras", "la compra específica de un proyecto va a su coste, no a un cajón general"),
            ("facturacion", "la certificación aprobada se convierte en factura"),
        ],
    },
    "personal": {
        "titulo": "Personal",
        "lema": "Lo imprescindible, sin convertirse en un software de RRHH aparte",
        "entradilla": "La mayoría de pymes no necesitan un sistema de recursos humanos completo. Necesitan saber quién está, quién falta, qué gastos hay que reembolsar y que todo eso llegue a la contabilidad.",
        "secciones": [
            ("Plantilla y ausencias", [
                "Una ficha por persona con su contrato, su calendario y sus ausencias. Las vacaciones se piden y se aprueban en el sistema, así que el calendario del equipo es el mismo para todos.",
                "El registro de jornada es una obligación legal en España desde 2019 para la mayoría de empresas. Aquí se registra sin instalar nada aparte.",
            ]),
            ("Gastos y dietas", [
                "El ticket se fotografía, se lee y se propone clasificado. Quien aprueba ve el importe y el justificante; lo aprobado va al reembolso y a la contabilidad.",
            ]),
            ("Lo que no hace", [
                "Contaes no calcula nóminas ni sustituye a una gestoría laboral. La nómina la elabora quien tenga esa responsabilidad, y su asiento entra en la contabilidad. Confundir gestión y responsabilidad laboral es una manera rápida de meterse en un problema.",
            ]),
        ],
        "incluye": [
            "Ficha de empleado y documentación asociada",
            "Ausencias, vacaciones y aprobaciones",
            "Registro de jornada",
            "Gastos con justificante fotografiado",
            "Imputación de horas a proyectos",
            "Asiento contable de la nómina recibida",
        ],
        "conecta": [
            ("proyectos", "las horas de cada persona van al proyecto correspondiente"),
            ("contabilidad", "gastos, dietas y nóminas acaban en su cuenta"),
            ("asesoria-fiscal", "las retenciones practicadas alimentan el modelo 111"),
        ],
    },
    "informes": {
        "titulo": "Informes",
        "lema": "Cuadros de mando sobre datos en vivo, sin exportar a una hoja de cálculo",
        "entradilla": "El informe que hay que exportar, pegar y formatear cada lunes deja de hacerse en marzo. El que está ahí cuando entras se mira todos los días.",
        "secciones": [
            ("Sobre el dato, no sobre una copia", [
                "Cada informe consulta el libro mayor, el almacén y los documentos directamente. No hay proceso nocturno ni copia intermedia, así que la cifra que ves es la que hay.",
                "Cuando un número extraña, se puede bajar hasta el apunte que lo compone y desde ahí al documento original. Un informe que no permite eso obliga a creer, y creer no es gestionar.",
            ]),
            ("Lo que suele mirarse", [
                "Facturación por periodo y su comparación con el anterior, margen por línea de negocio, deuda de clientes por antigüedad, previsión de cobros y pagos, rotación de existencias y coste por proyecto.",
                "Y por encima, el asistente: preguntar «¿qué clientes han bajado respecto al año pasado?» suele ser más rápido que buscar el informe que responde a eso.",
            ]),
        ],
        "incluye": [
            "Cuadro de mando de inicio, configurable",
            "Facturación, margen y comparación entre periodos",
            "Antigüedad de la deuda de clientes",
            "Previsión de cobros y pagos a partir de vencimientos",
            "Rotación y valoración de existencias",
            "Rentabilidad por proyecto, cliente y artículo",
            "Descenso hasta el apunte y el documento original",
        ],
        "conecta": [
            ("asistente-ia", "preguntar en tu idioma suele ser más rápido que buscar el informe"),
            ("contabilidad", "todo sale del libro mayor, no de una copia"),
        ],
    },
}

# ═════════════════════════════════════════════════════════════════════
# Lo que lo hace distinto
# ═════════════════════════════════════════════════════════════════════
CAPACIDADES = {
    "asesoria-fiscal": {
        "titulo": "Asesoría fiscal incluida",
        "lema": "La IA prepara los modelos; un asesor los revisa, los firma y los presenta",
        "entradilla": "Esto es lo que separa a Contaes de un ERP normal. No es un programa que te ayuda a hacer la contabilidad: es un servicio en el que la contabilidad ya está hecha y los modelos se presentan por ti.",
        "secciones": [
            ("Dos cosas que hoy están separadas", [
                "Hoy una pyme tiene un ERP donde mete los datos y una asesoría a la que se los manda. En medio hay un mes de correos, un Excel y la pregunta de siempre: «¿me pasas las facturas?».",
                "Cuando el programa que lleva las facturas es el mismo que prepara los modelos, ese trasvase desaparece. Y con él desaparecen los errores que nacen en el trasvase, que son casi todos.",
            ]),
            ("Quién firma", [
                "La IA prepara. La responsabilidad ante la Administración es de una persona colegiada que revisa, firma y presenta. Esto no es un matiz: es la diferencia entre un servicio profesional y una herramienta que te deja solo ante un requerimiento.",
                "Un modelo mal presentado no lo arregla un algoritmo. Lo arregla alguien que responde por él.",
            ]),
            ("Los modelos que suelen tocar", [
                "Trimestrales: 303 de IVA, 111 de retenciones de IRPF, 115 de retenciones por alquiler, 130 de pago fraccionado para autónomos en estimación directa y 349 de operaciones intracomunitarias.",
                "Anuales: 390 como resumen de IVA, 190 como resumen de retenciones, 347 de operaciones con terceros por encima de 3.005,06 € y 200 del Impuesto de Sociedades.",
                "Cuáles te tocan a ti depende de tu forma jurídica, tu actividad y tu volumen. Eso se determina en el diagnóstico, no en una tabla de una web.",
            ]),
        ],
        "incluye": [
            "Contabilidad mantenida al día sobre tus propios datos",
            "Modelos calculados sobre los libros, no sobre una copia",
            "Revisión, firma y presentación por una persona colegiada",
            "Aviso de lo que descuadra antes de presentar",
            "Conservación de los modelos presentados y sus justificantes",
            "Atención ante requerimientos sobre lo presentado",
        ],
        "conecta": [
            ("contabilidad", "los libros son el origen de cada casilla"),
            ("facturacion", "el libro de emitidas es la mitad del 303"),
            ("compras", "el de recibidas es la otra mitad"),
        ],
        "aviso": "El alcance concreto del servicio de asesoría, quién lo presta y qué incluye se define por contrato. Esta página describe cómo está pensado el producto, no sustituye a ese contrato.",
    },
    "asistente-ia": {
        "titulo": "Asistente con IA",
        "lema": "Preguntar en tu idioma en vez de buscar por menús",
        "entradilla": "La IA de un ERP no está para escribir textos bonitos. Está para que no tengas que aprenderte dónde vive cada informe, y para hacer el trabajo repetitivo que hoy hace una persona a mano.",
        "secciones": [
            ("Qué hace", [
                "Responde preguntas sobre tus datos: qué facturas siguen sin cobrar, qué cliente ha bajado respecto al año pasado, cuánto llevamos gastado en un proyecto. La respuesta viene con el detalle detrás, para poder comprobarla.",
                "Clasifica lo que entra: la factura del proveedor, el ticket del gasto, el movimiento del banco. Propone la cuenta y el tipo de IVA; la persona confirma.",
                "Prepara trabajo: los recordatorios de cobro de lo que pasa de un plazo, el borrador de un modelo, la lista de lo que descuadra antes de un cierre.",
            ]),
            ("Qué no hace", [
                "No presenta nada por su cuenta. No manda correos sin que alguien los vea. No firma. Todo lo que sale de la empresa pasa por una persona.",
                "No inventa cifras. Si un dato no está, lo dice; no lo estima. Un ERP que redondea al alza es peor que no tener ERP.",
            ]),
            ("Por qué importa que esté dentro", [
                "Una IA conectada por fuera solo ve lo que le dejan ver. Estando dentro, ve el libro mayor, el almacén y los documentos, y por eso puede responder con el detalle que permite comprobarla.",
            ]),
        ],
        "incluye": [
            "Preguntas en lenguaje natural sobre tus datos",
            "Respuesta con el detalle que la compone",
            "Clasificación propuesta de facturas, gastos y movimientos",
            "Preparación de recordatorios de cobro",
            "Aviso de descuadres antes de un cierre o un modelo",
            "Nada se envía ni se presenta sin aprobación de una persona",
        ],
        "conecta": [
            ("informes", "muchas veces preguntar es más rápido que buscar el informe"),
            ("escaner-facturas", "la lectura del documento y su clasificación son el mismo trabajo"),
        ],
    },
    "escaner-facturas": {
        "titulo": "Escáner de facturas",
        "lema": "La factura del proveedor entra sin teclearla",
        "entradilla": "Teclear facturas de compra es el trabajo más repetitivo de una administración pequeña, y el que más errores de clasificación produce. Es exactamente el tipo de tarea que debe hacer una máquina y revisar una persona.",
        "secciones": [
            ("Cómo funciona", [
                "La factura llega en PDF, en foto o por correo a una dirección del sistema. Se lee proveedor, fecha, número, base, tipo y cuota de IVA, retención si la hay, y las líneas de detalle.",
                "Con eso se propone el asiento: cuenta de gasto, tipo de IVA y proveedor. Quien revisa ve el documento original al lado de la propuesta, así que comprobar cuesta segundos.",
            ]),
            ("Por qué la revisión no sobra", [
                "Una lectura automática acierta la mayoría de veces y falla algunas. El problema no es el fallo: es el fallo silencioso. Por eso lo leído se propone, no se aplica, y lo que el sistema no ve claro lo marca en vez de rellenarlo a ojo.",
                "Lo que se corrige mejora la propuesta siguiente para ese mismo proveedor, que suele mandar siempre el mismo formato.",
            ]),
        ],
        "incluye": [
            "Lectura de PDF, imagen y correo entrante",
            "Extracción de proveedor, fechas, importes, IVA y retención",
            "Líneas de detalle cuando el documento las trae",
            "Propuesta de cuenta contable y tipo de IVA",
            "Documento original siempre visible junto a la propuesta",
            "Marcado de lo dudoso en vez de relleno a ojo",
        ],
        "conecta": [
            ("compras", "es donde más se usa, con las facturas de proveedor"),
            ("personal", "los tickets de gasto entran por el mismo camino"),
            ("contabilidad", "lo aprobado se convierte en apunte con su documento enlazado"),
        ],
    },
    "conciliacion-bancaria": {
        "titulo": "Conciliación bancaria",
        "lema": "El extracto contra los apuntes, cuadrado",
        "entradilla": "La conciliación es la prueba de que la contabilidad se parece a la realidad. Si el banco dice una cosa y los libros otra, uno de los dos está mal, y casi siempre son los libros.",
        "secciones": [
            ("Casar movimientos", [
                "El movimiento del banco se propone contra el cobro o el pago que le corresponde. Lo evidente (importe y fecha que coinciden con una factura pendiente) se propone casado; lo demás se marca.",
                "Los que no casan son los interesantes: cobros parciales, transferencias agrupadas, comisiones, devoluciones. Verlos aparte es lo que evita que se pierdan en el montón.",
            ]),
            ("Lo que aparece al conciliar de verdad", [
                "Facturas cobradas que seguían figurando como pendientes. Recibos domiciliados que nadie había contabilizado. Comisiones que llevaban meses sin registrarse. Cobros de un cliente aplicados a otro.",
                "Ninguna de esas cosas se ve mirando solo el ERP ni mirando solo el banco.",
            ]),
        ],
        "incluye": [
            "Importación del extracto bancario",
            "Propuesta automática de casación",
            "Cobros parciales y agrupados",
            "Comisiones y gastos bancarios",
            "Saldo contable frente a saldo real, en todo momento",
            "Lo no conciliado, siempre visible",
        ],
        "conecta": [
            ("contabilidad", "el apunte de banco deja de teclearse a mano"),
            ("facturacion", "el estado de cobro de la factura se actualiza al conciliar"),
        ],
    },
    "verifactu": {
        "titulo": "VeriFactu",
        "lema": "Qué es y qué obliga",
        "entradilla": "VeriFactu es el nombre corriente del sistema de emisión de facturas verificables que desarrolla el Reglamento de requisitos de los sistemas informáticos de facturación en España. Afecta al programa con el que facturas, no solo a la factura.",
        "secciones": [
            ("Qué exige, en corto", [
                "Que el sistema de facturación genere un registro de cada factura con encadenamiento, de forma que alterar una factura pasada sea detectable. Que ese registro lleve huella y, en la modalidad verificable, se remita a la Agencia Tributaria. Que la factura incluya un código QR que permita comprobarla.",
                "Y, sobre todo, que el sistema no permita llevar contabilidades paralelas ni borrar sin rastro. Buena parte del reglamento va de eso.",
            ]),
            ("A quién afecta y desde cuándo", [
                "Afecta a quienes emiten facturas usando sistemas informáticos, con excepciones (entre ellas, quienes ya están en el Suministro Inmediato de Información). Las fechas de entrada en vigor han cambiado varias veces desde que se aprobó el reglamento.",
                "Por eso aquí no vas a encontrar una fecha con aire de certeza absoluta: consulta el calendario vigente en la sede de la Agencia Tributaria o pregunta a tu asesor por tu caso concreto. Lo que sí puedes dar por hecho es que el sistema con el que factures tendrá que cumplirlo.",
            ]),
            ("Qué significa para Contaes", [
                "Que la facturación se está construyendo con estos requisitos desde el principio y no como un parche: numeración sin huecos, imposibilidad de editar lo emitido, rectificativas enlazadas y conservación del documento tal como se envió.",
            ]),
        ],
        "incluye": [
            "Numeración correlativa sin huecos, por serie",
            "Imposibilidad de modificar una factura ya emitida",
            "Rectificativas enlazadas a la original",
            "Registro de eventos sobre cada documento",
            "Conservación del documento tal como se emitió",
        ],
        "conecta": [
            ("facturacion", "es el módulo directamente afectado"),
            ("asesoria-fiscal", "el asesor es quien sabe si a tu caso le aplica y desde cuándo"),
        ],
        "aviso": "Esta página explica el marco general y no es asesoramiento fiscal. Las fechas de aplicación y las excepciones han cambiado desde la aprobación del reglamento: confirma tu situación concreta con tu asesor o en la sede electrónica de la Agencia Tributaria.",
    },
}

# ═════════════════════════════════════════════════════════════════════
# Sectores
# ═════════════════════════════════════════════════════════════════════
SECTORES = {
    "fabricacion": {
        "preguntas": [
            ("¿El escandallo está actualizado o es el del año pasado?",
             "Es la primera. Un escandallo con precios de materia prima antiguos convierte el margen en una cifra inventada, y casi nadie los revisa hasta que algo duele."),
            ("¿Las horas de taller se imputan a la orden?",
             "Si no, el coste de mano de obra se reparte a ojo entre todo lo que se fabrica, y los productos que dan más trabajo salen baratos en los papeles."),
            ("¿Qué se hace con las mermas y los destríos?",
             "Si aparecen solo en el recuento anual, durante doce meses el almacén ha estado diciendo que hay más de lo que hay."),
        ],
        "titulo": "Fabricación",
        "lema": "Escandallos, órdenes y coste real de producción",
        "entradilla": "Fabricar es transformar materiales y horas en producto. Si el coste de esa transformación se estima en lugar de medirse, el margen es una opinión.",
        "duele": [
            "El escandallo se hizo hace tres años y los precios de materia prima ya no son esos.",
            "El producto terminado entra en almacén a un coste teórico que nadie revisa.",
            "Las horas de taller no se imputan a la orden, así que el coste de mano de obra se reparte a ojo.",
            "Las mermas no se registran, y aparecen en el recuento anual como una diferencia inexplicable.",
        ],
        "aporta": [
            ("Escandallo vivo", "la lista de materiales toma el coste actual de almacén, no el del día que se creó"),
            ("Órdenes de fabricación", "consumen materia prima y generan producto terminado, moviendo existencias y valor"),
            ("Horas imputadas", "el parte de taller va contra la orden, así que la mano de obra es un dato"),
            ("Mermas con motivo", "la diferencia se registra cuando ocurre, no en el recuento de diciembre"),
            ("Lotes y trazabilidad", "de la materia prima al cliente final, en los dos sentidos"),
        ],
        "modulos": ["inventario", "compras", "proyectos", "contabilidad", "informes"],
    },
    "distribucion": {
        "preguntas": [
            ("¿Cuántas tarifas distintas manejáis?",
             "Y sobre todo: ¿están en el sistema o en la cabeza de quien vende? Es de donde salen la mitad de las facturas mal hechas."),
            ("¿Los rappeles del proveedor bajan el coste del artículo?",
             "Si el rappel entra como un ingreso suelto a final de año, el margen por línea que estáis mirando durante todo el año está mal."),
            ("¿Con qué antigüedad miráis lo que os deben?",
             "Ordenar la deuda por importe es lo natural y es el orden equivocado. Lo que dice de verdad quién va a dejar de pagar es la antigüedad."),
        ],
        "titulo": "Distribución y mayorista",
        "lema": "Muchas referencias, márgenes finos y stock que se mueve",
        "entradilla": "En distribución el margen por línea es pequeño, así que un error de precio o una rotura de stock se comen el beneficio de varias operaciones buenas.",
        "duele": [
            "Tarifas distintas por cliente que se aplican de memoria.",
            "Roturas de stock que se descubren al ir a servir el pedido.",
            "Rappeles y descuentos de proveedor que no se reflejan en el coste.",
            "Deuda de clientes que crece sin que nadie la mire hasta que duele.",
        ],
        "aporta": [
            ("Tarifas por cliente", "el precio pactado se aplica solo, no se recuerda"),
            ("Stock mínimo y reposición", "el aviso llega antes de la rotura, no después"),
            ("Margen por línea", "con el coste real de almacén, no con el de la última compra"),
            ("Antigüedad de la deuda", "quién debe qué y desde cuándo, siempre a la vista"),
            ("Varios almacenes", "central, tienda y depósito son sitios distintos con el mismo artículo"),
        ],
        "modulos": ["inventario", "ventas", "compras", "facturacion", "informes"],
    },
    "construccion": {
        "preguntas": [
            ("¿Sabéis el desvío de cada obra mientras está en marcha?",
             "O se sabe al certificar. Es la diferencia entre corregir y enterarse."),
            ("¿El material comprado para una obra acaba imputado a esa obra?",
             "Cuando se mueve entre obras y nadie lo ajusta, una sale barata y otra cara sin que ninguna de las dos sea verdad."),
            ("¿Los partes llegan en papel?",
             "El coste de las horas no es el problema. El problema es que llegan tarde, y para entonces la decisión ya está tomada."),
        ],
        "titulo": "Construcción",
        "lema": "Obra a obra: certificaciones, coste y desvío",
        "entradilla": "En obra el resultado no es de la empresa: es de cada obra. Una empresa con cinco obras puede tener beneficio y estar perdiendo dinero en tres de ellas.",
        "duele": [
            "El coste de la obra se conoce al terminarla, cuando ya no se puede hacer nada.",
            "Las certificaciones se llevan en una hoja aparte y no cuadran con lo facturado.",
            "El material comprado para una obra acaba en otra y nadie lo ajusta.",
            "Los partes de los operarios llegan en papel y se transcriben tarde o no se transcriben.",
        ],
        "aporta": [
            ("Presupuesto por partidas", "y el coste acumulado al lado, mientras la obra avanza"),
            ("Certificaciones", "lo certificado, lo facturado y lo que queda, en el mismo sitio"),
            ("Compras contra obra", "el material se imputa a la obra que lo consume"),
            ("Partes desde el móvil", "las horas se apuntan donde se trabajan"),
            ("Desvío visible", "la diferencia con el presupuesto sale mientras aún se puede corregir"),
        ],
        "modulos": ["proyectos", "compras", "personal", "facturacion", "contabilidad"],
    },
    "comercio": {
        "preguntas": [
            ("¿Cuadra lo que dice el sistema con lo que hay en la estantería?",
             "Si hace falta un recuento para saberlo, el margen que estáis viendo es una estimación con nombre de dato."),
            ("¿Sabéis el margen por producto o solo la caja del día?",
             "La caja dice cuánto ha entrado. No dice qué productos os están dando de comer y cuáles ocupan sitio."),
            ("¿Las devoluciones y los cambios dejan rastro contable?",
             "Es donde se cuela la mayor parte del descuadre entre lo que se vendió y lo que se declaró."),
        ],
        "titulo": "Comercio y retail",
        "lema": "Tienda, almacén y contabilidad en el mismo sitio",
        "entradilla": "El comercio pequeño suele tener un TPV que vende, un almacén en la cabeza del encargado y una gestoría que lo contabiliza tres meses después. Tres verdades distintas del mismo negocio.",
        "duele": [
            "Lo que dice el sistema que hay y lo que hay en la estantería no coinciden.",
            "El margen por producto no se conoce, solo la caja del día.",
            "Las devoluciones y los cambios no dejan rastro contable.",
            "El IVA se calcula a final de trimestre a partir de un resumen, no de los tickets.",
        ],
        "aporta": [
            ("Existencias reales", "cada venta descuenta stock en el momento"),
            ("Margen por producto", "y por familia, con el coste de compra real"),
            ("Devoluciones con rastro", "el cambio deja su apunte, no un agujero"),
            ("Varios puntos de venta", "cada tienda es un almacén con sus propias existencias"),
            ("IVA sobre el dato", "el 303 sale del libro de emitidas, no de un resumen"),
        ],
        "modulos": ["inventario", "ventas", "facturacion", "contabilidad", "informes"],
    },
    "logistica": {
        "preguntas": [
            ("¿Cómo repartís el coste entre servicios que comparten viaje?",
             "Si es por kilómetro medio, hay rutas que llevan años perdiendo dinero sin que nadie lo sepa."),
            ("¿Los portes de terceros se imputan al servicio que los genera?",
             "Cuando van a un cajón general, los servicios que subcontratáis parecen los más rentables."),
            ("¿El mantenimiento del vehículo entra en el coste?",
             "Suele quedarse fuera, y es de los pocos costes que crecen justo con los servicios que más margen parecen dar."),
        ],
        "titulo": "Logística y transporte",
        "lema": "Rutas, portes y lo que cuesta cada servicio",
        "entradilla": "En transporte el coste se reparte entre servicios que comparten vehículo, combustible y conductor. Si el reparto se hace por intuición, hay rutas que se mantienen porque nadie ha calculado que pierden dinero.",
        "duele": [
            "El coste por servicio se estima sobre el precio medio del kilómetro.",
            "Los suplidos y los portes de terceros se facturan mal o se olvidan.",
            "Los partes del conductor llegan en papel días después.",
            "El mantenimiento del vehículo no se imputa a nada.",
        ],
        "aporta": [
            ("Coste por servicio", "combustible, horas y peajes imputados donde corresponde"),
            ("Portes de terceros", "el coste del subcontratado va contra el servicio que lo genera"),
            ("Partes desde el móvil", "el conductor cierra el servicio donde está"),
            ("Rentabilidad por ruta", "y por cliente, con el coste real"),
            ("Facturación agrupada", "varios servicios en una factura, con su detalle"),
        ],
        "modulos": ["proyectos", "compras", "facturacion", "personal", "informes"],
    },
    "servicios": {
        "preguntas": [
            ("¿Cuándo se apuntan las horas?",
             "Si es a fin de mes y de memoria, el número que sale es siempre menor que el real. Nadie exagera sus propias horas hacia arriba."),
            ("¿Qué pasa con el trabajo fuera de alcance?",
             "Se hace, no se factura y no se registra. Después nadie entiende por qué ese proyecto salió mal."),
            ("¿Sabéis qué cliente es rentable?",
             "No cuál factura más: cuál deja más después de contar las horas dedicadas y los días que tarda en pagar."),
        ],
        "titulo": "Servicios profesionales",
        "lema": "Horas facturables, proyectos y rentabilidad",
        "entradilla": "Cuando lo que vendes es tiempo, la rentabilidad es la diferencia entre las horas que cobras y las que dedicas. Muchos despachos y estudios solo miden la primera mitad.",
        "duele": [
            "Las horas se apuntan al final del mes, de memoria y a la baja.",
            "El proyecto de precio cerrado consume el doble de horas de lo previsto y se sabe al facturar.",
            "El trabajo fuera de alcance se hace y no se factura.",
            "No se sabe qué cliente es rentable y cuál se sostiene por costumbre.",
        ],
        "aporta": [
            ("Imputación cómoda", "las horas se apuntan sobre las tareas asignadas, desde el móvil"),
            ("Precio cerrado con control", "el consumo frente al presupuesto, mientras el proyecto vive"),
            ("Fuera de alcance visible", "lo extra queda registrado y se puede decidir si se factura"),
            ("Rentabilidad por cliente", "no solo facturación: margen"),
            ("Facturación recurrente", "las igualas se emiten solas y su cobro se sigue"),
        ],
        "modulos": ["proyectos", "personal", "facturacion", "ventas", "informes"],
    },
    "instalaciones": {
        "preguntas": [
            ("¿El material de la furgoneta está en algún almacén del sistema?",
             "Casi nunca. Y es donde desaparece la diferencia entre lo que se compró y lo que se facturó."),
            ("¿El parte se firma en destino?",
             "Firmado allí, con las horas y el material, no hay conversación posterior sobre qué se hizo."),
            ("¿Sabéis si un contrato de mantenimiento es rentable?",
             "Se cobra la cuota y se atienden avisos. Cruzar las dos cosas es lo que dice si ese contrato conviene renovarlo."),
        ],
        "titulo": "Instalaciones y mantenimiento",
        "lema": "Partes de trabajo, materiales y garantías",
        "entradilla": "El técnico que sale a una avería consume horas, kilómetros y material de la furgoneta. Si nada de eso se registra donde ocurre, el parte se convierte en una factura aproximada.",
        "duele": [
            "El material de la furgoneta no está en ningún almacén del sistema.",
            "El parte se rellena en papel y se transcribe con errores o con retraso.",
            "Las intervenciones en garantía se facturan por error, o al revés.",
            "El contrato de mantenimiento se factura, pero nadie sabe si es rentable.",
        ],
        "aporta": [
            ("La furgoneta como almacén", "el material que sale del vehículo descuenta stock"),
            ("Parte firmado en destino", "con las horas, el material y la firma del cliente"),
            ("Garantías controladas", "la intervención sabe si está cubierta antes de facturarse"),
            ("Contratos de mantenimiento", "lo cobrado frente a las intervenciones consumidas"),
            ("Histórico por equipo", "qué se hizo en esa máquina y cuándo"),
        ],
        "modulos": ["proyectos", "inventario", "personal", "facturacion", "ventas"],
    },
    "agroalimentario": {
        "preguntas": [
            ("¿Cuánto tardaríais en saber a qué clientes fue un lote?",
             "Es la pregunta que hay que poder responder en minutos, no en días. Y la que decide si una retirada es quirúrgica o total."),
            ("¿La campaña se liquida al final?",
             "Si el coste y el ingreso solo cuadran en la liquidación, durante toda la campaña se ha ido a ciegas."),
            ("¿Los envases retornables están controlados?",
             "Suelen tratarse como si no valieran nada, y en volumen son una partida que se nota."),
        ],
        "titulo": "Agroalimentario",
        "lema": "Lotes, trazabilidad y campañas",
        "entradilla": "En alimentación la trazabilidad no es una mejora: es una obligación legal y la diferencia entre retirar un lote y retirar una marca.",
        "duele": [
            "El lote se anota en una libreta y reconstruir a quién fue lleva días.",
            "La campaña se liquida a final de temporada, cuando ya no se puede ajustar nada.",
            "Las mermas y los destríos no se registran como tales.",
            "Los envases y palés retornables no se controlan.",
        ],
        "aporta": [
            ("Lote de principio a fin", "de la entrada de materia prima al cliente que lo recibió"),
            ("Trazabilidad en los dos sentidos", "hacia atrás desde el cliente y hacia delante desde el lote"),
            ("Caducidades", "y salida por orden, no por lo que está más a mano"),
            ("Campañas", "coste e ingreso agrupados por campaña, no solo por ejercicio"),
            ("Mermas registradas", "con motivo, cuando ocurren"),
        ],
        "modulos": ["inventario", "compras", "ventas", "contabilidad", "informes"],
    },
}
