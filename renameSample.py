import os,shutil
renamelist=open('C:\\Python27\\rename_Q3_blurbs.txt')

targetname=renamelist.readlines()
for p in targetname:
	p=p.strip()
	shutil.copy(os.path.join('D:\\Q3_Blurb\\BlukPublishing',"sample.csv"),os.path.join('D:\\Q3_Blurb\\BlukPublishing\\ToBePublish'))
	os.rename(os.path.join('D:\\Q3_Blurb\\BlukPublishing\\ToBePublish',"sample.csv"),os.path.join('D:\\Q3_Blurb\\BlukPublishing\\ToBePublish',p))

renamelist.close()
