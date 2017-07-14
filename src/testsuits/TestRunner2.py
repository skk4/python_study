#-*- coding:utf-8 -*-
# coding = utf-8
import unittest
#import testsuits
#from testsuits.baidu_search import BaiduSearch
import time
import os
import HTMLTestRunner


'''
构建addTest方法
suite = unittest.TestSuite()    
suite.addTest(BaiduSearch('test_baidu_search'))
suite.addTest(BaiduSearch('test_baidu_search2'))
'''

'''
构建makeSuite方法
suite = unittest.TestSuite(unittest.makeSuite(BaiduSearch))
'''
case_dir=os.path.dirname(os.path.abspath('.')) + '/testsuits/'
report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
HtmlFile = report_path + now + "HTMLtemplate.html"  
fp = file(HtmlFile, "wb")

#构建discover方法
suite = unittest.TestLoader().discover(case_dir, pattern="*.py", top_level_dir=None)


if __name__=='__main__':
    #执行用例
    #runner=unittest.TextTestRunner()
    
    #初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"某某项目测试报告", description=u"用例测试情况")
    runner.run(suite)