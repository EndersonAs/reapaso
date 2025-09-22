text ="Ella sabe programar python"
print("javascript" in text) # con el metodo "in" podemos validar si una palabra esta dentro de una cadena de texto
print("python" in text)

if "JS" in text:
    print("elejiste bien")
else:
    print("buen comienzo")

size = len("amor") # metodo para contar el numero de caracteres inlcuyendo los espacios
print(size)
size_2 = ("desamor")
print(len(size_2))

print(text)
print(text.upper()) #convertir texto en mayuscula
print(text.lower()) #convertir texto en minuscula
print(text.count("a")) # contar cuantos veces aparece un caracter
print(text.swapcase()) # convertir al contrario el texto de min a mayus y al contrario
print(text.startswith("Ella")) #validar se ina cadena empieza con alguna palabra
print(text.endswith("python")) #validar se una cadena termina con alguna palabra
print(text.replace("python", "Go")) #Remplazar una pabra por otra

text_2 = "este es un texto"
print(text_2)
print(text_2.capitalize) # poner la primera palabra en mayus de la cadena de texto
print(text_2.title) # dejar acada palabra con mayuscula en el inicio
print(text_2.isdigit) # validar si la cadena es un posible digito




