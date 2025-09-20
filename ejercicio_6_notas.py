#ingresar su nota par a saber que calificación tendra
nota = float(input("ingrese su nota: "))

if nota >= 9 and nota <= 10:
        print("Excelente")
elif  nota < 9 and nota >= 7.5:
        print("sobresaliente")
elif  nota < 7.5 and nota >= 6:
        print("aceptable")
elif  nota < 6 and nota >= 3:
      print("insuficiente")
elif  nota < 3 and nota >= 0:
    print("deficiente")
else:
     print("nota invalida")
