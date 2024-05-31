# https://aprendeconalf.es/docencia/python/ejercicios/cadenas/

# Ejercicio 1

'''
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
'''
""" nombre = input("Ingrese nombre: ")
numero = int(input("Ingrese numero: ")) """

    # opcion 1
# print((nombre + "\n") * numero)

    # opcion 2

""" for i in range(numero):
    print(nombre) """

# Ejecicio 2

'''
Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
'''

""" nombre = input("Ingrese nombre completo: ")

print(nombre.lower())
print(nombre.upper())
print(nombre.title())
 """

# Ejercicio 3

'''
Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.
'''

""" nombre = input("Ingrese nombre: ")

print(f"{nombre.upper()} tiene {len(nombre)} letras") """

# Ejercicio 4

'''
Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
'''

""" numero=input("Numero telefonico completo: ")

print(numero[4:-3]) """

# Ejercicio 5

'''
Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.
'''

""" frase=input("Ingrese frase: ")

print(frase[::-1]) """

# Ejecricio 6

'''
Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
'''

""" frase = input("Ingrese una frase: ")
vocal = input("Ingrese una vocal: ")

print(frase.replace(vocal, vocal.upper()))
print(frase.replace(vocal,"3")) """

# Ejercicio 7

'''
Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
'''

""" mail= input("Ingrese su mail: ")

print(mail[:mail.find("@")]+"@ceu.es") """

# Ejercicio 8

'''
Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
'''

""" precio = input("Ingrese precio: ")

print(f"{precio[:precio.find(".")]} euros con {precio[precio.find(".")+1:]} centavos") """

# ejercicio 9

'''
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
'''

""" fecha_nacimiento = input("Fecha de nacimiento (DD/MM/AA): ")

dia = fecha_nacimiento[:fecha_nacimiento.find("/")]
mes_año = fecha_nacimiento[fecha_nacimiento.find("/")+1:]
mes = mes_año[:mes_año.find("/")]
año = mes_año[mes_año.find("/")+1:]
print(f"Dia: {dia}\nMes: {mes}\nAño: {año}") """

# Ejercicio 10

'''
Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
'''
""" producto = (input("Ingrese productos separados por coma: ")).split(","and", ")

print("Lista de productos: ")
for i in producto:
    print(f"- {i.title()}") """

# Ejercicio 11

'''
Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
'''

""" producto = input("Ingrese el producto: ")
precio = float(input("Ingrese precio: "))
unidades = int(input("Ingrese unidades: "))

print(f"{producto}, cuesta ${precio}, tenemos {unidades}, precio total acumulado ${(precio*unidades):.2f}") """


