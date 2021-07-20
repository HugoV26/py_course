"""
    * lambda
    ~ Es una pequeña función anónima.
    ~ Puede tomar cualquier número de elementos o parámetros pero sólo puede tener una expresión a evaluar.

    ^ lambda arguments: expression
"""

s = lambda a: a * 10

print(s(2))

k = lambda a, b, c: a + b + c
print(k(5, 7, 3))

full_name = lambda fn, ln : fn.strip().title() + " " + ln.strip().title()

print(full_name("      pacO", "gonzalez     "))

scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Robert Heinlein", "Arthus C. Clarke", "Frank Herbert", "Orson Scott Card", "Douglas Adams", "H. G. Wells", "Leigh Brackett"]

#help(scifi_authors.sort)

#scifi_authors.sort(key=lambda name: name.split(" ")[1])

scifi_authors.sort(key=lambda name: name.split(" ")[-1])

print(scifi_authors)

# & Quadratic Functions
# ~ f(x) = ax^2 + b*x + c

def quadraticFunction(a, b , c):
    return lambda x: a*x**2 + b*x + c

res = quadraticFunction(2, 3, -5)
#res = lambda x: 2*x**2 + 3*x - 5
print(res(0))
print(res(1))
print(res(2))