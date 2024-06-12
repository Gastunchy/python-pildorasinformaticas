# https://www.youtube.com/watch?v=KFz-mXB7qVI

# bucles tipo range y especiales en print (utilizacion de 'f' p/unir texto con variable)

for i in range (2,9): # Imprime desde el 2 hasta el 8
    print(f"Numero: {i}")

print("-")

for i in range (2,9,2): # Imprime desde el 2 hasta el 8, pero la 3ra opcion dice que imprima de dos en dos
    print(f"Numero: {i}")

# len= imprime la cantidad

hola = input("Ingrese el texto a contar: ")

print(f"'{hola}' tiene {len(hola)} letras")

# otra validacion con LEN

valido = False
email = input("Ingrese un email: ")

for i in range(len(email)):
    if i=="@":
        valido= True
if valido == True:
    print("Esta todo bien")
else:
    print("Poner un email valido.")
