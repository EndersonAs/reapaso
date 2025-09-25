import pandas as pd

periodos =[120,150,90,200]
indices = ["Semana_1","Semana_2","Semana_3","Semana_4"]

series_data = pd.Series(periodos, indices)
print(series_data)

print("-----------------------------------------------------------------------------------------")

total_ventas= series_data.sum()
print(f"ventas totales: {total_ventas}")

print("-----------------------------------------------------------------------------------------")

media = series_data.mean()
print(f"el promedio de ventas: {media}")

print("-----------------------------------------------------------------------------------------")

print(f"mayor venta: {series_data.max()}, menor venta: {series_data.min()}")

print("-----------------------------------------------------------------------------------------")
print("semana con con mayor y menor venta")
periodo_2 = series_data.sort_values()
print(periodo_2.index[0])
print(periodo_2.index[-1])

print("-----------------------------------------------------------------------------------------")
print("el incremento del 10%")
incremento = series_data * 1.1
print((incremento))



