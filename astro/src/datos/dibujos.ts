/**
 * Diagramas que explican cada servicio sin leer.
 *
 * Una pagina que solo tiene titulo, parrafo y lista obliga a leerlo todo
 * para entender que hace la cosa. Un dibujo que se mueve lo cuenta antes.
 *
 * Reglas de estos dibujos:
 *   - Explican algo. No son adorno: cada uno muestra un flujo, una
 *     relacion o un antes y un despues que el texto tambien cuenta.
 *   - Usan el sistema visual del sitio y nada mas.
 *   - Se paran con prefers-reduced-motion, y sin animacion siguen
 *     entendiendose: la animacion subraya, no informa.
 *   - Llevan su descripcion en texto para quien no los ve.
 *
 * Traduccion literal de scripts/dibujos.py.
 */

type Paso = [string, string];

function marco(svg: string, pie: string, alto = 200, ancho = 860): string {
  return (
    '<figure class="dibujo revela">\n' +
    `  <svg viewBox="0 0 ${ancho} ${alto}" role="img" aria-label="${pie.replace(/"/g, "'")}">\n` +
    `${svg}\n  </svg>\n` +
    `  <figcaption>${pie}</figcaption>\n</figure>`
  );
}

/**
 * Un flujo de tres o cuatro pasos.
 *
 * Va en HTML y no en SVG a proposito. Estaba en SVG con las cajas
 * puestas a mano en pixeles y en el movil se escalaba entero: el texto
 * acababa en seis pixeles. En HTML se apila.
 *
 * Cuando se pasan los actores, cada paso dice encima quien lo hace. En
 * el flujo del modelo 303 eso es justo lo que hay que ver: lo que separa
 * esto de un programa suelto es que en medio hay una persona colegiada
 * que firma, y cuatro cajas iguales no lo cuentan.
 */
export function flujo(pasos: Paso[], pie: string, actores: string[] = []): string {
  const n = pasos.length;
  const piezas = pasos.map(([titulo, sub], i) => {
    const quien = actores[i] ?? "";
    const final = i === n - 1 ? " es-final" : "";
    return (
      `    <li class="fl-paso${final}">\n` +
      '      <span class="fl-nodo" aria-hidden="true"></span>\n' +
      (quien ? `      <p class="fl-actor">${quien}</p>\n` : "") +
      '      <div class="fl-tarjeta">\n' +
      `        <p class="fl-tit">${titulo}</p>\n` +
      `        <p class="fl-sub">${sub}</p>\n` +
      "      </div>\n    </li>"
    );
  });
  // El carril va fuera de la lista: un <span> suelto dentro de un <ol>
  // no es HTML valido, y ademas obligaba a contar los pasos desde el
  // segundo, que es como se descuadraron los colores.
  return (
    '<figure class="dibujo">\n  <div class="flujo-caja">\n' +
    '    <span class="fl-carril" aria-hidden="true"><i></i></span>\n' +
    `    <ol class="flujo flujo-${n}">\n${piezas.join("\n")}\n    </ol>\n` +
    `  </div>\n  <figcaption>${pie}</figcaption>\n</figure>`
  );
}

/** Papeles que caen y se convierten en apuntes. */
export function entradaDocumentos(
  pie: string,
  etiquetas: string[] = ["Factura", "Ticket", "Extracto"],
  destino = "Apunte contable",
): string {
  const filas: string[] = [];
  etiquetas.forEach((e, i) => {
    const y = 30 + i * 52;
    filas.push(
      `    <g class="cae${i ? ` cae-${i + 1}` : ""}">\n` +
        `      <rect class="caja" x="24" y="${y}" width="176" height="40" rx="8"/>\n` +
        `      <rect x="40" y="${y + 12}" width="46" height="5" rx="2.5" fill="var(--azul)" opacity=".6"/>\n` +
        `      <rect x="40" y="${y + 24}" width="120" height="4" rx="2" fill="rgba(0,0,0,.13)"/>\n` +
        `      <text class="et-p" x="210" y="${y + 25}">${e}</text>\n    </g>`,
    );
    filas.push(
      `    <path class="linea traza" style="--largo:180" d="M206 ${y + 20} C320 ${y + 20} 400 108 480 108"/>`,
    );
  });
  filas.push(
    '    <g class="sella">\n' +
      '      <rect class="caja-viva" x="490" y="62" width="346" height="92" rx="10"/>\n' +
      `      <text class="et" x="512" y="92">${destino}</text>\n` +
      '      <rect x="512" y="106" width="150" height="5" rx="2.5" fill="var(--azul)"/>\n' +
      '      <rect x="512" y="120" width="220" height="4" rx="2" fill="rgba(0,0,0,.13)"/>\n' +
      '      <rect x="512" y="132" width="180" height="4" rx="2" fill="rgba(0,0,0,.10)"/>\n    </g>',
  );
  return marco(filas.join("\n"), pie, 200);
}

