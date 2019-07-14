import sys
import pygame
from ship import Ship

def run_test():
    pygame.init()

    screen = pygame.display.set_mode((800,600))
    ship = Ship(screen)
    pygame.display.set_caption("test-12_5")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        ship.blitme()
        screen.fill((0,0,255))
        pygame.display.flip()


run_test()


