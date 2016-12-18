from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import webbrowser, sys, pyperclip, time, pyautogui

def completeTranslationforMor(ID):
    
    browser=webdriver.Firefox()
    projecturl='http://worldserver9.amazon.com/ws/assignments_tasks?&token=1383336796&project='+ID
    browser.get(projecturl)
    #login
    login=open('C:\\Python27\\login.txt')
    loginname=login.readlines()
    name, pw=loginname
    name=name.strip()
    pw=pw.strip()
    login.close()   
    username=browser.find_element_by_id('username')
    username.send_keys(name)

    password=browser.find_element_by_id('password')
    password.send_keys(pw)

    login=browser.find_element_by_id('loginButton')
    login.click()
    time.sleep(1)
    #check if the tasks are in Translate step
    try:
        tanslateLink=browser.find_element_by_link_text('Translate')
        try:
            checkbox=browser.find_element_by_name('checkAllBox')
            if not checkbox.is_selected():
                checkbox.click()
            #unclaim the task from Moravia
            Unclaimbotton=browser.find_element_by_css_selector('body > form:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(17) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > a:nth-child(1)')
            Unclaimbotton.click()
            time.sleep(2)
            #click OK button to unclaim the task
            #from commnadline pyautogui.displayMousePosition()
            #if there's error for pyautogui see https://github.com/asweigart/pyautogui/issues/45
            pyautogui.click(72,305)
            time.sleep(2)
            # need to select all teh tasks again
            checkbox=browser.find_element_by_name('checkAllBox')
            if not checkbox.is_selected():
                checkbox.click()

            #find Complete button and click
            CompleteButton=browser.find_element_by_css_selector('body > form:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(17) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(9) > a:nth-child(1)')
            CompleteButton.click()
            time.sleep(1)
            pyautogui.click(77,552)
            time.sleep(1)

        except NoSuchElementException, e:
            print('test')
    except NoSuchElementException, e:
        print('Project '+ID +' is not in Translate step')
        browser.quit()

PJlist=open('C:\\Python27\\UncliamTasks.txt')
projectIDs=PJlist.readlines()
for p in projectIDs:
    p=p.strip()
    completeTranslationforMor(p)
