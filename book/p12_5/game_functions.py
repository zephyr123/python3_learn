import sys
import pygame
from bullet import Bullet

def check_keydown_events(event,ai_settings,screen,boat,bullets):
    if event.key == pygame.K_DOWN:
        boat.moving_down = True  #向下移动
    elif event.key == pygame.K_UP:
        boat.moving_up = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen ,boat,bullets)

def check_keyup_events(event,boat):
    if event.key == pygame.K_DOWN:
        boat.moving_down = False
    elif event.key == pygame.K_UP:
        boat.moving_up = False

def check_events(ai_settings,screen,boat,bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,boat,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,boat)

def update_screen(ai_settings,screen,boat,bullets):
    screen.fill((0, 0, 255))  # 先绘制屏幕,再绘制飞船
    #每次循环时更新屏幕
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    boat.blitme()
    pygame.display.flip()

def update_bullets(bullets,ai_settings):
    bullets.update()
    #删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.right  > ai_settings.screen_width:
            bullets.remove(bullet)

def fire_bullet(ai_settings,screen,boat,bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,boat)
        bullets.add(new_bullet)