"""
 
1. Ale: Definir una función que reciba como parámetros tres números y retorne el menor de ellos.
 
 
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
print(False <= True)    True ---> 1      False -->  0
 
 
2. Hiro: Definir una función que calcule la longitud de una cadena de texto (sin usar len).
 


def myvariable (string):
     global count
    count = 0
    for letra in string:
        print(letra)
        count += 1    
    return count

 data = myvariable("hola")

 print(myvariable("hola")) 
 print(count) 
 print(count)
 
 3. Sara: Definir una función que reciba como parámetro un carácter y devuelva True si es una param, de lo contrario devuelve False.
 

def myfuncion(param):
    return param in 'aeiou'
     
    if  param == "a" or param == "e" or param == "i" or param == "o" or param == "u":
        return True
    else:
        return False
     
     
    if param == ("a" or "e" or "i" or "o" or "u"):
        return True
    else:
        return False
     
     
    elif param == "e" :
         print("Es param")
        return True
    elif param == "i" :
         print("Es param")
        return True
    elif param == "o":
         print("Es param")
        return True
    elif param == "u" :
        print("Es param")
     

 
test = print("hola")
print("Test:", test)

param = input("Que caracter desea saber? ").lower()

print(myfuncion(param))



 
5. Rodri: Definir una función que reciba como parámetro una lista de números y retorne la suma y multiplicación de todos sus elementos. 
 
 
Por ejemplo
my_list = [1, 2, 3, 4]
"La suma de los elementos de la lista es: 10"
"La suma de la multiplicación de los elementos de la lista es: 24"
 
def sumalista(listaNumeros):
    laSuma = 0
    for i in listaNumeros:
        laSuma = laSuma + i
    return laSuma

print(sumalista([1,2,3,4]))
 
6. Definir una función que reciba como parámetro una cadena de texto y retornar cuántas letras mayúsculas tiene.
 


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


"""
 * Completa el código para que la función imprima todos los factores primos de un número. Un factor primo es un número que es primo y divide a otro sin dejar residuo.
"""

def primeFactors(number):                   #100 -->   100/2 --> 50 --> Residuo: 0
  factor = 2                                #50 - -->  50/2 --->  25 -->> Residuo:0
  while factor <= number:                   #25  ---->  25/2 ---> 12.5 --->  Resiudio: 1    
    if number % factor == 0:                # 25 ---> 25/3 ----> 8. --> Residuio: 1
      print(factor)                         # 25 --> 25/4 ---> 6. --> resiudio: 1
      number = number / factor              # 25 ---> 25/5 ----> 5 ---> residuo: 0
    else:                                   # 5 ---> 5/5 ----> 1--- > 0
        factor += 1                         # 1 --> 
  return "Done"

  
#primeFactors(100)  # 2, 2, 5, 5

"""
 * El siguiente código puede llevarnos a ejecutar un ciclo infinito. Arregla el código para que pueda finalizar correctamente para todos los números.
"""

#print(1%2)
def isPowerOfTwo(n):
    while n % 2 == 0 and n >= 1:                                             #0 --> True --> 0
        n = n / 2
        
        # If after dividing by two the number is 1, it's a power of two
    if n == 1:
        return True
    else:
        return False

#print(isPowerOfTwo(0)) # False
#print(isPowerOfTwo(1)) # True
#print(isPowerOfTwo(8)) # True
#print(isPowerOfTwo(9)) # False

"""
Completa el siguiente código para que la función retorne la suma de todos los divisores de un número, sin incluir este. Un divisor es un número que divide a otro sin generar un residuo.
"""

def sumDivisors(n):
  sum = 0
  aux = n - 1
  
  while aux > 0:
      if n % aux == 0:
        sum += aux  #-> sum = sum + aux -> 0 + 18 --> suma = 18  -->> suma = 18 + aux ---> suma = 18 + 12 
      aux-=1 
  return sum
""" 
print(sumDivisors(0))
# 0
print(sumDivisors(3)) # suma de 1
# 1
print(sumDivisors(36)) # suma de 1+2+3+4+6+9+12+18
# 55
print(sumDivisors(102)) # suma de 2+3+6+17+34+51
# 114
"""


def paco(x):
    x = 1/(x+1/(x+1/(x+1/x)))
    print(x)

paco(1)
paco(100)


"""
1)  Minimizar el número de invocaciones de la función print() insertando la secuencia \n en las cadenas.
1.1) Hacer la flecha dos veces más grande (pero mantener las proporciones).
1.2) Duplicar la flecha, colocando ambas flechas lado a lado.
"""
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
