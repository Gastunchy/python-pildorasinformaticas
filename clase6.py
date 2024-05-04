# https://www.youtube.com/watch?v=vawEHhV_HFA
# Funciones II

""" def suma(num1, num2):
    print(num1+num2)
# importante al momento de llamar, se deben declarar los parametros    
suma(1,2,0,0,0) """

# Otra variable

def suma2(num1,num2):
    resultado= num1+num2
    return resultado
# el uso de print nos es util para que se muestre el resultado y asi ver que el programa funciona
print(suma2(2,2))

# Tambien podemos almacenar el valor de return en una variable e imprimir esa variable

almacena_resultado = suma2(3,5)
print(f"valor que esta almacenado en una variable del return: {almacena_resultado}")
