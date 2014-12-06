__author__ = 'Argann'

"""
Classe Bouton

@author  : Argann Bonneau
@version : 0.1
@date    : 20-11-14
"""


class Bouton():

    """
    Classe définissant un bouton de menu
    """

    def __init__(self, posx=0, posy=0, texte="NOTEXT",
                 taillex=10, tailley=10, fonction=None,
                 activeColor=(200, 200, 200), inactiveColor=(20, 20, 20),
                 textColor=(0, 0, 0)):
        """
        Constructeur de Bouton
        :param posx:
        :param posy:
        :param texte:
        :param taillex:
        :param tailley:
        :param fonction:
        :param activeColor:
        :param inactiveColor:
        :param textColor:
        :return:
        """
        self.__posx = posx
        self.__posy = posy
        self.__text = texte
        self.__textColor = textColor
        self.__taillex = taillex
        self.__tailley = tailley
        self.__fonction = fonction
        self.__activeColor = activeColor
        self.__inactiveColor = inactiveColor

    def getPosX(self):
        """
        Getter de posX
        :return:
        """
        return self.__posx

    def setPosX(self, newValeur):
        """Setter de posX

        :param newValeur: Nouvelle valeur pour posX

        :return: Null
        """
        self.__posx = newValeur

    def getPosY(self):
        """
            Getter de __posy
        """
        return self.__posy

    def setPosY(self, newValeur):
        """
            Setter __posy
        """
        self.__posy = newValeur

    def getTailleX(self):
        """
            Getter de __taillex
        """
        return self.__taillex

    def setTailleX(self, newValeur):
        """
            Setter __taillex
        """
        self.__taillex = newValeur

    def getTailleY(self):
        """
            Getter de __tailley
        """
        return self.__tailley

    def setTailleY(self, newValeur):
        """
            Setter __tailley
        """
        self.__tailley = newValeur

    def getFonction(self):
        """
            Getter de __fonction
        """
        return self.__fonction

    def setFonction(self, newValeur):
        """
            Setter __fonction
        """
        self.__fonction = newValeur

    def getText(self):
        """
            Getter de __text
        """
        return self.__text

    def setText(self, newValeur):
        """
            Setter __text
        """
        self.__text = newValeur

    def getActiveColor(self):
        """
            Getter de __activeColor
        """
        return self.__activeColor

    def setActiveColor(self, newValeur):
        """
            Setter __activeColor
        """
        self.__activeColor = newValeur

    def getInactiveColor(self):
        """
            Getter de __inactiveColor
        """
        return self.__inactiveColor

    def setInactiveColor(self, newValeur):
        """
            Setter __inactiveColor
        """
        self.__inactiveColor = newValeur

    def getPos(self):
        """
            Getter de la position (x, y) du bouton
        """
        return (self.__posx, self.__posy)

    def getTextColor(self):
        """
            Getter de __textColor
        """
        return self.__textColor

    def setTextColor(self, newValeur):
        """
            Setter __textColor
        """
        self.__textColor = newValeur

    def execCommande(self, *args):
        """
            Méthode permettant de lancer la commande liée au bouton
        """
        self.__fonction(args)
