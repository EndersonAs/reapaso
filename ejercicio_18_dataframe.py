#clase de dataframe
import pandas as pd

data = {
    "nombre":["ana","luis","carlos"],
    "edad":[25,30,30],
    "ciudad":["Bogota","medellin","cali"]
}

df_data = pd.DataFrame(data)
print(data)
print("-------------------------------------------------------------")
nombre_luis = df_data["nombre"][1]  #aqui a estas variables creadas le asignamos la ruta o el indexado de los datos de luis 
edad_luis = df_data["edad"][1]
ciudad_luis = df_data["ciudad"][1]

#imprimimos las variables anterior mente asignadas
print(f"nombre: {nombre_luis}, edad: {edad_luis}, y su ciudad es {ciudad_luis}") 

print("-------------------------------------------------------------")
#imprimimos la misma información pero desde el diccionario
print(f"nombre: {df_data['nombre'][1]}, edad: {df_data['edad'][1]}, y su ciudad es {df_data['ciudad'][1]}") 