/** Dos columnas que se emparejan. */
export function emparejar(
  izq: string[],
  der: string[],
  pie: string,
  tituloIzq = "Banco",
  tituloDer = "Tus apuntes",
): string {
  const filas = [
    `    <text class="et-p" x="24" y="24">${tituloIzq}</text>`,
    `    <text class="et-p" x="520" y="24">${tituloDer}</text>`,
  ];
  const n = Math.max(izq.length, der.length);
  for (let i = 0; i < n; i++) {
    const y = 40 + i * 48;
    if (i < izq.length) {
      filas.push(`    <rect class="caja" x="24" y="${y}" width="290" height="36" rx="8"/>`);
      filas.push(`    <text class="et" x="42" y="${y + 23}">${izq[i]}</text>`);
    }
    if (i < der.length) {
      filas.push(`    <rect class="caja" x="520" y="${y}" width="316" height="36" rx="8"/>`);
      filas.push(`    <text class="et" x="538" y="${y + 23}">${der[i]}</text>`);
    }
    if (i < Math.min(izq.length, der.length)) {
      filas.push(
        `    <g class="casa${i ? ` casa-${i + 1}` : ""}">\n` +
          `      <path class="linea" style="stroke:var(--azul);stroke-width:1.5" d="M320 ${y + 18} H514"/>\n` +
          `      <circle cx="417" cy="${y + 18}" r="10" fill="var(--azul-tinte)" stroke="var(--azul)" stroke-width="1.2"/>\n` +
          `      <path d="M412 ${y + 17} l4 4 6.5 -7" fill="none" stroke="var(--azul)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>\n    </g>`,
      );
    }
  }
  return marco(filas.join("\n"), pie, 40 + n * 48 + 12);
}

/** Barras que crecen: un cuadro de mando. */
export function barras(
  valores: number[],
  etiquetas: string[],
  pie: string,
  resalta: number[] | null = null,
): string {
  const filas = ['    <path class="linea" d="M24 156 H836"/>'];
  const ancho = 60;
  const hueco = (812 - ancho * valores.length) / (valores.length - 1);
  valores.forEach((v, i) => {
    const x = 24 + i * (ancho + hueco);
    const alto = Math.trunc(112 * v);
    const color = resalta === null || resalta.includes(i) ? "var(--azul)" : "rgba(0,117,222,.28)";
    filas.push(
      `    <rect class="crece${i ? ` crece-${i + 1}` : ""}" x="${Math.round(x)}" y="${156 - alto}" width="${ancho}" height="${alto}" rx="5" fill="${color}"/>`,
    );
    filas.push(
      `    <text class="et-p" x="${Math.round(x + ancho / 2)}" y="174" text-anchor="middle">${etiquetas[i]}</text>`,
    );
  });
  return marco(filas.join("\n"), pie, 186);
}

/** Antes y despues. */
export function comparacion(
  antes: string[],
  despues: string[],
  pie: string,
  titAntes = "Cómo suele ir",
  titDespues = "Cómo va aquí",
): string {
  const columna = (x: number, titulo: string, puntos: string[], vivo: boolean) => {
    const piezas = [`    <text class="et-p" x="${x + 18}" y="22">${titulo}</text>`];
    piezas.push(
      `    <rect class="${vivo ? "caja-viva" : "caja"}" x="${x}" y="32" width="394" height="${22 + puntos.length * 34}" rx="10"/>`,
    );
    puntos.forEach((p, i) => {
      const y = 62 + i * 34;
      const marca = vivo ? "var(--azul)" : "rgba(0,0,0,.22)";
      piezas.push(`    <circle cx="${x + 22}" cy="${y - 5}" r="4" fill="${marca}"/>`);
      piezas.push(`    <text class="et" x="${x + 36}" y="${y}">${p}</text>`);
    });
    return piezas.join("\n");
  };
  const alto = 32 + 22 + Math.max(antes.length, despues.length) * 34 + 16;
  return marco(
    columna(24, titAntes, antes, false) + "\n" + columna(442, titDespues, despues, true),
    pie,
    alto,
  );
}
