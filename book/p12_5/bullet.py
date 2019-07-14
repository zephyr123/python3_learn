import pygame
from pygame.sprite import Sprite

#继承了Sprite父类
class Bullet(Sprite):
    """一个对飞船发射的子弹管理的类"""
    def __init__(self,ai_settings,screen,boat):
        super(Bullet,self).__init__()
        self.screen = screen
        #在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centery = boat.rect.centery
        self.rect.right = boat.rect.right
        #存储用小数表示子弹的位置
        self.x = float(self.rect.x)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向右移动子弹"""
        #更新表示子弹位置的小数值
        self.x += self.speed_factor
        #更新表示子弹的rect的位置
        self.rect.x = self.x

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)

