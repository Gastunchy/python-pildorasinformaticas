# https://www.youtube.com/watch?v=D416qOEDrhI

# Bucles II

'''
Bucle for, recorrido de strings, tipo range, notaciones especiales con print'''

# uso de 'end=""' en print para hacer que no haga el salto o lo que querramos

""" for i in "Hola, como estas?":
    print(i,end="") # Imprime todo seguido """

""" print("-") """

""" for i in "Hola, como estas?":
    print(i,end=" ") # Imprime todo con espacio """

# Ejemplo validador de mail

""" mail = input("Ingrese su mail: ")
validador = False
for i in mail: # i recorre toda la direccion de mail
    if i=="@": # cuando i es igual a @
        validador = True # cambia a True la variable validador
if validador == True: # valida si la variable validador es True
    print("Mail correcto") # Si lo es, imprime que es correcto
else:
    print("Mail incorrecto") # Si no lo es, imprime que es incorrecto """

# Contador de letra 'a'

""" contador = input("Ingrese una palabra: ")
letra_a=0

for i in contador:
    if i=="a":
        letra_a = letra_a +1

print(f"En su oracion hay {letra_a} letras 'a'") """

# Validador de mail con @ y con .

""" mail=input("Ingrese mail: ")

contador = 0

for i in mail:
    if  (i=="@" or i=="."):
        contador = contador +1

if contador == 2:
    print("El mail es correcto")
else:
    print("El email es incorrecto") """


# Range

for i in range(6):
    print("Hola", i)