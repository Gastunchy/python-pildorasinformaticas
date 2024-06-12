# https://www.youtube.com/watch?v=2MaAs7XU2T0&t=2s

# Excepciones I

'''
Las excepciones son errores que ocurren durante la ejecucion de un programa. la sintaxis del código es correcta pero ocurre "algo inesperado".

las captura o control de excepcion se realizan para decirle al codigo que intente realizar una instruccion y si no puede, no pare el recorrido del codigo, si no, que lo continue

para ello se utiliza Try y except en la operacion o linea que puede generar error

en nuestro ejemplo la operacion division no se puede dividir por cero, por ende proboca error si pasa y se utiliza 'ZeroDivisionError' para excepcionar el error
'''

def suma(num1, num2):
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

op1=(int(input("Introduce el primer numero: ")))


op2=(int(input("Introduce el segundo numero: ")))		
	
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


print("Operacion ejecutada. Continuacion de ejecucion del programa ")