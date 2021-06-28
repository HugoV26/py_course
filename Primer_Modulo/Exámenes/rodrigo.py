#1. Escribir un programa que pida al usuario un número y determina si un número es par o impar.

""""
number = 0
number = int(input("introduzca un numero"))


if number %2 == 0:
    print ("el numero es par")
else:
    print ("el numero no es par")
"""

#2. Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

""""
word = input("Introduce una palabra: ")
reversed_word = word
word = list(word)
reversed_word = list(reversed_word)
reversed_word.reverse()
if word == reversed_word:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
"""

#3. Dada la siguiente tupla, imprimir los siguientes valores: Adiós & 9

"""
my_tuple = (2, "Hola", (5, ("Adiós",), (-95, "Cerveza", ("Mario", ("5", 9)))))

print(my_tuple[2][1])
print(my_tuple[2][2][2][1][1])
"""


#4. Escribir un programa que solicite al usuario un número entero positivo y 
#muestre por pantalla la cuenta atrás desde ese número hasta su mismo valor pero negativo.

"""
number = int(input("Ingresa por favor un número entero positivo: "))
numero1 = (number*(-1))-1

while number != numero1: 
    print(number)
    number -= 1
"""

#5. Escribir un programa que solicite al usuario un número entero positivo e 
# imprima en consola un triángulo rectángulo como el de abajo.

"""
Triangulo = int(input("Introduzca la altura del triángulo (entero positivo): "))
for i in range(Triangulo):
    for j in range(i+1):
        print("*", end="")
    print("")
"""

#6. Hacer un programa que permita saber si un año es bisiesto.

#¿Múltiplo de 4?	    ¿Múltiplo de 100?	¿Múltiplo de 400?	Es bisiesto	            Ejemplos
#No	                           No	            No	                No	            2019, 1981
#Sí	                           No	            No	                Sí	            2020, 2012
#Sí	                           Sí	            No	                No	            1900, 2100
#Sí	                           Sí	            Sí	                Sí	            2000, 2400

"""
año = int(input('Introduce un año: '))

if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print('El año es bisiesto')
        else:
            print('El año no es bisiesto')
    else:
        print('El año es bisiesto.')
else:
    print('El año no es bisiesto.')
"""

#7. Hacer qun programa que permita al usuario ingresar 6 números enteros, 
# que pueden ser positivos o negativos. Al finalizar, mostrar la sumatoria de los números negativos 
# y la resta de los positivos.

"""
my_number1 = 0
my_number2 = 0
for element in range(6):
    numero = int(input("Ingresa un número entero: "))
    if numero > 0 :
        my_number1 += numero
    elif numero <= 0:
        my_number2 -= numero
print("Sumatoria de números negativos: " + str(my_number1))
print("Resta de números positivos: "+ str(my_number2))

"""