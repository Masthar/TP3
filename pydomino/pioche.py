import pydomino
from random import randint


class Pioche(pydomino.Donne):
    """
    Documentation de la classe Pioche. Cette classe hérite de la classe Donne
    Attributs:
        Aucun attribut spécifique autre que ceux de la classe Donne.
    """

    # def __init__(self, dominos):
    #     super().__init__(dominos)

    def prendre_dans_la_pioche(self):
        """
        Méthode pour prendre un domino dans la pioche.
        :return:
            (domino): le domino pris dans la pioche
        """
        return self.dominos.pop(randint(0, len(self.dominos) - 1))
