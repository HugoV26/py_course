"""
 * Conjuntos -> Sets

 ~ Almacenan múltiples valores o ítems en una sola variable.
 ! NO es ordenada (por lo que no sabremos en que orden se mostrarán los elementos)
 ! NO es indexada
 ! Inmutables
 ! No permite duplicidad

"""

#my_set = {"red", "black", 10, -5.2, True, False, {"Hola", 9}, [False, "Bye", -24], (-3, "Sexy")}

my_set = {"red", "black", 10, -5.2, True, False, (-3, "Sexy")}

#my_set = set(("red", "black", 10, -5.2, True, False, (-3, "Sexy")))

print(my_set)

my_set_two = {"red", "black", 10, -5.2, True, False, (-3, "red"), "red"}

print(my_set_two)

# ^ Acceder a los elementos de un conjunto

for x in my_set_two:
    print(x)

# ^ Verificar si el set contiene un valor en particular
print("red" in my_set_two)

# ^ Agregar un nuevo elemento
my_set_two.add("pink")
print(my_set_two)

my_set.update(my_set_two)
print(my_set)

my_list = [2, 5]

my_set.update(my_list)

print(my_set)

# ^ Remover un elemento

my_set.remove("red")
print(my_set)

my_set.discard("pink")
print(my_set)

e = my_set.pop()
print(e)
print(my_set)


# ^ Limpiar el contenido
my_set.clear()
print(my_set)

# ^ Eliminar el conjunto
#del my_set

