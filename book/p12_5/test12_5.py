import sys
import pygame
from pygame.sprite import Group
from boat import Boat
from settings import Settings
import game_functions as gf
import bullet

def run_test():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    boat = Boat(screen,ai_settings)
    pygame.display.set_caption("test-12_5")
    bullets = Group()

    while True:
        gf.check_events(ai_settings,screen,boat,bullets)
        boat.update()
        gf.update_bullets(bullets,ai_settings)
        gf.update_screen(ai_settings,screen,boat,bullets)


run_test()


