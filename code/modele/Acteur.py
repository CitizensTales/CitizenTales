__author__ = 'Argann'

"""
Classe Acteur

@author  : Argann Bonneau
@version : 0.1
@date    : 01-10-14

Cette classe définit ce qu'est un Acteur en général dans le jeu.
---
    Attributs :

    - nom : String
        correspond au nom de l'acteur

    - pdv : int
        correspond aux points de vie actuels de l'acteur

    - pdvMax : int
        correspond aux points de vie maximaux de l'acteur

    - posx : int
        correspond à la position en X de l'acteur

    - posy : int
        correspond à la position en Y de l'acteur

    - img : String
        correspond au chemin d'accès au sprite de l'acteur

    - equipement : Equipement
        correspond a l'equipement courant de l'acteur
"""

from modele.Equipement import *


class Acteur():

    """
    Classe définissant un Acteur général

    """

    def __init__(self, nom, pdv, pdvMax, posx, posy, img, equip):
        """
        Constructeur d'acteur
        """
        #Définition des attributs
        self.__nom = nom
        self.__pointDeVie = pdv
        self.__pointDeVieMax = pdvMax
        self.__posX = posx
        self.__posY = posy
        self.__img = img
        self.__equipement = equip

    def deplacementRelatif(self, changeX, changeY):
        """
        Déplace l'acteur, en faisant ces changements :
        :param changeX: int valeur à ajouter à la position X courante
        :param changeY: int valeur à ajouter à la position Y courante
        """
        self.__posX += changeX
        self.__posY += changeY

    def deplacementAbsolu(self, posx, posy):
        """
        Déplace l'acteur, en faisant ces changements :
        :param posx: int nouvelle valeur de position X
        :param posy: int nouvelle valeur de position Y
        """
        self.__posX = posx
        self.__posY = posy

    def getPointDeVie(self):
        """
            Getter de __pointDeVie
        """
        return self.__pointDeVie

    def setPointDeVie(self, newValeur):
        """
            Setter __pointDeVie
        """
        self.__pointDeVie = newValeur

    def getPointDeVieMax(self):
        """
            Getter de __pointDeVieMax
        """
        return self.__pointDeVieMax

    def setPointDeVieMax(self, newValeur):
        """
            Setter __pointDeVieMax
        """
        self.__pointDeVieMax = newValeur

    def soigner(self, soin):
        """
        Permet de soigner de soin point de vie l'acteur.

        Ne peut pas dépasser ``pointDeVieMax``
        :param soin: int valeur a ajouter aux points de vie de l'acteur.
        """
        self.__pointDeVie += soin
        if self.__pointDeVie > self.__pointDeVieMax:
            self.__pointDeVie = self.__pointDeVieMax

    def blesser(self, degats):
        """
        Permet de blesser de degats point de vie l'acteur.

        Active la méthode ``tuer()`` si les PV tombent en dessous de 0
        :param degats: int valeur à enlever aux points de vie de l'acteur
        """
        self.__pointDeVie -= degats
        if self.__pointDeVie <= 0:
            self.tuer()

    def tuer(self):
        """
        Methode activée une fois que l'acteur atteint les 0 PV
        """
        print("L'acteur ", self.__nom, " est mort !")

    def getPosX(self):
        """
            Getter de __posX
        """
        return self.__posX

    def getPosY(self):
        """
            Getter de __posY
        """
        return self.__posY

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

    def getNom(self):
        """
            Getter de nom
        """
        return self.nom

    def setNom(self, newValeur):
        """
            Setter nom
        """
        self.nom = newValeur
