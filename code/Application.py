__author__ = 'Argann'

import pygame
from pygame.locals import *
import Game
import modele.Terrain as Terrain

if __name__ == '__main__':
    immo = Terrain.Immeuble()
    nivo = Terrain.Niveau("dev_test1")
    immo.ajouterNiveau(nivo)
    jeu = Game.CurrentGame(immo)
    jeu.play()