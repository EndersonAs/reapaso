#funciones en pyhton
# 1. sin argumentos y sin retorno
# 2. con argumetos y sin retorno
# 3. sin argumentos y con retornos
# 4. con argumentos y con retornos

# 1. sin argumentos y sin retorno
num_1 = 10
num_2 = 20
def sumar():
  suma = num_1 + num_2
  print(suma)

sumar()

# 2. con argumetos y sin retorno
def sumar(num_1,num_2):
  suma = num_1 + num_2
  print(suma)

sumar(30,40)

# 3. sin argumentos y con retornos
num_1 = 50
num_2 = 50
def sumar():
  suma = num_1 + num_2
  return suma

resultado = sumar()
print(resultado)
print(sumar())


# 4. con argumentos y con retornos

def sumar(num_1,num_2):
  suma = num_1 + num_2
  return suma

resultado = sumar(70,70)
print(resultado)