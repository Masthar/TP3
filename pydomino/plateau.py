import pydomino


class Plateau:
    """
        Documentation de la classe Plateau
        Attributs:
            plateau (list): Liste de dominos contenant les dominos qui ont été joués.
        """

    def __init__(self):
        self.plateau = []

    def cote_gauche(self):
        """
        Méthode qui retourne la valeur numérique à gauche du plateau
        :return: La valeur extérieure du domino de gauche.
        """

        return self.plateau[0][0]

    def cote_droit(self):
        """
        Méthode qui retourne la valeur numérique à droite du plateau
        :return: La valeur extérieure du domino de droite.
        """
        return self.plateau[-1][-1]

    def ajouter_a_gauche(self, domino):
        """
        Méthode qui ajoute le domino reçu en argument à gauche du plateau. Le domino devra peut-être être inversé pour
        que les chiffres qui se touchent soient identiques.
        :param domino: (Domino) Le domino à ajouter à gauche.
        """

        if self.cote_gauche() == domino[0]:
            self.plateau.insert(0, domino.inverser())
        else:
            self.plateau.insert(0, domino)

    def ajouter_a_droite(self, domino):
        """
        Méthode qui ajoute le domino reçu en argument à gauche du plateau. Le domino devra peut-être être inversé pour
        que les chiffres qui se touchent soient identiques.
        :param domino: (Domino) Le domino à ajouter à droite.
        """

        if self.cote_droit() == domino[0]:
            self.plateau.append(domino)
        else:
            self.plateau.append(domino.inverser())

    def ajouter(self, domino, gauche):
        """
        Méthode qui ajoute le domino reçu en argument à gauche ou à droite du plateau.
        :param domino: (Domino) Le domino à ajouter à droite.
        :param gauche: (bool) True si le domino doit être ajouté gauche, False autrement
        """

        if gauche:
            self.ajouter_a_gauche(domino)
        else:
            self.ajouter_a_droite(domino)

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

    def __len__(self):
        return len(self.plateau)

    def __str__(self):
        """
        Méthode qui retourne une chaîne de caractères qui représente la liste de dominos sur le plateau en une ligne.
        :return: str: liste des dominos du plateau
        """

        ligne_domino = ''
        for domino in self.plateau:
            ligne_domino += domino.__str__()

    def __repr__(self):
        return str(self)
