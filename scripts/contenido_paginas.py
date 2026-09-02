# -*- coding: utf-8 -*-
"""El texto de las paginas sueltas: glosario, calendario, precios, legal.

Misma regla que en contenido.py: no se inventa nada. Donde falta un dato
real -la razon social, el precio- se dice que falta, con el marcador
PENDIENTE, en vez de rellenarlo con algo verosimil.
"""

# Lo que hay que rellenar antes de publicar las paginas legales. Se
# comprueba en build-sitio.py y se avisa por consola en cada generacion.
PENDIENTE = "[PENDIENTE]"

DATOS_EMPRESA = {
    "razon_social": PENDIENTE,
    "nif": PENDIENTE,
    "domicilio": PENDIENTE,
    "correo": "info@contaes.com",
    "registro": PENDIENTE,
}

# ═════════════════════════════════════════════════════════════════════
# Glosario: terminos reales de contabilidad y fiscalidad espanola
# ═════════════════════════════════════════════════════════════════════
GLOSARIO = [
    ("Asiento contable", "contabilidad",
     "El registro de un hecho económico en el libro diario. Siempre tiene al menos una anotación al debe y otra al haber, y la suma de ambas coincide: por eso se dice que la contabilidad es de partida doble. Un asiento descuadrado no es un asiento."),
    ("Base imponible", "fiscalidad",
     "El importe sobre el que se calcula un impuesto. En una factura, lo que se cobra antes de aplicar el IVA. Es la cifra que interesa para la contabilidad de ingresos y gastos; el IVA no es ni ingreso ni gasto, es dinero que se recauda o se soporta por cuenta de la Administración."),
    ("Conciliación bancaria", "contabilidad",
     "Comparar los movimientos del extracto del banco con los apuntes contables para comprobar que dicen lo mismo. Lo que no casa suele ser un cobro parcial, una comisión sin registrar o una factura que figuraba pendiente y ya estaba cobrada."),
    ("Cuenta de pérdidas y ganancias", "contabilidad",
     "El estado que muestra ingresos y gastos de un periodo y, por diferencia, el resultado. Junto al balance de situación forma el núcleo de las cuentas anuales."),
    ("Devengo", "contabilidad",
     "El criterio por el que un ingreso o un gasto se registra cuando ocurre el hecho, no cuando se cobra o se paga. Es el criterio general en contabilidad, y es lo que hace que el resultado de un mes no coincida con el saldo del banco."),
    ("Estimación directa", "fiscalidad",
     "El régimen por el que un autónomo determina su rendimiento por la diferencia real entre ingresos y gastos deducibles. Es el régimen de quienes presentan el modelo 130. Se distingue de la estimación objetiva, conocida como módulos."),
    ("Factura rectificativa", "facturación",
     "El documento que corrige una factura ya emitida. No sustituye a la original ni la borra: la referencia e invierte lo que corresponda. Es el único modo correcto de arreglar una factura con error, y deja el rastro que una inspección espera encontrar."),
    ("IVA repercutido", "fiscalidad",
     "El IVA que cobras a tus clientes en tus facturas emitidas. No es tuyo: lo recaudas por cuenta de la Administración y lo ingresas con el modelo 303."),
    ("IVA soportado", "fiscalidad",
     "El IVA que pagas a tus proveedores en las facturas recibidas. Es deducible si la compra está afecta a la actividad y la factura cumple los requisitos formales. La diferencia entre repercutido y soportado es lo que se liquida en el 303."),
    ("Inventario permanente", "contabilidad",
     "Llevar las existencias actualizadas en tiempo real, moviendo cantidad y valor con cada entrada y salida. Lo contrario es el inventario periódico, que ajusta contra un recuento; ese ajuste es la confesión de que durante el periodo no se conocía el margen real."),
    ("Libro registro de facturas", "fiscalidad",
     "El registro obligatorio de facturas emitidas y recibidas. Es el origen de las casillas del modelo 303 y, en el resumen anual, del 390. Cuando el 390 no cuadra con la suma de los 303, casi siempre es porque hubo correcciones que no se rehicieron en el libro."),
    ("Modelo 111", "modelos",
     "Declaración trimestral de las retenciones de IRPF practicadas a trabajadores y a profesionales que facturan con retención. Sale de las nóminas y de las facturas recibidas de autónomos. Su resumen anual es el modelo 190."),
    ("Modelo 115", "modelos",
     "Declaración trimestral de las retenciones practicadas por el alquiler de inmuebles urbanos afectos a la actividad. Solo aplica si se practica retención al arrendador. Su resumen anual es el modelo 180."),
    ("Modelo 130", "modelos",
     "Pago fraccionado a cuenta del IRPF para autónomos en estimación directa. Es un adelanto sobre el rendimiento del periodo. Una sociedad no lo presenta: su equivalente es el pago fraccionado del Impuesto de Sociedades, el modelo 202."),
    ("Modelo 190", "modelos",
     "Resumen anual de retenciones e ingresos a cuenta del IRPF. Se presenta en enero y debe cuadrar con la suma de los cuatro modelos 111 del año."),
    ("Modelo 200", "modelos",
     "Declaración del Impuesto sobre Sociedades. Para ejercicios que cierran el 31 de diciembre se presenta en julio del año siguiente."),
    ("Modelo 303", "modelos",
     "Autoliquidación periódica del IVA. Recoge el IVA repercutido en las ventas y el soportado deducible en las compras; la diferencia se ingresa o queda a compensar. Es el modelo que más veces se presenta en la vida de una empresa."),
    ("Modelo 347", "modelos",
     "Declaración anual de operaciones con terceros por encima de 3.005,06 € en el año. Se presenta en febrero. Es el que más discrepancias genera, porque la otra parte declara lo mismo desde su lado y los importes tienen que casar."),
    ("Modelo 349", "modelos",
     "Declaración recapitulativa de operaciones intracomunitarias: entregas y adquisiciones de bienes y servicios con otros Estados de la Unión Europea. Su periodicidad depende del volumen de operaciones."),
    ("Modelo 390", "modelos",
     "Resumen anual del IVA. Se presenta en enero y agrega los cuatro modelos 303 del ejercicio. Si no cuadra, el problema está en los trimestres, no en el resumen."),
    ("Operación intracomunitaria", "fiscalidad",
     "Compra o venta de bienes o servicios con un empresario de otro Estado de la Unión Europea. Tiene reglas propias de tributación y exige estar dado de alta en el Registro de Operadores Intracomunitarios. Tratarla como una operación nacional descuadra el 349 y arrastra al 303."),
    ("Periodificación", "contabilidad",
     "Repartir un ingreso o un gasto entre los periodos a los que corresponde, en lugar de imputarlo entero al periodo en que se factura. Un seguro anual pagado en enero es gasto de los doce meses, no solo de enero."),
    ("Plan General Contable", "contabilidad",
     "La norma que establece en España el cuadro de cuentas, los criterios de valoración y el formato de las cuentas anuales. Existe una versión para pymes con menos exigencias de desglose."),
    ("Retención", "fiscalidad",
     "Cantidad que quien paga descuenta de la factura o la nómina y que ingresa en Hacienda a cuenta del impuesto de quien cobra. Quien retiene la declara en el 111 o el 115; quien la soporta se la descuenta en su declaración."),
    ("SII", "fiscalidad",
     "Suministro Inmediato de Información: sistema por el que determinados obligados (grandes empresas, inscritos en el REDEME y grupos de IVA) remiten a la Agencia Tributaria los registros de facturación en plazos cortos, a través de la sede electrónica."),
    ("Trazabilidad", "operaciones",
     "La capacidad de seguir el rastro de un producto hacia atrás, hasta la materia prima y el proveedor, y hacia delante, hasta el cliente que lo recibió. En alimentación y farmacia es una obligación legal, no una mejora."),
    ("VeriFactu", "fiscalidad",
     "Nombre corriente del sistema de facturas verificables previsto en el reglamento español de requisitos de los sistemas informáticos de facturación. Exige encadenamiento de los registros, huella, código QR en la factura y, en la modalidad verificable, remisión a la Agencia Tributaria."),
    ("Vencimiento", "facturación",
     "La fecha en que una factura debe estar cobrada o pagada según las condiciones pactadas. La diferencia entre la fecha de vencimiento y la de hoy es la antigüedad de la deuda, que es el dato que de verdad importa para decidir a quién reclamar primero."),
    ("Albarán", "facturación",
     "Es el documento que acompaña a la entrega de mercancías y sirve para que el comprador confirme que ha recibido el pedido. No es una factura y no tiene efectos fiscales. Su función es probar la entrega física y dejar constancia de cantidades y estado. El error típico es contabilizarlo como factura, cuando luego hay que esperar al documento definitivo."),
    ("Amortización", "contabilidad",
     "Es la forma de reflejar que una máquina, un vehículo o un equipo se gasta con el uso. Cada año contabilizas una parte de su coste como gasto. No sale dinero de la caja, pero reduce el resultado. Hay que hacerlo según la vida útil real. El error típico es amortizar todo a un año o no llevar un control individualizado de cada bien."),
    ("Autoliquidación", "fiscalidad",
     "Es la declaración que presenta el contribuyente por su cuenta, calculando la cuota del impuesto y, en su caso, pagándola. En IVA suele ser trimestral o mensual; en el impuesto de sociedades se hace una vez al año. No es un trámite informativo: si la cifra sale a ingresar, hay que pagar. Un error común es presentarla sin revisar los datos reales y luego corregir con declaraciones complementarias."),
    ("Balance de comprobación", "contabilidad",
     "Un listado que muestra los saldos de todas las cuentas del libro mayor en una fecha. Su objetivo es verificar que la suma del debe y el haber coinciden, señal de que cada apunte cuadra. No demuestra que no haya errores, pero ayuda a detectarlos. El error típico: confiar ciegamente en que si cuadra, toda la contabilidad es correcta."),
    ("Cheque conformado", "tesorería",
     "Cheque en el que el banco garantiza el pago con cargo a los fondos del librador, marcándolo como 'conformado'. El beneficiario sabe que el dinero está reservado. Se usa para pagos de importe alto o entre desconocidos. Su error típico: olvidar que la conformidad caduca, así que hay que cobrarlo antes de la fecha límite; si no, pierdes la garantía."),
    ("Cierre contable", "contabilidad",
     "Cuando termina el año, toca cuadrar la contabilidad. Hacer el cierre significa repasar todas las cuentas, ajustar gastos e ingresos pendientes y dejar preparado todo para calcular el resultado del ejercicio. Es el paso previo a presentar las cuentas anuales. El error típico: dejar cuentas con saldo que no se corresponden con la realidad del banco o de los clientes."),
    ("Confirming", "tesorería",
     "Producto bancario para gestionar pagos a proveedores. La entidad adelanta a tu proveedor el importe de la factura y tú le pagas al banco más tarde, en la fecha pactada. Así alargas el pago sin que tu proveedor espere el dinero. Su error típico: no comparar comisiones y creer que siempre las paga el proveedor; en realidad las condiciones se negocian contigo."),
    ("Coste de oportunidad", "costes",
     "Es el valor de lo que sacrificas al elegir una opción en lugar de otra. Por ejemplo, si inviertes el dinero en maquinaria en vez de en un depósito, el coste de oportunidad es el interés que no vas a cobrar. No aparece en contabilidad, pero ayuda a decidir. El error típico: olvidarlo y pensar que solo cuenta lo que pagas."),
    ("Coste fijo", "costes",
     "Un coste fijo es el que no cambia cuando suben o bajan tus ventas dentro de un margen normal. Alquiler, sueldos administrativos o seguros son ejemplos. Cuidado: fijo no significa eterno ni inmóvil; puede variar por contrato o decisión. Un error típico es pensar que si vendes más, el coste fijo total baja: en realidad baja por unidad."),
    ("Cross-docking", "operaciones",
     "Cross-docking es una técnica logística donde la mercancía que entra al almacén se prepara y se sale directamente al cliente, sin quedarse almacenada. En lugar de guardar la caja y luego buscarla, la recepcionas y se reexpide en el mismo día. Solo se usa con productos estables y pedidos planificados. El error típico es confundirlo con un simple trasvase de camiones sin control de calidad."),
    ("Cuentas anuales", "contabilidad",
     "Son el resumen completo de la vida económica de tu empresa en un ejercicio. Incluyen el balance, la cuenta de resultados y la memoria, con sus respectivos detalles. Se elaboran al cierre y se presentan ante el registro mercantil. El error típico: tratarlas como un papeleo obligatorio y no como una foto real de tu negocio, lo que lleva a no revisarlas con detalle."),
    ("Exención interior", "fiscalidad",
     "En el IVA, hay operaciones que no pagan impuesto, pero tampoco permiten deducir el IVA de las compras que las originan. Es la llamada exención plena. Otras exenciones, llamadas limitadas, sí permiten deducir. Por ejemplo, muchas actividades educativas y sanitarias están exentas plenamente. El error típico del pequeño negocio es no marcar bien la diferencia y acabar pagando de más o teniendo problemas con Hacienda."),
    ("Factoring sin recurso", "tesorería",
     "Contrato por el que vendes tus facturas pendientes a una entidad, que te adelanta el importe y asume el riesgo de impago del deudor. Si el cliente no paga, el banco no te reclama el dinero. Es más caro que el factoring con recurso. Su error típico: pensar que cubre todos los riesgos, pero suele excluir deudas disputadas o de países concretos."),
    ("Factura proforma", "facturación",
     "Es un borrador de factura que se entrega antes de cerrar una venta para que el cliente vea el importe estimado y las condiciones. No sirve para cobrar ni para contabilizar gasto o ingreso, porque no es una factura real. Solo tiene valor informativo y comercial. El error típico es tratarla como factura definitiva en la contabilidad."),
    ("Impuesto sobre Actividades Económicas", "fiscalidad",
     "Es un impuesto municipal que grava el simple hecho de ejercer una actividad. No importa si tienes beneficios: se paga por estar de alta, aunque existan exenciones para pequeños negocios y para los dos primeros años de vida. Cada ayuntamiento puede subirlo o bajarlo, y la gestión la hace el Estado. El error frecuente es olvidar darse de alta antes de empezar a facturar o pensar que solo lo pagan las grandes empresas."),
    ("Inversión del sujeto pasivo", "fiscalidad",
     "En las entregas de inmuebles o en algunas operaciones de construcción, el que compra declara el IVA en lugar del vendedor. El vendedor no le cobra el impuesto, sino que hace una factura sin cuota y quien adquiere lo autoliquida. Evita que quien no está establecido en España tenga que declarar, y previene fraudes en el sector inmobiliario. Un error típico es creer que es una exención."),
    ("Lead time", "operaciones",
     "El lead time es el tiempo que pasa desde que haces un pedido a tu proveedor hasta que recibes la mercancía en tu almacén. Incluye el tiempo de preparación del proveedor, el transporte, y los trámites de aduanas o control interno. Se mide en días o semanas. Un error típico es calcularlo solo con el transporte y olvidar el tiempo de fabricación, que casi siempre es el más largo."),
    ("Margen de contribución", "costes",
     "El margen de contribución es lo que le queda a un producto tras restar sus costes variables. Es decir, el importe que cada venta aporta para pagar los costes fijos y, después, generar beneficios. Un error típico es confundirlo con el beneficio final: si los costes fijos son altos, puede haber buen margen y pérdidas."),
    ("Orden de compra", "operaciones",
     "Una orden de compra es el documento que envía tu empresa al proveedor para pedir una mercancía o servicio, con las cantidades, precio y plazo acordados. No es el contrato, pero sirve como prueba de la operación y para que el proveedor sepa exactamente qué servir. El error típico es usarla como factura o confundirla con el albarán, que son pasos distintos."),
    ("Presupuesto", "facturación",
     "Es una oferta escrita con el precio estimado de un trabajo o producto antes de que el cliente decida aceptar. No genera ningún apunte contable ni es una factura, pero si el cliente lo acepta, puede convertirse en contrato. Conviene detallar bien el alcance y la vigencia. El error típico es dar por hecha la venta sin confirmación."),
    ("Pro rata de IVA", "fiscalidad",
     "Cuando tu negocio mezcla operaciones con y sin derecho a deducir el IVA, no puedes deducir todo lo que te han cobrado. Se aplica un porcentaje que refleja el uso real de tus compras. Ese porcentaje se estima al empezar el año y se corrige luego con los datos definitivos. El error típico es deducir el cien por cien si una parte de tu actividad está exenta."),
    ("Provisión", "contabilidad",
     "Es una cantidad que guardas contablemente para cubrir un riesgo o una obligación futura probable, pero que aún no tiene importe exacto. Por ejemplo, una reclamación o una garantía que tendrás que atender. Se registra como gasto del año cuando nace el derecho. El error típico: usar la provisión para maquillar beneficios o confundirla con una reserva de capital."),
    ("Recibo", "facturación",
     "Es el documento que acredita que alguien ha pagado una cantidad de dinero. No sustituye a la factura, porque la factura documenta la operación económica y el recibo solo confirma el pago. Es muy útil como justificante de tesorería, sobre todo en pagos en efectivo. El error típico es emitir solo un recibo sin emitir la factura correspondiente."),
    ("Regularización", "contabilidad",
     "Consiste en pasar el saldo de todas las cuentas de ingresos y gastos a la cuenta del resultado del ejercicio. Así se queda a cero y vemos si hubo beneficio o pérdida. No es inventar nada, sino reclasificar lo que ya está anotado. Un fallo común: regularizar antes de verificar que todos los apuntes están correctos, y luego no cuadrar."),
    ("Remesa de recibos", "tesorería",
     "Conjunto de recibos que entregas al banco para que cobre a tus clientes en su cuenta. Sirve para domiciliar pagos recurrentes: lo que debía cada cliente y en qué fecha se pasa. Al vencimiento, el banco envía el cargo y te abona el dinero. Su error típico: no comprobar los vencimientos antes de enviarla, porque un recibo rechazado genera comisiones."),
    ("Rotura de stock", "operaciones",
     "Cuando un producto no está disponible en el almacén para servir un pedido, se produce lo que llamamos rotura de stock. Esto implica una venta perdida o un retraso en la entrega, y suele tener un coste mayor de lo que parece. El error típico es pensar que solo se produce si no tienes nada en el almacén. También hay rotura cuando apenas quedan unidades y no llegas a reponer a tiempo."),
    ("Stock de seguridad", "operaciones",
     "El stock de seguridad es la cantidad extra de un producto que mantienes en el almacén para evitar quedarte sin él cuando hay un aumento inesperado de demanda o un retraso en el proveedor. Se calcula según tu experiencia y el margen que quieras asumir. Un error típico es fijarlo por porcentajes fijos sin tener en cuenta periodos de más ventas o incidencias."),
    ("Transferencia inmediata", "tesorería",
     "Orden de pago entre bancos que se ejecuta en segundos, cualquier día del año, y el dinero llega al instante al beneficiario. No tienes que esperar al día hábil. Funciona con límites de importe que dependen de cada entidad. Su error típico: usar la transferencia ordinaria para pagos urgentes, cuando con la inmediata evitas recargos y avisos tarde."),
    ("Umbral de rentabilidad", "costes",
     "El umbral de rentabilidad es la cifra de ventas que necesitas para no perder dinero, cubriendo todos los costes. Se calcula dividiendo los costes fijos entre el margen de contribución porcentual. Si vendes por encima, empiezas a ganar; por debajo, pierdes. El error típico: calcularlo solo con costes variables y olvidar los fijos."),
]

