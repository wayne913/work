# coding=utf-8
from appium import webdriver
import appium
import time
import os
import re
import sys
import unittest

from test_work.KeyboardTest import Swipe


def open_test_view():
    global dr
    global t
    time = 3
    desired_caps = {'platformName': 'Android', 'platformVersion': '10', 'deviceName': '66J5T19604002706',
                    'appPackage': 'com.kikaoem.hw.qisiemoji.inputmethod',
                    'appActivity': 'com.qisi.ui.PrimaryActivity', 'noReset': 'false'}  # 1>获取手机信息--存储到字典中
    # android 版本
    # 设备名称 --adb
    # devices,#包名 --通过uiautomatorviewer获得.
    # Activity 名称
    # HTC:HT54DSV00048
    # Vivo1818:4c3a01bf
    # Vivo nex:f9adb3f3
    # 2>连接appium启动app,将手机信息导入;http://127.0.0.1:4723 是appium的地址和端口号，可在appium设置中查看。/wd/hub是appium规定的后缀，记住就好。。

    dr = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)




def run_home():

    dr.find_element_by_android_uiautomator('new UiSelector().text("主页")').click()
    dr.implicitly_wait(10)
    dr.find_element_by_android_uiautomator('new UiSelector().text("更多")').click()
    Swipe.Steps.swipe_up(t=1000, n=3)
    time.sleep(0.5)
    print("主页测试通过")

def run_theme():

    dr.find_element_by_android_uiautomator('new UiSelector().text("主题")').click()
    dr.implicitly_wait(10)
    dr.find_element_by_android_uiautomator('new UiSelector().text("更多")').click()
    Swipe.Steps.swipe_up(t=1000, n=3)
    time.sleep(0.5)
    print("主题测试通过")

if __name__ == "__main__":
    open_test_view()
    run_home()
    run_theme()
    print('Done.')


