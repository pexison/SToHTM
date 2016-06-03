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
browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/center/div[2]/div/button').click()
sleep(3)

# go to users
browser.find_element_by_xpath("(//a[contains(text(),'Usuarios')])").click()
sleep(3)

# Modify role
browser.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div/div[2]/center/div/table/tbody/tr[4]/td[1]').click()
sleep(2)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
sleep(3)
browser.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div/div[2]/div/div/div[2]/label/input').click()
browser.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div/div[2]/div/div/div[3]/label/input').click()
sleep(2)
browser.find_element_by_id("saveButton").click()
sleep(4)

browser.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div/div[2]/center/div/table/tbody/tr[4]/td[1]').click()
sleep(2)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")

sleep(2)
browser.find_element_by_xpath("(//a[contains(text(),'Usuarios')])").click()