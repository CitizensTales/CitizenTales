__author__ = 'Argann'

"""
Classe Equipement

@author  : Argann Bonneau
@version : 0.1
@date    : 18-11-14
"""


class Equipement():

    """
    Classe définissant un équipement
    """

    def __init__(self):
        self.__contenu = dict()

    def changerArmePrincipale(self, newArme):
        """
        Permet de changer l'arme principale par l'arme donnée en paramètre

        :param newArme: Objet nouvelle arme principale

        :return: Null
        """
        self.__contenu["ArmePrincipale"] = newArme

    def changerArmeSecondaire(self, newArme):
        """
        Permet de changer l'arme secondaire par l'arme donnée en paramètre

        :param newArme: Objet nouvelle arme secondaire

        :return: Null
        """
        self.__contenu["ArmeSecondaire"] = newArme

    def changerPlastron(self, newPlastron):
        """
        Permet de changer le plastron par l'objet donné en paramètre

        :param newArme: Objet nouveau plastron

        :return: Null
        """
        self.__contenu["Plastron"] = newPlastron

    def changerCasque(self, newCasque):
        """
        Permet de changer le casque par l'objet donné en paramètre

        :param newArme: Objet nouveau casque

        :return: Null
        """
        self.__contenu["Casque"] = newCasque

    def changerJambes(self, newJambes):
        """
        Permet de changer l'équipement de jambes par l'objet donné en paramètre

        :param newArme: Objet nouvel équipement de jambes

        :return: Null
        """
        self.__contenu["Jambes"] = newJambes

    def changerAccessoire(self, newAccessoire):
        """
        Permet de changer l'accessoire courant par l'objet donné en paramètre

        :param newArme: Objet nouvel accessoire

        :return: Null
        """
        self.__contenu["Accessoire"] = newAccessoire

    def getArmePrincipale(self):
        """
        Retourne l'arme principale de l'équipement

        :return: Objet arme principale
        """
        return self.__contenu["ArmePrincipale"]

    def getArmeSecondaire(self):
        """
        Retourne l'arme secondaire de l'équipement

        :return: Objet arme secondaire
        """
        return self.__contenu["ArmeSecondaire"]

    def getPlastron(self):
        """
        Retourne le plastron de l'équipement

        :return: Objet plastron
        """
        return self.__contenu["Plastron"]

    def getCasque(self):
        """
        Retourne le casque de l'équipement

        :return: Objet casque
        """
        return self.__contenu["Casque"]

    def getJambes(self):
        """
        Retourne l'équipement de jambes

        :return: Objet jambes
        """
        return self.__contenu["Jambes"]

    def getAccessoire(self):
        """
        Retourne l'accessoire de l'équipement

        :return: Objet accessoire
        """
        return self.__contenu["Accessoire"]
