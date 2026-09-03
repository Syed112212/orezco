import { getCollection, type CollectionEntry } from "astro:content";

/**
 * Solo salen los articulos cuya fecha ya ha llegado.
 *
 * Publicar ciento noventa articulos el mismo dia es la senal mas clara
 * que puede dar un sitio de que el contenido se ha generado en masa.
 * Google lo trata como lo que parece y el resto del dominio se contagia.
 * Aqui salen dos por dia, y la fecha de cada uno esta fijada en su
 * frontmatter: no se recalcula, porque un articulo que cambia de fecha
 * aparece y desaparece de la web.
 */
export async function publicados(): Promise<CollectionEntry<"blog">[]> {
  const hoy = new Date();
  hoy.setHours(23, 59, 59, 999);
  const todos = await getCollection("blog");
  return todos
    .filter((a) => a.data.fecha <= hoy)
    .sort((a, b) => b.data.fecha.getTime() - a.data.fecha.getTime());
}

/** Los temas que hay, con cuantos articulos publicados tiene cada uno. */
export async function temas(): Promise<[string, number][]> {
  const cuenta = new Map<string, number>();
  for (const a of await publicados()) {
    cuenta.set(a.data.tema, (cuenta.get(a.data.tema) ?? 0) + 1);
  }
  return [...cuenta.entries()].sort((a, b) => b[1] - a[1]);
}

export function enEspanol(d: Date): string {
  return d.toLocaleDateString("es-ES", { day: "numeric", month: "long", year: "numeric" });
}
