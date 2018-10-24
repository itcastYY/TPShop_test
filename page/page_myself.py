# -*- coding=utf-8 -*-
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base import Baseaction


class myselfPageAction(Baseaction):

    # 定义需要操作的元素特征：
    login_reg_feature = By.XPATH,"text,登录/注册,1"
    number_feature = By.XPATH,"text,请输入手机号码,1"
    pwd_feature = By.ID,"com.tpshop.malls:id/edit_password"
    enter_feature = By.ID,"com.tpshop.malls:id/btn_login"

    @allure.step(title="点击登录/注册按钮")
    def click_login_reg(self):
        self.click( self.login_reg_feature )

    @allure.step(title="输入手机账号")
    def input_number(self,value):
        allure.attach("描述","写入了账号%s"%value)
        self.input_txt(self.number_feature,value)

    @allure.step(title="输入账号密码")
    def input_pwd(self,value):
        self.input_txt(self.pwd_feature,value)

    @allure.step(title="点击登录")
    def click_enter(self):
        self.click( self.enter_feature )

    @allure.step(title="验证登录按钮是否可用")
    def get_enter_status(self):
        return self.get_btn_status( self.enter_feature )



