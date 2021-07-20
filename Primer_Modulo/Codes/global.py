"""

* Variables Globales & Locales

~ Es posible acceder al contenido de una variable si esta se declara afuera de una función, es decir, en el ambiente global.
~ En los siguientes ejemplos, le asignaremos un id a la variable que vamos a manipular para entender mejor cómo va evolucionando.
"""

#Esta variable fue declarada en el ambiente global
name_pokemon = "Charmander"     # name_pokemon --> id: 1

def pokemon():
    print("\nTu pokemon dentro de la función es: " + name_pokemon)      # name_pokemon (id: 1)

pokemon()
print("Tu pokemon fuera de la función es: " + name_pokemon + "\n")      # name_pokemon (id: 1)

"""
^ En el ejemplo anterior lo único que hicimos fue acceder al contenido de la variable name_pokemon, la cual fue definida en el ámbito global. Ahora vamos a ver un ejemplo de cómo cambiar su contenido.
"""

def changePokemon():
    #Esta variable está declarada en un ámbito local
    name_pokemon = "Charizard"                                  # name_pokemon (id: 2)
    print("Se ha cambiado el nombre a: " + name_pokemon)        # name_pokemon (id: 2)

changePokemon()
print("Tu pokemon después de haber ejecutado la función changePokemon es: " + name_pokemon + "\n")       # name_pokemon (id: 1)

"""
^ La variable name_pokemon (id: 2) que declaramos dentro de la función changePokemon es totalmente independiente de la variable name_pokemon (id: 1)
"""

def changePokemonTwo():
    #Esta variable está declarada en un ámbito local
    name_pokemon = name_pokemon + " es de tipo fuego"
    print(name_pokemon)

#changePokemonTwo()

"""
^ En la función changePokemonTwo() esperabamos imprimir:
    * Charmander es de tipo fuego 
^ Pero, al momento de ejecutar la función nos retorna el siguiente error:
    ! UnboundLocalError: local variable 'name_pokemon' referenced before assignment
^ Esto sucede porque la asignación que estamos realizando DENTRO de esta función es:
    ! name_pokemon (id: 3) = name_pokemon (id: 1) + " es de tipo fuego"
^ Y la variable name_pokemon (id: 1) NO existe en esta función.
"""

def changePokemonThree():
    global name_pokemon  #name_pokemon (id: 1) 
    print(name_pokemon)  #name_pokemon (id: 1)
    name_pokemon = name_pokemon + " es de tipo fuego"   # name_pokemon (id: 1) = name_pokemon (id: 1) + " es de tipo fuego" 
    print(name_pokemon + "\n")

changePokemonThree()

"""
^ En esta última función, changePokemonThree, definimimos como global la variable name_pokemon (id: 1), esta definición hace referencia a la variable que declaramos en un principio (Línea 10)
"""

def changePokemonFour():
    global other_pokemon            # other_pokemon (id: ?)
    other_pokemon = "Mewtwo"        # other_pokemon (id: 4)
    print(other_pokemon)

changePokemonFour()
print("\n")

"""
^ Sabiendo lo anterior, dentro de la función changePokemonFour, declaramos como global la variable other_pokemon (id: ?) pero nos indica un error:
    ! other_pokemon (id: ?) no está definida en el ámbito local
^ Es decir, esa variable NO está definida fuera de la función, a diferencia de como lo hicimos en changePokemonThree()
"""

"""
* Ahora veamos un ejemplo de variables NO locales
"""

def looneyTunes():
    character = "Pato Lucas"     # character (id: 1)

    def conejo():
        nonlocal character      # character (id: 1)
        character = character + " & Bugs Bunny"     # character (id: 1) = character (id: 1) + " & Bugs Bunny"
        print("Conejo:", character)         # character (id: 1)
    
    conejo()
    character = "Demonio de Tasmania"
    conejo()
    print("looneyTunes:", character)        # character (id: 1)


looneyTunes()

"""
^ Como podemos observar, la variable character (id: 1) es la misma para cualquier instrucción en la que la mandemos a llamar. 
^ Estas variables se utilizan en funciones anidadas, y ni son locales ni son globales.
"""

"""
* Conclusiones

    ~ Una variable definida dentro de una función es local, cuando esta función termine de ejecutarse, la variable ya no existirá.
    ~ Las variables definidas fuera de una función son globales, por lo que no es necesario colocarles la palabra reservada global.
    ~ Podemos declarar una variable global dentro de una función para re-asignar su valor siempre y cuando esta variable haya sido declarada en el ámbito global, es decir, afuera de la función.
    ~ Es muy mala práctica usar variables globales dentro de una función, por lo que, sólo si es necesario se deberá de usar esta declaración.

"""