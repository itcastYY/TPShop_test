# -*- coding=utf-8 -*-
import time
import pytest
from base import initDriver
from page import Page
from base import getData


class TestDemo:

    # 初始化 APP和页面对象
    def setup(self):
        self.driver = initDriver()
        self.page = Page(self.driver)

    # 1 账号不存在登录测试
    @pytest.mark.parametrize("arg",getData("test_login_num_unexist"))
    @pytest.mark.skip( "跳过测试" )
    def test_login_num_unexist(self,arg):
        # 点击我的 进入登录/注册 入口页
        self.page.initIndexPage.click_myself()

        print(arg, '------', type(arg))

        # 点击登录/注册按钮,并使用强制等待将请登录提示跳过
        self.page.initMyselfPage.click_login_reg()
        time.sleep( 3 )
        # 输入账号
        self.page.initMyselfPage.input_number(arg[0])
        # 输入密码
        self.page.initMyselfPage.input_pwd(arg[1])
        # 点击登录
        self.page.initMyselfPage.click_enter()
        # 添加断言【断言的依据是代码执行的结果，本例就是判断当toast里的值：账号不存在】
        assert self.page.initMyselfPage.is_toast_exist(arg[2])

    # 2 将空账号和空密码合在一个用例当中
    @pytest.mark.parametrize( "userInfo",getData("test_login_miss_info") )
    def test_login_miss_info(self,userInfo):
        print( userInfo,'-----',type(userInfo) )
        # 获取用户输入的账号和密码
        user_number = userInfo[0]
        user_pwd = userInfo[1]

        # 点击我的按钮
        self.page.initIndexPage.click_myself()

        time.sleep(2)  #界面跳过，等待一会

        # 点击登录注册
        self.page.initMyselfPage.click_login_reg()

        # 输入空的账号和密码
        self.page.initMyselfPage.input_number(user_number)
        # 输入合理的密码
        self.page.initMyselfPage.input_pwd(user_pwd)

        # 断言登录按钮的状态
        assert not self.page.initMyselfPage.get_enter_status()

    # 4 显示密码操作自动化
