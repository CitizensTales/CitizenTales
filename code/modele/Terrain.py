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
from levels import *

def loadConfigTiles():
    with open("modele/config_tiles.txt", "r") as configtiles:
        liste = [x for x in configtiles]
    raw_tilesList = [[x.strip() for x in y.split(";")] for y in liste]
    tilesDict = {name : Case(passable, bloque, "img/"+img) for (name, passable, bloque, img) in raw_tilesList}
    return tilesDict


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
            self.chargerFichier(fichier)
        elif matrice != []:
            self.__matrice = matrice
        else:
            self.__matrice = [[Case(True, False, ".") for x in range(taillex)] for y in range(tailley)]

    def getMatrice(self):
        return self.__matrice

    def chargerFichier(self, fichier):
        """
        Méthode permettant de charger la matrice contenue dans un fichier dans le niveau courant.

        :param fichier: chemin du fichier a charger
        """
        with open(fichier, "r") as niveau:
            liste = [x.strip("\n ") for x in niveau]
        raw_matrice = [x.split("|") for x in liste]

        maxTailleX = 0
        for x in raw_matrice:
            if(len(x) > maxTailleX):
                maxTailleX = len(x)

        self.tailley = len(raw_matrice)
        self.taillex = maxTailleX

        tilesDict = loadConfigTiles()
        print(raw_matrice)
        self.__matrice = [[tilesDict[name] for name in x] for x in raw_matrice]

    def chargerNiveau(self, nomNiveau):
        '''
        Méthode permettant de charger un niveau dans la matrice
        :param nomNiveau:
        :return:
        '''

class Immeuble():
    """
    Classe consistant en une structure de donnée ordonnée de Niveau
    """

    def __init__(self):
        self.__niveaux = [Niveau(20, 20)]
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
