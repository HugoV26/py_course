
"""
1. Ale: Definir una función que reciba como parámetros tres números y retorne el menor de ellos.
"""
"""
def myFunction (num1, num2, num3):
    if (num1 <= num2) <= (num1 <= num3):
        a = num1
    elif num2 <= num1 and num2 <= num3:
        a = num2
    elif num3 <= num1 and num3 <= num2:
        a = num3
    print("El menor número es: ", a)

myFunction (4,3,2)
print(1 <= 3)
print(1 <= 2)
print(False <= True)   #True ---> 1     #False -->  0
"""
"""
2. Hiro: Definir una función que calcule la longitud de una cadena de texto (sin usar len).
"""


def myvariable (string):
    #global count
    count = 0
    for letra in string:
        print(letra)
        count += 1    
    return count

#data = myvariable("hola")

#print(myvariable("hola")) 
#print(count) 
#print(count)
"""
#3. Sara: Definir una función que reciba como parámetro un carácter y devuelva True si es una param, de lo contrario devuelve False.
"""

def myfuncion(param):
    return param in 'aeiou'
    """
    if  param == "a" or param == "e" or param == "i" or param == "o" or param == "u":
        return True
    else:
        return False
    """
    """
    if param == ("a" or "e" or "i" or "o" or "u"):
        return True
    else:
        return False
    """
    """
    elif param == "e" :
        #print("Es param")
        return True
    elif param == "i" :
        #print("Es param")
        return True
    elif param == "o":
        #print("Es param")
        return True
    elif param == "u" :
        print("Es param")
    """

 
test = print("hola")
print("Test:", test)

param = input("Que caracter desea saber? ").lower()

print(myfuncion(param))



"""
5. Rodri: Definir una función que reciba como parámetro una lista de números y retorne la suma y multiplicación de todos sus elementos. 
"""
"""
Por ejemplo
my_list = [1, 2, 3, 4]
"La suma de los elementos de la lista es: 10"
"La suma de la multiplicación de los elementos de la lista es: 24"
"""
def sumalista(listaNumeros):
    laSuma = 0
    for i in listaNumeros:
        laSuma = laSuma + i
    return laSuma

print(sumalista([1,2,3,4]))
"""
6. Definir una función que reciba como parámetro una cadena de texto y retornar cuántas letras mayúsculas tiene.
"""


import random

names = {
    'Ale': 0,
    'Sara': 0,
    'Hiro': 0,
    'Rodri': 0
}

for e in names:
    aux = {e:(random.randint(1 ,6))}
    names.update(aux)

print(names)

"""
Global
text = "El paco está pachon"

def test():    
    global text
    text = "El mau está loco"
    print("Mi texto es: " + text)


text = "El chuy no se baña"
test()
print("Mi otro texto es: " + text)
text = "El paco está pachon"
print("Mi otro texto de nuevo es: " + text)
"""