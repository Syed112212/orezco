# -*- coding: utf-8 -*-
"""Calculadoras que funcionan en la propia pagina.

Cuatro cuentas que un empresario hace a mano en una servilleta y casi
siempre mal. Aqui se hacen bien y se explica de donde sale cada numero.

Regla de siempre: no se inventa nada. Ninguna calculadora trae tipos ni
porcentajes puestos por nosotros. Los tipos de cotizacion y de IVA cambian
y dependen del caso, asi que los pone quien calcula y cada herramienta lo
dice. Lo que aportamos es la formula y la explicacion, que es donde la
gente se equivoca.

Todo en JavaScript sin librerias: se calcula al teclear, sin enviar nada a
ninguna parte.
"""

CALCULADORAS = [
    {
        "id": "contratar",
        "titulo": "Cuánto cuesta de verdad contratar a alguien",
        "entradilla": "El salario bruto no es el coste. A eso se le suma lo que la empresa "
                      "cotiza por esa persona, y es la cifra que sale de la cuenta cada mes.",
        "campos": [
            ("bruto", "Salario bruto anual", "€", 24000, 1000),
            ("pagas", "Número de pagas", "", 14, 1),
            ("cotiza", "Tipo de cotización a cargo de la empresa", "%", 32, 0.1),
            ("extras", "Otros costes anuales (formación, equipo, seguro…)", "€", 600, 100),
        ],
        "formula": """
      var bruto = v('bruto'), cotiza = v('cotiza'), extras = v('extras'), pagas = v('pagas') || 12;
      var seguridad = bruto * cotiza / 100;
      var total = bruto + seguridad + extras;
      salida([
        ['Salario bruto anual', bruto],
        ['Cotización de la empresa', seguridad],
        ['Otros costes', extras],
        ['Coste total anual', total, true],
        ['Coste medio al mes', total / 12],
        ['Lo que cobra en cada paga (bruto)', bruto / pagas]
      ]);""",
        "nota": "El tipo de cotización a cargo de la empresa depende del grupo, del contrato y "
                "de la actividad, y cambia cada año. Ponlo tú o pregúntanoslo: el que traiga "
                "esta casilla por defecto es solo un punto de partida para ver la mecánica.",
        "explica": [
            "El error habitual es negociar sobre el bruto y descubrir después que la nómina "
            "cuesta a la empresa bastante más. La cotización a cargo de la empresa no aparece "
            "en la nómina que ve el trabajador, pero sale de la misma cuenta.",
            "Y falta lo que no es dinero: el tiempo hasta que la persona es productiva. Eso no "
            "se calcula, pero conviene contarlo antes de decidir.",
        ],
    },
    {
        "id": "equilibrio",
        "titulo": "Tu punto de equilibrio",
        "entradilla": "Cuánto tienes que vender para no perder dinero. Es la primera cifra que "
                      "debería saber cualquiera que tenga costes fijos.",
        "campos": [
            ("fijos", "Costes fijos al mes (alquiler, sueldos, cuotas…)", "€", 6000, 100),
            ("precio", "Precio medio de venta por unidad", "€", 100, 5),
            ("variable", "Coste variable por unidad", "€", 60, 5),
        ],
        "formula": """
      var fijos = v('fijos'), precio = v('precio'), variable = v('variable');
      var margen = precio - variable;
      if (margen <= 0) {
        salida([['Con ese precio pierdes dinero en cada venta', 0, true]]);
        return;
      }
      var unidades = Math.ceil(fijos / margen);
      salida([
        ['Margen de contribución por unidad', margen],
        ['Porcentaje sobre el precio', margen / precio * 100, false, '%'],
        ['Unidades al mes para no perder', unidades, true, 'ud'],
        ['Facturación al mes para no perder', unidades * precio],
        ['Cada unidad de más aporta', margen]
      ]);""",
        "nota": "Los costes fijos son los que no cambian aunque vendas más o menos, dentro de "
                "un rango normal. Si dudas de si algo es fijo o variable, pregúntate qué pasaría "
                "con esa factura si el mes que viene no vendieras nada.",
        "explica": [
            "El margen de contribución es lo que queda de cada venta después de pagar lo que "
            "esa venta consume. Es lo que va cubriendo los costes fijos, y cuando los cubre "
            "entero, empieza el beneficio.",
            "Subir precios mueve esta cifra mucho más rápido que vender más unidades, porque "
            "el precio afecta al margen y las unidades solo al volumen.",
        ],
    },
    {
        "id": "cobro",
        "titulo": "Lo que te cuesta cobrar tarde",
        "entradilla": "El dinero que está en una factura sin cobrar no es tuyo todavía, y "
                      "mientras esperas te cuesta algo. Esto pone número a ese algo.",
        "campos": [
            ("importe", "Importe pendiente de cobro", "€", 20000, 500),
            ("dias", "Días que tardan en pagarte de media", "días", 75, 5),
            ("coste", "Coste de tu financiación al año", "%", 7, 0.5),
        ],
        "formula": """
      var importe = v('importe'), dias = v('dias'), coste = v('coste');
      var alDia = importe * (coste / 100) / 365;
      salida([
        ['Coste por cada día de retraso', alDia],
        ['Coste de esos ' + Math.round(dias) + ' días', alDia * dias, true],
        ['Al año, si siempre cobras así', alDia * dias * (365 / Math.max(dias, 1))],
        ['Si adelantaras el cobro 15 días, ahorrarías', alDia * 15]
      ]);""",
        "nota": "El coste de tu financiación es el interés de tu póliza de crédito, o lo que te "
                "costaría pedir ese dinero. Si no tienes financiación, sigue habiendo un coste: "
                "es lo que no puedes hacer con ese dinero mientras no lo tienes.",
        "explica": [
            "Con este número en la mano, un descuento por pronto pago deja de ser una pérdida y "
            "se convierte en una cuenta: si el descuento cuesta menos que la espera, sale a "
            "cuenta ofrecerlo.",
            "Y sirve para lo contrario: saber cuánto te está costando de verdad ese cliente "
            "grande que paga a noventa días.",
        ],
    },
    {
        "id": "iva",
        "titulo": "IVA de una factura, al revés y del derecho",
        "entradilla": "Del importe sin IVA al total, o del total al importe sin IVA. La segunda "
                      "es la que se hace mal: no se resta el porcentaje, se divide.",
        "campos": [
            ("base", "Importe sin IVA", "€", 1000, 50),
            ("tipo", "Tipo de IVA", "%", 21, 1),
            ("total", "O al revés: importe total con IVA", "€", 1210, 50),
        ],
        "formula": """
      var base = v('base'), tipo = v('tipo'), total = v('total');
      var cuota = base * tipo / 100;
      var baseDesdeTotal = total / (1 + tipo / 100);
      salida([
        ['Cuota de IVA sobre ' + eur(base), cuota],
        ['Total con IVA', base + cuota, true],
        ['— — —', null],
        ['Base de ' + eur(total) + ' con IVA incluido', baseDesdeTotal, true],
        ['IVA contenido en ese total', total - baseDesdeTotal]
      ]);""",
        "nota": "El tipo lo pones tú porque depende de lo que vendas. Y hay operaciones exentas, "
                "otras con inversión del sujeto pasivo y comercios en recargo de equivalencia: "
                "si tu caso no es el normal, esta cuenta no basta.",
        "explica": [
            "Sacar la base de un total con IVA no es restar el porcentaje. A un total de 121 con "
            "IVA del 21 % no se le quita el 21 % de 121: se divide entre 1,21. La diferencia son "
            "casi cinco euros en ese ejemplo, y crece con el importe.",
            "El IVA no es ni ingreso ni gasto: lo recaudas o lo soportas por cuenta de la "
            "Administración, y la diferencia entre los dos es lo que se liquida.",
        ],
    },
]


