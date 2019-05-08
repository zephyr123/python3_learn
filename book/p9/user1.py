class User():
    """用户描述"""

    def __init__(self,first_name,last_name,sex):
        """初始化属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex

    def describe_user(self):
        """描述用户基本信息"""
        full_names = self.first_name + ' ' + self.last_name + ' ' + self.sex
        return full_names.title()

    def greet_user(self):
        """个性化问候"""
        full_name = self.first_name + ' ' + self.last_name
        message = full_name.title() + ",Welcome to here!"
        return message