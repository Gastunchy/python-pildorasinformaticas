# https://aprendeconalf.es/docencia/python/ejercicios/tipos-datos/

# 1
print("¡Hola Mundo!.")

# 2
variable = "¡Hola Mundo!."
print(variable)

# 3
nombre = input("Pone tu nombre carnero: ")
print(f"Hola {nombre}")

# 4
# op 1
suma = 3+2
mult = 2*5
div = suma / mult
expo = div**2

print(expo)

# op 2
print(((3+2)/(2*5))**2)

# 5

hora = float(input("Cantidad de horas: "))
costo = float(input("Costo de la hora: "))

print(f"Paga correspondiente: {hora * costo}")

# 6

n = int(input("Ingrese numero entero: "))

suma = (n * (n + 1))/2

print (suma)