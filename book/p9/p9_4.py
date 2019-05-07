class Restaurant():
    """描述餐馆的类"""

    def __init__(self,restaurant_name,cuisine_type):
        """初始化餐厅属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 23

    def describe_restaurant(self):
        print(self.restaurant_name + "类型是:" + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + "正在营业中，欢迎来就餐！")

    def set_number_served(self,number):
        """设置就餐人的数量"""
        self.number_served = number

    def increment_number_served(self,numbers):
        self.number_served += numbers

qingfengbaozi = Restaurant('庆丰包子','包子')
# print(qingfengbaozi.number_served)
# qingfengbaozi.set_number_served(60)
# print(qingfengbaozi.number_served)
qingfengbaozi.increment_number_served(10)
print(qingfengbaozi.number_served)
