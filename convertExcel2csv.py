#convert xlsx to csv
#http://stackoverflow.com/questions/20105118/convert-xlsx-to-csv-correctly-using-python
import xlrd
import csv, os
def E2c(targetXlsx):
    wb=xlrd.open_workbook(targetXlsx)
    targetCSV=targetXlsx+'.csv'
    sh = wb.sheet_by_name('Sheet')
    your_csv_file=open(targetCSV, 'wb')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
    for rownum in xrange(sh.nrows):
        wr.writerow([unicode(s).encode("utf-8") for s in sh.row_values(rownum)])
    your_csv_file.close()

PJlist=open('C:\\Python27\\convertExcel2csv.txt')
projectXlsx=PJlist.readlines()
for p in projectXlsx:
    p=p.strip()
    E2c(p)

PJlist.close()
