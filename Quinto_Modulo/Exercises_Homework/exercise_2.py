"""
 * Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.

"""
class Calculadora:

    a = 0
    b = 0

    def __init__(self, num1 = int(input("Ingresa un núnero: ")), num2 = int(input("Ingresa otro número: "))):
        self.num1 = num1
        self.num2 = num2
        print("Tus números son {} y {}".format(self.num1, self.num2))

        #self.ask()

    def suma(self):
        suma = self.num1 + self.num2
        return suma

    def ask(self):
        self.a = input("Ingresa el valor de a: ")
        self.b = input("Ingresa el valor de b: ")
        print("Valor de a {} | Valor de b {}".format(self.a , self.b))

test = Calculadora()
print(test.suma())
#suma = test.suma()