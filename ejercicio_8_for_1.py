"""ejecicio con for y dicionarios
1. calcular el promedio de notas de cada estudiante
"""
estudiantes ={
    "nombre": ["roger", "laura", "irwin"],
   "notas_1": [4, 4.2, 3.2],
   "notas_2": [3.8, 3.5, 3.9],
   "notas_3": [3.9, 4.1, 4.5],
   "notas_4": [4.5, 3.3, 4.8]
}

sum_nota_1 = 0

for i in range(len(estudiantes["notas_1"])):
    sum_nota_1 += estudiantes["notas_1"][i]

promedio_1 = sum_nota_1 / len(estudiantes["notas_1"])
print(promedio_1)
#____________________________________________________

sum_nota_2 = 0

for i in range(len(estudiantes["notas_2"])):
    sum_nota_2 += estudiantes["notas_2"][i]

promedio_2 = sum_nota_2 / len(estudiantes["notas_2"])
print(promedio_2)
#____________________________________________________

sum_nota_3 = 0

for i in range(len(estudiantes["notas_3"])):
    sum_nota_3 += estudiantes["notas_3"][i]

promedio_3 = sum_nota_3 / len(estudiantes["notas_3"])
print(promedio_3)

#____________________________________________________

sum_nota_4 = 0

for i in range(len(estudiantes["notas_4"])):
    sum_nota_4 += estudiantes["notas_4"][i]

promedio_4 = sum_nota_4 / len(estudiantes["notas_4"])
print(promedio_4)
