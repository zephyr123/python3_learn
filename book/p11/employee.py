class Employee():
    """雇员信息类"""
    def __init__(self,first_name,last_name,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = int(salary)
        # self.increase = 50000

    def give_raise(self,increase=50000):
        self.salary += int(increase)
        return self.salary

    def give_fullname(self):
        full_name = self.first_name + self.last_name + ':' + str(self.salary)
        return full_name
