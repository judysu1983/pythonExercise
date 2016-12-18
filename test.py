import csv
with open('D:\\test\\626027EN-PTBR_MT_Pilot_scope_info_pt_BR.csv','r') as f:
    r=csv.reader(f,delimiter=',')
    for row in r:
        if row[1] ==' Total':
            print(row[1]+','+row[2]+','+row[8])
