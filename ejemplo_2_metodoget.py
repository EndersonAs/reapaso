#Ejemplos de como usar el metodo get y el metodo keys.

dic = {
    "producto":["gaseosa","tablero","arroz","computador","celular"],
    "color":["negro","blanco","blanco","azul","gris"],
    "peso":["500gr","20kg","500gr","2kg","200gr"]
}

#Ejemplos con metodo .get

valor = dic.get("color")           #imprime el valor de esa clave en este caso la lista completa
print(valor)
print("------------------------------------------")

valor_1 = dic.get("color",[])[2]   #imprime un valor especifico de la lista.
print(valor_1)

print("------------------------------------------")
valor_2 = dic.get("color",[])[3]   #imprime un valor especifico de la lista.
print(valor_2)

print("------------------------------------------")
#Ejemplos con metodo .keys

claves = dic.keys()                     #imprime las claves de un diccionario mas no el contenido de cada clave. 
print(f"las claves del diccionario dic sn: {claves}")