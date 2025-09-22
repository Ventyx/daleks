#### Fichier Main
from msvcrt import getch
import os
from msvcrt import getch
import random
from time import sleep

# Codes de couleur pour console
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[1;33m"
BROWN = "\033[0;33m"
CYAN = "\033[0;36m"
WHITE = "\033[0m"

# Variables 
MAX_DALEKS = 3
Score = 0
daleks = []

class Grille :
    # longueur et largeur MAX de la grille 
    TAS_X, TAS_Y = 10, 10

    VIDE = f"{WHITE}O"
    ZAP = f"{CYAN}Z"
    FERRAILE = f"{BROWN}X"
    TELEPORTEUR = f"{YELLOW}T"
    DALEK = f"{RED}D"
    JOUEUR = f"{GREEN}J"

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

# Le joueur
class Player :
    # Constructeur
    def __init__(self, posX, posY, teleporteur, zappeur):
        self.posX = posX
        self.posY = posY
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

# Dalek
class Dalek :
    # Constructeur
    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY
        self.etat = True

    # Chasse le joueur
    def chasse(self, docteur):
        docX = docteur.posX
        docY = docteur.posY

        # Y et X sont inversés, position précédente remise a vide.
        Grille.grille[self.posY][self.posX] = Grille.VIDE

        if (self.posY < docY):
            self.posY += 1
        elif (self.posY > docY):
            self.posY -= 1
        elif (self.posX < docX):
            self.posX += 1
        elif (self.posX > docX):
            self.posX -= 1

# affichage de la grille (y = rangée, x = colonne)
def grilleAffichage() :
      for y in range (0, Grille.TAS_Y) :
        for x in range (0, Grille.TAS_X):
            print(Grille.grille[y][x] + ' ', end = '')
        print('')

# affichage du UI
def uiAffichage():
    print("\n UTILISER W,A,S,D POUR SE DÉPLACER    |    Q = Zappeur    |    E = Téléportation    |    O = Arrêter de jouer")
    print("\n\n")
    print(f"{RED}Daleks restants : " + str(daleks.count))
    print(f"{CYAN}Téléporteurs utilisables : " + str(docteur.teleporteur))
    print(f"{YELLOW}Zappeurs utilisables : " + str(docteur.zappeur))
    print(f"{WHITE}Score : " + str(Score))

# Menu principal
game_over = True
jouer = True
while jouer :
    print("Jeu du dalek! \n\n\n")
    print("Voulez vous Jouer ? (o/n)")
    choix_de_jouer = getch()

    if (choix_de_jouer == b'o'):
        game_over = False
        _ = os.system('cls')
    elif (choix_de_jouer == b'n'):
        jouer = False

    # Création d'un objet joueur nommé docteur
    docteur = Player(random.randint(1, 9), random.randint(1, 9), 0, 0)

    # création des daleks
    for i in range(MAX_DALEKS):
        # vérifie si la position est prise
        while True:
            posX = random.randint(1, 9)
            posY = random.randint(1, 9)
            position_prise = False
            # vérifie chaque element de la liste daleks, si la position est prise, recommence le procès
            for d in daleks:
                if (d.posX == posX and d.posY == posY):
                    position_prise = True
                    break
            # position n'est pas prise!
            if (position_prise == False):
                daleks.append(Dalek(posX, posY))
                break
            
    # Déroulement du jeu
    while not game_over:
        _ = os.system('cls')
        
        # Affichage position Joueur et Daleks
        Grille.grille[docteur.posY][docteur.posX] = Grille.JOUEUR

        for i in range(MAX_DALEKS):
            Grille.grille[daleks[i].posY][daleks[i].posX] = Grille.DALEK

        grilleAffichage()
        uiAffichage()

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
        
        for i in range(MAX_DALEKS):
            daleks[i].chasse(docteur)
            if (daleks[i].posX == docteur.posX and daleks[i].posY == docteur.posY) :
                _ = os.system('cls')
                print(f"{RED}GAME OVER !{WHITE}")
                sleep(2)
                _ = os.system('cls')
                game_over = True
