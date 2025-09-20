""""Otra forma de resolver el ejercicio 8, usando un solo ciclo for."""

estudiantes ={
    "nombre": ["roger", "laura", "irwin"],
   "notas_1": [4, 4.2, 3.2],
   "notas_2": [3.8, 3.5, 3.9],
   "notas_3": [3.9, 4.1, 4.5],
   "notas_4": [4.5, 3.3, 4.8]
}

sum_nota_1 = 0
sum_nota_2 = 0
sum_nota_3 = 0
sum_nota_4 = 0

for i in range(len(estudiantes["notas_1"])):
    sum_nota_1 += estudiantes["notas_1"][i]
    sum_nota_2 += estudiantes["notas_2"][i]
    sum_nota_3 += estudiantes["notas_3"][i]
    sum_nota_4 += estudiantes["notas_4"][i]


promedio_1 = sum_nota_1 / len(estudiantes["notas_1"])
promedio_2 = sum_nota_2 / len(estudiantes["notas_2"])
promedio_3 = sum_nota_3 / len(estudiantes["notas_3"])
promedio_4 = sum_nota_4 / len(estudiantes["notas_4"])

print(f"{promedio_1}, {promedio_2}, {promedio_3}, {promedio_4}")

