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

    var cuentas = {
      "contratar": function (v, salida, eur) {
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
      ]);
      },
      "equilibrio": function (v, salida, eur) {
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
      ]);
      },
      "cobro": function (v, salida, eur) {
      var importe = v('importe'), dias = v('dias'), coste = v('coste');
      var alDia = importe * (coste / 100) / 365;
      salida([
        ['Coste por cada día de retraso', alDia],
        ['Coste de esos ' + Math.round(dias) + ' días', alDia * dias, true],
        ['Al año, si siempre cobras así', alDia * dias * (365 / Math.max(dias, 1))],
        ['Si adelantaras el cobro 15 días, ahorrarías', alDia * 15]
      ]);
      },
      "iva": function (v, salida, eur) {
      var base = v('base'), tipo = v('tipo'), total = v('total');
      var cuota = base * tipo / 100;
      var baseDesdeTotal = total / (1 + tipo / 100);
      salida([
        ['Cuota de IVA sobre ' + eur(base), cuota],
        ['Total con IVA', base + cuota, true],
        ['— — —', null],
        ['Base de ' + eur(total) + ' con IVA incluido', baseDesdeTotal, true],
        ['IVA contenido en ese total', total - baseDesdeTotal]
      ]);
      }
    };
    function recalcula() { cuentas[id](v, salida, eur); }
    caja.querySelectorAll("input").forEach(function (i) {
      i.addEventListener("input", recalcula);
    });
    recalcula();
  });
})();
