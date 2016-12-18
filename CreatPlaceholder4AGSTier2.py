import os,shutil
renamelist=open('C:\\Python27\\rename_AGSTier2.txt')

targetname=renamelist.readlines()
for p in targetname:
	p=p.strip()
	if not os.path.exists(os.path.join('C:\\temp\\SEDIT-3677',p)):
                os.makedirs(os.path.join('C:\\temp\\SEDIT-3677',p))
	#shutil.copy(os.path.join('C:\\temp\\SEDIT-3677',"sample.xlsx"),os.path.join('C:\\temp\\SEDIT-3677',p))
	#os.rename(os.path.join('D:\\Q3_Blurb\\BlukPublishing\\ToBePublish',"sample.csv"),os.path.join('D:\\Q3_Blurb\\BlukPublishing\\ToBePublish',p))

renamelist.close()