# ═════════════════════════════════════════════════════════════════════
# Calendario fiscal: periodos, no fechas exactas de un ano concreto
# ═════════════════════════════════════════════════════════════════════
CALENDARIO = [
    ("Enero", [
        ("303", "IVA del cuarto trimestre del año anterior"),
        ("111", "Retenciones de IRPF del cuarto trimestre"),
        ("115", "Retenciones por alquiler del cuarto trimestre"),
        ("130", "Pago fraccionado del cuarto trimestre, en estimación directa"),
        ("390", "Resumen anual de IVA del ejercicio anterior"),
        ("190", "Resumen anual de retenciones del ejercicio anterior"),
        ("180", "Resumen anual de retenciones por alquiler"),
    ]),
    ("Febrero", [
        ("347", "Operaciones con terceros por encima de 3.005,06 € del año anterior"),
    ]),
    ("Abril", [
        ("303", "IVA del primer trimestre"),
        ("111", "Retenciones de IRPF del primer trimestre"),
        ("115", "Retenciones por alquiler del primer trimestre"),
        ("130", "Pago fraccionado del primer trimestre"),
        ("202", "Pago fraccionado del Impuesto de Sociedades"),
    ]),
    ("Julio", [
        ("303", "IVA del segundo trimestre"),
        ("111", "Retenciones de IRPF del segundo trimestre"),
        ("115", "Retenciones por alquiler del segundo trimestre"),
        ("130", "Pago fraccionado del segundo trimestre"),
        ("200", "Impuesto sobre Sociedades del ejercicio cerrado el 31 de diciembre"),
    ]),
    ("Octubre", [
        ("303", "IVA del tercer trimestre"),
        ("111", "Retenciones de IRPF del tercer trimestre"),
        ("115", "Retenciones por alquiler del tercer trimestre"),
        ("130", "Pago fraccionado del tercer trimestre"),
        ("202", "Pago fraccionado del Impuesto de Sociedades"),
    ]),
]

