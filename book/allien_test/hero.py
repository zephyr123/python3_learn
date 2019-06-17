import pygame

"""创建超人类"""
class Hero():
    """接受screen参数,在screen上绘制图像"""
    def __init__(self,ai_settings,screen):
        self.screen = screen
        self.ai_settings = ai_settings
        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/hero.bmp')
        self.rect = self.image.get_rect()  #获取图片的矩形
        self.screen_rect = screen.get_rect()    #获取屏幕的矩形
        #将超人放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.moving_right  = False  #移动标志
        self.moving_left = False #移动标志vt

    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.hero_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.hero_speed_factor
        self.rect.centerx = self.center #根据self.center更新rect对象
    def blitme(self):
        self.screen.blit(self.image,self.rect)

