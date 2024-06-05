# https://www.youtube.com/watch?v=Y_SiIgxc-xI

# POO III

# Construccion de una clase

# Nota: un objeto tiene estado, propiedad y comportamiento. 

#Clase coche
class coche():
# Propiedades (variables)
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False
# Comportamiento
    def arrancar(self):
        self.enmarcha=True # Hace que el valor de la propiedad 'enmarca' cambie a True

    def estado(self):
        if(self.enmarcha):# Python toma automaticamente que el valor para validar es True
            return "El coche esta en marcha"
        else:
            return "El coche esta apagado"

# Objeto de clase miCoche
miCoche = coche() # aqui se esta instanciando a una clase

# Usando la nomenclatura del punto se accede a la propiedad
print("El largo del coche es: ", miCoche.largoChasis)
print("El coche tiene: ", miCoche.ruedas, "ruedas")
print("Status de enmarcha antes: ", miCoche.enmarcha)
print(miCoche.estado()) # Imprimir estado basado en un comportamiento
miCoche.arrancar() # este comportamiento cambia el estado de 'enmarcha'
print("Status de enmarcha antes: ", miCoche.enmarcha)
print(miCoche.estado()) # Imprimir estado basado en un comportamiento

# Resumen
'''
Nuestra clase 'coche' tiene:
- 4 propiedades
- 2 comportamientos'''
