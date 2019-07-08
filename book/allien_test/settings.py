class Settings():
    """存储设置的类"""
    def __init__(self):
        """初始化游戏设置"""
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0,0,255)
        self.hero_speed_factor = 1.5
        #子弹的设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3