def bloque(c):
    campos = []
    for nombre, etiqueta, unidad, defecto, paso in c["campos"]:
        sufijo = ('<span class="calc-u">%s</span>' % unidad) if unidad else ""
        campos.append(
            '        <label class="calc-campo">\n'
            '          <span>%s</span>\n'
            '          <span class="calc-caja"><input type="number" inputmode="decimal" '
            'id="%s-%s" value="%s" step="%s" min="0">%s</span>\n'
            '        </label>' % (etiqueta, c["id"], nombre, defecto, paso, sufijo))

    explica = "".join("<p>%s</p>" % x for x in c["explica"])
    return '''  <section class="seccion" id="%(id)s">
    <div class="wrap estrecho">
      <h2 style="margin-top:0">%(titulo)s</h2>
      <p class="cuerpo" style="margin:8px 0 22px;max-width:62ch">%(entradilla)s</p>

      <div class="calc" data-calc="%(id)s">
        <div class="calc-campos">
%(campos)s
        </div>
        <output class="calc-salida" aria-live="polite"></output>
      </div>

      <div class="aviso">%(nota)s</div>
      <div class="prosa" style="margin-top:22px">%(explica)s</div>
    </div>
  </section>''' % {
        "id": c["id"], "titulo": c["titulo"], "entradilla": c["entradilla"],
        "campos": "\n".join(campos), "nota": c["nota"], "explica": explica,
    }


def indice():
    filas = "".join(
        '        <li><a href="#%s">%s</a></li>\n' % (c["id"], c["titulo"])
        for c in CALCULADORAS)
    return ('    <nav class="calc-indice" aria-label="Las calculadoras">\n'
            '      <ol>\n%s      </ol>\n    </nav>' % filas)


