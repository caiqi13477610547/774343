from time import sleep
import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
class TestContact:
    def setup(self):
        desired_caps = {}
        # 字典追加启动参数
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "6.0"
        desired_caps["deviceName"] = "192.168.95.101:5555"
        desired_caps["appPackage"] = "com.android.contacts"
        desired_caps["appActivity"] = ".activities.PeopleActivity"
        # 设置中文
        desired_caps["unicodeKeyboard"] = True
        desired_caps["resetKeyboard"] = True
        # 获取driver
        sleep(3)
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    def teardown(self):
        sleep(3)
        self.driver.quit()
    @pytest.mark.parametrize(("name","phone"),[("蔡奇","13477610547"),("蔡伟","13477610548")])
    def test_add_contact(self,name,phone):
        self.driver.find_element_by_id("com.android.contacts:id/floating_action_button").click()
        self.driver.find_element_by_xpath("//*[@text='本地保存']").click()
        self.driver.find_element_by_xpath("//*[@text='姓名']").send_keys(name)
        self.driver.find_element_by_xpath("//*[@text='电话']").send_keys(phone)
        sleep(3)
    # def test_add_contact01(self):
    #     self.driver.find_element_by_id("com.android.contacts:id/floating_action_button").click()
    #     self.driver.find_element_by_xpath("//*[@text='本地保存']").click()
    #     self.driver.find_element_by_xpath("//*[@text='姓名']").send_keys("蔡伟")
    #     sleep(3)
if __name__ == '__main__':
    pytest.main(["-s", "test_login.py"])
















