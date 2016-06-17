# -*- encoding: utf-8 -*
from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()

browser.get('http://127.0.0.1:5000')
assert 'SToHTM' in browser.title

# login

sleep(6)

user = browser.find_element_by_id('inputEmail')
password = browser.find_element_by_id('inputPassword')
user.send_keys('gsinovsky@gmail.com')
password.send_keys('123456')
sleep(2)
browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/center/div[2]/div/button').click()
sleep(2)

# go to users
browser.find_element_by_xpath("(//a[contains(text(),'Usuarios')])").click()
sleep(3)

# create user
email = browser.find_element_by_id('email')
email.send_keys('client@gmail.com')
sleep(1)
name = browser.find_element_by_id('name')
name.send_keys('Yolanda Moreno')
sleep(1)
password = browser.find_element_by_id('password')
password.send_keys('123456')
sleep(1)
password2 = browser.find_element_by_id('password2')
password2.send_keys('123456')
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight/3);")
sleep(2)

# Add client role
browser.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/div/div[1]/div/div/div[2]/label").click()
sleep(2)
browser.find_element_by_id("saveButton").click()
sleep(3)

# Logout
browser.find_element_by_xpath("(//a[contains(text(),'Salir')])").click()
sleep(2)

# Login with client user
user = browser.find_element_by_id('inputEmail')
password = browser.find_element_by_id('inputPassword')
user.send_keys('client@gmail.com')
password.send_keys('123456')
sleep(2)
browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/center/div[2]/div/button').click()
sleep(2)

# Go to services
browser.find_element_by_xpath("(//a[contains(text(),'Servicios')])").click()

service = browser.find_element_by_id("name")
service.send_keys("Reparacion de lavadora")
sleep(2)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(2)
browser.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/div/div/div/div/div[2]/div/div/ul/li[3]/i[1]").click()
sleep(2)
browser.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/div/div/div/div/div[2]/div/div/ul/li[3]/div/ul/li[1]/span").click()
sleep(2)
browser.find_element_by_id("saveButton").click()
sleep(2)

service = browser.find_element_by_id("name")
service.send_keys("Revision del compresor")
sleep(2)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(2)
browser.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/div/div/div/div/div[2]/div/div/ul/li[2]/i[1]").click()
sleep(2)
browser.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/div/div/div/div/div[2]/div/div/ul/li[2]/div/ul/li[2]/span").click()
sleep(2)
browser.find_element_by_id("saveButton").click()
sleep(3)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(2)
browser.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/div/div/div/table/tbody/tr[2]/td[3]/center/div").click()
sleep(2)

