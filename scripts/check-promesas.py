# -*- coding: utf-8 -*-
"""Busca en el sitio promesas que no podemos sostener.

    python scripts/check-promesas.py

Con ciento setenta articulos y sesenta paginas, casi todo el texto lo
redacto una maquina a partir de un brief. Una maquina no sabe que no
tenemos aplicacion movil, ni certificaciones, ni clientes que citar: si el
tono lo pide, lo escribe.

Esto no juzga estilo. Busca frases que un cliente podria reclamarnos
despues, que son de tres clases:

  1. Cosas que decimos tener y no tenemos.
  2. Cifras sobre nosotros o sobre el mercado que nadie puede comprobar.
  3. Garantias absolutas, que en fiscalidad no existen.
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ─────────────────────────────────────────────────────────────────────
# Cada regla: nombre, patron, y por que importa.
# ─────────────────────────────────────────────────────────────────────
REGLAS = [
    ("producto que no existe",
     r"\b(nuestra|la nuestra|contaes) (app|aplicaci[oó]n)\b|"
     r"\bnuestra aplicaci[oó]n m[oó]vil\b|\bdescarga (la|nuestra) app\b",
     "No hay aplicacion movil: hay un programa web que funciona en el movil. "
     "Prometer una app es de lo que despues alguien reclama."),

    ("certificacion que no tenemos",
     r"\b(certificad[oa]s?|acreditad[oa]s?)\s+(en\s+)?(ISO|SOC|ENS)\b|"
     r"\bcumplimos (con )?(la )?ISO\b|\bnivel bancario\b",
     "No tenemos ISO 27001 ni SOC 2, y la pagina de seguridad lo dice. "
     "Presumir de una certificacion que no existe descalifica al proveedor."),

    ("cliente o caso inventado",
     r"\b(nuestros|los) clientes (dicen|opinan|coinciden)\b|"
     r"\bcaso de [eé]xito\b|\bm[aá]s de \d+ (clientes|empresas|usuarios)\b|"
     r"\b(cientos|miles) de (clientes|empresas|usuarios)\b",
     "No hay clientes que citar, ni testimonios, ni casos. Ponerlos seria mentir."),

    ("cifra de mercado sin fuente",
     r"\b(el|un)\s+\d{1,3}\s*(?:%|por ciento)\s+de\s+(las|los)\s+(empresas|pymes|aut[oó]nomos)\b|"
     r"\bseg[uú]n (un )?estudio\b|\blas estad[ií]sticas (dicen|muestran)\b",
     "Una estadistica sin fuente en una web de contabilidad envejece mal y "
     "no se puede defender si alguien pregunta."),

    ("garantia absoluta",
     r"\bgarantizamos que (nunca|jam[aá]s|no)\b|\bcero errores\b|"
     r"\bsin ning[uú]n riesgo\b|\bnunca (m[aá]s )?(tendr[aá]s|vas a tener) (un )?problema\b|"
     r"\b100\s*%\s*(seguro|garantizado|libre)\b",
     "En fiscalidad no hay garantias absolutas. Lo que se puede prometer es "
     "que el error se cuenta en cuanto se detecta."),

    ("precio dicho de pasada",
     r"\bdesde \d+\s*(€|euros)\s*(al mes|\/mes|mensuales)\b|"
     r"\bcuota de \d+\s*(€|euros)\b|\bgratis para siempre\b",
     "No hay tarifa publicada. Si aparece un precio suelto en un articulo, "
     "contradice a la pagina de precios."),

    ("integracion que no hay",
     r"\b(nos )?integramos? (ya |directamente )?con [A-Z][a-z]+|"
     r"\bconexi[oó]n directa con (Stripe|Shopify|Amazon|PayPal|Holded|Odoo|Sage)\b",
     "Las conexiones se montan caso por caso. Nombrar una concreta como si "
     "estuviera hecha promete trabajo que no esta hecho."),
]


def texto_de(html):
    s = re.sub(r"<(script|style)\b.*?</\1>", " ", html, flags=re.S | re.I)
    s = re.sub(r"<nav\b.*?</nav>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<footer\b.*?</footer>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", s)


def paginas():
    saltar = {".git", "scripts", "assets", ".github", "__pycache__"}
    for base, dirs, ficheros in os.walk(RAIZ):
        dirs[:] = [d for d in dirs if d not in saltar]
        for f in sorted(ficheros):
            if f.endswith(".html") and not f.startswith("google"):
                yield os.path.relpath(os.path.join(base, f), RAIZ).replace(os.sep, "/")


def main():
    hallados = []
    for rel in paginas():
        visible = texto_de(io.open(os.path.join(RAIZ, rel), encoding="utf-8",
                                   errors="replace").read())
        for nombre, patron, _por_que in REGLAS:
            for m in re.finditer(patron, visible, re.I):
                antes = visible[max(0, m.start() - 90):m.start()]
                # Lo que va negado o entrecomillado no es una promesa: es
                # justo lo contrario, decir que eso no lo hacemos.
                if re.search(r"(no|nunca|jam[aá]s|sin|ning[uú]n|tampoco|"
                             r"deja de|evita|no es para)[^.]{0,70}$", antes, re.I):
                    continue
                if re.search(r"[«\"][^»\"]{0,60}$", antes):
                    continue
                frase = visible[max(0, m.start() - 60):m.end() + 60].strip()
                hallados.append((nombre, rel, " ".join(frase.split())))

    print("Promesas: lo que no podriamos sostener")
    print("=" * 62)
    if not hallados:
        print("  Nada que no podamos defender.")
    else:
        por_regla = {}
        for nombre, rel, frase in hallados:
            por_regla.setdefault(nombre, []).append((rel, frase))
        for nombre, casos in sorted(por_regla.items(), key=lambda x: -len(x[1])):
            porque = next(p for n, _pat, p in REGLAS if n == nombre)
            print()
            print("  %s  (%d)" % (nombre.upper(), len(casos)))
            print("    %s" % porque)
            for rel, frase in casos[:4]:
                print("      %-40s ...%s..." % (rel[:40], frase[:88]))
            if len(casos) > 4:
                print("      ... y %d mas" % (len(casos) - 4))
    print("=" * 62)
    print("%d frase(s) que revisar" % len(hallados))
    return 1 if hallados else 0


if __name__ == "__main__":
    sys.exit(main())
