# https://www.youtube.com/watch?v=dLH-oay4Bts

# Excepciones III

'''
En este vídeo vemos como lanzar excepciones bajo una condición con el uso de la instrucción "raise".
Para más cursos, ejercicios y manuales visita: https://www.pildorasinformaticas.es
'''

""" def evaluaEdad (edad):
    if edad<0:
        raise ZeroDivisionError("No se permiten edades negativas")

    if edad <20:
        return "Eres muy joven"
    elif edad<40:
        return "Eres joven"
    elif edad<65:
        return "Eres maduro"
    elif edad<100:
        return "Cuidate..."
    
print(evaluaEdad(-12)) """

# otro ejemplo

import math

def CalculaRaiz(num1):
    if num1<0:
        raise ValueError ("El numero no puede ser negativo")
    else:
        return math.sqrt(num1)

op1 = float(input("Numero: "))

try:
    print(CalculaRaiz(op1))
except ValueError as ErrorDeCero:
    print(ErrorDeCero)
print("Programa terminado")
    