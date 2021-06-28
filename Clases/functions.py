"""

* Funciones
    ~ Es un bloque de código que se ejecuta únicamente cuando es invocado
    ~ Podemos pasarle parámetros
    ~ Puede retornar un valor

"""

def my_function():
    print("Hola, soy un print dentro de una función")

my_function()


def my_name(name):
    print("Hola " + name)

my_name("Hugo")

def my_default(country = "México"):
    print("We are in " + country)

my_default()

def my_return(a, b):
    return a + b

print(my_return(4, 3))

r = my_return(4, 3)
print(r)

def my_pass():
    pass

def listsMethods(my_list_one = []):
    ask = int(input("How many values do you want: "))
    for i in range(ask):
        element = input("Ingresa los valores de la lista: ")
        my_list_one.append(element)

    return my_list_one

my_list = listsMethods()
print(my_list)