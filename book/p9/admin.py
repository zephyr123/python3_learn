from user import User
class Privileges():
    """定义Privileges类"""
    def __init__(self):
        """初始化属性"""
        self.privileges = ['can add post!', 'can delete post!!!', 'can ban user']

    def show_privileges(self):
        """显示管理员权限"""
        print("Admin的权限如下:")
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    """管理员类"""

    def __init__(self,first_name,last_name,sex):
        """初始化admin类"""
        super().__init__(first_name,last_name,sex)
        self.privileges = Privileges()