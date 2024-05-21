# https://www.youtube.com/watch?v=UfUM6uzl5SM

# Bucle while

# Sintaxis WHILE

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"

'''
while 'condicion':
    cuerpo del bucle
'''
""" i=1

while i<=100: # Se ejecuta mientras tanto 'i' sea menor o igual que 100
    print(f"Hola {i}")
    i=i+1 # en esto, i va a ir sumando de valor, cuando llegue a 100 el bucle se detendra """

""" # Validacion de edad
edad=int(input("Edad: "))

while edad < 0 or edad > 110:
    print (f"{RED}La edad es incorrecta{RESET}")
    edad=int(input("Edad: "))
print(f"{GREEN}OK! tu edad es de {edad} años{RESET}") """


""" import math
print ("Calculando la raiz cuadrada")
numero = int(input("Ingrese un número: "))
intentos = 0

while numero <0:
    print("Ese numero no es calculable")
    if intentos == 5:
        print("Supero los intentos")
        break
    numero = int(input("Ingrese un número: "))
    if numero<0:
        intentos=intentos+1
if intentos<5:
    solucion = math.sqrt(numero)
    print(f"La raiz cuadrada de {numero} es: {solucion}") """
