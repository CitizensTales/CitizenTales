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
import random

class Acteur():

    """
    Classe Acteur.

    Un Acteur peut définir plusieurs entitées en jeu :

    - Le personnage jouable
    - Les ennemis
    - Les objets destructibles
    """

    #Ces constantes permettent de différencier les différents types d'acteurs
    TYPE_PLAYER = 0
    TYPE_ENEMY = 1
    TYPE_OBJECT = 2
    TYPE_PICKABLE_OBJECT = 3

    MAX_BASE_DAMAGE = 3

    def allowedActors():
        """
        Cette méthode est particulièrement utile pour la personnalisation du jeu.

        Elle décrit tout les types d'acteurs qu'il est possible de trouver en jeu.

        :return: Dictionnaire d'acteurs autorisés, associant a une représentation dans la matrice l'acteur correspondant
        :rtype: dict(String : Acteur)
        """
        return {
            "@": Acteur(
                typeActeur=Acteur.TYPE_PLAYER,
                nom="Hero",
                pdv=50,
                pdvMax=100,
                img="img/dev_actor.png",
                equip=Equipement()
            ),
            ".": None,
            ">": None,
            "E": Acteur(
                typeActeur=Acteur.TYPE_ENEMY,
                nom="Ennemi",
                pdv=5,
                pdvMax=5,
                img="img/dev_enemi.png",
                equip=Equipement()
            ),
            "~": Acteur(
                typeActeur=Acteur.TYPE_OBJECT,
                nom="Cadavre",
                pdv=1,
                pdvMax=1,
                img="img/dev_cadavre.png",
                ghost=True
            )
        }

    def __init__(self, nom="", typeActeur=TYPE_PLAYER, pdv=0, pdvMax=0, posx=0, posy=0, img="", equip=None, ghost=False):
        """
        Constructeur d'acteur

        :param nom: Nom de l'instance d'acteur.
        :type nom: String

        :param typeActeur: Type de l'acteur (Joueur, ennemi, objet destructible)
        :type typeActeur: Constante TYPE d'Acteur

        :param pdv: Points de vie de l'instance d'acteur
        :type pdv: int

        :param pdvMax: Points de vie maximum de l'instance d'acteur
        :type pdvMax: int

        :param posx: Position X de l'acteur dans la matrice de jeu
        :type posx: int

        :param posy: Position Y de l'acteur dans la matrice de jeu
        :type posy: int

        :param img: Chemin vers l'image de l'instance d'acteur
        :type img: String

        :param equip: Equipement spécifique a l'acteur
        :type equip: Equipement
        """
        self.__nom = nom
        self.__pointDeVie = pdv
        self.__pointDeVieMax = pdvMax
        self.__posX = posx
        self.__posY = posy
        self.__img = img
        self.__equipement = equip
        self.__typeActeur = typeActeur

    def deplacementRelatif(self, changeX, changeY):
        """
        Déplace l'acteur, en faisant ces changements :

        :param changeX: Valeur à ajouter à la position X courante
        :type changeX: int

        :param changeY: Valeur à ajouter à la position Y courante
        :type changeY: int
        """
        self.__posX += changeX
        self.__posY += changeY

    def deplacementAbsolu(self, posx, posy):
        """
        Déplace l'acteur, en faisant ces changements :

        :param posx: Nouvelle valeur de position X
        :type posx: int

        :param posy: Nouvelle valeur de position Y
        :type posy: int
        """
        self.__posX = posx
        self.__posY = posy

    def getPointDeVie(self):
        """
            Getter de __pointDeVie

            :return: Point de vie de l'acteur
            :rtype: int
        """
        return self.__pointDeVie

    def setPointDeVie(self, newValeur):
        """
            Setter __pointDeVie

            :param newValeur: Nouvelle valeur de point de vie à assigner a l'acteur
            :type newValeur: int
        """
        self.__pointDeVie = newValeur

    def getPointDeVieMax(self):
        """
            Getter de __pointDeVieMax

            :return: Points de vie maximum de l'acteur
            :rtype: int
        """
        return self.__pointDeVieMax

    def setPointDeVieMax(self, newValeur):
        """
            Setter __pointDeVieMax

            :param newValeur: Nouvelle valeur maximum de point de vie pour l'acteur
            :type newValeur: int
        """
        self.__pointDeVieMax = newValeur

    def soigner(self, soin):
        """
        Permet de soigner de soin point de vie l'acteur.

        Ne peut pas dépasser ``pdvMax``

        :param soin: Valeur a ajouter aux points de vie de l'acteur.
        :type soin: int
        """
        self.__pointDeVie += soin
        if self.__pointDeVie > self.__pointDeVieMax:
            self.__pointDeVie = self.__pointDeVieMax

    def blesser(self, degats):
        """
        Permet de blesser de degats point de vie l'acteur.

        Active la méthode ``tuer()`` si les PV tombent en dessous de 0

        :param degats: Valeur à enlever aux points de vie de l'acteur
        :type degats: int
        """
        self.__pointDeVie -= degats
        if self.__pointDeVie <= 0:
            self.tuer()

    def tuer(self):
        """
        Methode activée une fois que l'acteur atteint les 0 PV
        """
        pass

    def getPosX(self):
        """
            Getter de __posX

            :return: Position X de l'acteur dans la matrice de jeu
            :rtype: int
        """
        return self.__posX

    def getPosY(self):
        """
            Getter de __posY

            :return: Position Y de l'acteur dans la matrice de jeu
            :rtype: int
        """
        return self.__posY

    def getImage(self):
        """
            Getter de __img

            :return: Chemin vers l'image décrivant l'acteur
            :rtype: String
        """
        return self.__img

    def setImage(self, newValeur):
        """
            Setter __img

            :param newValeur: Chemin vers une nouvelle image décrivant l'acteur
            :type newValeur: String
        """
        self.__img = newValeur

    def getNom(self):
        """
            Getter de nom

            :return: Nom de l'acteur
            :rtype: String
        """
        return self.__nom

    def setNom(self, newValeur):
        """
            Setter nom

            :param newValeur: Nouveau nom de l'acteur
            :type newValeur: String
        """
        self.__nom = newValeur

    def getType(self):
        """
            Getter du type de l'acteur

        :return: Type de l'acteur
        :rtype: constante TYPE d'Acteur
        """
        return self.__typeActeur

    def setType(self, newValeur):
        """
            Setter du type de l'acteur

        :param newValeur: nouveau type de l'acteur en cours
        :type newValeur: constante TYPE d'Acteur
        """
        self.__typeActeur = newValeur