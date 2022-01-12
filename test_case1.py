import unittest
from demo05 import login

class Testlogin(unittest.TestCase):
    def test_login1(self):
        self.assertEqual("登录成功",login('admin','123456'))
    def test_login2(self):
        self.assertEqual("登录失败",login('adim','12456'))
    def test_login3(self):
        self.assertEqual("用户名不能为空",login('','123456'))
    def test_login4(self):
        self.assertEqual("密码不能为空",login('admin',''))


a = unittest.TestSuite()
a.addTest(Testlogin('test_login1'))




