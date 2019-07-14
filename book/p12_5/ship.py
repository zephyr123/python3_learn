import pygame
"""创建飞船类"""
class Ship():
    """接受screen参数，在screen绘制飞船"""
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('images/rockek.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)