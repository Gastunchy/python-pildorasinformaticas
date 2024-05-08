# https://www.youtube.com/watch?v=iV-4F0jGWak
# Condicionales I
# Instrucciones IF

print("Programa de evaluacion de nota de alumnos")

nota_alumno = int(input("Nota: "))

def evaluacion(nota):
    valoracion="Aprobado"
    if nota<5:
        valoracion="suspenso"
    return valoracion

print (evaluacion(nota_alumno)) 