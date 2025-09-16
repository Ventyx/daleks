#Daleks_player

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

docteur = Player(0, 0, 4, 0, 0)

while True:
    

    print(docteur.getPos())