import { MODULOS, CAPACIDADES } from "./mapa";

/** Un identificador estable a partir de un titulo de seccion. */
export function ancla(texto: string): string {
  const s = texto
    .normalize("NFKD")
    .replace(/[̀-ͯ]/g, "")
    .replace(/[^a-zA-Z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .toLowerCase();
  return s.slice(0, 48) || "seccion";
}

/** El nombre de una pagina de software a partir de su slug. */
export function nombreDe(slug: string): string {
  const s = slug.replace(/\/$/, "");
  const m = [...MODULOS, ...CAPACIDADES].find(([x]) => x.replace(/\/$/, "") === s);
  return m ? m[1] : s;
}

/**
 * El nombre de la pagina y su lema, sin decirlo dos veces.
 *
 * Salia "Contabilidad. Contabilidad al dia, sin esperas ni sorpresas".
 * El lema de varias paginas empieza por el nombre, y cuando eso pasa el
 * nombre sobra: ya esta en la miga, en la etiqueta y en la pestana.
 */
export function titular(titulo: string, lema: string): string {
  if (lema.toLowerCase().startsWith(titulo.toLowerCase())) return lema;
  return `${titulo}. <span style="color:var(--grafito);font-weight:500">${lema}</span>`;
}

/** Ficha de organizacion para los datos estructurados. */
export function fichaOrganizacion() {
  return {
    "@type": "ProfessionalService",
    "@id": "https://contaes.com/#organizacion",
    name: "Contaes",
    url: "https://contaes.com/",
    description:
      "Gestoría online para autónomos, startups y pymes: contabilidad, impuestos, nóminas y contratos, con software propio incluido.",
    areaServed: "ES",
    availableLanguage: "es",
  };
}

export function fichaMigas(pasos: [string | null, string][]) {
  return {
    "@type": "BreadcrumbList",
    itemListElement: pasos.map(([ruta, nombre], i) => ({
      "@type": "ListItem",
      position: i + 1,
      name: nombre,
      ...(ruta ? { item: `https://contaes.com${ruta}` } : {}),
    })),
  };
}

export function fichaServicio(
  nombre: string,
  descripcion: string,
  ruta: string,
  tipo: "Service" | "SoftwareApplication" = "Service",
) {
  return {
    "@type": tipo,
    name: nombre,
    description: descripcion,
    url: `https://contaes.com${ruta}`,
    provider: { "@id": "https://contaes.com/#organizacion" },
    ...(tipo === "SoftwareApplication"
      ? { applicationCategory: "BusinessApplication", operatingSystem: "Web" }
      : {}),
  };
}

export function fichaFaq(preguntas: [string, string][]) {
  return {
    "@type": "FAQPage",
    mainEntity: preguntas.map(([q, r]) => ({
      "@type": "Question",
      name: q,
      acceptedAnswer: { "@type": "Answer", text: r },
    })),
  };
}
