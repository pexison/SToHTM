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
sleep(2)

# go to users
browser.find_element_by_xpath("(//a[contains(text(),'Usuarios')])").click()
sleep(3)

# create user
email = browser.find_element_by_id('email')
email.send_keys('analist@gmail.com')
sleep(1)
name = browser.find_element_by_id('name')
name.send_keys('Roger Bayes')
sleep(1)
password = browser.find_element_by_id('password')
password.send_keys('123456')
sleep(1)
password2 = browser.find_element_by_id('password2')
password2.send_keys('123456')
sleep(1)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight/3);")
sleep(2)

# Add analist role
browser.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/div/div[1]/div/div/div[2]/label").click()
sleep(2)
browser.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/div/div[1]/div/div/div[3]/label").click()
sleep(2)
browser.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/div/div[1]/div/div/div[5]/label").click()
sleep(2)
browser.find_element_by_id("saveButton").click()
sleep(3)

# Logout
browser.find_element_by_xpath("(//a[contains(text(),'Salir')])").click()
sleep(2)

# Login with analist user
user = browser.find_element_by_id('inputEmail')
password = browser.find_element_by_id('inputPassword')
user.send_keys('analist@gmail.com')
password.send_keys('123456')
sleep(2)
browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/center/div[2]/div/button').click()
sleep(2)

# Go to categories
browser.find_element_by_xpath("(//a[contains(text(),'Categorias')])").click()

browser.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
sleep(2)
#categoryName = browser.find_element_by_xpath("//*[@id='name']")
#categoryName.send_keys('Software')
#sleep(2)
#browser.find_element_by_xpath("//*[@id='saveButton']").click()



