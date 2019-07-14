class Settings():
    """存储所有设置的类"""
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.boat_speed_factor = 1
        #子弹的属性
        self.bullet_speed_factor = 1
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3