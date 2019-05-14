import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """针对Employee测试"""
    def setUp(self):
        """创建一组对象和答案"""
        first_name = 'Hu'
        last_name = 'yongsheng'
        salary = '10000'
        self.yuangong = Employee(first_name,last_name,salary)
        self.info = ['Huyongsheng:60000','Huyongsheng:30000']

    def test_give_default_raise(self):
        self.yuangong.give_raise()
        self.assertIn(self.yuangong.give_fullname(),self.info)

    def test_give_custom_raise(self):
        self.yuangong.give_raise(20000)
        self.assertIn(self.yuangong.give_fullname(),self.info)

unittest.main()