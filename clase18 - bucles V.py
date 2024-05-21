# https://www.youtube.com/watch?v=c8WCRTU4udo

# Bucles, Instrucciones: continue, pass, else

# Continue: salta una vuelta de bucle
# Pass: devuelve nule en cuanto se lee en una instruccion en el bucle
# else: lo mismo que en un condicional if

""" # Ejemplode cantinue:

for i in "Python":
    if i == "h":
        continue # cuando i valga H ignora la linea del print y continua
    print(f"Viendo la letra {i}")

 # Contador de solo letras
nombre = "pildoras informaticas"
contador = 0

for i in nombre:
    if i ==" ":
        continue
    contador+=1
print(contador) """

""" # ejemplo pass

class miClase:
    pass # para implementar mas tardes """
    
# Ejemplo de ELSE

email = input("Introduce mail: ")

for i in email:
    if i == "@":
        arroba = True
        break;
else:
    arroba=False
print(arroba)



