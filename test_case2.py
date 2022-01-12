# 导包
import unittest
from HTMLTestRunner import HTMLTestRunner
# 创建套件
suite = unittest.TestLoader().discover('.',pattern='test_case1.py')
# 生成文件
report = 'test_report1.html'
with open(report,'wb') as f:
    runner = HTMLTestRunner(f,title='测试报告',description='v.1.0')
    runner.run(suite)



