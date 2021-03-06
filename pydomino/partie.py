"""
Module contenant la description de la classe Partie. Cette classe contient toutes les méthodes pour jouer une partie de
domino sans pioche.
"""

import pydomino
import random


def distribuer_dominos(nombre_joueurs):
    """
    Méthode pour créer les donnes des joueurs. Pour une partie à 2 joueurs, 7 dominos sont distribués aux joueurs. Pour
    une partie à 3 ou 4 joueurs, 6 dominos sont distribués aux joueurs. Pour cette fonction, nous vous suggérons de
    générer tous les dominos de l'ensemble 'double-six', ensuite de les brasser aléatoirement (voir la fonction shuffle
    du module random), et de retourner le nombre de donnes demandé.
    :param nombre_joueurs: (int) Nombre de joueurs de la partie.
    :return: (list) La liste des donnes de dominos des joueurs.
    """

    ensemble_dominos = []
    ensemble_donnes = []
    for i in range(6, -1, -1):
        for j in range(i, -1, -1):
            ensemble_dominos.append(pydomino.Domino(i, j))
    random.shuffle(ensemble_dominos)
    if nombre_joueurs == 2:
        nombre_distribue = 7
    else:
        nombre_distribue = 6
    for i in range(nombre_joueurs):
        ensemble_donnes.append(pydomino.Donne(ensemble_dominos[i * nombre_distribue:(i + 1) * nombre_distribue]))
    return ensemble_donnes


