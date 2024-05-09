# https://www.youtube.com/watch?v=qxgEolsC6rg

# Condicionales III

# Operaciones de comparacion concatenados

# ejecicio de ejemplo

Sueldo_director = int(input("Ingrese sueldo de director: "))
print(f"Suelo de director: {Sueldo_director}")

Sueldo_gerente= int(input("Ingrese sueldo de gerente: "))
print(f"Suelo de gerente: {Sueldo_gerente}")

Sueldo_coordinador = int(input("Ingrese sueldo de coordinador: "))
print(f"Suelo de coordinador: {Sueldo_coordinador}")

Sueldo_tecnico = int(input("Ingrese sueldo de tecnico: "))
print(f"Suelo de tecnico: {Sueldo_tecnico}")

if Sueldo_tecnico<Sueldo_coordinador<Sueldo_gerente<Sueldo_director:
    print("Todo esta como correspode")
else:
    print("Se hizo justicia")