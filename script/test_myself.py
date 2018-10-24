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

    # 2 不填写账号登录测试
    @pytest.mark.skip("跳过测试")
    def test_login_no_num(self):
        # 进入首页 点击我的按钮
        self.page.initIndexPage.click_myself()
        # 进入登录注册入口页，点击入口按钮
        self.page.initMyselfPage.click_login_reg()
        # 输入空账号
        self.page.initMyselfPage.input_number( "" )
        # 输入密码
        self.page.initMyselfPage.input_pwd("123456")
        # 获取按登录按钮的状态是否为可点击,并执行 【断言的作用是判断当前用例是否通过】
        assert not self.page.initMyselfPage.get_enter_status()

    # 3 不填写密码登录测试
    def test_login_no_pwd(self):
        # 进入首页，点击我的
        self.page.initIndexPage.click_myself()
        # 进入登录注册界面
        self.page.initMyselfPage.click_login_reg()
        # 输入账号
        self.page.initMyselfPage.input_number("18513891234")
        # 输入空密码
        self.page.initMyselfPage.input_pwd("")
        # 判断状态，添加断言
        assert not self.page.initMyselfPage.get_enter_status()

    # 4 显示密码操作自动化
