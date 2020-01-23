class User_action:


  WELCOME_MSG = """ Tu vas devoir donner une direction à MacGyver
                      Gauche : 4
                      Haut : 8
                      Droite : 6
                      Bas : 2

                      Break : b
                      """

  def user_action():
    user_answer = str(input("Direction mac Gyver: "))
    return user_answer