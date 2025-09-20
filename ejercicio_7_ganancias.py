""" Con el siguiente diccionario 
1. obtener las ventas totales de cada producto 
2. calcular la ganacia de 20%
"""
inventario = {
    "producto": ["gaseosa", "arroz", "frijos", "gansito"],
    "precio_uni": [3000, 3500, 5000,2500],
    "cantidad": [100, 120, 50, 80]
}
print(inventario)

inventario["ventas_totales"] = inventario["precio_uni"][0] * inventario["cantidad"][0], \
                                inventario["precio_uni"][1] * inventario["cantidad"][1], \
                                inventario["precio_uni"][2] * inventario["cantidad"][2], \
                                inventario["precio_uni"][3] * inventario["cantidad"][3]



inventario["ganancia"] = inventario["ventas_totales"][0] * 1.2, inventario["ventas_totales"][1] * 1.2, inventario["ventas_totales"][2] * 1.2, inventario["ventas_totales"][3] * 1.2

print(inventario)