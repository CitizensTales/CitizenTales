__author__ = 'Argann'

from modele import Terrain
import pygame
from pygame.locals import *

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
        Méthode permettant de lire les différentes configurations choisies dans config.txt
        """
        with open("config.txt", "r") as configtiles:
            raw_config_list = [ligne for ligne in configtiles if ligne[0] != "#"]
        return {ligne.split(":")[0].strip() : ligne.split(":")[1].strip() for ligne in raw_config_list}

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
                    enCours = self.handleEvent(event.key)
