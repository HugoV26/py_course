"""

    * Funciones
    ~ Es un bloque de código que se ejecuta únicamente cuando es invocado.
    ~ Podemos pasarle parámetros o no
    ~ Puede retornar un valor o no

"""

def myFunction():
    print("Hola, soy un print dentro de una función")

myFunction()

def myName(name, age):
    print("Hola " + name + " Tienes ", age, " años")

myName("Hugo", 25)

def myCountry(country = "México"):
    print("Eres de " + country)

myCountry("España")

def myReturn(a, b):
    print("Antes del return")    
    return a + b
    print("Después del return")
    #return a * b

suma = myReturn(5, 8)
print(suma)

def myPass():
    print("Hola")
    pass

myPass()

def methodAppend(my_list = []):
    number = int(input("How many values do you want? "))
    for i in range(number):
        e = input("Enter the value: ")
        my_list.append(e)

    print(my_list)
    return my_list

my_list = methodAppend()
print(my_list)