"""    
^ Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para inicializar los atributos, para imprimir todos los valores de los lados, imprimir el valor del lado con mayor tamaño y el tipo de triángulo que es (equilátero, isósceles o escaleno). 
    Comprobamos el tipo de triángulo
        equilátero -> todos los lados iguales
        isósceles -> dos lados iguales
        escaleno -> todos los lados desiguales
"""

class Triangulo:

    def __init__(self, a, b, c):

        self.a = a
        self.b = b
        self.c = c

    def imprimirLados(self):
        print('''
            El lado a es {}
            El lado b es {}
            El lado c es {}
        '''.format(self.a, self.b, self.c))

    def tamañoMayor(self):

        if self.a > self.b and self.a > self.c:
            print(f"{self.a} es el lado más grande")
        elif self.b > self.a and self.b > self.c:
            print(f"{self.b} es el lado más grande")
        elif self.c > self.a and self.c > self.b:
            print(f"{self.c} es el lado más grande")
        else:
            print("Tus lados son iguales")

    def tipoDeTriangulo(self):
        """
         * equilátero -> todos los lados iguales
         * isósceles -> dos lados iguales
         * escaleno -> todos los lados desiguales
        """

        if self.a == self.b == self.c:
            print("Tu triángulo es equilatero")
        elif self.a == self.b and self.a != self.c:
            print("Tu triángulo es isósceles")
        elif self.b == self.c and self.b != self.a:
            print("Tu triángulo es isósceles")
        elif self.c == self.a and self.c != self.b:
            print("Tu triángulo es isósceles")
        elif self.a != self.b != self.c:
            print("Tu triángulo es escaleno")


escaleno = Triangulo(10, 40, 50)
escaleno.imprimirLados()
escaleno.tamañoMayor()
escaleno.tipoDeTriangulo()