__author__ = 'Argann'

import modele.Terrain as Terrain
import pygame
from pygame.locals import *
import Game

if __name__ == '__main__':
    niveau = Terrain.Niveau(fichier="levels/dev_level1")
    immo = Terrain.Immeuble()
    immo.ajouterNiveau(niveau)

    jeu = Game.CurrentGame(immeuble=immo)
    jeu.play()