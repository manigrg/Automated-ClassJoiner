import os
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

import secret

ask = input('which class you want to join')

path = os.path.join(os.getcwd(),"geckodriver.exe")
option = Options()
option.set_preference('permissions.default.microphone', 1)
option.set_preference('permissions.default.camera', 1)

browser = webdriver.Firefox(executable_path=path, options=option)
# browser.get('https://www.google.com')
url = "https://classroom.google.com/u/0/h"
email = secret.email
password = secret.password

#Xpath
signin = '/html/body/div[1]/div[1]/div/div/div/div[2]/a'
#input
signinput = '//*[@id="identifierId"]'
signbtn = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span'
pwinput = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input'
pwbtn = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span'
#search

search = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
classroom = 'google classroom'
searchbtn = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]'
classpreview = '/html/body/div[7]/div/div[10]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a/h3'
#diff classrooms
comp = '/html/body/div[2]/div/div[6]/div/ol/li[9]/div[1]/div[3]/h2/a[1]/div[1]'
compbtn = '/html/body/div[2]/div[2]/div[5]/div[2]/aside/div/div[1]/div/div[2]/div/a'

math = '/html/body/div[2]/div[1]/div[6]/div/ol/li[3]/div[1]/div[3]/h2/a[1]/div[1]'
mathbtn = '/html/body/div[2]/div[2]/div[5]/div[2]/aside/div/div[1]/div/div[2]/div/a'

pro = '/html/body/div[2]/div[1]/div[6]/div/ol/li[10]/div[1]/div[3]/h2/a[1]/div[1]'
probtn = '/html/body/div[2]/div[3]/div[5]/div[2]/aside/div/div[1]/div/div[2]/div/a'

#joinbtn
join = '/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span'

def __stuff__(email, password, sub):
    browser.get(url)

    # sigin
    step1 = browser.find_element(By.XPATH, signin)
    step1.click()
    time.sleep(2)

    step2 = browser.find_element(By.XPATH, signinput)
    step2.send_keys(email)
    step3 = browser.find_element(By.XPATH, signbtn)
    step3.click()
    time.sleep(3)

    step3 = browser.find_element(By.XPATH, pwinput)
    step3.send_keys(password)
    step4 = browser.find_element(By.XPATH, pwbtn)
    step4.click()
    #####################

    step5 = browser.find_element(By.XPATH, search)
    step5.send_keys(classroom)
    time.sleep(3)
    step6 = browser.find_element(By.XPATH, searchbtn)
    step6.click()
    time.sleep(3)

    step7 = browser.find_element(By.XPATH, classpreview)
    step7.click()
    time.sleep(3)
    #######################

    step8 = browser.find_element(By.XPATH, sub)
    step8.click()
    time.sleep(3)
    #########################

    step9 = browser.find_element(By.XPATH, compbtn)
    step9.click()
    time.sleep(5)


    step10 = browser.find_element(By.XPATH, mathbtn)
    step10.click()
    time.sleep(3)

    step11 = browser.find_element(By.XPATH, join)
    step11.click()
    time.sleep(2)

if ask == 'comp':
    __stuff__(email, password, comp)

elif ask == 'math':
    __stuff__(email, password, math)

if ask == 'pro':
    __stuff__(email, password, pro)

else:
    print('error')