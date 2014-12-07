from vue.Menu import MenuPrincipal
import pygame
from pygame.locals import *

__author__ = 'Argann'

if __name__ == '__main__':
    pygame.init()
    ecran = pygame.display.set_mode((500, 500))
    background = pygame.Surface(ecran.get_size())

    menucool = MenuPrincipal()
    rendu = menucool.render()

    background.blit(rendu, (0, 0))
    ecran.blit(background, (0, 0))
    pygame.display.update()

    enCours = True
    while enCours:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                enCours = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    enCours = False
                if event.key == pygame.K_DOWN:
                    menucool.selectButton_down()
                    rendu = menucool.render()
                    background.blit(rendu, (0, 0))
                    ecran.blit(background, (0, 0))
                    pygame.display.update()

                if event.key == pygame.K_UP:
                    menucool.selectButton_up()
                    rendu = menucool.render()
                    background.blit(rendu, (0, 0))
                    ecran.blit(background, (0, 0))
                    pygame.display.update()

                if event.key == pygame.K_RETURN:
                    menucool.activerBoutonCourant()