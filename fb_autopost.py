# import numpy as np
import getpass
from selenium import webdriver
import sys,pyautogui, time
import os
from pathlib import Path
from selenium.webdriver.chrome.options import Options

option=browser=""
# Define the URL's we will open and a few other variables 
main_url = 'https://www.facebook.com' # URL A
# target_url="https://www.facebook.com/groups/pythoncodingprogrammingselfinstructionhub/"

chromedriver = "/usr/local/lib/node_modules/webdriver-manager/selenium/chromedriver_77.0.3865.40"

def banner():
    print("\n\n")
    print('######## ########             ###    ##     ## ########  #######  ########   #######   ######  ######## ')
    print('##       ##     ##           ## ##   ##     ##    ##    ##     ## ##     ## ##     ## ##    ##    ##    ')
    print('##       ##     ##          ##   ##  ##     ##    ##    ##     ## ##     ## ##     ## ##          ##    ')
    print('######   ########          ##     ## ##     ##    ##    ##     ## ########  ##     ##  ######     ##    ')
    print('##       ##     ##         ######### ##     ##    ##    ##     ## ##        ##     ##       ##    ##    ')
    print('##       ##     ##         ##     ## ##     ##    ##    ##     ## ##        ##     ## ##    ##    ##    ')
    print('##       ########  ####### ##     ##  #######     ##     #######  ##         #######   ######     ##    ')
    print("\n\n")


def initsel(user,p,filename,caption,target_url):
    #####################configurations#############################
    option = Options()
    option.add_argument("--disable-infobars")
    # option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")
    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option("prefs", { \
        "profile.default_content_setting_values.media_stream_mic": 1, 
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 1, 
        "profile.default_content_setting_values.notifications": 1 
    })

    # Open main window with URL A
    browser= webdriver.Chrome(chrome_options=option, executable_path=chromedriver)
    browser.maximize_window()
    login(browser,user,p,filename,caption,target_url)
    #####################configurations#############################




def login(browser,user,p,filename,caption,target_url):
    # login
    browser.get(main_url)
    browser.execute_script("document.getElementById('email').setAttribute('type','password')")
    email=browser.find_element_by_id('email')
    password=browser.find_element_by_id('pass')
    email.send_keys(user)
    password.send_keys(p)
    login=browser.find_element_by_xpath("//label[@id='loginbutton']/input[1]")
    login.click()
    time.sleep(1)
    browser.get(target_url)
    time.sleep(1)
    post(browser,filename,caption)
    # login ends

def addtab(c,f):
    time.sleep(1)
    for i in range(0,c):
        pyautogui.press('tab')
    if f==1:
        pyautogui.press('enter')

def typewrite(filename,cf,e):
    time.sleep(1)
    if cf==1:
        pyautogui.hotkey('ctrl','f')
        pyautogui.typewrite(filename,interval=0.15)
    else:
        pyautogui.typewrite(filename,interval=0.15)
    if e==1:
        pyautogui.press("enter")

def mousemove(x,y):
    currentx,currenty=pyautogui.position()
    newx=x-currentx
    newy=y-currenty
    pyautogui.moveRel(newx,newy)
    


def checkpost(browser):
    post=browser.find_element_by_class_name("_1mf7 _4jy0 _4jy3 _4jy1 _51sy selected _42ft")
    post.click()

def post(browser,filename,caption):
    # addmedia
    if len(filename)>0:
        media=browser.find_element_by_xpath("//a[@attachmentid='MEDIA']/span[1]/span[1]")
        media.click()
        addtab(3,1)
        filepath=filename.split('/')
        for path in filepath:
            typewrite(path,1,1)
        # typewrite(filename,1,1)
        addtab(6,0)
        typewrite(caption,0,0)
    else:
        post=browser.find_element_by_xpath("//a[@label='Write post']/span[1]/span[1]")
        post.click()
        addtab(5,0)
        typewrite(caption,0,0)

    browser.execute_script("window.scrollBy(0,100)")
    time.sleep(5)
    buttons = browser.find_elements_by_tag_name('button')
    time.sleep(5)
    for button in buttons:
        if button.get_attribute('data-testid') == 'react-composer-post-button':
            button.click()
    time.sleep(5)
    exit()
    # anchor=browser.find_element_by_xpath("//a[@aria-labelledby='userNavigationLabel']")
    # anchor.click()
    # logout = browser.find_element_by_xpath("//ul[@role='menu']/li[last()]")
    # logout.click()
    
def attachfile():
    hasfile=input("Want to attach file? (y/n) : ")
    if hasfile.lower()=="y":
        filename=input("File Name to upload: ")
        return filename
    elif hasfile.lower()=="n":
        filename=""
        return filename
    else:
        attachfile()


def getpara():
    user=getpass.getpass(prompt="Facebook Username : ")
    p = getpass.getpass(prompt='Facebook Password? : ')
    filename=attachfile()
    caption=input("Caption for the post: ")
    target_url=input("Group or Page URL: ")
    initsel(user,p,filename,caption,target_url)

banner()
getpara()
time.sleep(30)

