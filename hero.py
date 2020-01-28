#! /usr/bin/env python3
# coding: utf-8

# Class Hero (Mac Gyver)
class Hero:


    # Définition du nom en créant l'instance
    def __init__(self, name, structure):
        self.name = name

        # Position Initiale
        self.position = [0, 0]
        self.structure = structure



    # Mouvements de Mac Gyver ?
    def move_left(self, position):
        
        # -1 sur axe x
        # Condition, si arrivé au bord supérieur de la map
        if position[1] == 0:
            # Message console
            print("Can't Move Left (Border limit)")
        else:

            # Regarder si c'est un mur (m) ou une case vide (v)
            if self.structure[self.position[0]][self.position[1]-1] == "v":

                self.position[1] -= 1
                # Message console
                print("Move Left")

            # il y a un mur
            else:
                # Message console
                print("Can't Move (Wall)")


        #retour
        return self.position


    def move_up(self, position):
        # +1 sur axe y
        # Condition, si arrivé au bord supérieur de la map
        if position[0] == 0:
            # Message console
            print("Can't Move Up (Border limit)")
        else:

            # Regarder si c'est un mur (m) ou une case vide (v)
            if self.structure[self.position[0]-1][self.position[1]] == "v":

                self.position[0] -= 1
                # Message console
                print("Move Up")

            # il y a un mur
            else:
                # Message console
                print("Can't Move (Wall)")

        # retour
        return self.position


    def move_right(self, position):
        # +1 sur axe x
        # Condition, si arrivé au bord droit de la map
        if position[1] == 14:
            # Message console
            print("Can't Move Right (Border limit)")
        else:

            # Regarder si c'est un mur (m) ou une case vide (v)
            if self.structure[self.position[0]][self.position[1]+1] == "v":

                self.position[1] += 1
                # Message console
                print("Move Right")

            # il y a un mur
            else:
                # Message console
                print("Can't Move (Wall)")

        # retour
        return self.position

    def move_down(self, position):
        # -1 sur axe y
        # Condition, si arrivé au bord inférieur de la map
        if position[0] == 14:
            # Message console
            print("Can't Move Down (Border limit)")
        else:

            # Regarder si c'est un mur (m) ou une case vide (v)
            if self.structure[self.position[0]+1][self.position[1]] == "v":

                self.position[0] += 1
                # Message console
                print("Move Down")

            # il y a un mur
            else:
                # Message console
                print("Can't Move (Wall)")

        # retour
        return self.position


    def message_position(self):
        print(self.name + " est à la position : ( x: " + str(self.position[0]) + ", y: " + str(self.position[1]) + " )")


