#### Fichier Main
from msvcrt import getch
import os

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


