# https://www.youtube.com/watch?v=cf7o4s9nFu8

# Condicionales II

# if elif else
# deben ir en ese orden, el 'elif' puede faltar, pero los otros no
#Ejercicio de ejemplo

print ("Validacion de notas")

nota = int(input("Ingrese la nota: "))

if nota < 5:
    print("No satisfactorio")
elif nota <6 :
    print("Satisfactorio")
elif nota < 7:
    print("Bueno")
elif nota <= 9:
    print("Muy bueno")
else:
    print("Excelente")