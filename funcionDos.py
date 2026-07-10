def validar_credenciales(numero_intentos, usuarios):

    contador = 0

    while contador < numero_intentos:

        correo = input("Correo: ")
        password = input("Contraseña: ")

        for usuario in usuarios:

            if usuario["correo"] == correo and usuario["password"] == password:
                print("Login exitoso")
                return True

        contador += 1

        if contador < numero_intentos:
            print("Credenciales incorrectas. Intentos restantes:", numero_intentos-contador)

    print("Cuenta bloqueada temporalmente")
    return False