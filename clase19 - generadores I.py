# https://www.youtube.com/watch?v=TLVnoqXGWpY

# Generadores I

'''
un generador en Python es una función que devuelve un objeto iterable que produce una secuencia de valores a medida que se itera sobre él, utilizando la palabra clave yield en lugar de return. Los generadores permiten manejar grandes conjuntos de datos de manera eficiente, ya que generan los valores bajo demanda y no almacenan toda la secuencia en memoria.
'''

def pares(limite):
    num = 1
    while num<limite:
        yield num*2
        num+=1

devuelve_pares = pares(95)
# entre llamada y llamada, el objeto generador entra en pausa hasta la siguiente llamada
print(next(devuelve_pares))
print(next(devuelve_pares))
# entre llamada y llamada, el objeto generador entra en pausa hasta la siguiente llamada
print(next(devuelve_pares))
print(next(devuelve_pares))
# entre llamada y llamada, el objeto generador entra en pausa hasta la siguiente llamada
print(next(devuelve_pares))
print(next(devuelve_pares))
# entre llamada y llamada, el objeto generador entra en pausa hasta la siguiente llamada
print(next(devuelve_pares))
print(next(devuelve_pares))
# entre llamada y llamada, el objeto generador entra en pausa hasta la siguiente llamada
print(next(devuelve_pares))
print(next(devuelve_pares))
# entre llamada y llamada, el objeto generador entra en pausa hasta la siguiente llamada
print(next(devuelve_pares))
print(next(devuelve_pares))
# entre llamada y llamada, el objeto generador entra en pausa hasta la siguiente llamada
print(next(devuelve_pares))
print(next(devuelve_pares))
print(next(devuelve_pares))
print(next(devuelve_pares))
print(next(devuelve_pares))
print(next(devuelve_pares))
print(next(devuelve_pares))
print(next(devuelve_pares))
print(next(devuelve_pares))
print(next(devuelve_pares))


