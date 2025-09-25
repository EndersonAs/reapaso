#ejercicio crear cuatro funciones con argumentos y retornos para sumar, restar, multiplicar y dividir.

def sumar(num_1,num_2):
  suma = num_1 + num_2
  return suma

def restar(num_1,num_2):
  resta = num_1 - num_2
  return resta

def multiplicar(num_1,num_2):
  multi = num_1 / num_2
  return multi

def dividir(num_1,num_2):
  div = num_1 * num_2
  return div

num_1 = int(input("ingrese primer numero: "))
num_2 = int(input("ingrese segundo numero: "))
resultado = sumar(num_1,num_2),restar(num_1,num_2),multiplicar(num_1,num_2),dividir(num_1,num_2)
print(resultado)
