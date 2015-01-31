__author__ = 'Argann'

from modele import Terrain
import pygame
from pygame.locals import *
from conf import Configuration

"""
Module décrivant certaines méchaniques de jeu
"""

class CurrentGame():
    """
    Classe décrivant l'état actuel du jeu
    """

    def __init__(self, immeuble=Terrain.Immeuble()):
        pygame.init()
        self.__settings = self.loadSettings()
        self.__immeuble = immeuble
        SCREEN_SIZE = (int(self.__settings["screen_width"]), int(self.__settings["screen_height"]))
        self.__ecran = pygame.display.set_mode(SCREEN_SIZE)
        self.__backLayer = pygame.Surface(self.__ecran.get_size())
        self.__midLayer = pygame.Surface(self.__ecran.get_size())
        self.__frontLayer = pygame.Surface(self.__ecran.get_size())

    def refreshBackLayer(self):
        backsurf = pygame.Surface((self.__immeuble.getNiveauCourant().taillex * int(self.__settings["tiles_height"]), self.__immeuble.getNiveauCourant().tailley * int(self.__settings["tiles_width"])))
        matriceNiveau = self.__immeuble.getNiveauCourant().getMatrice()
        x, y = 0, 0
        for ligne in matriceNiveau:
            for colonne in ligne:
                backsurf.blit(pygame.image.load(str(colonne.getImage())), (int(self.__settings["tiles_height"])*x, int(self.__settings["tiles_width"])*y))
                x += 1
            x = 0
            y += 1
        self.__backLayer = backsurf
        return self.__backLayer

    def loadSettings(self):
        """
        Méthode permettant de lire les différentes configurations choisies dans conf.py
        """
        confObject = Configuration()
        return confObject.confDict

    def handleEvent(self, pushedkey):
        """
        Méthode permettant de gérer les différents évenements de jeu
        :return:
        """
        if pushedkey == pygame.K_ESCAPE:
            return False

    def play(self):

        background = self.refreshBackLayer()
        self.__ecran.blit(background, (0, 0))
        pygame.display.update()
        enCours = True
        print(self.__settings)
        while enCours:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    enCours = False
                elif event.type == pygame.KEYDOWN:
                    print("loul")
                    print("event key : ", event.key, ", touche haut : ", self.__settings["key_up"])
                    if event.key == self.__settings["key_up"]:
                        print("Wow, you go up !")
                    elif event.key == self.__settings["key_down"]:
                        print("Wow, you go down !")
                    elif event.key == self.__settings["key_right"]:
                        print("Wow, you go right !")
                    elif event.key == self.__settings["key_left"]:
                        print("Wow, you go left !")
                    elif event.key == self.__settings["key_action"]:
                        print("Wow, you do something !")
