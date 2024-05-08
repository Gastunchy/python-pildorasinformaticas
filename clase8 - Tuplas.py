# https://www.youtube.com/watch?v=Ufqh8aoR9hE

# Tuplas
 # En una tupla no se puede agregar ni quitar un elemento, es decir, no se pueden modificar

nombre_tupla = ("hola", "como", "estas")

print(nombre_tupla)
print(nombre_tupla[2])

# Se puede converitr una lista en tupla y viceversa
mi_lista = ["Martin", "Guzman"]
print(mi_lista)

nueva_tupla = tuple(mi_lista)

print(nueva_tupla)

# Se puede saber que indice tiene un elemento dentro de una tupla
print(nueva_tupla.index("Martin"))

# Se puede saber si un elemento esta dentro de una tupla (True or False)

consulta= "Martin" in nueva_tupla
print(consulta)

# En una tupla se pueden contar cuantas veces esta un elemento.

otra_tupla = ("Maria", "Esta", "en", "la", "casa", "de", "Maria")
print(otra_tupla)
consulta = input("Ingrese un elemento: ")
print(f"'{consulta}' se encuentra {otra_tupla.count(consulta)} veces") 

# Contar la cantidad de elementos que tiene una tupla
print (len(otra_tupla))

# Se puede tener una tupla unitaria, con un unico elemento, importante finalizar con ',' por mas que sea un solo elemento
tupla_uni_elemento = ("Gaston",)

# Desempaquetado de tupla o asignacion de los elementos de una tupla a variables
# Importante: las variables y los elementos tienen que ser la misma cantidad

tupla_datos = ("Gaston", "Farias", 40, 1983)
Nombre, Apellido, Edad, Nacimiento = tupla_datos 
print(Apellido)
print(Nombre)
print(Nacimiento)
print(Edad)