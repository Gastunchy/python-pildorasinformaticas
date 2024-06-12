# https://www.youtube.com/watch?v=5Ohme4A2Weg&t=1s

# POO

# Explicacion desde chatgpt

'''
¿Qué es un Lenguaje de Programación Orientado a Objetos (OOP)?

La programación orientada a objetos (OOP, por sus siglas en inglés) es un paradigma de programación que utiliza "objetos" y sus interacciones para diseñar y programar aplicaciones. Un objeto es una instancia de una "clase", que es una plantilla que define las características y comportamientos del objeto. Los cuatro principios fundamentales de la OOP son:

- Encapsulamiento: Los objetos guardan sus datos (atributos) y comportamientos (métodos) dentro de sí mismos, protegiendo la integridad de esos datos y exponiendo solo lo necesario.
- Abstracción: Se enfocan solo en los detalles relevantes para la utilización de un objeto, ocultando los detalles de implementación.
- Herencia: Permite crear nuevas clases a partir de clases existentes, compartiendo código y comportamientos comunes y extendiéndolos o modificándolos según sea necesario.
- Polimorfismo: Permite que diferentes objetos sean tratados de la misma manera a través de una interfaz común, facilitando la reutilización de código.

Ejemplo en Python
Python es un lenguaje que soporta la programación orientada a objetos. Aquí hay un ejemplo simple que demuestra los conceptos básicos de la OOP en Python.
'''
# Definición de una Clase

# Primero, definimos una clase 'Persona' con atributos y métodos.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo de la instancia
        self.edad = edad      # Atributo de la instancia

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Creación de un objeto de la clase Persona
persona1 = Persona("Juan", 30)
persona1.saludar()  # Llamada al método saludar

'''
En este ejemplo:

La clase 'Persona' tiene un método especial '__init__' que actúa como constructor, inicializando los atributos 'nombre' y 'edad'.
El método 'saludar' es un comportamiento que pertenece a la clase Persona.
'''

# Herencia

'''
Ahora, extendemos la clase 'Persona' para crear una subclase 'Estudiante'.
'''

class Estudiante(Persona):
    def __init__(self, nombre, edad, universidad):
        super().__init__(nombre, edad)  # Llama al constructor de la clase base
        self.universidad = universidad  # Atributo específico de la subclase

    def saludar(self):
        super().saludar()  # Llama al método saludar de la clase base
        print(f"Estudio en la {self.universidad}.")

# Creación de un objeto de la clase Estudiante
estudiante1 = Estudiante("Ana", 22, "Universidad de Python")
estudiante1.saludar()  # Llamada al método saludar

'''
En este ejemplo:

- Estudiante es una subclase de Persona que hereda sus atributos y métodos.
- super() se utiliza para llamar al constructor y métodos de la clase base (Persona).
- Estudiante añade un nuevo atributo 'universidad' y sobrescribe el método 'saludar' para añadir información adicional.
'''

# Polimorfismo

'''
Podemos demostrar polimorfismo usando una función que acepte cualquier objeto que implemente el método 'saludar'.
'''
def presentar(persona):
    persona.saludar()

persona1 = Persona("Carlos", 40)
estudiante1 = Estudiante("Laura", 21, "MIT")

presentar(persona1)  # Hola, mi nombre es Carlos y tengo 40 años.
presentar(estudiante1)  
# Hola, mi nombre es Laura y tengo 21 años.
# Estudio en la universidad MIT.

'''
En este ejemplo, la función 'presentar' puede aceptar tanto objetos 'Persona' como 'Estudiante' y llamará al método 'saludar' adecuado, demostrando polimorfismo.

Estos ejemplos ilustran cómo Python soporta la programación orientada a objetos, permitiendo la creación y manipulación de objetos, la herencia de clases y el polimorfismo.
'''

presentar(persona1)