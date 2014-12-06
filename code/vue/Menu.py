__author__ = 'Argann'

import pygame
from pygame.locals import *


class Menu():

    """Classe gérant l'affichage d'un menu, composé de boutons.
    """

    def __init__(self, nom="NONAME", boutons=[], autre=[],
                 taillex=10, tailley=10, backgroundColor=(0, 0, 0),
                 backgroundImage=""):

        self.__titleText = nom
        self.__boutons = boutons
        self.__autre = autre
        self.__taillex = taillex
        self.__tailley = tailley
        self.__boutonCourant = 0
        self.__backgroundColor = backgroundColor
        self.__backgroundImage = backgroundImage

    """
    -------------------------------------------------------
                    Fonctions utiles
    -------------------------------------------------------
    """

    def render(self):
        """
        Méthode de génération du menu.
        :return: retourne la pygame.Surface contenant le menu généré.
        """
        #--Création de la surface principale--
        menu = pygame.Surface((self.__taillex, self.__tailley))
        menu.fill(self.__backgroundColor)

        #--Création du titre--
        font = pygame.font.Font(None, 36)
        titre = font.render(self.__titleText, 1, (50, 255, 75))
        posTitre = titre.get_rect()
        posTitre.centerx = menu.get_rect().centerx
        menu.blit(titre, posTitre)

        #--Placement des boutons--
        indice = 0
        for bouton in self.__boutons:
            if indice == self.__boutonCourant:
                couleur = bouton.getActiveColor()
            else:
                couleur = bouton.getInactiveColor()
            btn = pygame.Surface((bouton.getTailleX(),
                                  bouton.getTailleY()))
            btn.fill(couleur)
            titre = font.render(bouton.getText(), 1, (50, 255, 75))
            posTexte = titre.get_rect()
            posTexte.centerx = btn.get_rect().centerx
            posTexte.centery = btn.get_rect().centery
            btn.blit(titre, posTexte)
            menu.blit(btn, bouton.getPos())
            indice += 1

        #--Et c'est fini !--
        return menu

    def selectButton_down(self):
        """
        Méthode permettant de placer le curseur de menu sur le bouton suivant par rapport au bouton courant.
        Si le bouton courant est actuellement le dernier, le curseur remonte au premier bouton.
        :return: Null
        """
        self.__boutonCourant += 1
        if self.__boutonCourant == len(self.__boutons):
            self.__boutonCourant = 0
        print(self.__boutonCourant)

    def selectButton_up(self):
        """
        Méthode permettant de placer le curseur de menu sur le bouton précédent par rapport au bouton courant.
        Si le bouton courant est actuellement premier, le curseur descend au dernier bouton.
        :return: Null
        """
        self.__boutonCourant -= 1
        if self.__boutonCourant < 0:
            self.__boutonCourant = len(self.__boutons)-1

    def activerBoutonCourant(self):
        """
        Permet d'activer la méthode lié au bouton courant.
        :return: Null
        """
        self.__boutons[self.__boutonCourant].execCommande()

    def getBoutonCourant(self):
        """
        Retourne le numéro du bouton courant
        :return: int self.__boutonCourant
        """
        return self.__boutonCourant

    def setBoutonCourant(self, newValeur):
        """
        Méthode permettant de changer le bouton courant
        :param newValeur: int ID du bouton qui deviendra le nouveau bouton courant.
        """

        self.__boutonCourant = newValeur

    """
    -------------------------------------------------------
                            Menus
    -------------------------------------------------------
    """
