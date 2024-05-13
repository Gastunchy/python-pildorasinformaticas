# Ejercicios de Condicionales
# https://aprendeconalf.es/docencia/python/ejercicios/condicionales/

# Ejercicio 1
'''
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
'''

""" edad = int(input("Ingrese edad: "))

if edad < 0 or edad> 100:
    print ("Edad erronea")
elif 0 < edad < 18:
    print("Usted es menor de edad")
else:
    print ("Usted es mayor de edad") """

# Ejercicio 2

''' Escribir un programa que almacene la cadena de caracteres 'contraseña' en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.'''

""" password = "contraseña"

validacion = input("Ingrese contraseña: ").lower()

if password == validacion:
    print("Correcto")
else:
    print("Incorrecto!") """

# Ejercicio 3

''' Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.'''

""" print ("Ingrese dos numeros")
numero1 = int(input("1er numero: "))
numero2 = int(input("2do numero: "))

if numero1 == 0:
    print("La division no se puede realizar.")
else:
    print(f"Resultado de la division: {numero1 / numero2}") """

# Ejercicio 4

'''Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.'''

""" print("Validacion de número par o impar")
numero = int(input("Ingrese un número: "))

if (numero % 2) == 0:
    print (f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar") """

# Ejercicio 5

'''
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

'''
""" edad = int(input("Ingrese su edad: "))
salario = float(input("Ingrese su salario: "))

if 100 > edad > 16 and salario >= 1000:
    print ("Usted si tributa.")
else:
    print("Usted no tributa.") """

# Ejercicio 6

'''
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
'''

""" print("Clasificacion de grupos")
nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo (M/F): ").lower()


if (sexo == "f" and nombre.lower() < "m") or (sexo == "m" and nombre.lower() < "n"):
    print("Usted pertenece al Grupo A.")
else:
    print("Usted pertenece al Grupo B.") """

# Ejercicio 7

'''
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

Renta	Tipo impositivo
Menos de 10000€	5%
Entre 10000€ y 20000€	15%
Entre 20000€ y 35000€	20%
Entre 35000€ y 60000€	30%
Más de 60000€	45%
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
'''

""" renta=float(input("Ingrese su renta anual: "))

if renta <= 10000:
    print("Usted debe pagar 5%")
elif (renta >= 10001) and (renta <= 20000):
    print("Usted debe pagar 15%")
elif (renta >= 20001) and (renta <= 35000):
    print("Usted debe pagar 20%")
elif (renta >= 35001) and (renta <= 60000):
    print("Usted debe pagar 30%")
else:
    print("Usted debe pagar 45%") """

# Ejercicio 8

'''
En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

Nivel	Puntuación
Inaceptable	0.0
Aceptable	0.4
Meritorio	0.6 o más
Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.
'''

""" print("\nPuntuacion\n")

puntuacion = float(input("Ingrese puntuacion: "))
valor = 2400

print(f"Su puntuacion es: {puntuacion}")
Inaceptable	= 0.0
Aceptable = 0.4
Meritorio = 0.6

if puntuacion == Inaceptable:
    nivel = "Inaceptable"
elif puntuacion == Aceptable:
    nivel = "Aceptable"
elif puntuacion >= 0.6:
    nivel = "Meritorio"
else:
    nivel = ""

if nivel == "":
    print("Esta puntuacion es invalida")
else:
    print(f"Tu puntuacion es {puntuacion}")
    print(f"Te corresponde cobrar {puntuacion*valor}") """

# Ejercicio 9

'''
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
'''

""" edad = int(input("Ingrese la edad: "))

if edad <= 4:
    print("Ingresa gratis.")
elif edad > 4 and edad <= 18:
    print("Debe pagar 5€")
else:
    print("Debe pagar 10€") """

# or

""" if edad<=4:
    precio = 0
elif edad <= 18:
    precio = 5
else:
    precio = 10
print(f" El precio de la entrada es {precio}€") """

# Ejercicio 10

'''
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
'''
t_pizza = input("Tipo de pizza (Normal / Vegetariana): ").lower()

if t_pizza == "vegetariana":
    print("\nUsted eligió vegetariana, elija ingredientes:")
    ing = (input("- Tofu \n- Pimiento\n-> ")).lower()
    if ing == "tofu":
        ingrediente = "Tofu"
    else:
        ingrediente = "Pimiento"
else:
    print("\nUsted eligió normal, elija ingredientes:")
    ing = (input("- Peperoni \n- Jamon\n- Salmon \n-> ")).lower()
    if ing == "peperoni":
        ingrediente = "peperoni"
    elif ing == "jamon":
        ingrediente = "Jamon"
    else:
        ingrediente = "Salmon"
        
print (f"Su tipo de pizza es: {t_pizza} y los ingredientes son Mozzarella, tomate y {ingrediente}")