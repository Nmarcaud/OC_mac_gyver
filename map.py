#! /usr/bin/env python3
# coding: utf-8

import pygame

# Class Map
class Map():

    def __init__(self):

        # Chemin d'accès vers le fichier txt
        self.file = "map.txt"
        self.structure = []


    # Méthode de création de la map
    def create_map(self):

        # Ouverture du fichier ("r" signifie en lecture (read))
        with open(self.file, "r") as file:

            # Init strucutre globale map
            structure = []

            # Parcourir chaque ligne du fichier
            for line in file:

                # Init de la ligne
                line_map = []

                # Parcourir chaque sprite de la ligne
                for sprite in line:

                    # Condition si Sprite éxaminé n'est pas la fin de la ligne (\n)
                    if sprite != "\n":

                        # Alors on ajoute la sprite à la ligne
                        line_map.append(sprite)


                # Ajout de la ligne à lastructure globale de la map
                """Au début j'avais mis un Else, mais cela ne me retournait pas la dernière ligne (car il n'y a pas de saut de ligne sur la dernière)"""
                self.structure.append(line_map)


    def show_map(self, screen):

        # Définition sources images
        background = pygame.image.load("ressource/background.png").convert()
        mur = pygame.image.load("ressource/mur.png").convert()
        gardian = pygame.image.load("ressource/Gardien.png").convert_alpha()
        gardian = pygame.transform.scale(gardian, (40, 40)) # Resize

        # Items
        niddle = pygame.image.load("ressource/seringue.png").convert_alpha()
        niddle = pygame.transform.scale(niddle, (40, 40)) # Resize
        tube = pygame.image.load("ressource/tube_plastique.png").convert_alpha()
        tube = pygame.transform.scale(tube, (40, 40)) # Resize
        ether = pygame.image.load("ressource/ether.png").convert_alpha()
        ether = pygame.transform.scale(ether, (40, 40)) # Resize

        # Show background
        screen.blit(background, (0,0))

        # Init le nombre de ligne de la liste
        n_line = 0
        # Boucle sur la liste Structure
        for line in self.structure:

            # Init du nombre de sprite de la ligne concernée
            n_sprite = 0
            for sprite in line:

                # Inversion des X et y dans mon code ! 40 = largeur d'une sprite
                y = n_line * 40
                x = n_sprite * 40

                # Si c'est un mur
                if sprite == "m":
                    screen.blit(mur,(x,y))

                # Si c'est la sortie
                if sprite == "w":
                    screen.blit(gardian, (x,y))

                # Si niddle
                if sprite == "n":
                    screen.blit(niddle, (x,y))

                # Si tube
                if sprite == "t":
                    screen.blit(tube, (x,y))

                # Si ether
                if sprite == "e":
                    screen.blit(ether, (x,y))

                # incrémentation
                n_sprite += 1
            n_line += 1

