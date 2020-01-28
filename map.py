#! /usr/bin/env python3
# coding: utf-8

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


    # Affichage de la map
    def show_map(self):
        pass