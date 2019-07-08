import sys
import pygame
from bullet import Bullet

def check_keydown_events(event,ai_settings,screen,hero,bullets):
    if event.key == pygame.K_RIGHT:
        # 向右移动
        hero.moving_right = True
    elif event.key == pygame.K_LEFT:
        hero.moving_left = True
    elif event.key == pygame.K_SPACE:
        #按下空格,创建一颗子弹,并将其加入到编组bullets中
        fire_bullet(ai_settings,screen,hero,bullets)

def fire_bullet(ai_settings,screen,hero,bullets):
    """如果还没到达限制，就发射一颗子弹"""
    #创建新子弹,并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, hero)
        bullets.add(new_bullet)

def check_keyup_events(event,hero):
    if event.key == pygame.K_RIGHT:
        hero.moving_right = False
    elif event.key == pygame.K_LEFT:
        hero.moving_left = False

def check_events(ai_settings,screen,hero,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,hero,bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event,hero)

def update_screen(ai_settings,screen,hero,bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    screen.fill(ai_settings.bg_color)
    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    hero.blitme()
    #让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(bullets):
    """更新子弹的位置,并删除已消失的子弹"""
    bullets.update()
    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))
