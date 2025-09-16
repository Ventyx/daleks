#### Fichier Main
from msvcrt import getch
import os
from msvcrt import getch

# Le joueur
class Player :
    # Constructeur
    def __init__(self, posX, posY, vies, teleporteur, zappeur):
        self.posX = posX
        self.posY = posY
        self.vies = vies
        self.teleporteur = teleporteur
        self.zappeur = zappeur

    # Déplacer le joueur
    def move(self, moveX, moveY):

        self.posX += moveX
        if (self.posX < 0):
            self.posX = 0
        if (self.posX > 9):
            self.posX = 9
        self.posY += moveY
        if (self.posY < 0):
            self.posY = 0
        if (self.posY > 9):
            self.posY = 9
    # Obtenir la Position actuelle
    def getPos(self):
        return (self.posX, self.posY)

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
    
docteur = Player(0, 0, 4, 0, 0)

while not game_over:
    # Déroulement du jeu
    _ = os.system('cls')
    
    Grille.grille[docteur.posX][docteur.posY] = Grille.JOUEUR
    
    affichage()

    playerInput = getch()    

    if (playerInput == b'w'):
        docteur.move(0,1)
    elif (playerInput == b's'):
        docteur.move(0,-1)
    elif (playerInput == b'a'):
        docteur.move(-1,0)
    elif (playerInput == b'd'):
        docteur.move(1,0)
    elif (playerInput == b'o'):
        game_over = True
    


