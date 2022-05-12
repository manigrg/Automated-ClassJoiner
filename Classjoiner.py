from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import secret
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

email = secret.email
passwd = secret.password

subject = input('Enter the class you wish to join in?')


path = os.path.join(os.getcwd(),"geckodriver.exe")
options = Options()
options.set_preference('permissions.default.microphone', 1)
options.set_preference('permissions.default.camera', 1)

url = "https://classroom.google.com/u/0/"
dismissalertpath ='/html/body/div/div[3]/div/div[2]/div[3]/div/span/span'
emailpath = '//*[@id="identifierId"]'
buttonxpath = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span'
passwordXpath = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input'
passwordbuttonxpath = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button'

meetbutton ='/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span'
xpath3 = '/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span'

nepali = '/html/body/div[2]/div[1]/div[6]/div/ol/li[4]/div[1]/div[3]/h2/a[1]'
nepali_btn = '/html/body/div[2]/div[2]/div[5]/div[2]/aside/div/div[1]/div/div[2]/div/a'
joinep= '/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span'

comp = '/html/body/div[2]/div/div[6]/div/ol/li[9]/div[1]/div[3]/h2/a[1]/div[1]'
comp_btn = '/html/body/div[2]/div[2]/div[5]/div[2]/aside/div/div[1]/div/div[2]/div/a'
compjoin = '/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span'

pro = '/html/body/div[2]/div[1]/div[6]/div/ol/li[10]/div[1]/div[3]/h2/a[1]/div[1]'
pro_btn = '/html/body/div[2]/div[3]/div[5]/div[2]/aside/div/div[1]/div/div[2]/div/a'
projoin = '/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span'




def __cow__(email, passwd, sub, joinbtn, injoin):
    web = webdriver.Firefox(executable_path=path, options=options)
    web.get(url)
    time.sleep(4)
    wait = WebDriverWait(web, 10)
    emailputting = web.find_element_by_xpath(emailpath)
    buttonclicking = web.find_element_by_xpath(buttonxpath)
    emailputting.send_keys(email)
    buttonclicking.click()
    time.sleep(4)

    password_but = web.find_element_by_xpath(passwordbuttonxpath)
    passthis = web.find_element_by_xpath(passwordXpath)
    passthis.send_keys(passwd)
    password_but.click()
    time.sleep(7)

    classroom = web.find_element_by_xpath(sub)
    classroom.click()
    time.sleep(5)
    # meet = web.find_element_by_xpath(joinbtn)
    # meet.click()
    # time.sleep(3)

    ancor_tag = wait.until(EC.visibility_of_element_located((By.XPATH, joinbtn)))
    link = ancor_tag.get_attribute('href')
    web.get(link)
    join_button1 = wait.until(EC.visibility_of_element_located((By.XPATH, injoin)))
    join_button1.click()


if subject == "nepali":
    __cow__(email, passwd, nepali, nepali_btn, joinep)

elif subject == "comp":
    __cow__(email, passwd, comp, comp_btn, compjoin)

if subject == "pro":
    __cow__(email, passwd, pro, pro_btn, projoin)

else:
    print('error')

