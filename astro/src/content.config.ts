import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

// Los articulos. El cuerpo es HTML dentro de un .md: viene de un
// generador que ya escribia HTML, y markdown lo deja pasar tal cual.
const blog = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/blog" }),
  schema: z.object({
    titulo: z.string(),
    descripcion: z.string(),
    entradilla: z.string(),
    tema: z.string(),
    acento: z.string().optional(),
    minutos: z.number(),
    // La fecha se fija una vez y no se mueve nunca hacia atras: un
    // articulo que cambia de fecha aparece y desaparece de la web.
    fecha: z.date(),
  }),
});

export const collections = { blog };
