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
PINK = "\033[0;35m"
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
nbDaleksMortsAvant = 0

class Grille :
    # longueur et largeur MAX de la grille 
    TAS_X, TAS_Y = 10, 10

    VIDE = f"{WHITE}O"
    ZAP = f"{YELLOW}Z"
    FERRAILLE = f"{PINK}X"
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
         
# affichage de la grille (y = rangée, x = colonne)
def grilleAffichage(grilleDuJeu) :
      for y in range (0, Grille.TAS_Y) :
        for x in range (0, Grille.TAS_X):
            print(grilleDuJeu[y][x] + ' ', end = '')
        print('')

# affichage du UI
def uiAffichage():
    print(f"\n {WHITE}Controles : UTILISER W,A,S,D POUR SE DÉPLACER    |    Q = Utiliser Zappeur    |    E = Téléportation    |    O = Arrêter de jouer")
    print(f"{WHITE}--------------------------------------------------------------------------------------------------------------------------------------")
    print(f"{WHITE}Légende   : {RED}D{WHITE} -> Dalek    |    {YELLOW}Z{WHITE} -> Zappeur    |    {CYAN}T{WHITE} -> Téléporteur    |    {GREEN}J{WHITE} -> Joueur    |    O -> Case vide    |    {PINK}X{WHITE} -> Ferraille")
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

# Trouve une case vide dans la grille
def findEmptyCase(grilleDuJeu):
    isEmpty = False
    while not isEmpty :
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        if (grilleDuJeu[y][x] == Grille.VIDE):
            isEmpty = True
    return x, y

# Appelée lors de la fin de la partie, argument win en true si la partie est  gagnée.
def endTheGame(win):
    _ = os.system('cls')
    if (not win):
        print(f"{RED}VOUS AVEZ PERDU !{WHITE}")
    else:
        print(f"{GREEN}VOUS AVEZ GAGNÉ !{WHITE}")
    sleep(2)
    _ = os.system('cls')
    if (game_over):
        daleks.clear()

# Retourne le score total si un ou plusieurs nouveaux daleks sont tués, sinon retourne le vieux score.
def scoreTotal(daleksMortsAvant, daleksMorts, score):
        if (daleksMortsAvant < daleksMorts):
            nbMortsDepuis = daleksMorts - daleksMortsAvant
            score += nbMortsDepuis * 10
            nbDaleksMortsAvant = nbDaleksMorts
        return score

# Menu principal
while jouer :
    print("Jeu du dalek! \n\n\n")
    print("Voulez vous Jouer ? (o/n)")
    choix_de_jouer = getch().lower()
    if (choix_de_jouer == b'o'):
        game_over = False
    elif (choix_de_jouer == b'n'):
        jouer = False
    _ = os.system('cls')

    # Vider la grille
    Grille.setGrilleEmpty()

    # Création d'un objet joueur nommé docteur
    docteur = Player(random.randint(0, 9), random.randint(0, 9), 1, 0)
    Grille.grille[docteur.posY][docteur.posX] = Grille.JOUEUR

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

        affichageComplet()

        playerInput = getch().lower()
        
        # Tour du Joueur
        if (playerInput == b'w'):
            docteur.move(0,1)
        elif (playerInput == b's'):
            docteur.move(0,-1)
        elif (playerInput == b'a'):
            docteur.move(-1,0)
        elif (playerInput == b'd'):
            docteur.move(1,0)
        elif (playerInput == b'o'): # Recommence le jeu
            game_over = True
        elif (playerInput == b'e'): # Téléportation
            if (docteur.teleporteur > 0):
                x, y = findEmptyCase(Grille.grille)
                docteur.move(x, y)
                docteur.teleporteur -= 1
            continue
        elif (playerInput == b'q'):
            if (docteur.zappeur > 0): #Zappeurs
                for i in range(daleks.__len__()):
                    if (((docteur.posX + 1 == daleks[i].posX) and (docteur.posY == daleks[i].posY)) or 
                        ((docteur.posX - 1 == daleks[i].posX) and (docteur.posY == daleks[i].posY)) or 
                        ((docteur.posX == daleks[i].posX) and (docteur.posY + 1 == daleks[i].posY)) or 
                        ((docteur.posX == daleks[i].posX) and (docteur.posY - 1 == daleks[i].posY))):

                        daleks[i].vivant = False
                        nbDaleksMorts += 1
                docteur.zappeur -= 1
                Score = scoreTotal(nbDaleksMortsAvant, nbDaleksMorts, Score)
        elif (playerInput == b'o'):
            game_over = True

        # Ajout des objets dans l'inventaire du joueur
        if (Grille.grille[docteur.posY][docteur.posX] == Grille.ZAP):
            docteur.zappeur += 1
        if (Grille.grille[docteur.posY][docteur.posX] == Grille.TELEPORTEUR):
            docteur.teleporteur += 1
        nbDaleksMortsAvant = nbDaleksMorts
        nbDaleksMorts = 0

        # Tour des Daleks
        for i in range(MAX_DALEKS):
            daleks[i].chasse(docteur)
            # Quand un dalek entre en collision avec le joueur, Fin de la partie
            if (daleks[i].posX == docteur.posX and daleks[i].posY == docteur.posY) :
                game_over = True
                endTheGame(False)
                break
            # Verifie si le dalek[i] entre en collision avec un dalek vivant
            for d in daleks:
                # pour éviter collision avec lui-même ou si le dalek dans la liste est mort, continue
                if (d == daleks[i]):
                    continue
                if (daleks[i].posX == d.posX and daleks[i].posY == d.posY):
                    daleks[i].vivant = False
                    d.vivant = False
            if (not daleks[i].vivant):
                Grille.grille[daleks[i].posY][daleks[i].posX] = Grille.FERRAILLE
                nbDaleksMorts += 1
        
        if (MAX_DALEKS - nbDaleksMorts == 0):
            game_over = True
            endTheGame(True)
        while (kbhit()):
            getch()
            
        Score = scoreTotal(nbDaleksMortsAvant, nbDaleksMorts, Score)
