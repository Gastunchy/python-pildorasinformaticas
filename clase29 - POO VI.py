# https://www.youtube.com/watch?v=u_VbLsIyzRk

# Herencia

'''
la herencia es un mecanismo que permite crear una nueva clase a partir de una clase existente. La nueva clase, llamada clase derivada o subclase, hereda los atributos y métodos de la clase existente, llamada clase base o superclase. Esto promueve la reutilización de código y facilita la creación de estructuras más complejas.
'''

'''
Conceptos Clave de Herencia en Python
- Clase Base (Superclase): Es la clase original de la cual se derivan otras clases.
- Clase Derivada (Subclase): Es la clase nueva que hereda los atributos y métodos de la clase base.
'''
# Creamos una class padre
class vehiculos():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True

    def acelerar (self):
        self.aceleta=True
    
    def frenar (self):
        self.frena=True

    def estado (self):
        print ("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

# Creamos una class 'hija' que tiene las caracteristicas de la class padre
class Moto(vehiculos):
    pass

miMoto=Moto("Honda", 100)

miMoto.estado()