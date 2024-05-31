# https://www.youtube.com/watch?v=HH3c6ZBvSx8

# Excepciones II

'''
Continuamos agregando excepciones, en este caso, capturar varias excepciones y el uso de clausula finally y while para 
'''

# continuamos con el codigo de la clase anterior

""" def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):
	try:
		return num1/num2
	except ZeroDivisionError:
		print("No se puede dividir un numero por cero")
		return "Operacion erronea"

# While para que mientras no sea verdad continue, try para que trate y except para capturar el error y permitir que el codigo continue
while True:
	try:
		op1=(int(input("Introduce el primer numero: ")))
		op2=(int(input("Introduce el segundo numero: ")))
		break
	except ValueError:
		print("Ingesta de datos erroneo")
		print("Intentar de nuevo.")
 
operacion=input("Introduce la operacion a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operacion no contemplada")


print("Operacion ejecutada. Continuacion de ejecucion del programa ") """

# Otro ejemplo de excepciones multiples

""" def division():
    try:
        primer_n = float(input("Ingrese primer numero: "))
        segundo_n = float(input("Ingrese segundo numero: "))
        resultado = primer_n/segundo_n
        print(f"El resultado es {resultado}")
        print("Operacion finalizada")
    except  ValueError:
        print("Valor agregado erroneo")
    except ZeroDivisionError:
        print("No se puede dividir por valor cero")

while True:
    division() """

# Ejemplo de excepcion generica

""" def division():
    try:
        primer_n = float(input("Ingrese primer numero: "))
        segundo_n = float(input("Ingrese segundo numero: "))
        resultado = primer_n/segundo_n
        print(f"El resultado es {resultado}")
        print("Operacion finalizada")
    except: # Se pone sin el error/tipo de excepcion, captura excepcion general
        print("Hubo un error, intenta nuevamente")

while True:
    division() """

# Opcion de poner finally, esto hace que se imprima un resultado de try pase o no el error

""" def division():
    try:
        primer_n = float(input("Ingrese primer numero: "))
        segundo_n = float(input("Ingrese segundo numero: "))
        resultado = primer_n/segundo_n
        print(f"El resultado es {resultado}")
        print("Operacion finalizada")
    except  ValueError:
        print("Valor agregado erroneo")
    except ZeroDivisionError:
        print("No se puede dividir por valor cero")
    finally: # Si bien esto imprime algo, puede ser usado para cerrar una base de datos, se pueda o no hacer una transaccion
        print("Esto esta finalizado")

while True:
    division()  """

# Otro uso de finally, util para cerrar un codigo Try

try:
    numero=int(input("Ingrese un numero: ")) # Si ingresas una letra el codigo falla
    print(numero)
finally: # Pero el finally se ejecuta igual y si no esta el try falla
    print("Esto es porno")