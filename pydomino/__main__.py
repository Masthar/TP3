"""
Module principal du package pydomino. C'est ce module que nous allons exécuter pour démarrer votre jeu.
"""

from pydomino.partie import Partie
from pydomino.partie_avec_pioche import PartieAvecPioche


if __name__ == '__main__':
    """
    Point d'entrée de votre programme pydomino. Dans cette fonction, il faut d'abord demander quel type de partie de
    dominos l'utilisateur veut jouer. L'entrée de l'utilisateur doit être validée. Ensuite, le programme demande à
    l'utilisateur à combien de joueur il veut jouer une partie. Un objet de la classe Partie ou de la classe 
    PartieAvecPioche est ensuite instancié. Finalement, la partie est démarrée en appelant la méthode jouer().
    """
    print("Jouons une partie de pydomino!\n")
    choix_partie = input("À quel type de partie souhaitez vous jouer?\n1. Sans pioche\n2. Avec pioche\n")
    while choix_partie not in ['1', '2']:
        choix_partie = input("\nChoix non valide. Veuillez choisir dans les indexes fournis.\n")
    nombre_joueurs = input('\nShouaitez-vous jouer à 2, 3 ou 4 joueurs?\n')
    while nombre_joueurs not in ['2', '3', '4']:
        nombre_joueurs = input("Choix non valide. Veuillez-entrer le nombre de joueurs avec lequel vous voulez jouer."
                               "\n")
    nombre_joueurs = int(nombre_joueurs)
    if choix_partie == '1':
        partie = Partie.nouvelle_partie(nombre_joueurs)
    else:
        partie = PartieAvecPioche.nouvelle_partie(nombre_joueurs)
    partie.jouer()
    input('Appuyer sur ENTER pour quitter.')
