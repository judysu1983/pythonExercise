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

def Reviewcheck(ID):
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
        print(ID+'\t Ready for Review')
        browser.quit()


            
    except NoSuchElementException, e:
        print('pass')
        browser.quit()
    
   
PJlist=open('C:\\Python27\\CheckifInReviewstep.txt')
projectIDs=PJlist.readlines()
for p in projectIDs:
    p=p.strip()
    Reviewcheck(p)
    