def cuerpo():
    return "\n\n".join(bloque(c) for c in CALCULADORAS)


ESTILOS = '''
/* ── Calculadoras ────────────────────────────────────────────
   Se calcula al teclear y no se envia nada a ninguna parte: la
   cuenta ocurre en el navegador de quien la hace.              */
.calc{
  background:var(--blanco);border:1px solid var(--borde);border-radius:var(--r-card);
  padding:24px;display:grid;gap:22px;
}
.calc-campos{display:grid;gap:14px}
.calc-campo{display:grid;gap:7px;font-size:14.5px;color:var(--grafito)}
.calc-caja{display:flex;align-items:stretch;border:1px solid var(--borde);
  border-radius:var(--r-btn);overflow:hidden;background:var(--papel);max-width:22rem}
.calc-caja:focus-within{border-color:var(--azul);box-shadow:0 0 0 3px var(--azul-tinte)}
.calc-caja input{
  flex:1 1 auto;min-width:0;font:inherit;font-size:16px;font-variant-numeric:tabular-nums;
  color:var(--tinta);background:var(--blanco);border:0;padding:11px 13px;
}
.calc-caja input:focus{outline:0}
.calc-u{
  flex:0 0 auto;display:grid;place-items:center;padding:0 13px;
  font-size:14px;color:var(--piedra);border-left:1px solid var(--borde);
}
.calc-salida{display:grid;gap:0;border-top:1px solid var(--borde);padding-top:4px}
.calc-fila{
  display:flex;justify-content:space-between;align-items:baseline;gap:18px;
  padding:11px 0;border-bottom:1px solid var(--borde);font-size:15.5px;color:var(--grafito);
}
.calc-fila:last-child{border-bottom:0}
.calc-fila b{
  font-size:17px;font-weight:600;color:var(--tinta-fuerte);
  font-variant-numeric:tabular-nums;white-space:nowrap;
}
.calc-fila.fuerte{background:var(--azul-tinte);margin:0 -12px;padding:13px 12px;
  border-radius:var(--r-btn);border-bottom:0}
.calc-fila.fuerte b{color:#004a91}
.calc-fila.raya{border-bottom:0;padding:4px 0}
.calc-indice{margin:26px 0 8px}
.calc-indice ol{margin:0;padding-left:20px;display:grid;gap:8px;color:var(--piedra)}
.calc-indice a{color:var(--azul);text-decoration:none;font-weight:500}
.calc-indice a:hover{text-decoration:underline}
@media(min-width:720px){.calc-campos{grid-template-columns:1fr 1fr;gap:14px 20px}}
'''

JS = '''
/* -- Las calculadoras ----------------------------------------
   Se recalcula al teclear. Nada se envia: la cuenta ocurre aqui.
   Si el JavaScript no va, quedan los campos y la explicacion,
   que es la mitad del valor de la pagina.                     */
(function () {
  var euro = new Intl.NumberFormat("es-ES", {style: "currency", currency: "EUR",
                                             maximumFractionDigits: 2});
  var numero = new Intl.NumberFormat("es-ES", {maximumFractionDigits: 2});

  function eur(x) { return euro.format(isFinite(x) ? x : 0); }

  document.querySelectorAll(".calc").forEach(function (caja) {
    var id = caja.getAttribute("data-calc");
    var out = caja.querySelector(".calc-salida");

    function v(nombre) {
      var e = document.getElementById(id + "-" + nombre);
      var n = e ? parseFloat(String(e.value).replace(",", ".")) : 0;
      return isFinite(n) ? n : 0;
    }
    function salida(filas) {
      out.innerHTML = filas.map(function (f) {
        if (f[1] === null) return '<div class="calc-fila raya"></div>';
        var unidad = f[3];
        var valor = unidad === "%" ? numero.format(f[1]) + " %"
                  : unidad === "ud" ? numero.format(f[1]) + " ud."
                  : eur(f[1]);
        return '<div class="calc-fila' + (f[2] ? " fuerte" : "") + '">' +
               "<span>" + f[0] + "</span><b>" + valor + "</b></div>";
      }).join("");
    }

    var cuentas = {CUENTAS};
    function recalcula() { cuentas[id](v, salida, eur); }
    caja.querySelectorAll("input").forEach(function (i) {
      i.addEventListener("input", recalcula);
    });
    recalcula();
  });
})();
'''


def js():
    cuentas = ",\n      ".join(
        '"%s": function (v, salida, eur) {%s\n      }' % (c["id"], c["formula"])
        for c in CALCULADORAS)
    return JS.replace("{CUENTAS}", "{\n      %s\n    }" % cuentas)
