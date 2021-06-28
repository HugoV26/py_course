"""
* Diccionarios

    ~ Se utilizan para almacenar valores con una estructura key:value
    ~ Son ordenados
    ~ Son mutables
    ! No permite duplicidad

"""

my_dict = {
    "color": "red",
    "number": 5,
    "value": True,
    "list": ["Hola", "Mundo"],
    "tuple": (24, 95),
    "set": {5, 6}
}

print(my_dict["set"])

x = my_dict.get("color")
print(x)

y = my_dict.keys()
print(y)


v = my_dict.values()
my_dict["year"] = 2021

print(y)
print(v)

i =  my_dict.items()
print(i)

# ^ Revisar si existe un llave

if "color" in my_dict:
    print("Yes, there is a color key")