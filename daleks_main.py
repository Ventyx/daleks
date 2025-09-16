#### Fichier Main
from msvcrt import getch
import os


class Grille :
    TAS_X, TAS_Y = 10, 10

    VIDE = "O"
    ZAP = "Z"
    FERRAILE = "X"
    TELEPORTEUR = "T"
    DALEK = "D"
    JOUEUR = "J"

    grille = [
    [VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE],
    [VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE],
    [VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE],
    [VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE],
    [VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE],
    [VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE],
    [VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE],
    [VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE],
    [VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE],
    [VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE, VIDE], 
    ]
    
def affichage() :
      for i in range (0, Grille.TAS_Y) :
        print(Grille.grille[i][0], Grille.grille[i][1], Grille.grille[i][2], Grille.grille[i][3], Grille.grille[i][4], Grille.grille[i][5], Grille.grille[i][6], Grille.grille[i][7], Grille.grille[i][8], Grille.grille[i][9])


game_over = True

print("Jeu du dalek! \n\n\n")
print("Voulez vous Jouer ? (o/n)")
choix_de_jouer = getch()

if (choix_de_jouer == b'o'):
    game_over = False
    _ = os.system('cls')
    

while not game_over:
    # Déroulement du jeu
    print("skibidi")
    game_over = True


