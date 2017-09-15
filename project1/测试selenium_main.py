# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
DesiredCapabilities.INTERNETEXPLORER["ignoreProtectedModeSettings"] = True


def login(name, password):
    login = driver.find_element_by_xpath(".//*[@id='top']/div/span[2]/a[1]")
    login.click()
    login1 = driver.find_element_by_xpath(".//*[@id='username']")
    login1.send_keys(name)
    login2 = driver.find_element_by_xpath(".//*[@id='password']")
    login2.send_keys(password)
    login3 = driver.find_element_by_xpath(".//*[@id='code']")
    login3.send_keys("1234")
    login4 = driver.find_element_by_xpath(".//*[@id='normal_form']/div/input[1]")
    login4.click()
    
if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get('http://192.168.6.29:9090')#
    login('13813388478' ,'123456')
    xelem = driver.find_element_by_name('keyword')  # 找到搜索框
    xelem.send_keys(u'东方月亮' + Keys.ENTER)  # 搜索seleniumhq
    b = driver.window_handles
    driver.switch_to.window(b[-1])
    driver.find_element_by_link_text("东方月亮").click()
    c = driver.current_window_handle
    e = driver.find_element_by_link_text("东方月亮").get_attribute('href')
    driver.get(e)
    #body = driver.find_element_by_tag_name("body")
    #action = ActionChains(driver)
    #action.key_down(Keys.CONTROL).send_keys('w').perform()
    # driver.get("http://192.168.6.29:9090/goods_565.htm")

    print b ,c ,driver.current_url
    driver.switch_to.window(b[-1])
    a1 = driver.find_element_by_link_text(u"加入购物车")
    a1.click()
    a2 = driver.find_element_by_id("car")
    a2.click()
    a3 = driver.find_element_by_link_text(u"进入购物车")
    a3.click()
    print b ,c ,driver.current_url
    a4 = driver.find_element_by_xpath(".//*[@id='cart_form']/div[1]/table/tbody/tr[1]/th[1]/span/label/span")
    a4.click()
    a5 = driver.find_element_by_xpath(".//*[@id='shopping_operate']/span[1]/a")
    a5.click()
    print b ,c ,driver.current_url
    a4 = driver.find_element_by_xpath(".//*[@id='cart_form']/div[1]/table/tbody/tr[1]/th[1]/span/label/span")
    a4.click()
    a5 = driver.find_element_by_xpath(".//*[@id='shopping_operate']/span[1]/a")
    a5.click()
    print b ,c ,driver.current_url
    a6 = driver.find_element_by_xpath(".//*[@id='order_save']")
    a6.click()
    a7 = driver.find_element_by_xpath(".//*[@id='theForm']/div/div[2]/div/ul[2]/li[1]")
    a7.click()
    a8 = driver.find_element_by_name('pay_password')
    a8.click()
    a8.send_keys("123456")
    a9 = driver.find_element_by_xpath(".//*[@id='theForm']/div/div[3]/input[1]")
    a9.click()
    body = driver.find_element_by_tag_name("body")
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL).send_keys('w').perform()
    driver.get("http://192.168.6.29:9090/order_pay.htm")
    print driver.window_handles ,driver.current_window_handle ,driver.current_url
    driver.switch_to.window(driver.window_handles[-2])
    a10 = driver.find_element_by_xpath(".//*[@id='pay_msg']")
    a10.click()
    a10.send_keys("hehehe")
    a11 = driver.find_element_by_xpath(".//*[@id='submit_button']")
    a11.click()
