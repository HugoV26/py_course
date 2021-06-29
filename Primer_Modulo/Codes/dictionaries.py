"""

* Diccionarios
    ~ Se utilizan para almacenar valores con una estructura key:Valor
    ~ Son ordenados (a partir de la versión 3.7)
    ~ Son mutables
    ! No permie duplicidad

"""
my_key = "Text"
my_value = "Hola mundo"

my_dict = {
    "color": "red",
    "number": 24,
    my_key: my_value,
    "list": [2, 5],
    "tuple": ("Topla", 5),
    "set": {"El", "Paco"},
    5: "my numero"
}

print(my_dict)

print(my_dict["set"])

print(my_dict[5])


color = my_dict.get("color")
print(color)

keys = my_dict.keys()
print(keys)

val = my_dict.values()
my_dict["year"] = 2021

print(keys)
print(val)

items = my_dict.items()
print(items)


# ^ Revisar si existe una llave

if "color" in my_dict:
    print("Si esta color")
