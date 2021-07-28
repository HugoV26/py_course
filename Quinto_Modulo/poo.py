#!/usr/bin/env python3.8
"""
	* Programación Orientada a Objetos

		~ Es un paradigma de la programación.
		~ Se enfoca en reutilizar código.
		~ También se le conoce como DRY (Don't Repeat Yourself).

		¿Qué es un paradigma?

			~ Modelo básico de diseño y desarrollo de programas.

		¿Qué es una clase?
			~ Es como un molde que se toma como base para fabricar distintos objetos con la misma estructura.
			~ Para generar un objeto a partir de una clase, se la debe instanciar.
			~ Los objetos de la misma clase, tienen los mismos métodos y atributos, pero los atributos pueden tener distintos valores.

		¿Qué es un objeto?
			~ Todo lo que nos rodea.
			~ Es una instancia de una clase.

			* Un objeto tiene atributos y métodos.
				~ Atributos: características que lo definen
				~ Métodos: acciones que puede realizar

		Atributos

			~ Propiedades del objeto representados mediante variables.
			~ Pueden ser de cualquier tipo de dato (incluso otros objetos)
			~ Pueden crearse de forma dinámica durante la ejecución.

		Métodos
			~ Dan funcionalidad a los objetos.
			~ Necesitan de una clase para existir.
			~ Similares a las funciones (puede recibir parámetros y retornar un valor)
			~ Puede invocarse desde el propio objeto que lo contiene o desde otro, con la sintaxis object.method()

		Constructor
			~ Es un método especial: instancia objetos de una clase (se invoca automáticamente).
			~ En él pueden inicializarse los atributos de un objeto.
			~ NO es obligatorio crearlo ni inicializar todos los atributos.
			~ Las funciones de las clases que comienzan con __ son llamadas funciones especiales, pero si se usan bajo un entorno de POO se les conoce como constructores.

"""
"""
class Jedi:
	#Atributos
	name = "Anakin Skaywalker"
	height = 1.88
	master = "Obi-Wan Kenobi"

	#Métodos
	def darthVader(self):
		print("Yo soy tu padre")

jedi_one = Jedi()
print("El nombre del jedi es: " + jedi_one.name)
jedi_one.darthVader()

jedi_two = Jedi()
jedi_two.name = "Master Yoda"
jedi_two.height = 1.30

print("El nombre del segundo jedi es: " + jedi_two.name + " y su altura es de: " , jedi_two.height)
"""

class Princess:

	#Atributo de clase
	company = "Disney"

	def __init__(self, param1, param2):
		#Atributos de instancia, privados
		self.name = param1
		self.skill = param2
		self.friends = []

	def getInfo(self):
		print("Su nombre es: " + self.name)
		print("Su habilidad es: " + self.skill)
		print("Trabaja para: " + self.__class__.company) #Accedieno al atributo de la clase

	def isFriend(self, friend):
		return friend in self.friends

	def __str__(self):
		return 'Nombre :' + self.name + ' | Skill: ' + self.skill

	def addAttr(self, attr):
		setattr(self, attr, attr)
				#self.attr = attr

mulan = Princess('Mulán', "Guerrera, Valiente")
mulan.getInfo()

print(mulan)
mulan.friends.append("Mushu")

print(mulan.isFriend("Shang"))

elsa = Princess("Elsa", "Controla el Hielo")
elsa.getInfo()
elsa.enemy = "Hans"
print("El enemigo de {}".format(elsa.name) + " es {}".format(elsa.enemy))

#print(mulan.enemy)

setattr(Princess, "enemy", "Mongoles")

print(f"El enemigo de mulan es {mulan.enemy}")

la_sirenita = Princess("Ariel", "Nadar")

la_sirenita.enemy = "Ursula"

print(f"El enemigo de {la_sirenita.name} es {la_sirenita.enemy}")

"""
 * Tarea 1:
	~ Investigar UML y modelar un clase.

	* Exposición

	# ^ Sara -> Tema 3: Excepción definida por el usuario (raise)
	# ^ La Ale -> Tema 1: Python OS Module
	# ^ Hiroshi -> Tema 2: Recursión
	# ^ Rodrigo -> Tema 4: Iteradores (__iter__, __next)
"""
