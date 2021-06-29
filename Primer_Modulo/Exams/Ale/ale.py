#1. Escribir un programa que pida al usuario un número y determina si un número es par o impar.
print ("Verificación de par o impar...\n")
my_var = int(input("¿Que número entero deseas verificar? "))
my_var %= 2

if my_var == 0:
    print("Tu número es par.")

else:
    print("Tu número es impar.")



# #2. Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
my_list = []

print ("Verificación de palindromos...\n")
my_word = (input("¿Que palabra deseas verificar? "))

for element in my_word:
    my_list.append(element)

if my_list == (my_list[::-1]):
    print("\n¡Tu palabra es un palindromo!\n")

else:
    print("\n¡Tu palabra NO es un palindromo!\n")



# 3. Dada la siguiente tupla, imprimir los siguientes valores: Adiós & 9
my_tuple = (2, "Hola", (5, ("Adiós",), (-95, "Cerveza", ("Mario", ("5", 9)))))

print(my_tuple[2][1][0])
print(my_tuple[2][2][2][1][1])



# 4. Escribir un programa que solicite al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta su mismo valor pero negativo.
my_fourth = int(input("Ingresa por favor un número entero positivo: "))
my_fourth_sup = (my_fourth*(-1))-1

while my_fourth != my_fourth_sup: 
    print(my_fourth)
    my_fourth -= 1



# 5. Escribir un programa que solicite al usuario un número entero positivo e imprima en consola un triángulo rectángulo como el de abajo.
my_fifth = int(input("Ingresa por favor un número: "))

for element in range(my_fifth):
    print ("*" * (element+1))



# 6. Hacer un programa que permita saber si un año es bisiesto.
# ¿Múltiplo de 4?	    ¿Múltiplo de 100?	¿Múltiplo de 400?	Es bisiesto	            Ejemplos
# No	                           No	            No	                No	            2019, 1981
# Sí	                           No	            No	                Sí	            2020, 2012
# Sí	                           Sí	            No	                No	            1900, 2100
# Sí	                           Sí	            Sí	                Sí	            2000, 2400


print ("Verificación año bisiesto...\n")
my_var = int(input("¿Que año deseas verificar? "))
fourth = (my_var % 4)
hund = (my_var % 100)
fourth_hund = (my_var % 400)

if fourth == 0 and hund == 0 and fourth_hund == 0:
    print("El año " + str(my_var) + " SI es un año bisiesto.")

elif fourth == 0 and hund == 0 and fourth_hund != 0:
    print("El año " + str(my_var) + " NO es un año bisiesto.")

elif fourth == 0 and hund != 0 and fourth_hund != 0:
    print("El año " + str(my_var) + " SI es un año bisiesto.")

else:
    print("El año " + str(my_var) + " NO es un año bisiesto.")




# 7. Hacer qun programa que permita al usuario ingresar 6 números enteros, que pueden ser positivos o negativos. Al finalizar, mostrar la sumatoria de los números negativos y la resta de los positivos.
my_l = 0
my_h = 0
            
for element in range(6):
    num = int(input("Ingresa un número entero: "))
    if num < 0 :
        my_l += num
    elif num >= 0:
        my_h -= num

print("Sumatoria de números negativos: " + str(my_l))
print("Resta de números positivos: "+ str(my_h))
