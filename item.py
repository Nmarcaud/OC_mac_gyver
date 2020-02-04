#! /usr/bin/env python3
# coding: utf-8

# Class item
class Item:

	# Définition du nom et de la position en créant l'instance
	def __init__(self, name, position):
		self.name = name
		self.position = position


	# Methode permetant de savoir si la case de la structure représente un item (et de le renvoyer)
	@classmethod
	def is_it_an_item(cls, structure, position):

		#print(position)

		# Si c'est la case niddle
		if structure[position[0]][position[1]] == "n":

			# Modifie la case par v (afin de modifier l'affichage visuel) 
			structure[position[0]][position[1]] = "v"

			# Return le mot niddle afin de l'ajouter au bag
			return "niddle"


		# Si c'est la case tube
		elif structure[position[0]][position[1]] == "t":

			# Modifie la case par v (afin de modifier l'affichage visuel) 
			structure[position[0]][position[1]] = "v"

			# Return le mot niddle afin de l'ajouter au bag
			return "tube"


		# Si c'est la case ether
		elif structure[position[0]][position[1]] == "e":

			# Modifie la case par v (afin de modifier l'affichage visuel) 
			structure[position[0]][position[1]] = "v"

			# Return le mot niddle afin de l'ajouter au bag
			return "ether"





