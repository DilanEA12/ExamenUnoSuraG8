from funcionUno import registrar_usuario
from funcionDos import validar_credenciales
from funcionTres import crear_jugador
from funcionCuatro import mostrar_jugadores
from funcionCinco import ordenar_jugadores

usuarios = []

correo = input("Ingrese un correo: ")
password = input("Ingrese una contraseña: ")

usuarios.append(registrar_usuario(correo, password))

if validar_credenciales(3, usuarios):

    jugadores_tenis = []

    jugadores_tenis.append(crear_jugador(1,"Carlos Alcaraz","España",22,[10,9,8],"ACTIVO"))
    jugadores_tenis.append(crear_jugador(2,"Novak Djokovic","Serbia",38,[12,11,10],"ACTIVO"))
    jugadores_tenis.append(crear_jugador(3,"Jannik Sinner","Italia",23,[8,10,9],"ACTIVO"))
    jugadores_tenis.append(crear_jugador(4,"Alexander Zverev","Alemania",28,[7,6,8],"ACTIVO"))
    jugadores_tenis.append(crear_jugador(5,"Daniil Medvedev","Rusia",29,[9,8,7],"LESIONADO"))
    jugadores_tenis.append(crear_jugador(6,"Casper Ruud","Noruega",26,[6,7,8],"ACTIVO"))
    jugadores_tenis.append(crear_jugador(7,"Holger Rune","Dinamarca",22,[5,7,6],"LESIONADO"))
    jugadores_tenis.append(crear_jugador(8,"Taylor Fritz","Estados Unidos",27,[8,7,9],"ACTIVO"))
    jugadores_tenis.append(crear_jugador(9,"Andrey Rublev","Rusia",27,[9,10,8],"ACTIVO"))
    jugadores_tenis.append(crear_jugador(10,"Stefanos Tsitsipas","Grecia",26,[7,8,9],"ACTIVO"))

    while True:

        print("\n===== MENÚ =====")
        print("1. Gestionar jugadores de tenis")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            print("\n1. Mostrar jugadores")
            print("2. Ordenar jugadores por partidos ganados")

            opcion2 = input("Seleccione una opción: ")

            if opcion2 == "1":
                mostrar_jugadores(jugadores_tenis)

            elif opcion2 == "2":
                ordenar_jugadores(jugadores_tenis)
                mostrar_jugadores(jugadores_tenis)

            else:
                print("Opción inválida")

        elif opcion == "2":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida.")