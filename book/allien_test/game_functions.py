import sys
import pygame

def check_keydown_events(event,hero):
    if event.key == pygame.K_RIGHT:
        # 向右移动
        hero.moving_right = True
    elif event.key == pygame.K_LEFT:
        hero.moving_left = True
def check_keyup_events(event,hero):
    if event.key == pygame.K_RIGHT:
        hero.moving_right = False
    elif event.key == pygame.K_LEFT:
        hero.moving_left = False

def check_events(hero):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,hero)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event,hero)

def update_screen(ai_settings,screen,hero):
    """更新屏幕上的图像，并切换到新屏幕"""
    screen.fill(ai_settings.bg_color)
    hero.blitme()
    #让最近绘制的屏幕可见
    pygame.display.flip()


