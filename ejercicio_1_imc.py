
"""
1 Solicitar al usuario que ingrese 
   - su nombre -tipo str
   - su edad -tipo int
   - su altura  -tipo float
   - su peso -tipo float
2 Al final el programa debe imprimir 
    - un saludo con su nombre
    - si es mayor o menor de edad
    *-su edad, altura y peso
    - su índice de masa corporal (IMC), que se calcula como: IMC = peso / (altura ** 2)
   """

nombre =(input("ingrese su nombre: "))
edad = int(input("ingrese su edad: "))
altura = float(input("ingrese su altura en metros: "))
peso = float(input("ingrese su peso en kg: "))

print("Hola", nombre)
print(f"Tienes {edad} años, tu altura es {altura}, y  pesas {peso} kg.")

if edad > 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

imc = peso / (altura ** 2)
print(f"Tu índice de masa corporal (IMC) es: {imc}")