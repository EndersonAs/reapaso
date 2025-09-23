#añardir a este diccionario dos columnas (listas) una con gr(for) y kg(while) 
# 1. convertir los datos desde la columna (lista) pasarlos a cada columna creada anterior mente una con solo gr y otra con solo kg

dic = {
    "producto":["gaseosa","tablero","arroz","computador","celular"],
    "color":["negro","blanco","blanco","azul","gris"],
    "peso":["500gr","20kg","500gr","2kg","200gr", "205"]
}

print(dic)
print("-------------------------------------------------------------------")

# primera parte estahecha con el loop For

peso_gr = []
size = len(dic["peso"])

for i in range(size):
    if "kg" in (dic["peso"][i]):
        aux = 0
        aux = dic["peso"][i].replace("kg", "")
        aux = int(aux)
        peso_gr.append(aux * 1000)

    elif "gr" in (dic["peso"][i]):
        aux = 0
        aux = dic["peso"][i].replace("gr", "") #"500"
        aux = int(aux) #500
        peso_gr.append(aux)

    else:
        peso_gr.append(None)

dic["peso_gr"] = peso_gr
print(dic)

print("-------------------------------------------------------------------")


# la segunda parte esta hecha con el loop While
peso_kg = []
lista_peso = dic["peso"]
i = 0

while i < len(lista_peso):
    if "kg" in (dic["peso"][i]):
        aux = 0
        aux = dic["peso"][i].replace("kg", "")
        aux = int(aux)
        peso_kg.append(aux)

    elif "gr" in (dic["peso"][i]):
        aux = 0
        aux = dic["peso"][i].replace("gr", "") #"500"
        aux = int(aux) #500
        peso_kg.append(aux / 1000)

    else:
        peso_gr.append(None)

    i += 1


dic["peso_kg"] = peso_kg
print(dic)