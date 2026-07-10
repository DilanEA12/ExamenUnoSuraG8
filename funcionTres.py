def crear_jugador(id, nombre, pais, edad, partidosGanados, estado):

    jugador = {
        "id": id,
        "nombre": nombre,
        "pais": pais,
        "edad": edad,
        "partidosGanados": partidosGanados,
        "estado": estado
    }

    return jugador