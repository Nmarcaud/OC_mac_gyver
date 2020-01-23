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
    if position[0] == 0:
      position[0] = 0
      # Message console
      print("Can't Move Left")
    else:
      position[0] -= 1
      # Message console
      print("Move Left")

    #retour
    return position

  def move_up(self, position):
    # +1 sur axe y
    # Condition, si arrivé au bord supérieur de la map
    if position[1] == 14:
      position[1] = 14
      # Message console
      print("Can't Move Up")
    else:
      position[1] += 1
      # Message console
      print("Move Up")

    # retour
    return position

  def move_right(self, position):
    # +1 sur axe x
    # Condition, si arrivé au bord droit de la map
    if position[0] == 14:
      position[0] = 14
      # Message console
      print("Can't Move Right")
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
      position[1] = 0
      # Message console
      print("Can't Move Down")
    else:
      position[1] -= 1
      # Message console
      print("Move Down")

    # retour
    return position
