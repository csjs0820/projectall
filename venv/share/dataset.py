import openpyxl #패키지 불러오기
import numpy as np
from random import *
filename = "flex_value2.xlsx" #파일명
book = openpyxl.load_workbook(filename) #엑셀파일 book 변수에 저장
sheet=book.worksheets[0]
datasety = []
data = [] #리스트 자료형 생성
for row in sheet.rows: #전체 행에 대하여 반복실행
    data.append(row[0].value)  # 1열 데이터)
    if row[0].value > 200:
        datasety.append(1)
    else:
        datasety.append(0)

number = int(len(data)/5)
datasetx = np.reshape(data,(number,5))
datasety = np.reshape(datasety,(number,5))

testsetx = []
testsety = []

for i in range(0,500):
    testsetx.append(randint(100,350))
    if testsetx[i] >200:
        testsety.append(1)
    else:
        testsety.append(0)
testsetx = np.reshape(testsetx,(100,5))
testsety = np.reshape(testsety,(100,5))
print(testsetx)
print(testsety)