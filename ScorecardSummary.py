#https://www.udemy.com/automate/learn/v4/t/lecture/3470618?start=90
import openpyxl
import os
os.chdir('D:\\SEDIT-3677')
def getsummary(targetXlsx): 
    workbook = openpyxl.load_workbook(targetXlsx, data_only=True)
    summary= workbook.get_sheet_by_name('Summary')

    strprojectID=str(summary['B2'].value)
    strlocale=str(summary['B6'].value)
    strEvaluatedWordCount=str(summary['E6'].value)
    strLQM=str(summary['B18'].value)
    strLQAScore=str(summary['H54'].value)
    strLQAGrade=str(summary['G56'].value)

    #print(projectID.value+'\t'+locale.value+'\t'+EvaluatedWordCount.value+'\t'+LQM.value+'\t'+LQAGrade.value)
    print(strprojectID+'\t'+strlocale+'\t'+strLQAGrade+'\t'+strLQAScore+'\t'+strEvaluatedWordCount+'\t'+strLQM)

Projectlist=open('C:\\Python27\\ScorecardSummary.list')
projectXlsx=Projectlist.readlines()
for p in projectXlsx:
    p=p.strip()
    getsummary(p)

Projectlist.close()
