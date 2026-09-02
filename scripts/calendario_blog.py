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


def reparte(articulos):
    """Pone fecha a cada articulo y devuelve solo los que ya toca publicar.

    El orden importa: se mezcla por temas para que dos articulos del mismo
    area no salgan seguidos, que es como se ve un blog escrito por
    personas y no una lista volcada por orden de generacion.
    """
    por_tema = {}
    for a in articulos:
        por_tema.setdefault(a.get("tema", "General"), []).append(a)
    for lista in por_tema.values():
        lista.reverse()

    entrelazados, temas = [], sorted(por_tema)
    while any(por_tema[t] for t in temas):
        for t in temas:
            if por_tema[t]:
                entrelazados.append(por_tema[t].pop())

    limite = hoy()
    publicados = []
    for i, a in enumerate(entrelazados):
        a["fecha"] = fecha_de(i).isoformat()
        if fecha_de(i) <= limite:
            publicados.append(a)
    # los mas nuevos primero
    publicados.sort(key=lambda a: a["fecha"], reverse=True)
    return publicados, len(entrelazados)


def resumen(total, publicados):
    if total == publicados:
        return "  %d articulos, todos publicados" % total
    ultimo = fecha_de(total - 1)
    return ("  %d articulos escritos, %d publicados hoy.\n"
            "  El resto sale a %d por dia; el ultimo, el %s."
            % (total, publicados, POR_DIA, ultimo.strftime("%d/%m/%Y")))
