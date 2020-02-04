#! /usr/bin/env python3
# coding: utf-8

from map import Map
from hero import Hero
from bag import Bag
from item import Item
from user_action import User_action

import pygame
import random


# Init Pygame
pygame.init()
# Init taille de l'écran
screen = pygame.display.set_mode((600, 600))

# Titre du jeu
pygame.display.set_caption("MacGyver et le temple vraiment maudit 👻")





# Action
def main():

	# Instance de la Map
	ma_map = Map()
	ma_map.create_map()

	# Instance du bag
	bag = Bag()

	# Liste Items
	items_coord_list = {}

	# Init Items
	niddle_position = Item.random_position(ma_map.structure)
	items_coord_list["niddle"] = niddle_position

	tube_position = Item.random_position(ma_map.structure)
	items_coord_list["tube"] = tube_position

	ether_position = Item.random_position(ma_map.structure)
	items_coord_list["ether"] = ether_position


	# Creation du Hero
	mac_gyver = Hero("Mac Gyver", ma_map.structure)

	# Chargement et collage du personnage
	perso = pygame.image.load("ressource/MacGyver.png").convert_alpha()
	perso = pygame.transform.scale(perso, (40, 40)) # Resize
	position_perso = perso.get_rect()	# = 0, 0 si vide
	screen.blit(perso, position_perso)

	# Création visuelle de la map
	ma_map.show_map(screen, items_coord_list)


	# Refresh
	pygame.display.flip()


	launched = True
	while launched:

		# Limitation de vitesse de la boucle (nécessaire pour éviter de surcharger le processeur !)
		pygame.time.Clock().tick(30)

		# Ecoute pour un évènement
		for event in pygame.event.get():

			# Si on clic sur QUIT
			if event.type == pygame.QUIT:
				launched = False

			# Si on presse une touche du clavier
			if event.type == pygame.KEYDOWN:

				# Action si fleche directionnelle Gauche
				if event.key == pygame.K_LEFT:
					position_perso = mac_gyver.move_left(mac_gyver.position, position_perso, bag.items)

				# Action si fleche directionnelle Haut
				elif event.key == pygame.K_UP:
					position_perso = mac_gyver.move_up(mac_gyver.position, position_perso, bag.items)

				# Action si fleche directionnelle Droite
				elif event.key == pygame.K_RIGHT:
					position_perso = mac_gyver.move_right(mac_gyver.position, position_perso, bag.items)

				# Action si fleche directionnelle Bas
				elif event.key == pygame.K_DOWN:
					position_perso = mac_gyver.move_down(mac_gyver.position, position_perso, bag.items)

				# Ajout au bag si objet
				# Stockage du retour dans une variable pour plus de lisibilité
				item_to_add = Item.is_it_an_item(mac_gyver.position, items_coord_list)
				if item_to_add != None:

					# Pour éviter d'ajouter 2 fois l'item !
					if bag.items.count(item_to_add) == 0:

						# Ajout de l'item à la liste bag.items
						bag.items.append(item_to_add)
				
				print("Bag : " + str(bag.items))	#test


		# Re-génération visuelle de la map
		ma_map.show_map(screen, items_coord_list)
		# Modification visuelle position perso
		screen.blit(perso, position_perso)
		# Refresh
		pygame.display.flip()


if __name__ == "__main__":
    main()