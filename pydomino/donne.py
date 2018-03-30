"""
Module contenant la description de la classe Donne. Une donne contient une liste de dominos.
"""

import pydomino


class Donne:
    """
    Documentation de la classe Donne
    Attributs:
        dominos (list): Liste de dominos contenant la donne d'un joueur
    """

    def __init__(self, des_dominos):
        self.dominos = list(des_dominos)

    def jouer(self, domino):
        """
        En jouant un domino, on le retire de la donne
        :param Domino domino: domino à retirer de la donne
        :return: l'index du domino dans la donne
        """
        index_domino = self.dominos.index(domino)
        self.dominos.remove(domino)
        return index_domino

    def piger(self, domino, i=None):
        """
        Ajouter un domino dans la donne.
        :param Domino domino: domino à ajouter à la donne
        :param int i: index où le domino doit être ajouter;
                      par défaut, on ajoute le domino à la fin
        """
        if i is None:
            i = len(self.dominos)

        self.dominos.insert(i, domino)

    def __getitem__(self, i):
        return self.dominos[i]

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

    def __len__(self):
        return len(self.dominos)

    def __str__(self):
        """
        Méthode qui retourne une chaîne de caractères qui représente la liste de dominos de la donne en une ligne.
        :return: str: liste des dominos de la donne
        """

        ligne_domino = ""
        for domino in self.dominos:
            ligne_domino += (' ' + domino.__str__())
        return ligne_domino

    def __repr__(self):
        return str(self)


if __name__ == '__main__':
    print(sorted(Donne([pydomino.Domino(6, 6), pydomino.Domino(6, 4), pydomino.Domino(4, 6), pydomino.Domino(5, 5)])))
