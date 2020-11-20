from random import *
import numpy as np
import openpyxl
from common.util import shuffle_dataset

def loadData():
    # 1.훈련 데이터 만들기
    datasetx = np.zeros((120000,1)) #입력 데이터 24000*5개
    datasety = np.zeros((24000,7)) #출력 데이터 24000개
    temp = np.array((120000,1)) #입력 데이터가 저장될 임시 공간

    # 2.훈련 출력 데이터 만들기
    data_zero = np.ones((2000, 5))
    data_one = np.ones((2000, 5))
    data_two = np.ones((2000, 5))
    data_two2 = np.ones((2000, 5))
    data_three = np.zeros((2000, 5))
    data_three2 = np.zeros((2000, 5))
    data_four = np.zeros((2000, 5))
    data_five = np.zeros((2000, 5))

    for i in range(0,2000):
        data_one[i][1] = 0
        data_two[i][1] = 0
        data_two[i][2] = 0
        data_two2[i][0] = 0
        data_two2[i][1] = 0
        data_three[i][0] = 1
        data_three[i][4] = 1
        data_three2[i][3] = 1
        data_three2[i][4] = 1
        data_four[i][0] = 1

    data_zero = np.reshape(data_zero,(10000,1))
    data_one = np.reshape(data_one, (10000, 1))
    data_two = np.reshape(data_two, (10000, 1))
    data_two2 = np.reshape(data_two2, (10000, 1))
    data_three = np.reshape(data_three, (10000, 1))
    data_three2 = np.reshape(data_three2, (10000, 1))
    data_four = np.reshape(data_four, (10000, 1))
    data_five = np.reshape(data_five, (10000, 1))

    temp = np.concatenate([data_zero, data_one, data_two,data_two2, data_three, data_three2 ,data_four, data_five])

    for i in range(0,80000):
        if temp[i] == 1:
            datasetx[i] = randint(801,930)
        else:
            datasetx[i] = randint(700,800)

    for i in range(80000,120000):
        datasetx[i] = randint(700,930)

    datasetx = np.reshape(datasetx,(24000,5))

    for i in range(0,16000):
        if i <2000:
            datasety[i][0] = 1
        elif i <4000:
            datasety[i][1] = 1
        elif i <8000:
            datasety[i][2] = 1
        elif i <12000:
            datasety[i][3] = 1
        elif i <14000:
            datasety[i][4] = 1
        elif i < 16000:
            datasety[i][5] = 1

    for j in range(16000, 24000):
        k = 0
        if (datasetx[j][k] > 800) and (datasetx[j][k + 1] > 800) and datasetx[j][k + 2] >800 and datasetx[j][k + 3] > 800 and datasetx[j][k + 4] > 800:
            datasety[j][0] = 1
        elif (datasetx[j][k] > 800) and (datasetx[j][k + 1] <= 800) and datasetx[j][k + 2] > 800 and datasetx[j][k + 3] > 800 and \
                datasetx[j][k + 4] > 800:
            datasety[j][1] = 1
        elif (datasetx[j][k] > 800) and (datasetx[j][k + 1] <= 800) and datasetx[j][k + 2] <= 800 and datasetx[j][k + 3] > 800 and \
                datasetx[j][k + 4] > 800:
            datasety[j][2] = 1
        elif (datasetx[j][k] <= 800) and (datasetx[j][k + 1] <= 800) and datasetx[j][k + 2] > 800 and datasetx[j][k + 3] > 800 and \
                datasetx[j][k + 4] > 800:
            datasety[j][2] = 1
        elif (datasetx[j][k] > 800) and (datasetx[j][k + 1] <= 800) and datasetx[j][k + 2] <= 800 and datasetx[j][k + 3] <= 800 and \
                datasetx[j][k + 4] > 800:
            datasety[j][3] = 1
        elif (datasetx[j][k] <= 800) and (datasetx[j][k + 1] <= 800) and datasetx[j][k + 2] <= 800 and datasetx[j][k + 3] > 800 and \
                datasetx[j][k + 4] > 800:
            datasety[j][3] = 1
        elif (datasetx[j][k] > 800) and (datasetx[j][k + 1] <= 800) and datasetx[j][k + 2] <= 800 and datasetx[j][k + 3] <= 800 and \
                datasetx[j][k + 4] <= 800:
            datasety[j][4] = 1
        elif (datasetx[j][k] <= 800) and (datasetx[j][k + 1] <= 800) and datasetx[j][k + 2] <= 800 and datasetx[j][k + 3] <= 800 and \
                datasetx[j][k + 4] <= 800:
            datasety[j][5] = 1
        else:
            datasety[j][6] = 1

    validation_rate = 0.20
    validation_num = int(datasetx.shape[0] * validation_rate)
    datasetx, datasety = shuffle_dataset(datasetx, datasety)

    # 2.검증 데이터 만들기
    testsetx = []
    testsety = []

    filename = "dataset.xlsx"  # 파일명
    book = openpyxl.load_workbook(filename)  # 엑셀파일 book 변수에 저장
    sheet = book.worksheets[0]

    for row in sheet.rows:  # 전체 행에 대하여 반복실행
        testsetx.append(row[0].value)  # 1열 데이터

    number = int(len(testsetx) / 5)
    testsetx = np.reshape(testsetx, (number, 5))
    testsety = np.zeros((number, 7))

    for j in range(0, number):
        k = 0
        if (testsetx[j][k] > 800) and (testsetx[j][k + 1] > 800) and testsetx[j][k + 2] > 800 and testsetx[j][k + 3] > 800 and testsetx[j][
            k + 4] > 800:
            testsety[j][0] = 1
        elif (testsetx[j][k] > 800) and (testsetx[j][k + 1] <= 800) and testsetx[j][k + 2] > 800 and testsetx[j][k + 3] > 800 and \
                testsetx[j][k + 4] > 800:
            testsety[j][1] = 1
        elif (testsetx[j][k] > 800) and (testsetx[j][k + 1] <= 800) and testsetx[j][k + 2] <= 800 and testsetx[j][k + 3] > 800 and \
                testsetx[j][k + 4] > 800:
            testsety[j][2] = 1
        elif (testsetx[j][k] <= 800) and (testsetx[j][k + 1] <= 800) and testsetx[j][k + 2] > 800 and testsetx[j][k + 3] > 800 and \
                testsetx[j][k + 4] > 800:
            testsety[j][2] = 1
        elif (testsetx[j][k] > 800) and (testsetx[j][k + 1] <= 800) and testsetx[j][k + 2] <= 800 and testsetx[j][k + 3] <= 800 and \
                testsetx[j][k + 4] > 800:
            testsety[j][3] = 1
        elif (testsetx[j][k] <= 800) and (testsetx[j][k + 1] <= 800) and testsetx[j][k + 2] <= 800 and testsetx[j][k + 3] > 800 and \
                testsetx[j][k + 4] > 800:
            testsety[j][3] = 1
        elif (testsetx[j][k] > 800) and (testsetx[j][k + 1] <= 800) and testsetx[j][k + 2] <= 800 and testsetx[j][k + 3] <= 800 and \
                testsetx[j][k + 4] <= 800:
            testsety[j][4] = 1
        elif (testsetx[j][k] <= 800) and (testsetx[j][k + 1] <= 800) and testsetx[j][k + 2] <= 800 and testsetx[j][k + 3] <= 800 and \
                testsetx[j][k + 4] <= 800:
            testsety[j][5] = 1
        else:
            testsety[j][6] = 1

    testsetx, testsety = shuffle_dataset(testsetx, testsety)

    datasetx = datasetx.astype(dtype=np.int64)
    datasety = datasety.astype(dtype=np.int64)
    testsetx = testsetx.astype(dtype=np.int64)
    testsety = testsety.astype(dtype=np.int64)


    #print(testsetx[0])
    return ((datasetx, datasety),(testsetx,testsety))
    #return ((datasetx, datasety), (x_val, t_val))

if __name__ == '__main__':
    loadData()