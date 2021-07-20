*Tarea 1*

1. Investigar los operadores aritméticos y de asignación; mostrar un ejemplo de cada uno.

*Tarea 2*

**Listas**
1. Escribir un programa que le pida al usuario ingresar 5 calificaciones y realizar las siguientes comprobaciones.

    - Verificar cuántas calificaciones están en el rango 0 - 5 e imprimirlas en una lista nueva llamada calificaciones_reprobadas = []
    - Verificar cuántas calificaciones están en el rango 6 - 10 e imprimirlas en una lista nueva llamada calificaciones_aprobatorias = []

2. Escribir un programa que le pida al usuario una palabra y almacena en una lista únicamente las vocales.

Truco:
    word = "Hola"
    print(word[0])   #H
    print(word[1])   #o

3. Mostrar en pantalla todos los métodos que se pueden implementar en una Lista y solicitarle al usuario cuál es el método que desea usuar y ejecutar el método.

Por ejemplo:
Puedes tomar estas listas o puedes crear tus proprias listas.

my_list = ["Hola", "Mundo", 2]
my_second_list = ["Perro", "Gato", True]

"Estos son los métodos disponibles de una Lista: " 
    1) append()
    2) clear()
    3) copy()
    4) count()
    5) extend()
    6) index()
    7) insert()
    8) pop()
    9) remove()
    10) reverse()
    11) sort()

"Ingresa el método que deseas usar: 1"
    "Elegiste el método append, por favor indicame en cuál lista deseas agregar un elemento: "
        1) my_list
        2) my_second_list
        3) Ambas
        "Opcion: 2"
            "Ingresa el nuevo elemento para agregar: "
            **Ejecuto el método append**
            "Tu lista se ha actualizado", my_second_list

"Fin del programa"

Las 3 opciones deben de mostrarse en todos los métodos.

*Tarea 3*  *Fecha Límite de Entrega: 11:59 p.m Viernes 2 de Julio*

1. Definir dos variables que almacenen dos conjuntos respectivamente y dos variables que almacenen dos diccionarios respectivamente.
    1.1 Los valores pueden ser definidos por ustedes o pueden pedirle al usuario que los ingrese.

2. Mostrar en pantalla un menú que despliegue los siguientes métodos que se pueden implementar en conjuntos y diccionarios y solicitarle al usuario cuál es el método que desea usuar y cuál es el conjunto y/o diccionario al que desea aplicarle el método. Ejecutar el método por medio de *funciones*.

    Métodos de los Conjuntos:

        - add()
        - clear()
        - copy()
        - difference()
        - difference_update()
        - discard()
        - intersection()
        - intersection_update()
        - isdisjoint()
        - issubset()
        - issuperset()
        - pop()
        - remove()
        - symmetric_difference()
        - symmetric_difference_update()
        - union()
        - update()

    Métodos de los Diccionarios:
        - clear()
        - copy()
        - fromkeys()
        - get()
        - items()
        - keys()
        - pop()
        - popitem()
        - setdefault()
        - update()
        - values()

3. Después de haber ejecutado cualquier método, se deberá preguntarle al usuario si quiere volver a ver el menú, de ser así, mostrar todo el menú desde el inicio.

4. Subir la tarea a su repositorio en GitHub.