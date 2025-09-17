#### Fichier Main
from msvcrt import getch
import os
from msvcrt import getch

# Codes de couleur pour console
GREEN = '\033[32m'
WHITE = '\033[0m'

class Grille :
    TAS_X, TAS_Y = 10, 10

    VIDE = "O"
    ZAP = "Z"
    FERRAILE = "X"
    TELEPORTEUR = "T"
    DALEK = "D"
    JOUEUR = f"{GREEN}J{WHITE}"

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
      for y in range (0, Grille.TAS_Y) :
        for x in range (0, Grille.TAS_X):
            print(Grille.grille[y][x] + ' ', end = '')
        print('')

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
        
        # Y et X sont inversés, position précédente remise a vide.
        Grille.grille[self.posY][self.posX] = Grille.VIDE

        self.posX += moveX
        if (self.posX < 0):
            self.posX = 0
        if (self.posX > 9):
            self.posX = 9
        self.posY -= moveY
        if (self.posY < 0):
            self.posY = 0
        if (self.posY > 9):
            self.posY = 9
        
    # Obtenir la Position actuelle
    def getPos(self):
        return (self.posX, self.posY)


# Menu principal
game_over = True

print("Jeu du dalek! \n\n\n")
print("Voulez vous Jouer ? (o/n)")
choix_de_jouer = getch()

if (choix_de_jouer == b'o'):
    game_over = False
    _ = os.system('cls')
    

# Création d'un objet joueur nommé docteur
docteur = Player(0, 0, 4, 0, 0)


# Déroulement du jeu
while not game_over:
    _ = os.system('cls')
    
    # Affichage position Joueur
    Grille.grille[docteur.posY][docteur.posX] = Grille.JOUEUR

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
    


