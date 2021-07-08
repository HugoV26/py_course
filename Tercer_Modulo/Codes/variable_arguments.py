"""
    ^ *args -> Parámetro de una lista y representa un número variable de argumentos que puede recibir la función sin que sean nombrados por una palabra clave, estos valores son almacenados en una tupla.
"""

def suma(a, b):
    return a + b

print(suma(2, 10))
"""
def sumaArgs(*args):
    num = 0
    print(type(args))
    for arg in args:
        #if type(arg) == int:
        if str(arg).isdigit():
            num += arg
    return num
"""

#print(sumaArgs(2, 10, 25, 4, 9, 7, "Hola"))

def ejemplo(*args):
    num = 0
    for arg in args:
        #print(arg)
        #if str(arg).isdigit(): #True o False
        if type(arg) is int:
            if arg % 2 == 0:
                print ("tu número", arg, "es par")
            else:
                print("Tu numero", arg, "es impar")

        elif "Cachondo" in arg:
            print ("si esta" + arg )

print("Ejemplo")
ejemplo(1, "Pancho Cachondo", -2, 4, 5, 10)
print("Fin Ejemplo")

"""
Rodri

def ejemplo(*args):
    num = 0
    for arg in args:
        print(arg)
        if str(arg).isdigit():
def compare (*args)
                num = 0
                if num %1 == 0:
                    print ("tu número es par")
                else:
                    print ("tu numero es impar")

print("Ejemplo")
ejemplo(1, "Pancho Cachondo", -2, 4, 5, 10)
print("Fin Ejemplo")


"""


"""
    ^ **kwargs -> Pasar un número variable de argumentos, estos deben de ser nombrados en formato key:value. Se almacenan en un diccionario. 

"""

def multiplicacion(*args):
    num = 0
    print(type(args))
    for arg in args:
        num *= arg
    return num

def sumaArgs(*args):
    num = 0
    print(type(args))
    for arg in args:
        #if type(arg) == int:
        if str(arg).isdigit():
            num += arg
    return num

OPERACIONES = {
    'suma': sumaArgs,
    'multiplicacion': multiplicacion
}

#print(OPERACIONES.get("suma"))

def operacion(*args, **kwargs):
    return OPERACIONES.get(kwargs.get("operacion"))(*args)
            #OPERACIONES.get("suma")(*args)
            #sumaArgs(*args)

print(operacion(2, 3, 4, operacion="resta"))

"""

~ operacion recibe un número variable de argumentos sin clave y con clave
~ Con kwargs.get("operacion"), obtenemos el valor de la clave "operacion" enviado cuando se llame a la función.
~ Luego, utilizamos el valor devuelto para obtener la función del diccionario OPERACIONES con el método get
~ Utilizamos * al enviar los valores dado a que dentro de la función operacion, args es una lista. Para pasar una lista como argumentos, se utiliza un asterisco antes de dicha lista.

"""