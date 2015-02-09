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

from modele.Acteur import Acteur
import copy

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
    #On a besoin de savoir quel symbole représente un mur...
    REPR_WALL = "X"

    def allowedTiles(self):
        return {
        ".": Case(
            passable=True,
            bloqueVision=False,
            img="img/dev_floor.png"
        ),

        "X": Case(
            passable=False,
            bloqueVision=True,
            img="img/dev_wall.png"
        ),

        "_": Case(
            passable=False,
            bloqueVision=True,
            img="img/dev_void.png"
        )
    }

    def customLevels(self):
        return {
            "dev_test1": {
                "base_building": [
                    "XXXXXXXXX__XXXXXXX__XXXXXXXXX",
                    "X.......X__X.....X__X.......X",
                    "X.......X__X.....X__X.......X",
                    "X.......X__X.....X__X.......X",
                    "X.......X__X.....X__X.......X",
                    "X.......X__X.....X__X.......X",
                    "X.......X__X.....X__X.......X",
                    "X.......X__X.....X__X.......X",
                    "X.......X__X.....X__X.......X",
                    "X.......X__X.....X__X.......X",
                    "X.......X__X.....X__X.......X",
                    "X.......X__X.....X__X.......X",
                    "X.......X__X.....X__X.......X",
                    "X.......XXXX.....XXXX.......X",
                    "X...........................X",
                    "X...........................X",
                    "X...........................X",
                    "X...........................X",
                    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
                ],
                "actors": [
                    ".............................",
                    ".............................",
                    "....@...................>....",
                    ".............................",
                    ".............................",
                    ".............................",
                    ".............................",
                    ".............................",
                    ".............................",
                    ".............................",
                    ".............................",
                    ".............................",
                    ".............................",
                    ".............................",
                    ".............................",
                    ".............................",
                    "..............E..............",
                    ".............................",
                    "............................."
                ]
            },
            "dev_emptyRoom": {
                "base_building": [
                    "XXXXXXXXXXXXXXXXXXXXX",
                    "X...................X",
                    "X...................X",
                    "X...................X",
                    "X...................X",
                    "X...................X",
                    "X...................X",
                    "XXXXXXXXXXXXXXXXXXXXX"
                ],
                "actors": [
                    ".....................",
                    ".....................",
                    ".....................",
                    "..........@..........",
                    ".....................",
                    ".....................",
                    ".....................",
                    "....................."
                ]
            },
            "dev_wallsTest" : {
                "base_building": [
                    "XXXXXXXXXXXXXXXXXXXXX",
                    "X....X....X.........X",
                    "X...XXX..XX.........X",
                    "X....X...X..........X",
                    "X....X..............X",
                    "X...........X.......X",
                    "X...................X",
                    "XXXXXXXXXXXXXXXXXXXXX"
                ],
                "actors": [
                    ".....................",
                    ".@...................",
                    ".....................",
                    "....................",
                    ".....................",
                    ".....................",
                    ".....................",
                    "....................."
                ]
            }
        }

    def __init__(self, nomNiveau="dev_wallsTest"):
        """
        Constructeur de la classe Niveau de jeu

        :return: Null
        """
        self.allowedtiles = self.allowedTiles()
        self.customlevels = self.customLevels()
        self.__backMatrix = self.translateBackLevel(self.customlevels[nomNiveau]["base_building"])
        self.__actorsList = self.translateMidLevel(self.customlevels[nomNiveau]["actors"])
        self.taillex = len(self.__backMatrix)
        self.tailley = len(self.__backMatrix[0])

    def getWallImagePath(self, x, y, matrice):
        resultat = "img/dev_wall_"
        if x > 0:
            if matrice[x-1][y] == self.REPR_WALL:
                resultat += "u"
        if x < (len(matrice)-1):
            if matrice[x+1][y] == self.REPR_WALL:
                resultat += "d"
        if y > 0:
            if matrice[x][y-1] == self.REPR_WALL:
                resultat += "l"
        if y < (len(matrice[x])-1):
            if matrice[x][y+1] == self.REPR_WALL:
                resultat += "r"
        resultat += ".png"
        return resultat

    def translateBackLevel(self, matrice):
        x, y = 0, 0
        resultat = []
        for ligne in matrice:
            restLigne = []
            for case in ligne:
                if case == self.REPR_WALL:
                    pathImage = self.getWallImagePath(x, y, matrice)
                    caseObject = self.allowedTiles()[case]
                    caseObject.setImage(pathImage)
                    restLigne.append(caseObject)
                else:
                    restLigne.append(self.allowedTiles()[case])
                y += 1
            resultat.append(restLigne)
            y = 0
            x += 1
        return resultat

    def translateMidLevel(self, matrice):
        act = Acteur.allowedActors()
        actList = []
        x, y, z = 0, 0, 0
        for ligne in matrice:
            for case in ligne:
                if act[case] is not None:
                    actor = copy.deepcopy(act[case])
                    actor.deplacementAbsolu(x, y)
                    actList.append(actor)
                    if act[case].getNom() == "Hero":
                        self.indiceHero = z
                    z += 1
                x += 1
            x = 0
            y += 1
        return actList

    def getBackMatrice(self):
        return self.__backMatrix

    def getActorList(self):
        return self.__actorsList

class Immeuble():
    """
    Classe consistant en une structure de donnée ordonnée de Niveau
    """

    def __init__(self, niveauBase="dev_wallsTest"):
        self.__niveaux = [Niveau(nomNiveau=niveauBase)]
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
