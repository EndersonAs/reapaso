#recibir una lista
#hacer una funcion para  el promedio
#hacer una funcion para  el maximo
#hacer una funcion para  el minimo
#hacer una funcion que ejecute todo el codigo y lo imprima en un diccionario


valores = [2, 4, 9, 5, 3, 8]


def promedio():
  suma = 0
  for var in valores:
    suma += var
  media = suma / len(valores)
  return media

def maximo():
  maximo = valores[0]
  for elem in valores:
    if elem > maximo:
      maximo = elem
  return maximo

def minimo():
  minimo = valores[0]
  for elem in valores:
    if elem < minimo:
      minimo = elem
  return minimo

##Falta hacer el ultimo punto de imprmir en un diccionario. 

def main():
  data = [promedio(), maximo(),minimo()]

  print(data)


main()