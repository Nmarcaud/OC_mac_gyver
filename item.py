#! /usr/bin/env python3
# coding: utf-8

import pygame
import random


# Class item
class Item:

	# Définition du nom et de la position en créant l'instance
	def __init__(self, name, position, frame):
		self.name = name
		self.position = position
		self.frame = frame


	@classmethod
	def random_position(cls, structure):

		valid_position = False

		while valid_position == False:

			random_position = [random.randint(0,14),random.randint(0,14)]

			line_incr = 0

			for line in structure:

				if line_incr == random_position[0]:

					sprite_incr = 0

					for sprite in line:

						if sprite_incr == random_position[1] and sprite == "v":

							#print(line_incr, sprite_incr)
							# Calcul des coordonnées avec la taille de mes sprites
							coord = (sprite_incr * 40, line_incr * 40)

							# Vérifier qu'un item n'est pas déjà présent sur cet emplacement
							#for value in items_list.values():


							# Mettre fin à la boucle While
							valid_position = True

							# Retourner les coordonées
							return coord

						sprite_incr += 1
				line_incr += 1



	# Methode d'affichage des items selon ce qu'il reste dans la liste des coordoonées
	@classmethod
	def show_items(cls, screen, items_coord_list):

		# obliger de mettre un if sinon la fonction blit plante faute d'élément à renvoyer

		# If
		if items_coord_list.get("niddle") != None:
			niddle = pygame.image.load("ressource/aiguille.png").convert()
			niddle = pygame.transform.scale(niddle, (40, 40)) # Resize
			screen.blit(niddle, items_coord_list.get("niddle"))

		if items_coord_list.get("tube") != None:
			tube = pygame.image.load("ressource/tube_plastique.png").convert_alpha()
			tube = pygame.transform.scale(tube, (40, 40)) # Resize
			screen.blit(tube, items_coord_list.get("tube"))

		if items_coord_list.get("ether") != None:
			ether = pygame.image.load("ressource/ether.png").convert_alpha()
			ether = pygame.transform.scale(ether, (40, 40)) # Resize
			screen.blit(ether, items_coord_list.get("ether"))






	# Methode permetant de savoir si la case de la structure représente un item (et de le renvoyer)
	@classmethod
	def is_it_an_item(cls, position, items_coord_list):

		for key, val in items_coord_list.items():

			#print(val, position[0]*40, position[1]*40)

			if val == (position[1]*40, position[0]*40):

				print("Get " + key)
				del items_coord_list[key]

				return key
				








