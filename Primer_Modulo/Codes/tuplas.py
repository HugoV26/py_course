###print("Tuplas")

"""
* Son utilizadas para almacenar múltiples valores o ítems en una variable.
    ? Sus elementos
        ~ Están ordenados.
        ~ Permite duplicidad.
        ! NO se pueden cambiar (inmutables).

* Cuando creamos una tupla, se le conoce como "packing".
"""

my_tuple = ("red", "black", 10, -6.2, True, (5, 9))
# my_tuple = tuple(("red", "black", 10, -6.2, True, (5, ,9))) 
###print(my_tuple)

# * Si se quiere crear una tupla de un sólo elemento, debe de colocarse una coma
my_second_tuple = ("pavo",)
###print(my_second_tuple)
###print(type(my_second_tuple))

# ^ Acceder a los elementos de la siguiente tupla
my_third_tuple = (True, 2.5, (2,-5.6), "Hola", (True, -95.21, ("Perro", "Gato", ("Sol", "Luna", "Planeta", "Tierra"))))

"""
^ Imprimir el valor que está en la posición [2] con un índice negativo
^ Imprimir los primeros cuatro valores de la tupla con un índico de rangos negativo
^ Imprimir el valor -5.6
^ Imprimir el valor "Gato"
^ Imprimir el valor "Planeta"
"""

###print (my_third_tuple[-3]) 

###print(my_third_tuple[-5:-1])

###print(my_third_tuple[2][1])

###print(my_third_tuple[4][2][1])

###print(my_third_tuple[4][2][2][2])

# ! Inmutables
"""
my_fourth_tuple = (4, 10, 12)
my_fourth_tuple[3] = 6
###print(my_fourth_tuple)
"""

# * Existen otras formas para agregar elementos a una tupla
# * 1.Convertir la tupla a una lista, agregar el elemento y convertirla a una tupla de nuevo.

my_fifth_tuple =  ("Whisky", "Vodka", "Tequila")
###print(type(my_fifth_tuple))
# Casteo

aux = list(my_fifth_tuple)
aux.append("Cerveza")

my_fifth_tuple = tuple(aux)
###print(my_fifth_tuple)
###print(type(my_fifth_tuple))


# * 2. Agregar una tupla a otra tupla


my_sixth_tuple = ("Apple", "Orange", "Pineapple")

aux = ("Watermelon",)
my_sixth_tuple += aux
###print(my_sixth_tuple)

# ^ Eliminar "Apple" de la tupla
#Hiroshi fachero facherito
###print("\n\nEliminar elemento de tupla")
aux= list(my_sixth_tuple)
aux.remove("Apple")

my_sixth_tuple = tuple(aux)
###print(my_sixth_tuple)
###print(type(my_sixth_tuple))
"""
#Sara

aux= list(my_sixth_tuple)
aux.remove("Apple")
my_sixth_tuple = tuple(aux)
###print(my_sixth_tuple)



#La Ale
aux = list(my_sixth_tuple)
aux.remove("Apple")
my_sixth_tuple = tuple(aux)
###print (my_sixth_tuple)
"""

"""
my_eight_tuple = ("Kia", "Audi", "Ford")
del my_eight_tuple
#print(my_eight_tuple)
"""

# * Unpack tuplas
my_nineth_tuple = ("Hola", "Mundo")
"""
my_string, my_string_two = my_nineth_tuple[0], my_nineth_tuple[1]
(a, b) = my_nineth_tuple
#print(a, b)
#print(my_string, my_string_two)

# * Si el número de variables es menor a los valores que contiene la tupla, podemos agregar un * a una variable para indicarle que será de tipo lista para almacenar los valores sobrantes.

my_final_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
(number1, *number2, number3) = my_final_tuple

# 1, 2, [3, ..., 10]

#print(number1, number2, number3)

"""

# * Ciclo While


tmp = 0
while tmp <= 10:
    #print(tmp)
    tmp += 1
else:
    print("Fin del ciclo")



mytuple = (2, "Hola", (5, ("Adiós",), (-95, "Cerveza", ("Mario", ("5", 9)))))

print(mytuple)
print(mytuple[2][1][0])
print(mytuple[2][2][2][1][1])
# ^ Imprimir Adios
# ^ Imprimir 9