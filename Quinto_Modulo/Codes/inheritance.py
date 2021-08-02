#!/usr/bin/env python3.8

"""
	* Herencia
		~ Es una forma de crear una nueva clase tomando como referencia una clase existente ('clase padre' o 'superclase') sin alterarla.
		~ Esta nueva clase, se le conoce como "Clase Hija" ó 'Subclase'.
		~ La subclase hereda los métodos de la superclase, a menos que la subclase los reimplemente.
"""


class Whisky():

	def __init__(self, name, country):
		self.name = name
		self.country = country

	def getInfo(self):
		print(f"Whisky Marca: {self.name} | País de Origen: {self.country}")


class JohnnieWalker(Whisky):

	def __init__(self, name, country, label, degrees, cost):
		#Envíamos los parámetros al constructor de la súper clase 
		super().__init__(name, country)
		
		self.label = label
		self.degrees = degrees
		self.cost = cost

	def makeACockatil(self, cocktail):

		self.bebida = cocktail

		print(self.bebida)

		if self.bebida == "Johnnie Ginger":
			pass
		elif self.bebida == "Johnnie Walker Red y Arándanos":
			pass
		elif self.bebida == "Johnnie Walker Black & Soda":
			pass

class Aforita(JohnnieWalker):

	def __init__(self, name, country, label, degrees, cost, capacity):
		super().__init__(name, country, label, degrees, cost)

		self.capacity = capacity

	def test(self):
		print("Capaciad: ", self.capacity)
	

red_label = JohnnieWalker("Johnnie Walker", "Escocia", "Black Label", 35, 800)

red_label.getInfo()

red_label.makeACockatil("Test")

blue_label = Aforita("Johnnie Walker", "Escocia", "Blue Label", 40, 120, "250ml")

blue_label.test()