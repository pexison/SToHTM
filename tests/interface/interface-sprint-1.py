# -*- encoding: utf-8 -*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div/center[2]/div/div/button").click()
sleep(4)
# go to users
browser.find_element_by_xpath("(//a[contains(text(),'Usuarios')])").click()
# create a new user
email = browser.find_element_by_id('email')
email.send_keys('test@gmail.com')
sleep(2)
name = browser.find_element_by_id('name')
name.send_keys('Carlos Roberto')
sleep(2)
browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/center/div[1]/div/div/div[3]/div/select/option[3]").click()
sleep(2)
password = browser.find_element_by_id('password')
password.send_keys('123456')
sleep(2)
password2 = browser.find_element_by_id('password2')
password2.send_keys('123456')
sleep(2)
browser.find_element_by_id('saveButton').click()
sleep(4)
# select user

browser.find_element_by_css_selector('tbody > tr:nth-child(3) > td:nth-child(1)').click()
name = browser.find_element_by_id('name')
name.clear()
name.send_keys('Julio Alberto')
sleep(2)
browser.find_element_by_id('saveButton').click()
sleep(4)
# delete created user
browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/center/div[2]/div/table/tbody/tr[3]/td[4]/center/div').click()
sleep(2)
