# https://www.youtube.com/watch?v=2OmgHl8lp0I

# Diccionario

mi_diccionario = {
    "Alemania":"Berlin",
    "Francia":"Paris",
    "Reino unido":"Londres",
    "España":"Madrid"}

print(mi_diccionario)
print(mi_diccionario["Alemania"])

# Agregar un elemento al diccionario

mi_diccionario["Argentina"]="BsAs"
print(mi_diccionario)

# Imprimir el diccionario en formato json
import json

print(json.dumps(mi_diccionario, indent=4))

# Se puede modificar el valor de una clave poniendo la clave y añadiendo un valos nuevo

mi_diccionario["Argentina"]="Cordoba"

print(f"Nuevo valor de 'Argentina' en el diciconario: \n    {mi_diccionario}")

# Se puede eliminar un elemento

del mi_diccionario["Argentina"]

print(json.dumps(mi_diccionario, indent=2))

# Se puede usar una tupla como clave para un diccionario

mi_tupla = ("Nombre", "Apellido")
mi_diccionario ={mi_tupla[0]:"Gaston", mi_tupla[1]:"Farias"}

print (mi_diccionario)

# Una clave puede tener varios valores, esto se logra con una tupla/lista

mi_diccionario = {"Nombre":"Gaston", "Apellido":"Farias","Titulos":("TSIA", "ACE")}

print(json.dumps(mi_diccionario, indent=3))

# Tambien se puede guardar un diccionario en otro diccionario

diccionario1 = {"Nombre":"Gaston","Apellido":"Farias", "Estudios":{"TSIA":2008,"ACE":2022}}
print (json.dumps(diccionario1, indent=3))

# Otros datos para imprimir

print(diccionario1.keys()) # Imprime las claves
print(diccionario1.values()) # Imprime los valores
print(diccionario1.items()) # Im