def ordenar_jugadores(jugadores_tenis):

    jugadores_tenis.sort(key=lambda x: sum(x["partidosGanados"]))

    return jugadores_tenis