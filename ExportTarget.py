#! python2.7
#see video https://www.udemy.com/automate/learn/v4/t/lecture/3470590
#https://www.udemy.com/automate/learn/v4/t/lecture/3470614


from selenium import webdriver
import urllib
import re
import sys

# usage: Ctrl+R then input ExportTarget 534666
sys.argv
if len(sys.argv) > 1:
    userinputID=sys.argv[1]
else:
    print("Ctrl+R then input ExportTarget <000000>")
#open by projectID



browser = webdriver.Firefox()
baseURL="http://worldserver9.amazon.com/ws/assignments_tasks?&token=1416441266&project="
projectID=userinputID
url=baseURL+projectID
browser.get(url)

#login
username=browser.find_element_by_id('username')
username.send_keys('sujudy')

password=browser.find_element_by_id('password')
password.send_keys('lina88*)')

login=browser.find_element_by_id('loginButton')
login.click()

#click View Full asset paths check box
checkbox=browser.find_element_by_name('viewFullPathMode')
if not checkbox.is_selected():
    checkbox.click()
#---print(checkbox.is_selected())

asset=browser.find_element_by_partial_link_text('samples')
filepath=asset.text
#---print(asset.text)

#regular experssion to match the taget file download path
assetRegex=re.compile(r'''
#/samples/tam - soafba/Projects/534956_Paramount_2 Workflows_Aug 4_Blurbs_DE/Source-English/Product Identifiers_blurbs_US_clean for translation.xml../Target-German/Product Identifiers_blurbs_US_clean for translation.xml
#samples
#client name
#projects group number project name

/samples/.*?/\d{6}.*?/

''', re.VERBOSE)

foldernameRegex=re.compile(r'''
/\d{6}.*?/
''', re.VERBOSE)
foldername=foldernameRegex.findall(asset.text)

foldernamestr=''.join(foldername) #convert list to string
foldernamestr=foldernamestr.strip('/')
print(foldernamestr)

PartialDownloadPath = assetRegex.findall(asset.text)
#convert list to string
PartialDownloadPathStr=''.join(PartialDownloadPath)
#print(PartialDownloadPathStr)
#partialdownloadURL

str1=PartialDownloadPathStr.replace("/","%2F")
str2=str1.replace("(","%28")
str3=str2.replace(")","%29")
str4=str3.replace(" ","+")
str5=str4.replace("%2FProjects%2F","%2FProjects&aisSP=%2F")

#str5 is that path format required by WS
downloadURL="http://worldserver9.amazon.com/ws/download_assets?&aisCF="+str5+"&token=937829789"
print(downloadURL)

#open project group download page by webdriver
browser.get(downloadURL)

#login again:
login()
#click download button
downloadButton=browser.find_element_by_id('__wsDialog_button_download')
downloadButton.click()
time.sleep(3)

#press Save file and OK on the pop up window
pyautogui.hotkey('alt', 's')
time.sleep(1)
pyautogui.press('enter')
time.sleep(2)
#unzip the download file to C:\7z\unzip
os.system(r"C:\7z\7z e C:\Users\sujudy\Downloads\assets.zip -oC:\7z\unzip -spf -aos")
browser.quit()

#rename the folder from project groupID to projectID
if os.path.exists(os.path.join('C:\\7z\\unzip',foldernamestr)):
    #print("Folder found, rename it.")
    newname1=projectID+' of '+foldernamestr
    os.rename(os.path.join('C:\\7z\\unzip',foldernamestr),os.path.join('C:\\7z\\unzip',newname1))





