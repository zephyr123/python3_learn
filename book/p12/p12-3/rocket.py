import pygame

class Rocket():
    def __init__(self,screen):
        """初始化飞船并设置初始位置"""
        self.screen = screen
        self.image = pygame.image.load('images/rocket.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将每艘新火箭放到屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整火箭位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.moving_left and self.rect.left >0:
            self.rect.centerx -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 1
        if self.moving_up and self.rect.top >0:
            self.rect.centery -= 1


    def blitme(self):
        """在指定位置绘制火箭"""
        self.screen.blit(self.image,self.rect)
