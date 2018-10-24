# -*- coding=utf-8 -*-
import time
import allure
from selenium.webdriver.common.by import By
from base import Baseaction


class indexPageAction(Baseaction):
    startBtn_feature = By.ID,"com.tpshop.malls:id/start_Button"
    homeBtn_feature = By.XPATH,("text,首页,1","resource-id,com.tpshop.malls:id/tab_txtv,1")
    myselfBtn_feature = By.XPATH,("text,我的,1","resource-id,com.tpshop.malls:id/tab_txtv,1")

    # 一 、定义一个判断当前是否进入主界面的动作
    @allure.step(title="自动进入首页")
    def enterHome(self):
        # 区分用户是第一次还是非第一次使用，如果是第一次界面上则会出现首页字符
        try:
            time.sleep(3)
            allure.attach( "说明","判断当前加载的界面的底部是否有首页选项卡" )
            self.find_element(self.homeBtn_feature)
        except Exception:
            # 如果有语法错误我们就默认第一次进入首页
            # 1.强制跳过之后会看到四个欢迎界面，我们需要手动滑动跳过 【 手动滑屏操作很常用，我们选择定义在base中 】
            for i in range(3):
                self.swipe_left()
                time.sleep(1)
            # 2. 点击开始按钮进入首页
            self.click(self.startBtn_feature)
        else:
            print( "欢迎来到首页" )

    # 二、定义点击 我的 功能
    def click_myself(self):
        self.enterHome()
        time.sleep(2)
        self.click( self.myselfBtn_feature )

