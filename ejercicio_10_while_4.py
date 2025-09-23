#imprimir la lista_1 de forma contraria. 

lista_1 = ["jonier","camilo","brayan","jualiana","ana"]
i = len(lista_1) - 1
lista_2 = []

while i != -1:
  lista_2.append(lista_1[i])
  i -= 1


print(lista_1)
print(lista_2)