// El mapa del sitio. Es la unica lista: de aqui salen el menu, el pie y
// el sitemap, asi que anadir una pagina en un sitio la anade en los tres.
// Antes vivia en plantilla.py y esto es su traduccion literal.
import mapa from "./mapa.json";

/** [slug, nombre, pie] */
export type Entrada = [string, string, string];

export const MODULOS = mapa.modulos as Entrada[];
export const CAPACIDADES = mapa.capacidades as Entrada[];
export const SECTORES = mapa.sectores as Entrada[];
export const GESTORIA = mapa.gestoria as Entrada[];
export const CRECIMIENTO = mapa.crecimiento as Entrada[];
export const PUBLICO = mapa.publico as Entrada[];
export const RECURSOS = mapa.recursos as Entrada[];
export const EMPRESA = mapa.empresa as Entrada[];
export const LEGAL = mapa.legal as [string, string][];
export const TRAZOS = mapa.trazos as Record<string, string>;
export const DOMINIO = mapa.dominio as string;

/** El icono de un elemento del menu. Si no lo tiene, uno neutro. */
export function trazo(slug: string): string {
  return TRAZOS[slug] ?? "M5 12h14 M13 6l6 6-6 6";
}

/** Las areas del menu, en el orden en que se despliegan. */
export const AREAS: {
  nombre: string;
  base: string;
  entradas: Entrada[];
  doble?: boolean;
}[] = [
  { nombre: "Gestoría", base: "/gestoria/", entradas: GESTORIA },
  { nombre: "Crecimiento", base: "/crecimiento/", entradas: CRECIMIENTO },
  {
    nombre: "Software",
    base: "/funcionalidades/",
    entradas: [...MODULOS, ...CAPACIDADES],
    doble: true,
  },
  { nombre: "Para quién", base: "/para/", entradas: PUBLICO },
  { nombre: "Recursos", base: "/", entradas: RECURSOS },
];
