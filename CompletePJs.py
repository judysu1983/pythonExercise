#see a video about how to open new tab instead of open too many filefox window
#https://www.youtube.com/watch?v=AH-q_X3Fktk
    #browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
    #browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.PAGE_UP)

#complete WS project by projectID
#open project by projectID
# need to edit and add project IDs to C:\\Python27\\CompletePJs_list.txt file

import webbrowser, sys, pyperclip, time, pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

def completeproject(ID):
    browser = webdriver.Firefox()

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
    #check if the tasks are in Review step and only complete the task in Reivew step

    try:
        reviewlink=browser.find_element_by_link_text('Review')

        checkbox=browser.find_element_by_name('checkAllBox')
        if not checkbox.is_selected():
            checkbox.click()
        # find complete button    
        CompleteButton=browser.find_element_by_css_selector('body > form:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(18) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(9) > a:nth-child(1)')
        CompleteButton.click()
        time.sleep(1)
        #click the OK button without choosing TM to update
        pyautogui.click(72,552)
        time.sleep(2)
            
    except NoSuchElementException, e:
        print('Project '+ID+' Tasks are not in Review step')
        browser.quit()
    
   
PJlist=open('C:\\Python27\\CompletePJs_list.txt')
projectIDs=PJlist.readlines()
for p in projectIDs:
    p=p.strip()
    completeproject(p)
    




