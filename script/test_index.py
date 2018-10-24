# -*- coding=utf-8 -*-
import time
from base import initDriver
from page import Page
import pytest
pytestmark = pytest.mark.skip( "跳过测试" )


class TestDemo:

    def setup(self):
        self.driver = initDriver()
        self.page = Page(self.driver)

    def test_enterHome(self):
        time.sleep(3)
        self.page.initIndexPage.enterHome()