CALENDARIO_NOTA = (
    "Los modelos trimestrales se presentan en los veinte primeros días naturales del mes "
    "siguiente al fin del trimestre, con particularidades cuando el plazo acaba en fin de "
    "semana o festivo y cuando se domicilia el pago, que adelanta la fecha límite. El modelo "
    "349 se presenta con periodicidad mensual o trimestral según el volumen de operaciones. "
    "Cuáles de estos modelos te tocan a ti depende de tu forma jurídica, tu actividad y tu "
    "volumen."
)

# ═════════════════════════════════════════════════════════════════════
# Preguntas frecuentes
# ═════════════════════════════════════════════════════════════════════
PREGUNTAS = [
    ("¿Está disponible ya?",
     "No. Contaes está en desarrollo. Lo que puedes hacer hoy es contarnos cómo trabajáis y qué os duele: eso decide qué se construye antes. No hay ninguna versión de pago ni prueba gratuita porque no habría nada que probar."),
    ("¿Qué es exactamente: un programa o una asesoría?",
     "Las dos cosas, y por eso existe. El programa lleva la gestión y la contabilidad; el servicio de asesoría revisa, firma y presenta los modelos. Un ERP solo te deja los modelos hechos pero sin presentar. Una asesoría sola no tiene tus datos al día."),
    ("¿Qué hace la IA y qué no hace?",
     "Hace lo repetitivo: leer facturas, proponer clasificación contable, responder preguntas sobre tus datos y preparar borradores. No presenta nada, no manda correos sin que alguien los apruebe y no firma. Y no inventa cifras: si un dato no está, lo dice."),
    ("¿Quién responde ante Hacienda?",
     "Una persona colegiada. La IA prepara y una persona revisa, firma y presenta. Esa responsabilidad no se puede delegar en un algoritmo, y quien te diga lo contrario te está vendiendo un riesgo."),
    ("¿Se puede migrar desde Odoo, SAP o una hoja de cálculo?",
     "Ese es el caso normal, no la excepción. La migración se plantea desde el primer día: qué datos se traen con su histórico, cuánto dura el periodo en que conviven los dos sistemas y cuál es el punto de retorno si algo sale mal. Por escrito, antes de empezar."),
    ("¿Qué pasa con nuestros datos durante el cambio?",
     "El sistema antiguo sigue vivo en solo lectura durante la convivencia, para consultar y comparar. No se apaga nada hasta que lo nuevo está funcionando y cuadrado."),
    ("¿Cuánto cuesta?",
     "Todavía no hay tarifa pública, porque el producto no está terminado y poner un precio ahora sería inventarlo. Lo que sí podemos decir es de qué dependerá: número de personas que lo usan, módulos activos y si incluye o no el servicio de asesoría."),
    ("¿Cómo empieza el proceso?",
     "Con una llamada sobre lo que usáis hoy y qué es lo que peor lleváis. Si no encajamos, se dice en esa llamada y no en la tercera. Si encajamos, la siguiente es una demo sobre vuestro caso, no una presentación genérica."),
    ("¿Sirve para autónomos?",
     "Depende del caso. Un autónomo sin empleados ni almacén probablemente necesite algo más ligero que un ERP completo. Un autónomo con equipo, stock y proyectos sí encaja. Es una de las cosas que se aclara en la primera llamada."),
    ("¿Y si necesitamos algo muy específico de nuestro sector?",
     "Hay procesos muy particulares (fabricación compleja, normativa sectorial concreta) que hoy no cubrimos. Preferimos decirlo antes que después de la demo."),
]
