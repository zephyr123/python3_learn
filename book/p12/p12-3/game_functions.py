import sys
import pygame

def check_events(rocket):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rocket.moving_right = True
            elif event.key == pygame.K_LEFT:
                rocket.moving_left = True
            elif event.key == pygame.K_DOWN:
                rocket.moving_down = True
            elif event.key == pygame.K_UP:
                rocket.moving_up = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                rocket.moving_right = False
            elif event.key == pygame.K_LEFT:
                rocket.moving_left = False
            elif event.key == pygame.K_UP:
                rocket.moving_up = False
            elif event.key == pygame.K_DOWN:
                rocket.moving_down = False

def update_screen(ai_settings,screen,rocket):
    """更新屏幕上的图像,并切换到新屏幕"""
    screen.fill(ai_settings.bg_color)
    rocket.blitme()
    pygame.display.flip()  # 让最近绘制的屏幕可见

