"""
* 1.- Dada la cadena “El veloz murciélago hindú comía feliz cardillo y kiwi”, imprimir su variante justificada a la derecha rellenando con ‘>’, a la izquierda rellenando con ‘<‘ y centrada en 60 caracteres con asteriscos utilizando métodos de cadenas.
"""
my_text = 'El veloz murciélago hindú comía feliz cardillo y kiwi'
print(my_text.rjust(60, '>'))
print(my_text.ljust(60, '<'))
print(my_text.center(60, '*'))

"""
* 2. Dada la cadena "El Paco es el hombre más guapo de Tu Nerd":
    ~ Imprimir su variante en mayúsculas
    ~ Imprimir su variante en minúsculas
    ~ Intercambiando mayúsculas y minúsculas
    ~ Convertir el primer caracter de cada letra a mayúscula  
"""
my_paco = "El Paco es el hombre más guapo de Tu Nerd"
print(my_paco.upper())
print(my_paco.lower())
print(my_paco.swapcase())
print(my_paco.title())