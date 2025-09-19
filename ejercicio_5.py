#pedir un usuario y contraseña, de no ser validos mostrar cual no es valido

usuario = input("ingrese el usuario: ")
contraseña = int(input("ingrese una contraseña de 4 numeros: "))

if contraseña == 1234 and usuario == "david":
    print("acceso permitido")
else:
    if contraseña != 1234 and usuario == "david":
        print("contraseña incorrecta")
    elif  usuario != "david" and contraseña == 1234:
        print("usuario incorrecto")
    else:
        print("contraseña y usuario incorrecto")
