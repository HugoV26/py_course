people = ('Hugo', 'Sara', ' Ale',' Hiro')

def isValid(name, edad):
    if name in people and edad >= 18:
        return True

#print(isValid(input("Ingresa tu nombre: "), int(input('Ingresa tu edad: '))))


def ordenarFrase(frase: str, invertida: bool = False):
    """
    * sorted(iterable, key, reverse)
    ~ iterable -> required, la secuencia a ordenar: list, string, tupla, etc
    ~ key -> opcional, funcion que decide el orden. Por default es None
    ~ reverse -> opcional, es un booleano, False ordena de forma ascendente, True ordena de forma descendente. Default es Falso
    """
    
    aux = " ".join(sorted(frase.split(), key=len, reverse=invertida))
    # return " ".join(sorted(frase.split(), key=len, reverse=invertida))
    print(aux)
    return sorted(sorted(aux.split()), key=len)


print(ordenarFrase('I really love her you know who you are'))
print(ordenarFrase.__annotations__)
print(ordenarFrase.__doc__)

my_str = "Hola mundo"
print(my_str.split())

#a = ("c", "a", "d", "x")
#b = sorted(a)
#print(b)

"""
def test(text: str):
    print("My text is: " + text)

test(106)
"""