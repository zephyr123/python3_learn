class Restaurant():
    """描述餐馆的类"""

    def __init__(self,restaurant_name,cuisine_type):
        """初始化餐厅属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name + "类型是:" + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + "正在营业中，欢迎来就餐！")

class IceCreamStand(Restaurant):
    """一个雪餐馆"""
    def __init__(self,restaurant_name,cuisine_type,flavors):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = flavors

    def show_list(self):
        for flavor in self.flavors:
            print(flavor)

flavors = ['四个圈','小雪人','酸奶']
bingqiling = IceCreamStand('sanmingzhi','冷饮',flavors)
bingqiling.show_list()