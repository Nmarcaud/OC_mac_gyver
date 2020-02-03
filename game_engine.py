#! /usr/bin/env python3
# coding: utf-8

from map import Map
from hero import Hero
from bag import Bag
from item import Item
from user_action import User_action

import pygame

# Init Pygame
pygame.init()
# Init taille de l'écran
screen = pygame.display.set_mode((600, 600))

# Titre du jeu
pygame.display.set_caption("MacGyver et le temple Maudit")


# Action
def main():

	# Instance de la Map
	ma_map = Map()
	ma_map.create_map()

	# Création visuelle de la map
	ma_map.show_map(screen)


	# Creation du Hero
	mac_gyver = Hero("Mac Gyver", ma_map.structure)

	# Chargement et collage du personnage
	perso = pygame.image.load("ressource/MacGyver.png").convert_alpha()
	position_perso = perso.get_rect()	# = 0, 0 si vide
	screen.blit(perso, position_perso)


	# Refresh
	pygame.display.flip()


	launched = True
	while launched:

		# Ecoute pour un évènement
		for event in pygame.event.get():

			# Si on clic sur QUIT
			if event.type == pygame.QUIT:
				launched = False

			# Si on presse une touche du clavier
			if event.type == pygame.KEYDOWN:

				# Action si fleche directionnelle Gauche
				if event.key == pygame.K_LEFT:
					position_perso = mac_gyver.move_left(mac_gyver.position, position_perso)

				# Action si fleche directionnelle Haut
				elif event.key == pygame.K_UP:
					position_perso = mac_gyver.move_up(mac_gyver.position, position_perso)

				# Action si fleche directionnelle Droite
				elif event.key == pygame.K_RIGHT:
					position_perso = mac_gyver.move_right(mac_gyver.position, position_perso)

				# Action si fleche directionnelle Bas
				elif event.key == pygame.K_DOWN:
					position_perso = mac_gyver.move_down(mac_gyver.position, position_perso)


		# Re-génération visuelle de la map
		ma_map.show_map(screen)
		# Modification visuelle position perso
		screen.blit(perso, position_perso)
		# Refresh
		pygame.display.flip()


if __name__ == "__main__":
    main()