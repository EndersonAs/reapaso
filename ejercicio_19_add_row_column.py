import pandas as pd 

carros = {
    "marca":["reanult","suzuki","mazda"],
    "modelo":["logan","swift","cx30"],
    "año":[2018,2020,2023]
}

df_carros =pd.DataFrame(carros)
print(df_carros)
print("-----------------------------------------------------------------------------------")

df_carros["precio"] = ["$20'000.000","$30'000.000","$28'000.000",] #agregar una columna.
df_carros.loc[len(df_carros)]= ["toyota", "corola", 2021, "$55'000.000"] #agregar una fila
print(df_carros)
