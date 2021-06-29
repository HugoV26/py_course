
print("Holis")

numberS = 26
numberR = 26
numberA = 26


#Operadores Aritméticos
#Suma +
#Resta - 
#Multuplicación *
#Divisón /
#Exponencial **
#print(10**2)
#print(2+5)

#Operadores de asignación
#my_var = 10
#my_var = my_var + 3
#my_var += 3

#Sumarla en dos unidades, restarle 5 unidades, multiplcarla por 8, dividirla entre 2 y exponenciarla por 3
#Sara 
#print("Sara")
numberS += 2
numberS -= 5
numberS *= 8
numberS /= 2
numberS **= 3 
#print(numberS)

#Rodrigo
#print("Rodrigo")
numberR += 2
numberR -= 5
numberR *= 8
numberR /= 2
numberR **= 3
#print(numberR)

#Ale
#print ("Ale")
numberA += 2
numberA -= 5
numberA *= 8
numberA /= 2
numberA **=3
#print (numberA)




#Listas
"""
Se usan para almacenar múltiplces valores o ítems en una sola variable.
    - Están ordenados.
    - Pueden cambiar (mutables)
    - Permite duplicidad
"""

my_list = ["Cerveza", -5, 36.2, False, [4,6], "Hola", True]
# 0 ... n

print(my_list)

print(type(my_list))
print(len(my_list))

print("Valor en la posición[1]: ", my_list[1])
print("Valor en la posición[4]: ", my_list[4][1])
print("Valor en la posición[-1]: ", my_list[-1])
print("Valores en la posición [2:5]", my_list[2:5])
print("Valores en el rango [:3]", my_list[:3])
print("Valores en el rango [3:]", my_list[3:])
print("Valores en la posición [2:10]", my_list[2:10])

print("Valores en el rango [-4:-1]: ", my_list[-4:-1])

my_new_list_ale = ["Hugo", 21, "Paco", True, "Luis"] #Hugo --> Enrique
my_new_list_sara = ["Ed", "Edd", "Eddy", 25 ,26]
my_new_list_rodri = ["Daniel" , 88 , "Sandia" , False, "Paco"]

print(my_new_list_ale)
my_new_list_ale[0] = "Enrique"
print(my_new_list_ale)

print (my_new_list_rodri)
my_new_list_rodri[1:4] = ["20", "Melon", True]
print (my_new_list_rodri)

list_two = ["Whisky", "Vodka", "Tequila"]
#Vodka y tequila por cerveza
#print(list_two) 
list_two [1:4] = ["Cerveza"]
print(list_two) 

#print (list_two) []

names = ["Hugo", "Jesus", 10]

#Comprobrar si un valot está en la lista
if "Hugo" not in names:  #True o False
    print("Hugo no está en la lista")
    print("Ejecuto todo lo que esté aquí")
elif "Hu" in names:    
    print("Hugo sí está en la lista")
else:                   
    print("No hay nada")

if True:
    print()

#Condicional
if True:
    print()
else:
    print()

if True:
    print()
elif False:
    print()    

alcohol = True

if alcohol == True:
    print("Hay peda")

#print("Ingresa tu edad: ")
"""
x = int(input("Ingresa tu edad: "))
print(type(x))
print("Hola ", x)
"""
#Métodos

animals = ["Paco", "Perro", "Tigre"]
#animals[1:4] = ["Elefante"]
#print(animals)

animals.insert(1, "Pavo")
animals.insert(2, "Pájaro")

print(animals)

"""

Métodos de una lista en Python

append()
clear()
copy()
count()
extend()
index()
insert()
pop()
remove()
reverse()
sort()

"""

#cars = list(("Elemneto 1", "Elemento 2"))
cars = ["Kia", "Audi", "Ford"]

num_cars = len(cars) #Retorna un valor de tipo int
"""
print(cars)
print(cars[0:])
print(cars[0:len(cars)])
print(cars[0:num_cars])
"""

#Ciclos
for element in cars:
    print(element)   #1° Vuelta element = "Kia" 
                    #2° Vuelta element = "Audi"
                    #3° Vuelta element = "Ford"

print("\n")
for i in range(len(cars)):  #[0:len(list)]
    print(cars[i])       #1° i = 0, 2° i = 1, 3° i = 2

#Si kia está en la lista, imprimir "Es una Soul"
#Si audi está en la lista, imprimir "Es un T4"
#Si Ford está en la lista, imprimir "Es un Fiesta"
#Si nada coindice, imprimir "No tenemos carros"
#Código Sara
print("***")    
print("***")    
print("***")    
print("Código SARA")

for element in cars:
    if "Kia" in cars:
        print("Es una Soul")
    elif "Audi" in cars:
        print("Es un T4 ")
    elif "Ford" in cars:
        print("Es un Fiesta")
    else:
        print("No tenemos carros ")
        
print("***")    
    


    #Código Ale
print("Ale")
for i in range(len(cars)):  
    if cars[i] == "Kia":
        print("Es una Soul.")
    elif cars[i] == "Audi":
        print("Es un T4.")
    elif cars[i] == "Ford":
        print("Es un Fiesta.")
    else:
        print("No tenemos carros.")
print("***")
    

for element in cars:
    if "Kia" in cars:
        print ("Es un Soul")
    elif "Audi" in cars:
        print ("Es un T4")
    elif "Ford" in cars:
        print ("Es un Fiesta")
    else:
        print ("No tenemos carros")
    #Código Rodri

for element in cars:
    if element == "kia":
        print("Es una soul")
    elif element == "Audi":
        print("Es un T4")