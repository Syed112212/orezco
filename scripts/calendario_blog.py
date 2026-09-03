# -*- coding: utf-8 -*-
"""Reparte los articulos en el tiempo en vez de publicarlos de golpe.

Publicar ciento ochenta articulos el mismo dia es la senal mas clara que
puede dar un sitio de que el contenido se ha generado en masa. Google lo
trata como lo que parece, y el resto del dominio se contagia.

Un blog normal publica unas cuantas veces por semana. Aqui se hace lo
mismo: los primeros salen hoy y el resto se reparte a un ritmo constante
hacia delante. build-blog.py solo escribe los que ya tocan, asi que la
web crece sola segun pasan los dias.

No se retrasan fechas hacia atras. Fechar un articulo antes de que el
dominio existiera seria mentir, y ademas se nota.
"""
import datetime
import os

# Cuantos salen el primer dia y a que ritmo va el resto.
PRIMEROS = 14
POR_DIA = 2

# El dia en que arranco el blog. Fijo, para que las fechas no se muevan
# cada vez que se regenera.
ARRANQUE = datetime.date(2026, 9, 2)


def fecha_de(indice):
    """La fecha que le toca al articulo numero `indice` (empezando en 0)."""
    if indice < PRIMEROS:
        return ARRANQUE
    dias = (indice - PRIMEROS) // POR_DIA + 1
    return ARRANQUE + datetime.timedelta(days=dias)


def hoy():
    # Permite probar el calendario sin esperar: CONTAES_HOY=2026-11-30
    forzado = os.environ.get("CONTAES_HOY")
    if forzado:
        return datetime.date.fromisoformat(forzado)
    return datetime.date.today()


REGISTRO = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "blog", "calendario.json")


def _leer_registro():
    if os.path.exists(REGISTRO):
        import json
        with open(REGISTRO, encoding="utf-8") as f:
            return json.load(f)
    return {}


def _guardar_registro(fechas):
    import json
    os.makedirs(os.path.dirname(REGISTRO), exist_ok=True)
    with open(REGISTRO, "w", encoding="utf-8") as f:
        json.dump(dict(sorted(fechas.items())), f, ensure_ascii=False, indent=1)


def reparte(articulos):
    """Pone fecha a cada articulo y devuelve los que ya toca publicar.

    La fecha se asigna una sola vez y se guarda en blog/calendario.json.
    Si se recalculara por posicion, anadir un articulo nuevo moveria a
    todos los demas y habria articulos que aparecen y desaparecen de la
    web. Una fecha de publicacion no se mueve nunca hacia atras.

    Los que llegan nuevos se reparten entrelazando temas, para que no
    salgan cuatro de fiscalidad seguidos, y se colocan detras del ultimo
    hueco ocupado.
    """
    fechas = _leer_registro()

    nuevos = [a for a in articulos if a["slug"] not in fechas]
    if nuevos:
        por_tema = {}
        for a in nuevos:
            por_tema.setdefault(a.get("tema", "General"), []).append(a)
        for lista in por_tema.values():
            lista.reverse()
        entrelazados, temas = [], sorted(por_tema)
        while any(por_tema[t] for t in temas):
            for t in temas:
                if por_tema[t]:
                    entrelazados.append(por_tema[t].pop())

        ocupados = len(fechas)
        for i, a in enumerate(entrelazados):
            fechas[a["slug"]] = fecha_de(ocupados + i).isoformat()
        _guardar_registro(fechas)

    limite = hoy()
    publicados = []
    for a in articulos:
        a["fecha"] = fechas.get(a["slug"], fecha_de(0).isoformat())
        if datetime.date.fromisoformat(a["fecha"]) <= limite:
            publicados.append(a)
    publicados.sort(key=lambda a: (a["fecha"], a["slug"]), reverse=True)
    return publicados, len(articulos)


def resumen(total, publicados):
    if total == publicados:
        return "  %d articulos, todos publicados" % total
    ultimo = fecha_de(total - 1)
    return ("  %d articulos escritos, %d publicados hoy.\n"
            "  El resto sale a %d por dia; el ultimo, el %s."
            % (total, publicados, POR_DIA, ultimo.strftime("%d/%m/%Y")))
