# https://www.youtube.com/watch?v=rDGsWYnQEJY

# operadores logicos 'and' y 'or' y operador 'in'

# Validacion con 'and'

print("Validacion de beca (and)")

distancia = int(input("Ingrese distancia en KM de su casa a escuela: "))
print(distancia)

hermanos = int(input("Ingrese la cantidad de hermanos: "))
print(hermanos)

salario = int(input("Ingrese salario familiar anual: "))
print (salario)

if distancia>40 and hermanos>2 and salario<=10000:
    print("Tiene derecho a beca")
else:
    print("No tiene derecho a beca")

# Validacion con 'or'
print("|_|")
print("Validacion de beca (or) ")

distancia = int(input("Ingrese distancia en KM de su casa a escuela: "))
print(distancia)

hermanos = int(input("Ingrese la cantidad de hermanos: "))
print(hermanos)

salario = int(input("Ingrese salario familiar anual: "))
print (salario)

if distancia>40 and hermanos>2 or salario<=10000: # aqui le emos metido un or
    print("Tiene derecho a beca")
else:
    print("No tiene derecho a beca")

# Validacion con 'in'

print("Frutas en la canasta (in)")
print ("manzana, naranja, banana, pera, mandarina")
fruta = input("Elija una fruta: ").lower()
canasta = ["manzana", "naranja", "banana", "pera", "mandarina"]

if fruta in canasta:
    print(f"Elegiste: {fruta}")
else:
    print(f"{fruta}: no esta en la canasta")