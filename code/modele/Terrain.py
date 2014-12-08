__author__ = 'Argann'

"""
Module Terrain

@author  : Argann Bonneau
@version : 0.1a
@date    : 02-10-14

Ce module regroupe toutes les cases liées au terrain.
    - Case
    - Terrain
"""


class Case():

    """
    Classe définissant une case du terrain
    """

    def __init__(self, passable, bloqueVision, img):
        """
        Constructeur de Case
        """
        self.__passable = passable
        self.__bloqueVision = bloqueVision
        self.__img = img

    def estPassable(self):
        """
            Getter de __passable
        """
        return self.__passable

    def setPassable(self, newValeur):
        """
        Setter __passable

        :param newValeur: est ce que la case est passable ?

        :type newValeur: boolean
        """
        self.__passable = newValeur

    def getBloqueVision(self):
        """
            Getter de __bloqueVision
        """
        return self.__bloqueVision

    def setBloqueVision(self, newValeur):
        """
            Setter __bloqueVision
        """
        self.__bloqueVision = newValeur

    def getImage(self):
        """
            Getter de __img
        """
        return self.__img

    def setImage(self, newValeur):
        """
            Setter __img
        """
        self.__img = newValeur


class Niveau():
    """
    Classe définissant les méthodes et attributs d'un niveau de jeu
    """

    def __init__(self, taillex=0, tailley=0, matrice=[], fichier="defaut"):
        """
        Constructeur de la classe Niveau de jeu

        :return: Null
        """
        if fichier != "defaut":
            self.__matrice = self.chargerFichier(fichier)
        elif matrice != []:
            self._matrice = matrice
        else:
            self.__matrice = [[Case(True, False, ".") for x in range(taillex)] for y in range(tailley)]


    def chargerFichier(self, fichier):
        """
        Méthode permettant de charger la matrice contenue dans un fichier dans le niveau courant.

        :param fichier: chemin du fichier a charger
        """
        #TODO Ecrire cette méthode