from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time, pyperclip
##def WSprojectIsComplete(ID):
browser = webdriver.Firefox()

projecturl='http://worldserver9.amazon.com/ws/assignments_projects?&token=1383336796'

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
time.sleep(5)


viewMode=Select(browser.find_element_by_name('viewMode'))
viewMode.select_by_visible_text('completed and canceled projects for my locales and workgroups')
#completed and canceled projects for my locales and workgroups
#maybe need to waite 30 seconds or more to load the query page
time.sleep(30)

    
bodyText=browser.page_source

PJlist=open('C:\\Python27\\CompleteCheckList.txt')
projectIDs=PJlist.readlines()
for p in projectIDs:
    p=p.strip()

    #get page source

    #see if project ID appear in page source
    if p in bodyText:
        print(p+' completed')
    else:
        print('\t'+p+ ' not completed')
    #assert p in bodyText, p+' not found'


