import pygame
import sys
from settings import Settings
from rocket import Rocket
import game_functions as gf

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_heigh))
    pygame.display.set_caption("rocket")
    rocket = Rocket(screen)

    #监视键盘和鼠标事件
    while True:
        gf.check_events(rocket)
        gf.update_screen(ai_settings,screen,rocket)
        rocket.update()
run_game()
