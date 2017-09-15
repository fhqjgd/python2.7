# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait

DesiredCapabilities.INTERNETEXPLORER["ignoreProtectedModeSettings"] = True

class go(object):

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(60)
        #self.name = name
        #self.password = password
        #self.goods = goods#

    def login(self ,name ,password):
        self.driver.get('http://192.168.6.29:9090')
        login = self.driver.find_element_by_xpath(".//*[@id='top']/div/span[2]/a[1]")
        login.click()
        login1 = self.driver.find_element_by_xpath(".//*[@id='username']")
        login1.send_keys(name)
        login2 = self.driver.find_element_by_xpath(".//*[@id='password']")
        login2.send_keys(password)
        
        login3 = self.driver.find_element_by_xpath(".//*[@id='code']")
        login3.send_keys("1234")
        login4 = self.driver.find_element_by_xpath(".//*[@id='normal_form']/div/input[1]")
        
        login4.click()
        

    def go_m (self ,goods):
        self.driver.implicitly_wait(10)
        xelem = self.driver.find_element_by_name('keyword')  # 找到搜索框
        xelem.send_keys(goods + Keys.ENTER)  # 搜索seleniumhq
        b = self.driver.window_handles
        self.driver.switch_to.window(b[-1])
        self.driver.find_element_by_link_text(goods).click()
        c = self.driver.current_window_handle
        self.driver.switch_to.window(b[-1])
        e = self.driver.find_element_by_link_text(goods).get_attribute('href')
        self.driver.get(e)
        print b, c, self.driver.current_url
        time.sleep(1)
        self.driver.switch_to.window(b[-1])
        a1 = self.driver.find_element_by_link_text(u"加入购物车")
        a1.click()
        a2 = self.driver.find_element_by_id("car")
        a2.click()
        a3 = self.driver.find_element_by_link_text(u"进入购物车")
        a3.click()
        print b, c, self.driver.current_url
        a4 = self.driver.find_element_by_xpath(".//*[@id='cart_form']/div[1]/table/tbody/tr[1]/th[1]/span/label/span")
        a4.click()
        a5 = self.driver.find_element_by_xpath(".//*[@id='shopping_operate']/span[1]/a")
        a5.click()
        print b, c, self.driver.current_url
        a4 = self.driver.find_element_by_xpath(".//*[@id='cart_form']/div[1]/table/tbody/tr[1]/th[1]/span/label/span")
        a4.click()
        a5 = self.driver.find_element_by_xpath(".//*[@id='shopping_operate']/span[1]/a")
        a5.click()
        print b, c, self.driver.current_url
        a6 = self.driver.find_element_by_xpath(".//*[@id='order_save']")
        a6.click()
        a7 = self.driver.find_element_by_xpath(".//*[@id='theForm']/div/div[2]/div/ul[2]/li[1]")
        a7.click()
        a8 = self.driver.find_element_by_name('pay_password')
        a8.click()
        a8.send_keys("123456")
        a9 = self.driver.find_element_by_xpath(".//*[@id='theForm']/div/div[3]/input[1]")
        a9.click()
        self.driver.get("http://192.168.6.29:9090/order_pay.htm")
        print self.driver.window_handles, self.driver.current_window_handle, self.driver.current_url
        self.driver.switch_to.window(self.driver.window_handles[-2])
        a10 = self.driver.find_element_by_xpath(".//*[@id='pay_msg']")
        a10.click()
        a10.send_keys("hehehe")
        a11 = self.driver.find_element_by_xpath(".//*[@id='submit_button']")
        a11.click()
        self.driver.quit()
        time.sleep(3)


if __name__ == '__main__':
        str = [u'东方明珠' ,u'东方月亮']
        for x in str:
                gogo = go()
                gogo.login(u'13813388478' ,'123456')
                gogo.go_m(x)
