"""

* Conjuntos --> Sets

~ Almacenan múltiples valores valores o ítems en una sola variable-
! No es ordenada
! No es indecada
! Inmutables
! No permite duplicidad

"""

my_set = {"red", 5, True, -24.6, (9, 8)}
#my_set = set(("Cnntenido"))
print(my_set)

# ^ Acceder a los elementos de un conjunto


for element in my_set:
    print(element)

#print(my_set[0])

# ^ Verificar si el conjunto tiene un valor en particular
print("red" in my_set)

# ^ Agregar un nuevo elemento
my_set.add("pink")
print(my_set)


my_list = [5, 4]
my_set.update(my_list)
print(my_set)