# https://www.youtube.com/watch?v=OU-e2uhoGxE

# POO V

# Repaso de bloqueo

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
            chequeo=self.chequeo_interno()

        if(self.__enmarcha and chequeo):
            return "El coche esta en marcha"
        elif(self.__enmarcha and chequeo==False):
            return "Algo a ido mal en el chequeo"
        else:
            return "El conche esta parado"

    def estado(self):
        print("El conche tiene", self.__ruedas, "ruedas, Un ancho de", self.__anchoChasis, "y un largo de", self.__largoChasis)

    def chequeo_interno(self):
        print("Realizando chequeo interno")

        self.gasolina="OK"
        self.aceite="OK"
        self.puertas="Cerrada"

        if (self.gasolina=="OK" and self.aceite=="OK" and self.puertas=="Cerrada"):
            return True
        else:
            return False



# Objeto de clase miCoche

miCoche = coche() # aqui se esta instanciando a una clase
print(miCoche.arrancar(True)) # este comportamiento cambia el estado de 'enmarcha'
miCoche.estado()
print("\n -- A continuacion creamos el segundo objeto 'coche2'--\n")

# Objeto de clase miCoche2
miCoche2 = coche()
print(miCoche2.arrancar(True))
miCoche2.estado()
