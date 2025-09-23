#imprimir de la lista _1 solo los campos 0,2,4 en una nueva lista

lista_1 = ["jonier","camilo","brayan","jualiana","ana"]
i = 0
lista_2 = []

while i < len(lista_1):
  if i == 0 or i == 2 or i == 4:
    lista_2.append(lista_1[1])
  i += 1

print(lista_1)
print(lista_2)