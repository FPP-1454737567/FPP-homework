# @Time : 2020/12/27 
# @Author : FPP
import logging
import time

import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from test_frame.black_handle import black_wrapper

logging.basicConfig(level=logging.INFO)


class BasePage:
    # FIND = 'find'
    # ACTION = 'action'
    # FIND_AND_CLICK = 'find_and_click'
    # SEND = 'send'
    # CONTENT = 'content'
    """
    :WebDriver  注解,声明类型
    """

    def __init__(self, driver: WebDriver = None):
        self.driver = driver
        self.black_list = [(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]

    # 设计模式，代理模式，装饰器模式
    # 装饰器
    @black_wrapper
    def find(self, by, locator):
        # 截图每个定位的元素
        self.screenshot('../' + str(time.time()) + ".png")
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def find_and_click(self, by, locator):
        return self.find(by, locator).click()

    def find_and_send(self, by, locator, text):
        return self.find(by, locator).send_keys(text)

    def scroll_find(self, text):
        return self.driver.find_element(MobileBy.
                                        ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                             'scrollable(true).instance(0)).'
                                                             'scrollIntoView(new UiSelector().'
                                                             f'text("{text}").instance(0));')

    def scroll_find_click(self, text):
        return self.scroll_find(text).click()

    def wait_for(self, by, locator):
        def wait_for_ele(driver):
            ele = driver.find_elements(by, locator)
            return len(ele) > 0

        WebDriverWait(self.driver, 10).until(wait_for_ele)

    def swip_find(self, by, locator):
        self.driver.implicitly_wait(1)
        # 找到所有元素
        eles = self.driver.find_elements(by, locator)
        # 不停滑动，直到找到为止
        while len(eles) == 0:
            # 滑动
            self.driver.swipe(0, 600, 0, 400)
            eles = self.driver.find_elements(by, locator)
        self.driver.implicitly_wait(5)
        return eles[0]

    def load(self, yaml_path):
        # yaml文件的读方法
        with open(yaml_path, encoding="utf-8") as f:
            data = yaml.load(f)
            for step in data:
                # find = step[0]
                # action = step[1]
                # content = step[2]
                # 注意yaml的用法，对于里面的字典取值
                find = step.get("find")
                action = step.get("action")
                content = step.get("content")
                logging.info(f"find 的值是：{find}, action的只是：{action}, content的值是：{content}")
                if action == 'find_and_click':
                    self.find_and_click(MobileBy.XPATH, find)
                elif action == 'find_and_send':
                    self.find_and_send(MobileBy.XPATH, find, content)

    def screenshot(self, picture_path):
        self.driver.save_screenshot(picture_path)
