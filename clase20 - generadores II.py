# https://www.youtube.com/watch?v=ucaHqGII350

# Generadores II

# yield from (busca los elementos dentro de un elemento)

# Funcion generador que devuelva ciudades

def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        yield from elemento

ciudades_devueltas=devuelve_ciudades("Cordoba", "CPaz", "Chascomus", "Chacarita")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))


