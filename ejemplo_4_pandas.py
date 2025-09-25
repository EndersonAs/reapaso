import pandas as pd


lista_productos = ["frijol","arroz","lebntejas","papa","sal"]
indices = ["a","b","c","d","e"]
series_data = pd.Series(lista_productos, indices)
print(series_data)
print("-----------------------------------------------------------------------------------------")
print(series_data[0])
print(series_data["e"])

print("-----------------------------------------------------------------------------------------")

series_data[2] = "programación"
print(series_data)


