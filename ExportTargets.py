#! python2.7
#see video https://www.udemy.com/automate/learn/v4/t/lecture/3470590
#https://www.udemy.com/automate/learn/v4/t/lecture/3470614
#export target files by project ID,
#open the project and view full path to find the download path
#get the download URL by regular expression


from selenium import webdriver
import re
import sys
import pyautogui,time
import shutil
import os

#check if the download file with same name already exists and empty the unzip to folder
if os.path.exists("C:\\Users\\sujudy\\Downloads\\assets.zip"):
    os.remove("C:\\Users\\sujudy\\Downloads\\assets.zip")
if os.path.exists("C:\\7z\unzip"):
    shutil.rmtree("C:\\7z\unzip")

def exporttarget(projectID):
    if os.path.exists("C:\\Users\\sujudy\\Downloads\\assets.zip"):
        os.remove("C:\\Users\\sujudy\\Downloads\\assets.zip")
    browser = webdriver.Firefox()
    baseURL="http://worldserver9.amazon.com/ws/assignments_tasks?&token=1416441266&project="

    url=baseURL+projectID
    browser.get(url)

    #login
    def login():
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

    login()
    #click View Full asset paths check box
    checkbox=browser.find_element_by_name('viewFullPathMode')
    if not checkbox.is_selected():
        checkbox.click()
    #---print(checkbox.is_selected())

    asset=browser.find_element_by_partial_link_text('samples') #samples is the root folder name of ocelot projects
    filepath=asset.text
    #print(asset.text)

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
    foldernamestr=foldernamestr.split('/')
    downloadFolder=foldernamestr[1]
    #print(downloadFolder)
    
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
    print('Downloading '+projectID+'\n'+downloadURL+'\n')
    

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
    if os.path.exists(os.path.join('C:\\7z\\unzip',downloadFolder)):
        #print("Folder found, rename it.")
        newname1=projectID+'#'+downloadFolder
        os.rename(os.path.join('C:\\7z\\unzip',downloadFolder),os.path.join('C:\\7z\\unzip',newname1))

PJlist=open('C:\\Python27\\ExportTargets.txt')
projectIDs=PJlist.readlines()
for p in projectIDs:
    p=p.strip()
    exporttarget(p)

time.sleep(2)
PJlist.close()

#rename C:\7z\unzip to a folder wtih todays date as folder name
def renameoutput():
    basedir='c:\\7z'
    newname=time.strftime("%m_%d_%Y_")+time.strftime("%H%M%S")
    os.rename(os.path.join(basedir,"unzip"), os.path.join(basedir,'Dumped_at_'+ newname))

renameoutput()



