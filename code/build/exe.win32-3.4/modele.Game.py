__author__ = 'Argann'


import pygame
from pygame.locals import *
from conf import Configuration
from modele import Terrain
from modele.Acteur import Acteur

"""
Module décrivant certaines méchaniques de jeu
"""

class CurrentGame():
    """
    Classe décrivant l'état actuel du jeu
    """

    def __init__(self, immeuble=Terrain.Immeuble(niveauBase="dev_test1")):
        pygame.init()
        self.__settings = self.loadSettings()
        self.__immeuble = immeuble
        self.__niveauCourant = self.__immeuble.getNiveauCourant()
        if self.__settings["screen_autoAdjust"]:
            SCREEN_SIZE = (self.__niveauCourant.tailley * self.__settings["tiles_height"], self.__niveauCourant.taillex * self.__settings["tiles_width"])
        else :
            SCREEN_SIZE = (self.__settings["screen_width"], self.__settings["screen_height"])
        self.__ecran = pygame.display.set_mode(SCREEN_SIZE)
        self.__backLayer = pygame.Surface(self.__ecran.get_size())
        self.__midLayer = pygame.Surface(self.__ecran.get_size())
        self.__frontLayer = pygame.Surface(self.__ecran.get_size())

    def refreshBackLayer(self):
        backsurf = pygame.Surface((self.__niveauCourant.tailley * self.__settings["tiles_height"], self.__niveauCourant.taillex * self.__settings["tiles_width"]))
        matriceNiveau = self.__niveauCourant.getBackMatrice()
        x, y = 0, 0
        for ligne in matriceNiveau:
            for colonne in ligne:
                backsurf.blit(pygame.image.load(colonne.getImage()), (self.__settings["tiles_height"]*x, self.__settings["tiles_width"]*y))
                x += 1
            x = 0
            y += 1
        self.__backLayer = backsurf
        self.__ecran.blit(self.__backLayer, (0, 0))
        pygame.display.update()

    def refreshMidLayer(self):
        midsurf = pygame.Surface((self.__niveauCourant.tailley * self.__settings["tiles_height"], self.__niveauCourant.taillex * self.__settings["tiles_width"]), pygame.SRCALPHA, 32)
        midsurf.convert_alpha()
        actlist = self.__niveauCourant.getActorList()
        for actor in actlist:
            midsurf.blit(pygame.image.load(actor.getImage()), (actor.getPosX() * self.__settings["tiles_height"], actor.getPosY() * self.__settings["tiles_width"]))
        midsurf.blit(pygame.image.load(self.hero.getImage()), (self.hero.getPosX() * self.__settings["tiles_height"], self.hero.getPosY() * self.__settings["tiles_width"]))
        self.__midLayer = midsurf

    def loadSettings(self):
        """
        Méthode permettant de lire les différentes configurations choisies dans conf.py
        """
        confObject = Configuration()
        return confObject.confDict

    def deplacementEstPossible(self, acteur, x, y):
        """
        Méthode permettant de savoir si le déplacement relatif a l'acteur
        (positionXacteur + x et positionYacteur + y) est possible ou non
        """
        #TODO Gérer la couche du milieu, suivant si les acteurs sont ghost=True et sont PICKABLE
        try:
            return self.__niveauCourant.getBackMatrice()[acteur.getPosY() + y][acteur.getPosX() + x].estPassable()
        except:
            return False

    def handleEvent(self, pushedkey):
        """
        Méthode permettant de gérer les différents évenements de jeu
        :return:
        """
        if pushedkey == self.__settings["key_up"]:
            if self.deplacementEstPossible(self.hero, 0, -1):
                self.hero.deplacementRelatif(0, -1)
        elif pushedkey == self.__settings["key_down"]:
            if self.deplacementEstPossible(self.hero, 0, 1):
                self.hero.deplacementRelatif(0, 1)
        elif pushedkey == self.__settings["key_right"]:
            if self.deplacementEstPossible(self.hero, 1, 0):
                self.hero.deplacementRelatif(1, 0)
        elif pushedkey == self.__settings["key_left"]:
            if self.deplacementEstPossible(self.hero, -1, 0):
                self.hero.deplacementRelatif(-1, 0)
        elif pushedkey == self.__settings["key_action"]:
        self.actorsLoop()
        self.refreshAll()

    def actorsLoop(self):
        actorlist = self.__niveauCourant.getActorList()
        for acteur in actorlist:
            if acteur.getType() == Acteur.TYPE_ENEMY:
                if self.deplacementEstPossible(acteur, 0, -1):
                    acteur.deplacementRelatif(0, -1)
                acteur.blesser(2)
                if acteur.getPointDeVie() <= 0:
                    actorlist.remove(acteur)
                    actorlist.append(Acteur(nom="cadavre",
                                            typeActeur=Acteur.TYPE_OBJECT,
                                            img="img/dev_cadavre.png",
                                            posx=acteur.getPosX(),
                                            posy=acteur.getPosY()))

    def refreshAll(self):
        """
        Permet d'actualiser le niveau du milieu, et d'afficher le niveau du bas (qui devra déjà être généré), puis le
        niveau du milieu.
        """
        self.refreshMidLayer()
        self.__ecran.blit(self.__backLayer, (0, 0))
        self.__ecran.blit(self.__midLayer, (0, 0))
        pygame.display.update()

    def play(self):
        self.hero = self.__niveauCourant.getActorList()[self.__niveauCourant.indiceHero]
        self.refreshBackLayer()
        self.refreshAll()
        enCours = True
        while enCours:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    enCours = False
                elif event.type == pygame.KEYDOWN:
                    self.handleEvent(event.key)

