# https://www.youtube.com/watch?v=x5CY8fVyYLo

# POO IV

# Estado inicial t encapsulado

# El encapsulado hace que las propiedades de la clase, no se puedan modificar desde afuera de la clase la variable se encapsula con dos guiones bajos "__"

# Clase coche
class coche():
    def __init__(self): # Este constructor me da el estado inicial de mi clase
        pass
    # Propiedades (variables)
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False
# Comportamiento
    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos # Hace que el valor de la propiedad 'enmarca' cambie a True

        if(self.__enmarcha):
            return "El coche esta en marcha"
        else:
            return "El conche esta parado"

    def estado(self):
        print("El conche tiene", self.__ruedas, "ruedas, Un ancho de", self.__anchoChasis, "y un largo de", self.__largoChasis)

# Objeto de clase miCoche

miCoche = coche() # aqui se esta instanciando a una clase
print(miCoche.arrancar(False)) # este comportamiento cambia el estado de 'enmarcha'
miCoche.estado()
print("\n -- A continuacion creamos el segundo objeto 'coche2'--\n")

# Objeto de clase miCoche2
miCoche2 = coche()
print(miCoche2.arrancar(True))
miCoche.__ruedas=2
miCoche2.estado()