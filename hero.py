#! /usr/bin/env python3
# coding: utf-8

import pygame

# Class Hero (Mac Gyver)
class Hero:


    # Définition du nom en créant l'instance
    def __init__(self, name, structure):
        self.name = name

        # Position Initiale
        self.position = [0, 0]
        self.structure = structure


    # Message de position pour la console
    def message_position(self):
        print(self.name + " est à la position : ( x: " + str(self.position[0]) + ", y: " + str(self.position[1]) + " )")


    # Mouvements de Mac Gyver
    def move_left(self, position, position_perso, bag):
        
        # -1 sur axe y
        # Condition, si arrivé au bord supérieur de la map
        if position[1] == 0:
            # Message console
            print("Can't Move Left (Border limit)")

            # RETURN position inchangée pour affichage
            return position_perso, True

        else:

            # Regarder si c'est un mur (m) ou une case win (w)
            if self.structure[self.position[0]][self.position[1]-1] != "w" and self.structure[self.position[0]][self.position[1]-1] != "m":

                # Modification de la position
                self.position[1] -= 1
                # Message console
                print("Move Left")
                #print(self.message_position())

                # RETURN position modifiée pour affichage
                return position_perso.move(-40,0), True


            # Si c'est l'arrivée
            elif self.structure[self.position[0]-1][self.position[1]] == "w":

                if len(bag) == 3:
                    # Modification de la position
                    self.position[1] -= 1
                    # Message console
                    print("You Win !")

                    # RETURN position modifiée pour affichage
                    return position_perso.move(-40,0), True
                else:

                    # Messages console
                    print("You died ! Il manque " + str(3-len(bag)) + " objets pour gagner !")

                    # RETURN position inchangée pour affichage
                    return position_perso, False


            # il y a un mur
            else:
                # Message console
                print("Can't Move (Wall)")

                # RETURN position inchangée pour affichage
                return position_perso, True



    def move_up(self, position, position_perso, bag):
        # +1 sur axe x
        # Condition, si arrivé au bord supérieur de la map
        if position[0] == 0:
            # Message console
            print("Can't Move Up (Border limit)")

            # RETURN position inchangée pour affichage
            return position_perso, True

        else:

            # Regarder si c'est un mur (m) ou une case win (w)
            if self.structure[self.position[0]-1][self.position[1]] != "w" and self.structure[self.position[0]-1][self.position[1]] != "m":

                # Modification de la position
                self.position[0] -= 1
                # Message console
                print("Move Up")
                #print(self.message_position())

                # RETURN position modifiée pour affichage
                return position_perso.move(0,-40), True


            # Si c'est l'arrivée
            elif self.structure[self.position[0]-1][self.position[1]] == "w":

                if len(bag) == 3:
                    # Modification de la position
                    self.position[0] -= 1
                    # Message console
                    print("You Win !")

                    # RETURN position modifiée pour affichage
                    return position_perso.move(0,-40), True
                else:

                    # Messages console
                    print("You died ! Il manque " + str(3-len(bag)) + " objets pour gagner !")

                    # RETURN position inchangée pour affichage
                    return position_perso, False

                
            # il y a un mur
            else:
                # Message console
                print("Can't Move (Wall)")

                # RETURN position inchangée pour affichage
                return position_perso, True



    def move_right(self, position, position_perso, bag):
        # +1 sur axe y
        # Condition, si arrivé au bord droit de la map
        if position[1] == 14:
            # Message console
            print("Can't Move Right (Border limit)")

            # RETURN position inchangée pour affichage
            return position_perso, True

        else:

            # Regarder si c'est un mur (m) ou une case win (w)
            if self.structure[self.position[0]][self.position[1]+1] != "w" and self.structure[self.position[0]][self.position[1]+1] != "m": 

                # Modification de la position
                self.position[1] += 1
                # Message console
                print("Move Right")
                #print(self.message_position())
                
                # RETURN position modifiée pour affichage
                return position_perso.move(40,0), True


            # Si c'est l'arrivée
            elif self.structure[self.position[0]][self.position[1]+1] == "w":

                if len(bag) == 3:
                    # Modification de la position
                    self.position[1] += 1
                    # Message console
                    print("You Win !")

                    # RETURN position modifiée pour affichage
                    return position_perso.move(40,0), True
                else:

                    # Messages console
                    print("You died ! Il manque " + str(3-len(bag)) + " objets pour gagner !")

                    # RETURN position inchangée pour affichage
                    return position_perso, False




            # il y a un mur
            else:
                # Message console
                print("Can't Move (Wall)")

                # RETURN position inchangée pour affichage
                return position_perso, True



    def move_down(self, position, position_perso, bag):
        # -1 sur axe x
        # Condition, si arrivé au bord inférieur de la map
        if position[0] == 14:
            # Message console
            print("Can't Move Down (Border limit)")

            # RETURN position inchangée pour affichage
            return position_perso, True

        else:

            # Regarder si c'est un mur (m) ou une case win (w)
            if self.structure[self.position[0]+1][self.position[1]] != "w" and self.structure[self.position[0]+1][self.position[1]] != "m":

                # Modification de la position
                self.position[0] += 1
                # Message console
                print("Move Down")
                #print(self.message_position())

                # RETURN position modifiée pour affichage
                return position_perso.move(0,40), True


            # Si c'est l'arrivée
            elif self.structure[self.position[0]+1][self.position[1]] == "w":

                if len(bag) == 3:
                    # Modification de la position
                    self.position[0] += 1
                    # Messages console
                    print("You Win !")

                    # RETURN position modifiée pour affichage
                    return position_perso.move(0,40), True
                else:

                    # Messages console
                    print("You died ! Il manque " + str(3-len(bag)) + " objets pour gagner !")

                    # RETURN position inchangée pour affichage
                    return position_perso, False


            # il y a un mur
            else:
                # Message console
                print("Can't Move (Wall)")

                # RETURN position inchangée pour affichage
                return position_perso, True
    

    