class Partie:
    """
    Documentation de la classe Partie
    Attributs:
        plateau (Plateau): Objet qui contiendra les dominos qui seront joués par les joueurs
        donnes (list): Liste des donnes des joueurs. Les donnes sont des objets de la classe Donne
        tour (int): Nombre qui représente le joueur dont c'est le tour de jouer
        passe (int): Nombre de joueurs consécutifs qui passent leur tour.
        gagnant (int): Nombre qui représente le joueur gagnant lorsqu'on joueur gagne la partie
    """

    def __init__(self, plateau, donnes):
        self.plateau = plateau
        self.donnes = donnes
        self.tour = None
        self.passe = 0
        self.gagnant = None

    @classmethod
    def nouvelle_partie(cls, nombre_joueurs):
        """
        Méthode de classe pour créer une nouvelle partie. Cette méthode instancie le plateau de jeu, crée les donnes
        des joueurs (selon le nombre de joueurs reçu en argument) et instancie l'objet partie.
        :param nombre_joueurs: (int) nombre de joueurs de la partie
        :return: (Partie) objet de la classe Partie
        """

        plateau = pydomino.Plateau()
        donnes = distribuer_dominos(nombre_joueurs)
        partie = cls(plateau, donnes)
        return partie

    @staticmethod
    def afficher_instructions():
        """
        Méthode statique qui affiche les instructions du jeu
        """

        print("\nPartie sans pioche:\n\n\
        Le jeu peut être joué par 2, 3 ou 4 joueurs. À partir d’un ensemble de 28 dominos ”doublesix”,\n\
        chaque joueur a une donne de dominos constituée au hasard (son jeu). Pour une\n\
        partie à 2 joueurs, chaque joueur reçoit 7 dominos. Pour une partie à 3 ou 4 joueurs, chaque\n\
        joueur reçoit 6 dominos.\n\n\
        Le premier joueur à déposer un domino est celui qui a le domino le plus élevé (les trois\n\
        dominos les plus élevés sont [6,6], [5,6] et [5,5]). Il doit nécessairement déposer ce domino en premier.\n\
        Ensuite, chaque joueur joue à tour de rôle. Pour déposer un domino, un joueur doit choisir un domino de\n\
        sa donne qui a un numéro identique à une des extrémités de la suite de dominos qui s’assemble sur la table.\n\
        Par exemple, si la suite sur la table est la suivante : [3,6][6,6][6,5], le joueur dont c’est le tour peut\n\
        jouer un domino contenant soit le numéro 3 (par exemple, [2,3]), soit le numéro 5 (par exemple [5,5]). \n\
        Si un joueur ne peut jouer aucun domino, il doit passer son tour.\n\n\
        La partie se termine dans deux conditions :\n\
        \t1. Si un joueur a déposé tous ses dominos et a vidé sa donne. Ce joueur est déclaré gagnant.\n\
        \t2. Si aucun joueur ne peut déposer un domino (ils auront donc tous passé leur tour), la partie\n\
        \t   est arrêtée. Le joueur à qui il reste le moins de dominos dans sa donne est déclaré gagnant.\n\
        \t   En comptant le nombre de dominos restants, il se peut qu’il y ait égalité entre 2 joueurs ou plus.")

    def afficher_etat_donnes(self):
        """
        Méthode qui affiche l'état des donnes des joueurs de la partie.
        L'information affichée doit contenir le numéro du joueur et le nombre de dominos de sa donne.
        """
        print("\nListe des joueurs:")
        for i in range(len(self.donnes)):
            print("\n\tJoueur " + str(i + 1))
            print('\tNombre de dominos: ' + str(len(self.donnes[i])))

    def trouver_premier_joueur(self):
        """
        Méthode qui détermine le premier joueur à déposer un domino sur le plateau. Ce joueur est celui qui a le domino
        le plus élevé ([6,6], [5,6], [5,5], ou moins).
        :return:
            int: le numéro du joueur ayant le domino le plus élevé
            domino: le domino le plus élevé de ce joueur
        """
        num_joueur = 0
        domino_max = pydomino.Domino(0, 0)
        for i in range(len(self.donnes)):
            if max(self.donnes[i]) > domino_max:
                num_joueur = i
                domino_max = max(self.donnes[i])
        return num_joueur, domino_max

    def passer_au_prochain_joueur(self):
        """
        Méthode qui modifie l'attribut self.tour pour passer au joueur suivant.
        """
        if self.tour == len(self.donnes) - 1:
            self.tour = 0
        else:
            self.tour += 1

    def tour_du_premier_joueur(self):
        """
        Méthode qui complète les étapes du tour du premier joueur. Trouve le joueur ayant le domino le plus élevé,
        joue ce domino sur le plateau et annonce ce mouvement.
        """
        joueur, domino = self.trouver_premier_joueur()
        self.tour = joueur
        print("\nLe joueur {} commence avec le domino {}.".format(joueur + 1, domino))
        self.plateau.ajouter(domino, False)
        self.donnes[joueur].jouer(domino)
        self.passer_au_prochain_joueur()

    def determiner_si_domino_peut_etre_joue(self, domino):
        """
        Méthode qui détermine si un domino peut être joué sur le plateau de jeu.
        :param domino: (Domino) Domino dont on veut savoir s'il peut être posé à une des deux extrémités du plateau
        :return: (bool) True, si le domino peut être joué, False autrement.
        """
        return self.plateau.cote_droit() in domino.lister_valeurs() or\
            self.plateau.cote_gauche() in domino.lister_valeurs()

    def determiner_si_joueur_joue_ou_passe(self):
        """
        Méthode qui détermine si le joueur courant peut jouer un domino ou s'il doit passer son tour.
        :return: (bool) True, si au moins un domino de la donne du joueur courant peut être joué sur le plateau. False,
        autrement.
        """

        for domino in self.donnes[self.tour]:
            if self.determiner_si_domino_peut_etre_joue(domino):
                return True
        return False

    def afficher_informations_debut_tour(self):
        """
        Méthode qui affiche les informations données à chaque début de tour: le numéro du joueur qui doit jouer, l'état
        du plateau de jeu, l'état des donnes de tous les joueurs (nombre de dominos en main) et la donne du joueur qui
        doit jouer.
        """

        print("\nTour du joueur {}".format(self.tour + 1))
        self.afficher_etat_donnes()
        print("\nPlateau: {}".format(self.plateau))

    def demander_numero_domino_a_jouer(self):
        """
        Méthode qui demande le numéro du domino que le joueur veut jouer. En posant la question, le programme affiche la
        liste des dominos dans la donne du joueur. Le numéro est validé et le programme redemande un numéro de domino
        tant que le numéro fourni n'est pas valide.
        :return: (Domino) L'objet domino associé au numéro de domino choisi.
        """
        print("\nDonne du joueur {}:".format(self.tour + 1))
        print(self.donnes[self.tour])
        choix_domino = input("\nQuel domino shouaitez-vous jouer?")
        while not (choix_domino.isnumeric() and int(choix_domino) in range(1, len(self.donnes[self.tour]) + 1)):
            print("\nChoix non valide. Veuillez entrer un des indexes fournis.")
            choix_domino = input("Quel domino shouaitez-vous jouer?")
        choix_domino = int(choix_domino) - 1
        return self.donnes[self.tour][choix_domino]

    def jouer_a_gauche_ou_a_droite(self, domino_joue):
        """
        Méthode qui est invoquée lorsque le domino choisi par le joueur peut être joué à gauche ou à droite. On demande
        ce que veut le joueur et le domino est joué selon son choix. Ce choix doit être validé par le programme.
        :param domino_joue: (Domino) Le domino à jouer
        :return:
        """
        choix_cote = input("\nDe quel côté souhaitez-vous placer ce domino?\n1. Gauche\n2. Droite\nRéponse : ")
        while choix_cote not in ['1', '2']:
            print("\nChoix non valide. Veuillez entrer un des indexes fournis.")
            choix_cote = input('1. Gauche\n2. Droite\n Réponse : ')
        if choix_cote == '1':
            self.jouer_a_gauche(domino_joue)
        else:
            self.jouer_a_droite(domino_joue)

    def jouer_a_gauche(self, domino_joue):
        """
        Méthode invoquée pour joueur un domino à gauche du plateau.
        :param domino_joue: (Domino) Le domino à jouer à gauche du plateau.
        """
        print("\nLe joueur {} joue le domino {} à gauche du plateau.".format(self.tour + 1, domino_joue))
        self.plateau.ajouter(domino_joue, True)
        self.donnes[self.tour].jouer(domino_joue)

    def jouer_a_droite(self, domino_joue):
        """
        Méthode invoquée pour joueur un domino à droite du plateau.
        :param domino_joue: (Domino) Le domino à jouer à droite du plateau.
        """
        print("\nLe joueur {} joue le domino {} à droite du plateau.".format(self.tour + 1, domino_joue))
        self.plateau.ajouter(domino_joue, False)
        self.donnes[self.tour].jouer(domino_joue)

    def jouer_un_domino(self):
        """
        Méthode pour jouer un domino. Cette méthode demande au joueur le numéro du domino qu'il souhaite jouer. Elle
        vérifie ensuite si le domino peut être joué à gauche ou à droite du plateau. Si le domino peut être joué d'un
        seul côté, alors le domino est joué de ce côté-là. Si le domino peut être joué des deux côtés, alors on
        demande à l'utilateur le côté où il souhaite jouer le domino (en utilisant les méthodes appropriées).
        """
        domino_joue = self.demander_numero_domino_a_jouer()
        while self.plateau.cote_gauche() not in domino_joue.lister_valeurs() and\
                self.plateau.cote_droit() not in domino_joue.lister_valeurs():
            print("\nCe domino ne peut pas être joué pour l'instant.")
            print("\nPlateau: {}".format(self.plateau))
            domino_joue = self.demander_numero_domino_a_jouer()

        # Deux côtés possibles
        if self.plateau.cote_gauche() in domino_joue.lister_valeurs() and\
                self.plateau.cote_droit() in domino_joue.lister_valeurs():
            self.jouer_a_gauche_ou_a_droite(domino_joue)

        # Possible à gauche
        elif self.plateau.cote_gauche() in domino_joue.lister_valeurs():
            self.jouer_a_gauche(domino_joue)

        # Possible à droite
        else:
            self.jouer_a_droite(domino_joue)

    def tour_du_prochain_joueur(self):
        """
        Méthode qui exécute les étapes de jeu pour le tour d'un joueur (à l'exception du premier tour qui a une
        méthode dédiée). Dans cette méthode: 1) on affiche les informations de début de tour, ensuite 2) on teste si
        le joueur courant peut jouer ou s'il doit passer son tour, 3) s'il peut jouer, on réinitialise l'attribut passe,
        le joueur joue un domino, et on vérifie s'il y a un gagnant, 4) s'il ne peut pas jouer, on fait passer son tour
        au joueur, finalement 4) on passe au prochain joueur (en utilisant la méthode appropriée).
        """
        self.afficher_informations_debut_tour()
        peut_jouer = False
        for domino in self.donnes[self.tour]:
            if self.plateau.cote_gauche() in domino.lister_valeurs() or\
                    self.plateau.cote_droit() in domino.lister_valeurs():
                peut_jouer = True
                break
        if peut_jouer:
            self.passe = 0
            self.jouer_un_domino()
            self.verifier_gagnant()
        else:
            self.faire_passer_joueur()
        self.passer_au_prochain_joueur()

    def faire_passer_joueur(self):
        """
        Méthode qui contient les instructions à exécuter lorsqu'un joueur doit passer son tour. Cette méthode devrait
        afficher des informations et modifier l'attribut passe.
        """
        print("\nLe joueur {} ne peut pas jouer et doit passer son tour.".format(self.tour + 1))
        self.passe += 1

    def verifier_gagnant(self):
        """
        Méthode qui vérifie si le joueur courant est le gagnant (condition: il doit avoir vidé sa donne). Cette méthode
        modifie l'attribut gagnant si le joueur courant gagne la partie.
        """
        if not len(self.donnes[self.tour]):
            self.gagnant = self.tour + 1

    def trouver_joueurs_avec_moins_de_dominos(self):
        """
        Méthode qui détermine le ou les joueurs qui ont la plus petite donne.
        :return: (list) Liste contenant les numéros des joueurs ayant le moins de dominos dans leur donne. Ce nombre
        peut varier entre 1 et len(self.donnes)
        """
        longueur_minimum = 10
        liste_gagnants = []
        for i in range(len(self.donnes)):
            if len(self.donnes[i]) < longueur_minimum:
                longueur_minimum = len(self.donnes[i])
                liste_gagnants = [i + 1]
            elif len(self.donnes[i]) == longueur_minimum:
                liste_gagnants.append(i + 1)
        return liste_gagnants

    def afficher_message_egalite(self, indices):
        """
        Méthode qui affiche un message en cas d'égalité en fin de partie. Ce message doit indiquer quels sont les
        joueurs qui ont le moins de dominos dans leur donne.
        :param indices: (list) Liste qui contient les numéros des joueurs ayant le moins de dominos dans leur donne.
        """
        print('\nNous avons une égalité. Les gagnants sont les joueurs', end=' ')
        for i in range(len(indices)):
            if i == len(indices) - 1:
                print('et {}!'.format(indices[i]))
            else:
                print('{},'.format(indices[i]), end=' ')

    def afficher_message_victoire(self):
        """
        Méthode qui affiche le message de victoire. Il informe l'usager de l'identité du joueur gagnant.
        """
        print("\nLe joueur {} n'a plus de domino. Il gagne donc la partie!".format(self.gagnant))

    def jouer(self):
        """
        Méthode principale de la classe qui spécifie le déroulement d'une partie. Les étapes sont: 1) affichage des
        instructions, 2) premier tour de jeu, 3) boucle pour les tours suivants, cette boucle vérifie les conditions de
        fin de partie, 4) affichages de fin de partie (état des donnes, message en cas de victoire ou d'égalité)
        """

        self.afficher_instructions()
        self.tour_du_premier_joueur()
        while self.gagnant is None:
            self.tour_du_prochain_joueur()
            if self.passe == len(self.donnes):
                self.gagnant = self.trouver_joueurs_avec_moins_de_dominos()
        if isinstance(self.gagnant, int) or len(self.gagnant) == 1:
            if not isinstance(self.gagnant, int):
                self.gagnant = self.gagnant[0]
            self.afficher_message_victoire()
        else:
            self.afficher_message_egalite(self.gagnant)
