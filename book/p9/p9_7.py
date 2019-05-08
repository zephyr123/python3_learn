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

class Admin(User):
    """管理员类"""

    def __init__(self,first_name,last_name,sex,privileges):
        """初始化admin类"""
        super().__init__(first_name,last_name,sex)

    def show_privileges(self):
        """显示管理员权限"""
        print("Admin的权限如下:")
        for privilege in privileges:
            print(privilege)

privileges = ['can add post', 'can delete post', 'can ban user']
admin = Admin('胡','永生','男', privileges)
admin.show_privileges()


