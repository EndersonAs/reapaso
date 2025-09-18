"""
Ejercicio 2 - Listas
1. Crea una lista ue contenga al menos 6 números enteros, donde al nos números se repitan.
2. Muestra en pantalla el primer y el último elemento de la lista.
3. Agrega un nuevo número al final de Ia lista. (append)
4. Muestra cuántos elementos hay en la lista. (len).
5. Muestra cuál es el número más grande y cuál es el más pequeño de Ia lista. (sort)
6. Muestra cuántas veces aparece un número específico (elige tú cuál). (count)
7. Muestra cuántas veces aparece un número específico (elige tú cuál). (count)
8. Muestra en qué posición aparece por primera vez ese mismo número. (index)"""


# --------------------------------------------------------------------------
# punto 1
lista_1 = [24, 25, 35, 47, 58, 69, 58, 24, 12]
print(lista_1)
#punto 2 
print(lista_1[0], "primer elemento", lista_1[-1], "último elemento")
#punto 3 
lista_1.append(72)
print(lista_1) 
#punto 4 
print(len(lista_1))
#punto 5 
lista_1.sort()
print("Este es elemento menor: ", lista_1[0], "Este es el elemento mayor: ", lista_1[-1])
#punto 6 
suma = sum(lista_1)
print("Suma total es: ", suma)
#punto 7 
print(lista_1.count(58), "Repetidos") 
#punto 8 
print("El índice es: ", lista_1.index(35))
