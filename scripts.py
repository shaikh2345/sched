# import pandas as pd
from tabulate import tabulate
# data = pd.read_excel('./Book1.xlsx')
# s = data.head()
# # print('hello')
# print(s)
# for line in  s:
#     print(line[] )
# from openpyxl import load_workbook

# wb = load_workbook("Book1.xlsx")
# sheet = wb.active

#reading cell
# print("First cell: ", sheet['A1'].value)
# print("Second cell: ", sheet['A6'].value)
from pandas import DataFrame
import pandas

def readExcel(name):
    filename = name
    df = pandas.read_excel(filename)
    return df

# print(df)
# ldf = list(df)
# print(ldf)
# dic = dict(df)
# numberLines = len(df.index)
# print(numberLines)
# i =0
# for i in range(numberLines):
#     for item in df:
#         print(df[item][i],end=" ")
#     print('\n')
        # print('info',i)
# print('\n')
# print(df)
# dic={}
# dic[0] = {'first':'hasan','last':'amjad'}


def createDic(data):
    dataSize = len(data.index)
    result =  dict()
    # line = 0
    for line in range(dataSize):
        result[line] = dict()
        for heading in data:
            result[line][heading] = data[heading][line] 
    return result
# for rr in d:
#     print(rr)
# print(tabulate(d))
def createNewExcelWithFreq(d,Freq,name):
    new = {'Name' : [], 'Address' : [], 'Amount':[]}
    for item in d:
        if d[item]['Frequency'] == Freq:
            for headings in new:
                new[headings].append(d[item][headings])
    o = pandas.DataFrame(new)
    o.to_excel(f'./{name}.xlsx')

def createNewExcelWithWeeks(d,name,week):
    new = {'Name' : [], 'Address' : [], 'Amount':[]}
    for item in d:
        weeks = str(d[item]['Week']).split(',')
        if str(week) in weeks:
            for headings in new:
                new[headings].append(d[item][headings])
    # print(new)
    # o = pandas.DataFrame(new)
    # o.to_(f'./{name}.txt')
    with open(f'{name}.txt', 'w') as f:
        print(tabulate(new), file=f)
        
def createNewFileForNewMonth(d,fileName,monthName):
    with open(f'{fileName}.txt','w') as f:
        print(f'ACCOUNTS FOR {monthName.upper()}', file=f)
        for week in range(1,5):
            print(f"--- Week # {week} ---",file=f)
            new = {'Name' : [], 'Address' : [], 'Amount':[]}
            for item in d:
                weeks = str(d[item]['Week']).split(',')
                if str(week) in weeks:
                    for headings in new:
                        new[headings].append(d[item][headings])
            print(tabulate(new), file=f)
