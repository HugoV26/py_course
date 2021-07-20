#1. Escribir un programa que pida al usuario un número y determina si un número es par o impar.

num1 =int(input("Digite su numero porfavor : "))

if num1 % 2 == 0 :
    print(f"El {num1} un numero par")
else:
    print(f"El {num1} un numero impar")

#3. Dada la siguiente tupla, imprimir los siguientes valores: Adiós & 9

my_tuple = (2, "Hola", (5, ("Adiós",), (-95, "Cerveza", ("Mario", ("5", 9)))))

print(my_tuple[2][1]) # ! Error | Solución: print(my_tuple[2][1][0]) 
print(my_tuple[2][2][2][1][1])

#4. Escribir un programa que solicite al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta su mismo valor pero negativo.
num1 = int(input("Ingrese su numero: "))
num2= num1 * (-1)

while num1 >= num2 :
    print(num1)
    num1 -= 1

#5. Escribir un programa que solicite al usuario un número ent-ero positivo e imprima en consola un triángulo rectángulo como el de abajo.
num3 = int(input("Ingrese su numero: "))
num4 = 1

while num4 <= num3 :
    print("*"*num4)
    num4 += 1

#6. Hacer un programa que permita saber si un año es bisiesto.
num6= int(input("Ingrese el año: "))
if num6 % 400 == 0  and num6 % 100 == 0 and num6 % 4 == 0 :
    print("Es año Bisiesto")
else:
    print("No es año bisiesto")