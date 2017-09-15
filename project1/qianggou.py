# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
DesiredCapabilities.INTERNETEXPLORER["ignoreProtectedModeSettings"] = True


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.implicitly_wait(2)
    driver.get('https://i.umeng.com/loginframe?app_id=cnzz&redirectURL=https%3A%2F%2Fweb.umeng.com%2Fmain.php%3Fc%3Dsite%26a%3Dshow%26from%3Dlogin')
    login1 = driver.find_element_by_xpath(".//*[@id='ump']/div/form/div[1]/ul/li[1]/div/label/input")
    login1.send_keys('wangkai@forfarming.com')
    login2 = driver.find_element_by_xpath(".//*[@id='ump']/div/form/div[1]/ul/li[2]/label/input")
    login2.send_keys('fn@123456')
    login3 = driver.find_element_by_xpath(".//*[@id='submitForm']")
    login3.click()
    #login1.click()#
    #time.sleep(3)
    #login2 = driver.find_element_by_id('app').is_selected()
    #print login2
    #login3 = driver.find_element_by_id('TPL_password_1')
    #login3.send_keys('x19851028')
    #driver.find_element_by_xpath(".//*[@id='J_SubmitStatic']").click()