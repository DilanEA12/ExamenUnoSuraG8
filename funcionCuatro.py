def mostrar_jugadores(jugadores_tenis):

    for jugador in jugadores_tenis:

        print("-------------------------")
        print("ID:", jugador["id"])
        print("Nombre:", jugador["nombre"])
        print("País:", jugador["pais"])
        print("Edad:", jugador["edad"])
        print("Partidos ganados:", jugador["partidosGanados"])
        print("Estado:", jugador["estado"])