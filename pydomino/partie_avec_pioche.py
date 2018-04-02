import pydomino
import random


def distribuer_dominos_avec_pioche(nombre_joueurs):
    """
        Méthode pour créer les donnes des joueurs et la pioche. Pour une partie à 2 joueurs, 7 dominos sont distribués
        aux joueurs. Pour une partie à 3 ou 4 joueurs, 6 dominos sont distribués aux joueurs. Pour cette fonction, nous
        vous suggérons de générer tous les dominos de l'ensemble 'double-six', ensuite de les brasser aléatoirement
        (voir la fonction shuffle du module random), et de retourner le nombre de donnes demandé. Dans tous les cas,
        les jetons restants forment la pioche.
        :param nombre_joueurs: (int) Nombre de joueurs de la partie.
        :returns: (list) La liste des donnes de dominos des joueurs.
                (Pioche) L'objet pioche.
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

    pioche = pydomino.Pioche(ensemble_dominos[nombre_distribue * nombre_joueurs:])

    return ensemble_donnes, pioche


class PartieAvecPioche(pydomino.Partie):
    """
        Documentation de la classe PartieAvecPioche. Cette classe hérite de la classe Partie.
        Attributs:
            pioche (Pioche): Pioche contenant une liste de dominos.
        """

    def __init__(self, plateau, donnes, pioche):

        self.pioche = pioche
        super().__init__(plateau, donnes)

    @classmethod
    def nouvelle_partie(cls, nombre_joueurs):
        """
        Méthode de classe pour créer une nouvelle partie avec pioche. Cette méthode instancie le plateau de jeu, crée
        les donnes des joueurs (selon le nombre de joueurs reçu en argument), la pioche et instancie l'objet partie.
        :param nombre_joueurs: (int) nombre de joueurs de la partie
        :return: (Partie) objet de la classe Partie
        """
        plateau = pydomino.Plateau()

        donnes, pioche = distribuer_dominos_avec_pioche(nombre_joueurs)

        partie = cls(plateau, donnes, pioche)

        return partie

    @staticmethod
    def afficher_instructions():
        """
        Méthode statique qui affiche les instructions du jeu

        """
        print("\nPartie avec pioche:\n\n\
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
        Si un joueur ne peut pas jouer de domino, il doit piger un domino dans la pioche jusqu'à ce qu'il puisse jouer.\
        \n\
        Si la pioche est vide, il doit passer son tour.\n\n\
        La partie se termine dans deux conditions :\n\
        \t1. Si un joueur a déposé tous ses dominos et a vidé sa donne. Ce joueur est déclaré gagnant.\n\
        \t2. Si aucun joueur ne peut déposer un domino (ils auront donc tous passé leur tour), la partie\n\
        \t   est arrêtée. Le joueur à qui il reste le moins de dominos dans sa donne est déclaré gagnant.\n\
        \t   En comptant le nombre de dominos restants, il se peut qu’il y ait égalité entre 2 joueurs ou plus.")

    def afficher_etat_donnes(self):
        """
        Méthode qui affiche l'état des donnes des joueurs de la partie avec pioche.
        L'information affichée doit contenir le numéro du joueur et le nombre de dominos de sa donne, ainsi que le
        nombre de dominos dans la pioche.
        """
        for i in range(len(self.donnes)):
            print("\nJoueur " + str(i + 1))
            print('Nombre de dominos: ' + str(len(self.donnes[i])))
            print("Nombre de dominos dans la pioche: {}".format(len(self.pioche)))

    def faire_passer_joueur(self):
        """
        Méthode qui contient les instructions à exécuter lorsqu'un joueur doit passer son tour. Cette méthode devrait
        d'abord afficher des informations. Ensuite le joueur courant pige un domino dans la pioche. S'il peut jouer le
         domino, il le joue et son tour ce termine. S'il ne peut pas jouer, il pige un autre domino. Le joueur pigera
         des dominos tant qu'il ne pourra pas jouer le domino. Si jamais la pioche est vide, le programme affiche un
         message d'information et le joueur passe son tour.
        """
        while not self.determiner_si_joueur_joue_ou_passe():
            if len(self.pioche):
                print("\nLe joueur {} ne peut pas jouer. Il doit piger un domino dans la pioche.".format(self.tour + 1))
                domino = self.pioche.prendre_dans_la_pioche()
                print("\nLe joueur {} prend le domino {} dans la pioche et l'ajoute à sa donne.".format(self.tour + 1,
                                                                                                        domino))
                self.donnes[self.tour].piger(domino)
            else:
                print("\nLa pioche est vide, et le joueur {} ne peut pas jouer. Il doit donc passer son tour."
                      .format(self.tour + 1))
                self.passe += 1
                break
        if self.determiner_si_joueur_joue_ou_passe():
            print("\nLe joueur {} peut maintenant jouer.".format(self.tour + 1))
            self.jouer_un_domino()
