#complete WS project by projectID

#open project by projectID
#e.g. http://worldserver9.amazon.com/ws/assignments_tasks?&token=55087026&project=524558
import webbrowser, sys, pyperclip
from selenium import webdriver


sys.argv #['CompletePJ.py', '543666' ]
#check if command line argument were passed
if len(sys.argv) > 1:
    # get project ID from command ['CompletePJ.py', '543666' ]
    ID = ' '.join(sys.argv[1:])
else:
    ID = pyperclip.paste()

#go to http://worldserver9.amazon.com/ws/assignments_tasks?&token=1383336796&project=548699
projecturl='http://worldserver9.amazon.com/ws/assignments_tasks?&token=1383336796&project='+ID
browser = webdriver.Firefox()
browser.get(projecturl)

#login
username=browser.find_element_by_id('username')
username.send_keys('sujudy')

password=browser.find_element_by_id('password')
password.send_keys('lina000)')

login=browser.find_element_by_id('loginButton')
login.click()

checkbox=browser.find_element_by_name('checkAllBox')
if not checkbox.is_selected():
    checkbox.click()
    
CompleteButton=browser.find_element_by_css_selector('body > form:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(17) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(9) > a:nth-child(1)')
CompleteButton.click()

