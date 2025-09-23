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

class Grille :
    # longueur et largeur MAX de la grille 
    TAS_X, TAS_Y = 10, 10

    VIDE = f"{WHITE}O"
    ZAP = f"{YELLOW}Z"
    FERRAILLE = f"{BROWN}X"
    TELEPORTEUR = f"{CYAN}T"
    DALEK = f"{RED}D"
    JOUEUR = f"{GREEN}J"
    
    grille = []

    def setGrilleEmpty():
        Grille.grille = [
        [Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE],
        [Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE],
        [Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE],
        [Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE],
        [Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE],
        [Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE],
        [Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE],
        [Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE],
        [Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE],
        [Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE, Grille.VIDE], 
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
        self.vivant = True

    # Chasse le joueur
    def chasse(self, docteur):
        if (self.vivant == False): 
            return

        docX = docteur.posX
        docY = docteur.posY

        # Y et X sont inversés, position précédente remise a vide.
        if (self.vivant):
            Grille.grille[self.posY][self.posX] = Grille.VIDE

        if (self.posY < docY):
            self.posY += 1
        elif (self.posY > docY):
            self.posY -= 1
        elif (self.posX < docX):
            self.posX += 1
        elif (self.posX > docX):
            self.posX -= 1

        if (self.vivant == False):
            Grille.grille[self.posY][self.posX] = Grille.FERRAILLE

# verify collision entre daleks ou avec tas ferraille -> destruction + tas ferraille
def verCollision(dalek, autreDalek):
    if (autreDalek.vivant):
        if (dalek.posX == autreDalek.posX and dalek.posY == autreDalek.posY):
            Grille.grille[dalek.posY][dalek.posX] = Grille.FERRAILLE
            Grille.grille[autreDalek.posY][autreDalek.posX] = Grille.FERRAILLE
            dalek.vivant = False
            autreDalek.vivant = False
            return True
         
# affichage de la grille (y = rangée, x = colonne)
def grilleAffichage(grilleDuJeu) :
      for y in range (0, Grille.TAS_Y) :
        for x in range (0, Grille.TAS_X):
            print(grilleDuJeu[y][x] + ' ', end = '')
        print('')

# affichage du UI
def uiAffichage():
    print(f"\n {WHITE}UTILISER W,A,S,D POUR SE DÉPLACER    |    Q = Zappeur    |    E = Téléportation    |    O = Arrêter de jouer")
    print("\n\n")
    print(f"{RED}Daleks restants : " + str(daleks.count))
    print(f"{CYAN}Téléporteurs utilisables : " + str(docteur.teleporteur))
    print(f"{YELLOW}Zappeurs utilisables : " + str(docteur.zappeur))
    print(f"{WHITE}Score : " + str(Score))

def findEmptyCase(grilleDuJeu):
    isEmpty = False
    while not isEmpty :
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        if (grilleDuJeu[x][y] == Grille.VIDE):
            isEmpty = True
    return x, y

# Variables 
MAX_DALEKS = 5
MAX_ZAPPERS = 3
MAX_TELEPORTERS = 2
zappeurs = random.randint(0, MAX_ZAPPERS)
teleporteurs = random.randint(0, MAX_TELEPORTERS)
Score = 0
daleks = []
game_over = True
jouer = True

# Menu principal
while jouer :
    print("Jeu du dalek! \n\n\n")
    print("Voulez vous Jouer ? (o/n)")
    choix_de_jouer = getch()

    if (choix_de_jouer == b'o'):
        game_over = False
        _ = os.system('cls')
    elif (choix_de_jouer == b'n'):
        jouer = False

    # Création d'une instance de Grille
    Grille.setGrilleEmpty()

    # Création d'un objet joueur nommé docteur
    docteur = Player(random.randint(1, 9), random.randint(1, 9), 1, 0)

    # création des daleks
    for d in range(MAX_DALEKS):
        x, y = findEmptyCase(Grille.grille)
        daleks.append(Dalek(x,y))

    # Spawn des objets
    for z in range(zappeurs):
        x, y = findEmptyCase(Grille.grille)
        Grille.grille[x][y] = Grille.ZAP

    for t in range(teleporteurs):
        x, y = findEmptyCase(Grille.grille)
        Grille.grille[x][y] = Grille.TELEPORTEUR

    # Déroulement du jeu
    while not game_over:
        _ = os.system('cls')
        
        # Affichage position Joueur et Daleks
        Grille.grille[docteur.posY][docteur.posX] = Grille.JOUEUR

        for i in range(MAX_DALEKS):
            if (daleks[i].vivant):
                Grille.grille[daleks[i].posY][daleks[i].posX] = Grille.DALEK
            elif (daleks[i].vivant == False):
                Grille.grille[daleks[i].posY][daleks[i].posX] = Grille.FERRAILLE

        grilleAffichage(Grille.grille)
        uiAffichage()

        playerInput = getch()    

        # Tour du Joueur
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

        # Ajout des objets dans l'inventaire du joueur
        if (Grille.grille[docteur.posY][docteur.posX] == Grille.ZAP):
            docteur.zappeur += 1
        if (Grille.grille[docteur.posY][docteur.posX] == Grille.TELEPORTEUR):
            docteur.teleporteur += 1

        # Tour des Daleks
        for i in range(MAX_DALEKS):
            daleks[i].chasse(docteur)
            if (daleks[i].posX == docteur.posX and daleks[i].posY == docteur.posY) :
                _ = os.system('cls')
                print(f"{RED}GAME OVER !{WHITE}")
                sleep(2)
                _ = os.system('cls')
                game_over = True
            for d in daleks:
                # pour éviter collision avec lui-même ou si le dalek dans la liste est mort, continue
                if (d == daleks[i] or not d.vivant):
                    continue
                if (verCollision(daleks[i], d)):
                    Score += 10
