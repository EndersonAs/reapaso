#buscar el nombre de "lucia" dentro de la matrix e indicar si se encuentra  o no.
nombre = [
    ["ana", "luis", "carlos"],
    ["maria", "jorge", "lucia"],
    ["pedro", "sofia", "elena"]
]

buscar = "lucia"
encontrado = False

for i in range(len(nombre)):
    for j in range(len(nombre)):
        if nombre[i][j] == buscar:
            print(f"{buscar} Se encuentra en la matrix")
            encontrado = True
            break

if not encontrado:
    print(f"{buscar} No se encuentra en la matrix")