# Class Map
class Map():

  # Méthode de création de la map
  def def_map(self):

    map = []

    # Liste de Coordonnées
    x_list = range(0, 14)
    y_list = range(0, 14)

    # Boucle de création de la grille de coordonnées
    for x in x_list:
      for y in y_list:
        coord = [x, y]
        map.append(coord)

    # retour de la méthode
    return map

  # Affichage de la map
  def show_map(self):
    pass