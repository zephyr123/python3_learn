import pygame

"""创建飞船类"""
class Boat():
    """接受screen参数，在screen绘制飞船"""
    def __init__(self,screen,ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/rocket.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #将飞船放到屏幕底部中央,修改为屏幕左边中央
        self.rect.left = self.screen_rect.left
        self.rect.centery = self.screen_rect.centery
        self.center = float(self.rect.centery)
        """移动标志"""
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_up and self.rect.top > 0:
            self.center -= self.ai_settings.boat_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.height:
            self.center += self.ai_settings.boat_speed_factor
        self.rect.centery = self.center

    def blitme(self):
        self.screen.blit(self.image,self.rect)