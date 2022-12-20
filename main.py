from scripts import *
import math

excel = readExcel('BROOKLYN.xlsx')
excelToDic = createDic(excel)
# createNewExcelWithFreq(excelToDic,'M','freqExcel')

# createNewExcelWithWeeks(excelToDic,'results',1)
# createNewExcelWithWeeks(excelToDic,'results',3)
# print(excelToDic)
createNewFileForNewMonth(excelToDic,'3_Week_DEC','DEC')
# createNewExcelWithFreq(excelToDic,'2W','hassanfile')


# name = input('What is your name?')
# print(f'My name is {name}')


# week = "" 
# weeks = str(week).split(',')
# print(weeks)

# num = 2
# n = (float(num))
# print(n)
# print(int(n))
