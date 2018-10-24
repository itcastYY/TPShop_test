# -*- coding=utf-8 -*-
from page import indexPageAction
from page import myselfPageAction


class Page:

    def __init__(self,driver):
        self.driver = driver

    @property
    def initIndexPage(self):
        return indexPageAction(self.driver)

    @property
    def initMyselfPage(self):
        return myselfPageAction(self.driver)