#! /usr/bin/env python3
# coding: utf-8

# imports
import random


# Class Map
class Map():

  # Méthode de création de la map
  def def_map(self):

    liste_coordonnees = []

    # Liste de Coordonnées
    x_list = range(0, 14)
    y_list = range(0, 14)

    # Boucle de création de la grille de coordonnées
    for x in x_list:
      for y in y_list:
        coord = [x, y]
        liste_coordonnees.append(coord)

    # retour de la méthode
    return liste_coordonnees




# Class Hero (Mac Gyver)
class Hero():

  # Définition du nom en créant l'instance
  def __init__(self, name):
    self.name = name

  # Position Initiale
  position = [random.randint(0,14), random.randint(0,14)]


  # Mouvements de Mac Gyver ?
  def move_left(self, position):
    # -1 sur axe x
    position[0] -= 1

    # Message console
    print("Move Left")

    #retour
    return position


  def move_up(self, position):
    # +1 sur axe y
    position[1] += 1

    # Message console
    print("Move Up")

    # retour
    return position

  def move_right(self, position):
    # +1 sur axe x
    position[0] += 1

    # Message console
    print("Move Right")

    # retour
    return position

  def move_down(self, position):
    # -1 sur axe y
    position[1] -= 1

    # Message console
    print("Move Down")

    # retour
    return position




# Class item
class Item():

  # Définition du nom en créant l'instance
  def __init__(self, name):
    self.name = name



##########################################
# Fonctions

# Message de position
def message_position(hero):
  print(hero.name + " est à la position : ( x: " + str(hero.position[0]) + ", y: " + str(hero.position[1]) + " )")


##########################################
# Tests
#########################################
# Test de Mac Gyver
mac_gyver = Hero("MacGyver")
message_position(mac_gyver)

#Test mouvement
mac_gyver.move_left(mac_gyver.position)
message_position(mac_gyver)
#Test mouvement
mac_gyver.move_up(mac_gyver.position)
message_position(mac_gyver)
#Test mouvement
mac_gyver.move_right(mac_gyver.position)
message_position(mac_gyver)
#Test mouvement
mac_gyver.move_down(mac_gyver.position)
message_position(mac_gyver)

# Test de la map
map=Map()
print(map.def_map())