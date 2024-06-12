# https://aprendeconalf.es/docencia/python/ejercicios/bucles/

# Ejercicio 1

'''
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
'''

""" palabra = input("Ingrese una palabra: ")

for i in range(10):
    print(palabra) """

# Ejercicio 2

'''
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
'''
""" edad = int(input("Ingrese su edad: "))

for i in range(edad):
    print(f"Usted cumplio: {i+1} años") """

# Ejercicio 3

'''
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
'''

""" numero = int(input("Numero: "))

for i in range(1,numero+1,2):
    print(i, end=", ") """

# Ejercicio 4

'''
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
'''

""" n = int(input("Numero entero positivo: "))

for i in range(n,-1,-1):
    print(i, end=", ")
 """

# Ejercicio 5

'''
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
'''

""" monto = float(input("Ingrese un monto a invertir: "))
interes = float(input("Ingrese el interes anual: "))
año = int(input("Ingrese cantidad de años: "))

for i in range(año):
    i+=1
    rendimiento = round ((monto *(interes / 100 + 1)**i), 2)
    print(f"año: {i}, Rendimiento: {rendimiento}") """

# Ejercicio 6

'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
'''

""" numero = int(input("Numero entero: "))
a="*"
x=0

for i in range(numero):
    x+=1
    print(f"{a*x}")

print("\nOtra opcion\n")

for i in range(numero):
    print("*"*(i+1)) """

# Ejercicio 7

'''
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
'''
""" for i in range(1,11):
    for j in range(1,11):
        print(i*j, end="\t")
    print("") """

# Ejercicio 8

'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
'''
""" numero = int(input("Ingrese un numero: "))

for i in range(1,numero+1,2):
    for j in range(i,0,-2):
        print(i,end="")
    print("") """

# Ejercicio 9

'''
Escribir un programa que almacene la cadena de caracteres 'contraseña' en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
'''
""" contraseña = "contraseña"
key =""

while contraseña!=key:
    key = input("Ingrese la contraseña: ")
print("Contraseña correcta") """