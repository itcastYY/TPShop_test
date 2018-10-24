# -*- coding=utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Baseaction:

    def __init__(self,driver):
        self.driver = driver

    # 自定义一个元素查找方法
    def find_element(self,feature,timeout=5,poll=1.0):
        # feature = By.XPATH,"//*[@text='显示']"
        """
        依据用户传入的元素信息特征，然后返回当前用户想要查找元素
        :param feature: 元组类型，包含用户希望的查找方式，及该方式对应的值
        :return: 返回当前用户查找的元素
        """
        by = feature[0]
        value = feature[1]
        if by == By.XPATH:
            # print( "说明了用户想要使用 xpath 路径的方式来获取元素" )
            value = self.make_xpath(value)
        # print( value,'-----' )
        wait = WebDriverWait(self.driver, timeout, poll)
        return wait.until(lambda x: x.find_element(by, value))

    def find_elements(self,feature):
        wait = WebDriverWait(self.driver, 5, 1)
        return wait.until(lambda x: x.find_elements(feature[0], feature[1]))

    # 自定义一个元素点击的方法【 这个方法无论是在当前页面还是其它页面都通用 】
    def click(self, feature):
        """
        依据用户传入的元素特征 对其实现点击的操作
        :param feature: 元素的信息元组
        :return:none
        """
        self.find_element(feature).click()

    # 自定义一个函数实现对具体元素进行值的输入
    def input_txt(self, feature, value):
        """
        依据用户传入的元素特征，找到对应的元素，然后在它里面输入我们的传入的 value值
        :param feature: 元组类型，表示元素的特征
        :param value:  用户在元素中输入的内容
        :return: none
        """
        self.find_element(feature).send_keys(value)

    # 自定义了一个可以自动帮我们拼接 xpath 路径的工具函数
    def make_xpath(self,feature):
        start_path = "//*["
        end_path = "]"
        res_path = ""

        if isinstance(feature, str):

            # 如果是字符串 我们不能直接上来就拆我们可以判断一下它是否是默认正确的 xpath 写法
            if feature.startswith("//*["):
                return feature

            # 如果用户输入的是字符串，那么我们就拆成列表再次进行判断
            split_list = feature.split(",")
            if len(split_list) == 2:
                # //*[contains(@text,'设')]
                res_path = "%scontains(@%s,'%s')%s" % (start_path, split_list[0], split_list[1], end_path)
            elif len(split_list) == 3:
                # //[@text='设置']
                res_path = "%s@%s='%s'%s" % (start_path, split_list[0], split_list[1], end_path)
            else:
                print("请按规则使用")
        elif isinstance(feature, tuple):
            for item in feature:
                # 默认用户在元组当中定义的数据都是字符串
                split_list2 = item.split(',')
                if len(split_list2) == 2:
                    res_path += "contains(@%s,'%s') and " % (split_list2[0], split_list2[1])
                elif len(split_list2) == 3:
                    res_path += "@%s='%s' and " % (split_list2[0], split_list2[1])
                else:
                    print("请按规则使用")
            andIndex = res_path.rfind(" and")
            res_path = res_path[0:andIndex]
            res_path = start_path + res_path + end_path
        else:
            print("请按规则使用")

        return res_path

    # 定义二个滑屏操作 ，上滑和左滑
    def swipe_up(self):
        w = self.getDeviceSize()[0]
        h = self.getDeviceSize()[1]
        start_x = w * 0.5
        start_y = h * 0.9
        end_x = w * 0.5
        end_y = h * 0.4
        self.driver.swipe(start_x, start_y, end_x, end_y)

    def swipe_left(self):
        # 使用 appium 里的swipe() 方法,先定义起点坐标和终点坐标
        w = self.getDeviceSize()[0]
        h = self.getDeviceSize()[1]
        start_x = w*0.9
        start_y = h*0.5
        end_x = w*0.3
        end_y = h*0.5
        self.driver.swipe( start_x,start_y,end_x,end_y )

    # 定义一个获取设备分辨率的方法
    def getDeviceSize(self):
        """
        获取当前手机设备的屏幕分辨率 将它们以元素的形式返回
        :return: 返回一个元组，内部包含的是屏幕的宽高
        """
        w = self.driver.get_window_size()["width"]
        h = self.driver.get_window_size()["height"]
        return w,h

    # 获取某个 toast 里的内容
    def get_toast_txt(self, message):
        """
        依据用户传入的文字信息，查找到对应的 toast 然后返回它里面的内容
        :param message: 用来查找 toast 的内容
        :return:返回被查找到的 toast 的元素内容
        """
        # 依据 message 来查询某个toast ，然后返回这个 toast 里的内容
        message = "//*[contains(@text,'%s')]"%message
        ele = self.find_element(feature=(By.XPATH,message),timeout=5,poll=0.1)
        return ele.get_attribute("text")

    # 定义一个函数 依据用户传入的内容来判断目标 toast 是否存在
    def is_toast_exist(self,message):
        try:
            self.get_toast_txt(message)
        except Exception:
            return False
        else:
            return True

    # 定义一个函数 返回当前按钮状态
    def get_btn_status(self,feature):
        """
        依据用户传入的元素特征，来返回当前元素的点击状态【 可点击为True,不可点击为False 】
        :param feature: 被判断元素的特征
        :return: 返回一个表示当前状态的布尔值
        """
        ele = self.find_element( feature )
        print( type(ele.text),'----',ele.get_attribute("enabled") )
        if ele.get_attribute( "enabled" )== "true":
            # 当前状态为 true 返回 True 表示当前按钮可点击
            return True
        else:
            return False

