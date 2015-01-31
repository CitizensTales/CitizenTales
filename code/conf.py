import pygame

class Configuration:
    """
    Définissez les différentes options du jeu dans cette classe.
    """

    def __init__(self):
        # TOUCHES DE JEU
        # Vous pouvez allez voir ce site pour plus d'infos sur les correspondances entre touches pygame
        #   et touches réelles.
        # http://thepythongamebook.com/fr:glossaire:p:pygame:keycodes
        # /!\ Les touches pygame sont en QWERTY ! /!\
        self.confDict = {
            "key_up": pygame.K_UP,
            "key_down": pygame.K_DOWN,
            "key_left": pygame.K_LEFT,
            "key_right": pygame.K_RIGHT,
            "key_action": pygame.K_SPACE,
            "tiles_height": 16,
            "tiles_width": 16,
            "screen_height": 600,
            "screen_width": 600
        }