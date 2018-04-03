"""
Module contenant la description de la classe Domino. Un domino contient deux chiffres.
"""


class Domino:
    """
    Dominos qui seront joués. Chaque domino a deux chiffres, et chaque assortiment de chiffres est unique.
    Par exemple, on ne peut pas avoir le domino [6|6] dans deux donnes.
    Attributs:
        premier_chiffre (int): Premier chiffre du domino (entier entre 0 et 6)
        deuxiement_chiffre (int): Deuxieme chiffre du domino (entier entre 0 et 6)
    """

    def __init__(self, premier_chiffre, deuxieme_chiffre):
        self.premier_chiffre = premier_chiffre
        self.deuxieme_chiffre = deuxieme_chiffre

    def inverser(self):
        """
        Cette méthode renvoie un domino où les chiffres ont été inversés.
        :return (domino): domino inversé
        """
        return Domino(self.deuxieme_chiffre, self.premier_chiffre)

    def __str__(self):
        """
        Cette méthode retourne une chaîne de caractère qui représente l'objet domino.
        :return: (str): le string formatté représentant le domino.
        """
        return "[{}|{}]".format(self.premier_chiffre, self.deuxieme_chiffre)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        """
        Cette méthode spécifie le test d'équivalence entre deux objets de la classe domino.
        :param other: Autre objet à comparer avec celui-ci
        """
        if not isinstance(other, type(self)):
            return False
        else:
            return sorted((self.premier_chiffre, self.deuxieme_chiffre)) == \
                   sorted((other.premier_chiffre, other.deuxieme_chiffre))

    def __gt__(self, other):
        """
        Cette méthode spécifie le test de comparaison '>' pour des dominos en se basant sur la somme de leurs chiffre.
        Si la somme est égale, on prend le premier chiffre comme point de comparaison.
        :param other (domino): domino à comparer
        :return (bool): True si le domino est considéré plus grand que 'other'
        """
        if not isinstance(other, type(self)):
            return False
        if self.somme_chiffres() == other.somme_chiffres():
            return self.premier_chiffre > other.premier_chiffre
        else:
            return self.somme_chiffres() > other.somme_chiffres()

    def __hash__(self):
        """
        Cette méthode spécifie la fonction de hachage pour les objets de la classe domino. Ceci permet de créer des
        ensembles d'objets de cette classe
        """
        return hash(tuple(sorted((self.premier_chiffre, self.deuxieme_chiffre))))

    def __contains__(self, key):
        """
        Cette méthode spécifie le test d'appartenance pour un entier dans un objet de la classe domino
        :param key (int): Chiffre dont on vérifier l'appartenance dans l'objet domino
        :return (bool): True si le chiffre key est présent dans les attributs du domino, False autrement
        """
        return key == self.premier_chiffre or key == self.deuxieme_chiffre

    def somme_chiffres(self):
        """
        Cette méthode fait la somme des deux valeurs d'un domino
        :return (int): Somme des deux chiffre du domino
        """
        return self.premier_chiffre + self.deuxieme_chiffre

    def lister_valeurs(self):
        """
        Cette méthode met les deux chiffres du domino dans une liste.
        :return (list): Lliste contenant les deux chiffres du domino
        """
        return [self.premier_chiffre, self.deuxieme_chiffre]
