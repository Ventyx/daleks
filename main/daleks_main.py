#### Fichier Main
from msvcrt import getch, kbhit
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
MAX_DALEKS = 5
MAX_ZAPPERS = 3
MAX_TELEPORTERS = 2

Score = 0
daleks = []
game_over = True
jouer = True
nbDaleksMorts = 0

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
        
        # si le dalek est mort, devient tas ferraille
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
    print(f"{RED}Daleks restants : " + str(MAX_DALEKS - nbDaleksMorts))
    print(f"{CYAN}Téléporteurs utilisables : " + str(docteur.teleporteur))
    print(f"{YELLOW}Zappeurs utilisables : " + str(docteur.zappeur))
    print(f"{WHITE}Score : " + str(Score))

# Efface la console, puis affiche le ui et la grille
def affichageComplet():
    _ = os.system('cls')
    grilleAffichage(Grille.grille)
    uiAffichage()

def findEmptyCase(grilleDuJeu):
    isEmpty = False
    while not isEmpty :
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        if (grilleDuJeu[x][y] == Grille.VIDE):
            isEmpty = True
    return x, y

def endTheGame(win):
    _ = os.system('cls')
    if (not win):
        print(f"{RED}GAME OVER !{WHITE}")
    if (win):
        print(f"{GREEN}YOU WON !{WHITE}")
    sleep(2)
    _ = os.system('cls')
    if (game_over):
        daleks.clear()

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

    # Vider la grille
    Grille.setGrilleEmpty()

    # Création d'un objet joueur nommé docteur
    docteur = Player(random.randint(1, 9), random.randint(1, 9), 1, 0)

    # Spawn des objets
    for z in range(random.randint(0, MAX_ZAPPERS)):
        x, y = findEmptyCase(Grille.grille)
        Grille.grille[x][y] = Grille.ZAP

    for t in range(random.randint(0, MAX_TELEPORTERS)):
        x, y = findEmptyCase(Grille.grille)
        Grille.grille[x][y] = Grille.TELEPORTEUR

    # création des daleks si la liste est vide
    if (len(daleks) == 0):
        for d in range(MAX_DALEKS):
            x, y = findEmptyCase(Grille.grille)
            daleks.append(Dalek(x,y))

    # Déroulement du jeu
    while not game_over:
        
        # Affichage position Joueur et Daleks
        Grille.grille[docteur.posY][docteur.posX] = Grille.JOUEUR

        for i in range(MAX_DALEKS):
            if (daleks[i].vivant):
                Grille.grille[daleks[i].posY][daleks[i].posX] = Grille.DALEK
            elif (daleks[i].vivant == False):
                Grille.grille[daleks[i].posY][daleks[i].posX] = Grille.FERRAILLE

        affichageComplet()

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
        elif (playerInput == b'o'): #Recommence le jeu
            game_over = True
        elif (playerInput == b'e'): #Téléportation
            if (docteur.teleporteur > 0):
                x, y = findEmptyCase(Grille.grille)
                docteur.move(x, y)
                docteur.teleporteur -= 1
        elif (playerInput == b'q'):
            if (docteur.zappeur > 0): #Zappeurs
                for i in range(daleks.__len__()):
                    if (docteur.posX + 1 == daleks[i].posX or 
                        (docteur.posX - 1 == daleks[i].posX) or 
                        (docteur.posY + 1 == daleks[i].posY) or 
                        (docteur.posY - 1 == daleks[i].posY)):

                        daleks[i].vivant = False
                        nbDaleksMorts += 1
                docteur.zappeur -= 1
        elif (playerInput == b'o'):
            game_over = True

        # Ajout des objets dans l'inventaire du joueur
        if (Grille.grille[docteur.posY][docteur.posX] == Grille.ZAP):
            docteur.zappeur += 1
        if (Grille.grille[docteur.posY][docteur.posX] == Grille.TELEPORTEUR):
            docteur.teleporteur += 1
        nbDaleksMorts = 0
        
        affichageComplet()

        # Tour des Daleks
        for i in range(MAX_DALEKS):
            daleks[i].chasse(docteur)
            if (daleks[i].posX == docteur.posX and daleks[i].posY == docteur.posY) :
                game_over = True
                endTheGame(False)
                break
            # verifie si le dalek[i] fait une collision avec un dalek vivant
            for d in daleks:
                # pour éviter collision avec lui-même ou si le dalek dans la liste est mort, continue
                if (d == daleks[i] or not d.vivant):
                    continue
                if (verCollision(daleks[i], d)):
                    Score += 10
            if (not daleks[i].vivant):
                nbDaleksMorts += 1

        if (MAX_DALEKS - nbDaleksMorts == 0):
            game_over = True
            endTheGame(True)
        while (kbhit()):
            getch()