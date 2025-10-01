"""Ejemplo pråctico
La tienda tiene un archivo llamado "ventas sin.rocesar.xlsx" con los siguientes problemas:
l. Leer el archivo ventas sucias.xlsx en un DataFrame.
2. Eliminar duplicados (hay filas repetidas de "Manzanas").
3. Convertir tipos de datos:
    -Precio debe ser numérico (ej. "dos mil" -->2000).
    -Cantidad debe ser numérico (ej. "Cinco" —+ 5).
    -Fecha_Venta debe transformarse a formato fecha estándar (YYYY-MM-DD).
4. Rellenar valores faltantes en la columna Cantidad con la media de la columna.
5. Crear una columna Valor Total = Precio x Cantidad.
6. Guardar el resultado limpio en un nuevo archivo "ventas _ limpias.xlsx".
"""

import pandas as pd

print("1. importar y leer el Archivo Excel")
df_excel = pd.read_excel(r"C:\Users\ANDAP\Desktop\ventas_sin_procesar.xlsx")
print(df_excel)

print("---------------------------------------------------------------------")

#print(" importar y leer el Archivo Txt")
#df_txt = pd.read_csv(r"C:\Users\ANDAP\Desktop\ventas_sin_procesar.txt", delimiter ="\t")
#print(df_txt)

print("---------------------------------------------------------------------")
print("2. Eliminar Duplicados")
df_excel = df_excel.drop_duplicates()
print(df_excel)

print("---------------------------------------------------------------------")
print("3. convertir tipos de datos")

df_excel["Precio"][4] = 2000
df_excel["Cantidad"][1] = 5
df_excel["Fecha_Venta"] = pd.to_datetime(df_excel["Fecha_Venta"])
#df_txt["Fecha_Venta"] = pd.to_datetime(df_txt["Fecha_Venta"], format= "%d/%m/%Y") #cambio de fecha para el archivo txt
print(df_excel)

print("---------------------------------------------------------------------")
print("4. rellenar valores faltantes")

df_excel["Cantidad"][5]=int(df_excel["Cantidad"].mean())
print(df_excel)

print("---------------------------------------------------------------------")
print("5. Crear una columna Valor Total = Precio x Cantidad.")

df_excel["Valor_Tolta"]=df_excel["Cantidad"] * df_excel["Precio"]
print(df_excel)

print("---------------------------------------------------------------------")
print("6. Guardar el resultado limpio en un nuevo archivo ventas _ limpias.xlsx")

df_excel.to_excel("23. ventas_procesadas.xlsx", index=False)





