import pydomino
from random import randint


class Pioche(pydomino.Donne):
    """
    Type de donne.
    Il s'agiera du reste des dominos qui n'auront pas été distribués aux joueurs. Si un joueur ne peut
    pas jouer, il devra piocher dans la pioche jusqu'à ce qu'il puisse.
    Attributs:
        Aucun attribut spécifique autre que ceux de la classe Donne.
    """

    def prendre_dans_la_pioche(self):
        """
        Méthode pour prendre un domino dans la pioche.
        :return:
            (domino): le domino pris dans la pioche
        """
        return self.dominos.pop(randint(0, len(self.dominos) - 1))
