# https://aprendeconalf.es/docencia/python/ejercicios/tipos-datos/

# 7

""" peso = float (input("Ingrese peso (kg): "))
altura = float (input("Ingrese altura (m): "))

IMC = round (peso/(altura**2), 2)

print(f"Su indice de masa corporal es {str(IMC)}")
 """
# 8

""" n = int (input("Ingrese un numero entero: "))
m = int (input("Ingrese otro numero entero: "))
c = n//m
r = n%m
print(f"{n} entre {m} da un conciente {c} y un resto {r}") """

# 9

""" ci = float(input ("ingrese monto capital inicial: "))
ia = float(input ("Ingrese el interes anual: "))
ca = int(input ("Ingrese cantidad de años: "))
rendimiento = round ((ci * ( ia / 100 + 1) ** ca), 2)

print(f"Capital final: {rendimiento}") """

# 10

""" peso_payaso_gr = 112
peso_muñeca_gr = 75
c_m_v = int(input("Cantidad de muñecas en ultimo paquete: "))
c_p_v = int(input("Cantidad de payasos en ultimo paquete: "))

peso_paquete = (peso_payaso_gr*c_p_v)+(peso_muñeca_gr+c_m_v)

print(f"Peso de ultimo paquete: {peso_paquete}g o {round((peso_paquete/1000),3)}Kg") """

# 11

""" interes = 4
cantidad_inicial = float(input("Ingrese monto inicial: "))

print (f"Cantidad de ahorro primer año: {round((cantidad_inicial * (4/100+1)**1),2)}")
print (f"Cantidad de ahorro segundo año: {round((cantidad_inicial * (4/100+1)**2),2)}")
print (f"Cantidad de ahorro tercer año: {round((cantidad_inicial * (4/100+1)**3),2)}") """

# 12

""" fresco = 3.49
descuento = 0.6
ayer = fresco*0.60
final = fresco - ayer

pan = float(input("Cantidad vendida: "))

print (f"Precio pan fresco (habitual): {fresco} $")
print (f"Descuento realizado: {descuento*100} %")
print (f"Conste final: {round((pan*fresco*(1-descuento)),2)} $")
 """


