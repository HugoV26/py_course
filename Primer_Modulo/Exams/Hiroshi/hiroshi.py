#1

num1 =int(input("Inserte el numero : "))

if num1 % 2 == 0 :
    print(f"El {num1} es un numero par")
else:
    print(f"El {num1} es un numero impar")

#2

my_list = []

print ("Inserta tu palabra \n")
my_word = (input("inserta tu palabra "))

for element in my_word:
    my_list.append(element)

if my_list == (my_list[::-1]):
    print("\n¡si es un palindromo!\n")

else:
    print("\n no es un palindromo!\n")




#3

my_tuple = (2, "Hola", (5, ("Adiós",), (-95, "Cerveza", ("Mario", ("5", 9)))))

print(my_tuple[2][1][0])
print(my_tuple[2][2][2][1][1])




#4

my_fourth = int(input("Ingresa un numero positivo: "))
my_fourth_sup = (my_fourth*(-1))-1

while my_fourth != my_fourth_sup: 
    print(my_fourth)
    my_fourth -= 1


#5

my_fifth = int(input("Pon tu numero: "))

for element in range(my_fifth):
    print ("*" * (element+1))



#6 

my_var = int(input("Inserta el año "))
fourth = (my_var % 4)
hund = (my_var % 100)
fourth_hund = (my_var % 400)

if fourth == 0 and hund == 0 and fourth_hund == 0:
    print("El año " + str(my_var) + " no es un año bisiesto.")

elif fourth == 0 and hund == 0 and fourth_hund != 0:
    print("El año " + str(my_var) + " si es un año bisiesto.")

elif fourth == 0 and hund != 0 and fourth_hund != 0:
    print("El año " + str(my_var) + " si es un año bisiesto.")

else:
    print("El año " + str(my_var) + " no es un año bisiesto.")

#7

my_l = 0
my_h = 0
            
for element in range(6):
    num = int(input("pon aqui tu numero entero: "))
    if num < 0 :
        my_l += num
    elif num >= 0:
        my_h -= num

print("Sumatoria de números negativos: " + str(my_l))
print("Resta de números positivos: "+ str(my_h))


