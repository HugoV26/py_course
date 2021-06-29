# * Principales métodos de las cadenas.

# ^ Center -> str.center(width[, fillchar])

print(len("Cadena centranda den 50 caracteres"))
print("Cadena centrada en 50 caracteres".center(50))
print(len("Cadena centranda den 50 caracteres".center(50)))
print("Cadena centranda den 50 caracteres".center(50, '*'))

# ^ Rjust -> str.rjust(width[, fillchar])
# ^ Ljust -> str.ljust(width[, fillchar])
print(len("Cadena justificada a la derecha con 50 caracteres"))  
print("Cadena justificada a la derecha con 50 caracteres".rjust(50))
print("Cadena justificada a la derecha con 50 caracteres".rjust(60, '>'))

# ^ Zfill -> str.zfill(width)
# ~ Devuelve una cadena complementando el ancho rellenando con el caracter '0' a la izquierda. Si la cadena comienza con el caracter '-' o '+', el relleno comenzará después del mismo.

print('120'.zfill(5))
print('-120'.zfill(5))

# * Strip -> str.strip([chars])
# ~ Devuelve una cadena removiendo los caracteres iniciales y finales que se especifiquen en el parámetro [chars]. Si no se especifica, se eliminan los espacios. En caso de especificar un valor, NO es un prefijo Ni sufijo, sino que se eliminan todas sus combinaciones.

print("     El paco     ")
print("     El paco     ".strip())
print('I want some alcohol!'.rstrip('Ialcho!'))

# * Métodos de Conversión

# ^ Upper -> str.upper()
# ~ Devuelve una cadena con todos los caracteres en mayúsculas

print("La paca".upper())

# ^ Lower -> str.lower()
# ~ Devuelve una cadena con todos los caracteres en minúsculas

print("La paca DE NUEVO".lower())

# ^ Casefold -> str.casefold()
# ~ Es más agresivo que lower, algunos caracteres los convierte en su reprensentación minúsculas.

print('der Fluß'.lower())
print('der Fluß'.casefold())

# ^ Swapcase -> str.swapcase()
# ~ Devuelve una cadena intercambiando los caracteres entre mayúsculas y minúsculas

print("Hey, YOU wanna some Drugs?".swapcase())

# * Title -> str.title()
# ~ Cada de una las palabras comenzará con mayúscula

print("el paco se parece a escobar".title())

# * Capitalize -> str.capitalize()
# ~ Primer carácter en mayúscula

print("el perro es rojo".capitalize())

# * Find -> str.find(sub[, start[, end]]), str.rfind

# ~ Busca y devuelve la posición de la primera ocurrencia del parámetro sub dentro de la cadena. Adicionalmente se pueden especificar los parámetros start y end para acotar la búsqueda entre dichas posiciones. Si la búsqueda no es exitosa, devuelve -1.

mystr = 'Tres tristes tigres'
print('Tres tristes tigres'.find('e'))
print('Tres tristes tigres'.find('e', 3))
print(mystr.find('e', 11, len(mystr)))
print('Tres tristes tigres'.find('w'))

# * Index -> str.index(sub[, start[, end]]), str.rindex
# ~ Es similar a Find pero eleva ValueError en caso de que la búsqueda no sea exitosa

my_c = 'Hola mundo'
x = 2
try:
    #check = my_c.index('w', 0, 2)
    #print(check)
    print(x)
except NameError:
    print("No está la w :C")
else:
    print("La excepción no fue valuerror")

# Métodos de Validación de los strings