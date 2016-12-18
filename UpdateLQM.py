#https://www.udemy.com/automate/learn/v4/t/lecture/3470618?start=90
import openpyxl
import os
os.chdir('D:\\SEDIT-3677')
def getsummary(targetXlsx): 
    workbook = openpyxl.load_workbook(targetXlsx)
    summary= workbook.get_sheet_by_name('Summary')

    summary['B18']='=1-(Minor_Error*2+E18+E19*0.5)/E6'
    workbook.save(targetXlsx)

Projectlist=open('C:\\Python27\\UpdateLQM.txt')
projectXlsx=Projectlist.readlines()
for p in projectXlsx:
    p=p.strip()
    getsummary(p)

Projectlist.close()
