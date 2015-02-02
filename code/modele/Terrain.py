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
from modconf.tiles import Tiles
from modconf.levels import Levels

def loadConfigTiles():
    dictTiles = Tiles.tiles
    return dictTiles


class Case():

    """
    Classe définissant une case du terrain
    """

    def __init__(self, passable=True, bloqueVision=True, img="img/dev_void.png"):
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

    def __init__(self, nomNiveau="dev_emptyRoom"):
        """
        Constructeur de la classe Niveau de jeu

        :return: Null
        """
        try:
            levels = Levels.levels
            self.__matrice = levels[nomNiveau]
        except:
            print("Erreur de chargement de niveau")



class Immeuble():
    """
    Classe consistant en une structure de donnée ordonnée de Niveau
    """

    def __init__(self):
        self.__niveaux = [Niveau()]
        self.__niveauCourant = 0
        self.__nbrEtages = 0

    def ajouterNiveau(self, niveau):
        if (self.__nbrEtages == 0):
            self.__niveaux = [niveau]
        else:
            self.__niveaux += niveau
        self.__nbrEtages += 1

    def monterNiveau(self):
        if (self.__niveauCourant + 1) <= self.__nbrEtages:
            self.__niveauCourant += 1

    def descendreNiveau(self):
        if (self.__niveauCourant > 0):
            self.__niveauCourant += 1

    def setNiveauCourant(self, nouveauNiveauCourant):
        if (nouveauNiveauCourant >= 0) and (nouveauNiveauCourant <= self.__nbrEtages):
            self.__niveauCourant = nouveauNiveauCourant

    def getNiveauCourant(self):
        return self.__niveaux[self.__niveauCourant]
