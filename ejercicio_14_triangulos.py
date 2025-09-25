#unidad 7 - ejercicio 5
lado_1= int(input("ingrese lado_1: "))
lado_2= int(input("ingrese lado_2: "))
lado_3= int(input("ingrese lado_3: "))

if lado_1 == lado_2 and lado_1 == lado_3:
  print("Es equilatero")
elif lado_1 == lado_2 and lado_1 != lado_3:
  print("Es isoceles")
elif lado_1 != lado_2 and lado_1 != lado_3:
  print("Es escaleno")