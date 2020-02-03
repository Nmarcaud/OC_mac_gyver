#! /usr/bin/env python3
# coding: utf-8

# imports
import random

max_x = 14
max_y = 14

# Class Map
class Map():

  # Méthode de création de la map
  def def_map(self):

    liste_coordonnees = []

    # Liste de Coordonnées
    x_list = range(0, max_x)
    y_list = range(0, max_y)

    # Boucle de création de la grille de coordonnées
    for x in x_list:
      for y in y_list:
        coord = [x, y]
        liste_coordonnees.append(coord)

    # retour de la méthode
    return liste_coordonnees

  # Affichage de la map
  def show_map(self):
    pass



# Class Hero (Mac Gyver)
class Hero():

  # Définition du nom en créant l'instance
  def __init__(self, name):
    self.name = name

  # Position Initiale
  position = [random.randint(0,max_x), random.randint(0,max_y)]


  # Mouvements de Mac Gyver ?
  def move_left(self, position):
    # -1 sur axe x
    # Condition, si arrivé au bord gauche de la map
    if position[0] == 0:
      position[0] = max_x
    else:
      position[0] -= 1

    # Message console
    print("Move Left")

    #retour
    return position

  def move_up(self, position):
    # +1 sur axe y
    # Condition, si arrivé au bord supérieur de la map
    if position[1] == max_y:
      position[1] = 0
    else:
      position[1] += 1

    # Message console
    print("Move Up")

    # retour
    return position

  def move_right(self, position):
    # +1 sur axe x
    # Condition, si arrivé au bord droit de la map
    if position[0] == max_x:
      position[0] = 0
    else:
      position[0] += 1

    # Message console
    print("Move Right")

    # retour
    return position

  def move_down(self, position):
    # -1 sur axe y
    # Condition, si arrivé au bord inférieur de la map
    if position[1] == 0:
      position[1] = max_y
    else:
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

# Test mouvements
# mac_gyver.move_left(mac_gyver.position)
# message_position(mac_gyver)
# mac_gyver.move_up(mac_gyver.position)
# message_position(mac_gyver)
# mac_gyver.move_right(mac_gyver.position)
# message_position(mac_gyver)
# mac_gyver.move_down(mac_gyver.position)
# message_position(mac_gyver)

# Test de la map
map=Map()
print(map.def_map())

def user_action():
  user_answer = str(input("Direction mac Gyver: "))
  return user_answer


def main():

  message_accueil = """ Tu vas devoir donner une direction à MacGyver
                    Gauche : 4
                    Haut : 8
                    Droite : 6
                    Bas : 2
                    
                    Break : b
                    """

  # Affichage du message d'accueil
  print(message_accueil)
  user_answer = user_action()

  while user_answer != "b":

    if user_answer == "4":
      mac_gyver.move_left(mac_gyver.position)
      message_position(mac_gyver)
      user_answer = user_action()

    elif user_answer == "8":
      mac_gyver.move_up(mac_gyver.position)
      message_position(mac_gyver)
      user_answer = user_action()

    elif user_answer == "6":
      mac_gyver.move_right(mac_gyver.position)
      message_position(mac_gyver)
      user_answer = user_action()

    elif user_answer == "2":
      mac_gyver.move_down(mac_gyver.position)
      message_position(mac_gyver)
      user_answer = user_action()




if __name__ == "__main__":
    main()