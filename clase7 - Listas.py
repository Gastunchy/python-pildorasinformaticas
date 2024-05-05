# https://www.youtube.com/watch?v=Q8hugySbLQQ

# Listas
mi_lista = ["Maria", "Pepe", "Marta", "Antonio"]

# Impresion de la lista completa
print(mi_lista)
print(mi_lista[:])

# Impresion de un elemento de la lista indicando el indice 2=Marta
print(mi_lista[2])

# Impresion de una porsion de la lista, en este caso estamos imprimieno desde el 0 hasta el 3 y este ultimo se excluye
print(mi_lista[0:3])

# otras opciones
print(mi_lista[:5])
print(mi_lista[2:])

# Agregar un elemento al final de la lista
mi_lista.append("Gaston")
print(mi_lista)

# Agregar elemento indicando el indice donde queremos agregar
mi_lista.insert(2,"Facundo")
print(f"Lista completa: {mi_lista}")
print(f"Solo el indice 2: {mi_lista[2]}")

# Agregar varios elementos a la lista
mi_lista.extend(["Cristian", "Valeria"])
print(f"Nuenva lista: {mi_lista}")

# Saber el indice de un elemento de la lista
# Importante, si un dato se repite, se muestra el indice que tiene el primer dato
print(f"En que indice esta 'Gaston': {mi_lista.index("Gaston")}")

# Para saber si un elemento esta en la lista se puede usar eñ siguiente comando
print(f"Cristian se encuentra en la lista: {"Cristian" in mi_lista}")

# Una lista acepta todo tipo de dato/elemento, texto, numeros enteros, numeros decimales, valores buleanos
lista_full = ["Hola", 2, 0.9, True]
print(lista_full)
print(lista_full[2])

# Remover un elemento especifico de la lista
mi_lista.remove("Gaston")
print(mi_lista)

# Eliminar el ultimo elemento de una lista
mi_lista.pop()
print(mi_lista)

# Sumar listas para tener una sola
lista_nueva=mi_lista+lista_full
print(lista_nueva)

# Tambien se pueden multiplicar las listas, en este ejemplo x 10

lista_multiplicada = lista_nueva * 10

print(lista_multiplicada)