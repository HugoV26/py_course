"""
    * Constructores
    ^ Se utilizan para inicializar el estado de un objeto, es decir, se encargan de asignar valores a los atributos de una clase cuando se crea una instancia de esta. 
    ^ Contienen instrucciones (bloques de código) que se ejecutan cuando se crea un objeto (una instancia de una clase).
    ^ Se invoca en automático tan pronto como se crea la instancia de una clase

    *Self

    ^ Self siempre apunta al objeto actual.
    ^ Vincula los atributos con los argumentos dados.
    ^ Representa la instancia de la clase.
    
"""

class Cat:

    meow = False  #Atributo de Clase
    color = "Black"

    def __init__(self, name, owner, gender):
        print("A cat has been created")
        self.nombre = name
        self.dueno = owner
        self.genero = gender
        #tom.dueno

    def meowing(self):
        self.meow = True
        #tom.meow = True

    def changeColor(self, color):
        self.color = color
        var = "Algo"
        #tom.color = color

tom = Cat("Tom", "Max", "Male")
tom.color = "Gris"
tom.meow = True
    
garfield = Cat("Garfield", "John", "Male")
garfield.changeColor("Orange")

print("El color de garfield es: ", garfield.color)