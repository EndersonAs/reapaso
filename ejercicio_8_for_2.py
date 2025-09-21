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

#diferentes print usando el metodo format => Usa .2f si quieres siempre 2 decimales exactos (bueno para dinero, promedios con exactitud fija, etc.).
print(f"{promedio_1:.2f}, {promedio_2:.2f}, {promedio_3:.2f}, {promedio_4}") #👉 .2f significa: fijo con 2 decimales.
print(f"{promedio_1:.1f}, {promedio_2:.1f}, {promedio_3:.1f}, {promedio_4}") #👉 .1f significa: fijo con 2 decimales.
print(f"{promedio_1:.4f}, {promedio_2:.4f}, {promedio_3:.4f}, {promedio_4}") #👉 .3f significa: fijo con 2 decimales.

print(f"{promedio_1:.2g}, {promedio_2:.2g}, {promedio_3:.2g}, {promedio_4}") #Usa .2g si quieres valores cortos, adaptativos (solo 2 cifras importantes).
print(f"{promedio_1:.2e}, {promedio_2:.2e}, {promedio_3:.2e}, {promedio_4}") #Usa .2e para que salga con un valor exponencial

