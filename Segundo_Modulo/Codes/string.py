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

# * Endswith -> str.endswith(suffix [, start[, end]])
# ~ Devuelve True si la cadena termina con el sufijo especificado; de lo contrario devuevle False. El sufijo también puede ser una tupla de sufijos para buscar. Además, se puede especificar la posición de inicio y fin para acotar la búsqueda.

print('www.tunerd.mx'.endswith(('.net', '.mx'), 5, 15))
print("www.tunerd.mx".endswith(""))

# * Isalpha -> str.isalpha()
# ~ Devuelve True si todos los caracteres en la cadena son alfabéticos y hay al menos un caracter, False en caso contrario. Los caracteres alfabéticos son aquellos caracteres definidos en la base de datos de caracteres Unicode como "Letra".

print('Python'.isalpha())
print('Python 3.9'.isalpha())

# * Isascii -> str.ascii()
# ~ Devuelve True si la cadena está vacía o todos los caracteres son ASCII, False en caso contrario

print('n'.isascii())
print('ñ'.isascii())

# * Isdecimal -> str.decimal()

print('3'.isdecimal())
print('-8'.isdecimal())

# * Isdigit -> str.isdigit()
# ~ Similar a isdecimal, a diferencia de que tambi+en reconoce los números del sistema Kharosthi.

print('𐩁'.isdigit())
print('𐩁'.isdecimal())

# * Isnumeric -> str.isnumeric()
# ~ Similiar a isdigit pero también reconoce fracciones vulgares de Unicode

print('\u00BD'.isnumeric())
print('½'.isnumeric())

# * Isidentifier -> str.isidentifier()
# ~ Define si puedes utilizar dicho valor como nombre de variable o si la misma corresponde a una palabra reservada de Python.

print("my-var".isidentifier())
print("my_var".isidentifier())
print("my, var".isidentifier())
print('while'.isidentifier())

# * Método de unión y división

# * Join -> str.join(iterable)
# ~ Devuelve una cadena concatenando los elementos de un iterable (listas, tuplas, string) y serparándolos con la cadena str (a la que se aplica el método)

print(".".join(('www', 'pornhub', 'com')))

# * Partition -> str.partition(sep), str.rpartition(sep)
# ~ Devuelve una tupla de 3 elementos, donde se divide la cadena en la primer aparición del parámetro sep

print("www.tunerd.mx".partition('.'))

# * Split -> str.split(sep=None, maxsplit=1), rsplit
# ~ Devuelve una lista de las palabras existentes en la cadena, usando el parámetro sep como delimitador. Si se especifica maxsplit, se realizarán divisiones como máximo, por ende, la lista tendrá como máximo maxsplit+1 elementos. Si el maxsplit no se especifica, o es -1, implica que no hay límite en el número de divisiones, es decir que se realizan todas las divisiones posibles. Si no se especifica un separador con el parámetro sep, la cadena será divida por caracteres no imprimibles (espacios, tabulaciones, saltos de línea)

print('1\t2\n3 4'.split())
print("Hola* mundo* desde* tu* *Nerd".split('*', 2))
print('1\n2\n\n3\n4'.split('\n'))

# * Format -> str.format(*args, **kwargs)
# ~ Realiza una operación para formatear una cadena. Cuando una cadena utiliza este método, puede tener texto literal o campos de reemplazo delimitados por llaves {}. Cada campo de reemplazo puede ser el índice numérico de la posición de un argumento o el nombre de la clave del argumento. El orden sí importa.

print('El resultado de {0}*{1} es {2}'.format(2, 2, 2*2))
print('El resultado de {2}*{1} es {0}'.format(2, 2, 2*2))

my_var = 2
print(f'El resultado es: {my_var}*{10} es {my_var*10}')
print("El resultado es: ", my_var)
print(f"El resultado es: {my_var}")