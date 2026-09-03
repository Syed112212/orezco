/**
 * Que dibujo lleva cada pagina.
 *
 * Un diagrama por pagina, elegido porque explica lo que esa pagina
 * cuenta. Donde no hay nada que explicar visualmente no se pone ninguno:
 * un dibujo de relleno estorba mas que la falta de dibujo.
 *
 * El JSON solo dice cual y con que argumentos. El dibujo lo sigue
 * haciendo el codigo.
 */
import por from "./dibujos-por-pagina.json";
import * as D from "./dibujos";

type Llamada = { tipo: string; args: unknown[]; kw: Record<string, unknown> };

const TABLA = por as unknown as Record<string, Llamada>;

function dibuja(l: Llamada): string {
  const a = l.args;
  switch (l.tipo) {
    case "flujo":
      return D.flujo(
        a[0] as [string, string][],
        (l.kw.pie as string) ?? (a[1] as string),
        ((l.kw.actores as string[]) ?? []) as string[],
      );
    case "entrada_documentos":
      return D.entradaDocumentos(
        a[0] as string,
        (a[1] as string[]) ?? undefined,
        (a[2] as string) ?? undefined,
      );
    case "emparejar":
      return D.emparejar(
        a[0] as string[],
        a[1] as string[],
        a[2] as string,
        (a[3] as string) ?? undefined,
        (a[4] as string) ?? undefined,
      );
    case "barras":
      return D.barras(
        a[0] as number[],
        a[1] as string[],
        a[2] as string,
        (a[3] as number[]) ?? null,
      );
    case "comparacion":
      return D.comparacion(
        a[0] as string[],
        a[1] as string[],
        a[2] as string,
        (a[3] as string) ?? undefined,
        (a[4] as string) ?? undefined,
      );
    default:
      throw new Error(`dibujo desconocido: ${l.tipo}`);
  }
}

/** El dibujo de una pagina, o cadena vacia si no lleva. */
export function para(clave: string): string {
  const l = TABLA[clave];
  return l ? dibuja(l) : "";
}

/**
 * El flujo que define el servicio: el modelo lo prepara el programa, lo
 * confirma el cliente, lo presenta un asesor y el justificante vuelve.
 */
export function flujoModelo(): string {
  return dibuja(TABLA["_modelo"]!);
}
