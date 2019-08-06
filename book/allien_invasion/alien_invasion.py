import sys
import pygame
from pygame.sprite import Group
import bullet
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #创建一艘飞船
    ship = Ship(screen,ai_settings)
    #创建一个用于存储子弹的编组
    bullets = Group()
    alien = Alien(ai_settings,screen)

    #开始游戏主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        # print(len(bullets))
        #每次循环时都重绘屏幕
        gf.update_screen(ai_settings, screen,ship,alien,bullets)

run_game()