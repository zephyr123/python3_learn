class Settings():
    """存储外星人入侵的所有设置的类"""
    def __init__(self):
        """初始化屏幕"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5 #飞船的设置速度1.5像素

