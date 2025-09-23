#indexing

text = "Ella sabe Python"
print(text[0]) #validar que letra hay en cierta posisión 
print(text[3])

size = len(text)
print ("size=> ",size)
print(text[size - 1])
print(text[-1])

#slicing 

print(text[0:5]) #validar o extraer un rango de caracteres con las pociciones indicadas
print(text[10:16])
print(text[:10])
print(text[5:-1])
print(text[5:])

#con saltos
print(text[10:16:2])
print(text[::2]) # imprime de princio a fin con saltos de a 2