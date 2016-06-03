# -*- encoding: utf-8 -*
from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()

browser.get('http://127.0.0.1:5000')
assert 'SToHTM' in browser.title

user = browser.find_element_by_id('inputEmail')
password = browser.find_element_by_id('inputPassword')
user.send_keys('verdugoreinaldo@gmail.com')
password.send_keys('123456')
sleep(2)
browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/center/div[2]/div/button').click()
sleep(3)

browser.find_element_by_xpath("(//a[contains(text(),'Editar perfil')])").click()
sleep(2)
browser.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/div/div/center/form/div/div[1]/div[2]/div[1]/input").click()

age = browser.find_element_by_xpath('//*[@id="ageInput"]')
age.send_keys('23')
sleep(2)

vision = browser.find_element_by_xpath('//*[@id="visionInput"]')
vision.send_keys('Soy un ingeniero con la motivacion de emprender en el mundo laboral')
sleep(2)

browser.execute_script("window.scrollTo(0, document.body.scrollHeight/4);")
sleep(2)

abilities = browser.find_element_by_xpath('//*[@id="abilitiesInput"]')
abilities.send_keys('I can do stuff')
sleep(2)
skills = browser.find_element_by_xpath('//*[@id="skillsInput"]')
skills.send_keys('Sé hacer la vuelta canela. Y hago movil apps')
sleep(2)

browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(2)

browser.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div/div/center/form/div/button').click()
sleep(2)