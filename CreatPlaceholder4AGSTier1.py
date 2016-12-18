import os,shutil
renamelist=open('C:\\Python27\\rename_AGS_Tier1.txt')

targetname=renamelist.readlines()
for p in targetname:
	p=p.strip()
	shutil.copy(os.path.join('D:\\AGS_Tier1',"sample.xlsx"),os.path.join('D:\\AGS_Tier1\\TobeSignedoff'))
	os.rename(os.path.join('D:\\AGS_Tier1\\TobeSignedoff',"sample.xlsx"),os.path.join('D:\\AGS_Tier1\\TobeSignedoff',p))

renamelist.close()
