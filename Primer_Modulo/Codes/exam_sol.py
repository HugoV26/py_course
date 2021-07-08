# 1. Define una función que reciba un parámetro de tipo string e identifica si tiene caracteres únicos.
# Utilizar un conjunto para verificar esta condición.
def unicos (cadena_entrada):
    caracteres_unicos = set(cadena_entrada)
    print(caracteres_unicos)

cadena = "Hola mundo"
unicos(cadena)

# 2. Define una función que reciba dos parámetros; productos y precios.
# Estos valores se deberán guardar en un diccionario, en total se almacenarán 5 productos.
# Retornar cuál es el producto con mayor precio. 

def inventario (producto, precio):
    aux = 0
    dicc = {producto[i]: precio[i] for i in range(len(producto))}
    print(dicc)
    for v in dicc.values():
        if v > aux:
            aux = v
    
    return aux



lista1 = ["Huevos", "Jamon", "Salsa", "Chiles", "Aceite"]
lista2 = [5.50, 3.20, 10, 4.98, 8.30]

res = inventario(lista1, lista2)
print("El precio más alto fue de: ", res)