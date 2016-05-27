# -*- encoding: utf-8 -*
from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()

browser.get('http://127.0.0.1:5000')
assert 'SToHTM' in browser.title

# login
user = browser.find_element_by_id('inputEmail')
password = browser.find_element_by_id('inputPassword')
user.send_keys('gsinovsky@gmail.com')
password.send_keys('123456')
sleep(2)
browser.find_element_by_xpath(
    "/html/body/div[2]/div/div/div/div/center[2]/div/div/button").click()
sleep(5)

# go to users
browser.find_element_by_xpath("(//a[contains(text(),'Usuarios')])").click()
sleep(4)
browser.find_element_by_xpath('//*[@id="navbar"]/ul/li[2]/a').click()
sleep(3)

# invalid user
user = browser.find_element_by_id('inputEmail')
user.send_keys('gsinovsky@gmail.com')
password = browser.find_element_by_id('inputPassword')
password.send_keys('abcdef')
sleep(2)
browser.find_element_by_xpath(
    "/html/body/div[2]/div/div/div/div/center[2]/div/div/button").click()
sleep(5)

user.clear()
user.send_keys('adam@gmail.com')
password.clear()
password.send_keys('123456')
sleep(2)
browser.find_element_by_xpath(
    "/html/body/div[2]/div/div/div/div/center[2]/div/div/button").click()
sleep(5)
