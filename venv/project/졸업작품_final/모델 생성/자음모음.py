from random import *
import numpy as np

def shuffle_dataset(x, t):
    permutation = np.random.permutation(x.shape[0])
    x = x[permutation, :] if x.ndim == 2 else x[permutation, :, :, :]
    t = t[permutation]

    return x, t

def loadData():
    # 1.훈련 데이터 만들기
    datasetx = np.zeros((38000,7)) #입력 데이터 24000*5개
    datasety = np.zeros((38000,15)) #출력 데이터 24000개

    # 2.훈련 출력 데이터 만들기
    data_five = np.zeros((2000,7))
    data_ㄱ = np.ones((2000,7))
    data_ㄴ = np.ones((2000,7))
    data_ㄷ = np.ones((2000,7))
    data_ㄹ = np.zeros((2000,7))
    data_ㅁ = np.ones((2000,7))
    data_ㅂ = np.zeros((2000,7))
    data_ㅅ = np.ones((2000,7))
    data_ㅇ = np.zeros((2000,7))
    data_ㅈ = np.zeros((2000,7))
    data_ㅏ = np.ones((2000,7))
    data_ㅓ = np.ones((2000,7))
    data_ㅜ = np.ones((2000, 7))
    data_ㅣ = np.ones((2000, 7))
    data_temp = np.zeros((10000, 7))

    for i in range(0,2000):
        data_five[i][5] = choice([-1, 0,1])
        data_five[i][6] = choice([-1,0, 1])

        data_ㄱ[i][0] = 0
        data_ㄱ[i][1] = 0
        data_ㄱ[i][5] = 0
        data_ㄱ[i][6] = 1

        data_ㄴ[i][0] = 0
        data_ㄴ[i][1] = 0
        data_ㄴ[i][5] = 1
        data_ㄴ[i][6] = 0

        data_ㄷ[i][1] = 0
        data_ㄷ[i][2] = 0
        data_ㄷ[i][5] = 1
        data_ㄷ[i][6] = 0

        data_ㄹ[i][0] = 1
        data_ㄹ[i][4] = 1
        data_ㄹ[i][5] = 1
        data_ㄹ[i][6] = 0

        data_ㅁ[i][5] = 0
        data_ㅁ[i][6] = -1

        data_ㅂ[i][0] = 1
        data_ㅂ[i][5] = 0
        data_ㅂ[i][6] = -1

        data_ㅅ[i][1] = 0
        data_ㅅ[i][2] = 0
        data_ㅅ[i][5] = 0
        data_ㅅ[i][6] = 1

        data_ㅇ[i][0] = 1
        data_ㅇ[i][1] = 1
        data_ㅇ[i][5] = 0
        data_ㅇ[i][6] = -1

        data_ㅈ[i][3] = 1
        data_ㅈ[i][4] = 1
        data_ㅈ[i][5] = 0
        data_ㅈ[i][6] = 1

        data_ㅏ[i][1] = 0
        data_ㅏ[i][5] = 0
        data_ㅏ[i][6] = -1

        data_ㅓ[i][1] = 0
        data_ㅓ[i][5] = 1
        data_ㅓ[i][6] = 0

        data_ㅜ[i][1] = 0
        data_ㅜ[i][5] = 0
        data_ㅜ[i][6] = 1

        data_ㅣ[i][4] = 0
        data_ㅣ[i][5] = 0
        data_ㅣ[i][6] = -1

    datasetx = np.concatenate([data_five,data_ㄱ, data_ㄴ, data_ㄷ,data_ㄹ, data_ㅁ, data_ㅂ,data_ㅅ, data_ㅇ,data_ㅈ,data_ㅏ,data_ㅓ,data_ㅜ,data_ㅣ,data_temp])

    for i in range(0,28000):
        for j in range(0,5):
            if datasetx[i][j] == 1:
                datasetx[i][j] = randint(801, 930)
            elif datasetx[i][j] == 0:
                datasetx[i][j] = randint(700, 800)

    for i in range(28000,38000):
        for j in range(0,7):
            datasetx[i][j] = randint(700, 930)
            if(j == 5):
                datasetx[i][j] = randint(-1,1)
            elif(j == 6):
                datasetx[i][j] = randint(-1,1)

    p = 0
    for j in range(0, 28000, 2000):
        for i in range(j, j + 2000):
            datasety[i][p] = 1
        p = p + 1

    for j in range(28000, 38000):
        k=0
        if (datasetx[j][k] <= 800) and (datasetx[j][k + 1] <= 800) and datasetx[j][k + 2] <= 800 and datasetx[j][k + 3] <= 800 and \
                datasetx[j][k + 4] <= 800:#five
            datasety[j][0] = 1
        elif (datasetx[j][k] <= 800) and (datasetx[j][k + 1] <= 800) and datasetx[j][k + 2] > 800 and datasetx[j][k + 3] > 800 and \
                datasetx[j][k + 4] > 800 and datasetx[j][k+5] == 0 and datasetx[j][k+6] == 1: #ㄱ
            datasety[j][1] = 1
        elif (datasetx[j][k] <= 800) and (datasetx[j][k + 1] <= 800) and datasetx[j][k + 2] > 800 and datasetx[j][k + 3] > 800 and \
                datasetx[j][k + 4] > 800 and datasetx[j][k+5] == 1 and datasetx[j][k+6] == 0: #ㄴ
            datasety[j][2] = 1
        elif (datasetx[j][k] > 800) and (datasetx[j][k + 1] <= 800) and datasetx[j][k + 2] <= 800 and datasetx[j][k + 3] > 800 and \
                datasetx[j][k + 4] > 800 and datasetx[j][k+5] == 1 and datasetx[j][k+6] == 0: #ㄷ
            datasety[j][3] = 1
        elif (datasetx[j][k] > 800) and (datasetx[j][k + 1] <= 800) and datasetx[j][k + 2] <= 800 and datasetx[j][k + 3] <= 800 and \
                datasetx[j][k + 4] > 800 and datasetx[j][k+5] == 1 and datasetx[j][k+6] == 0: #ㄹ
            datasety[j][4] = 1
        elif (datasetx[j][k] > 800) and (datasetx[j][k + 1] > 800) and datasetx[j][k + 2] > 800 and datasetx[j][k + 3] > 800 and \
                datasetx[j][k + 4] > 800 and datasetx[j][k+5] == 0 and datasetx[j][k+6] == -1: #ㅁ
            datasety[j][5] = 1
        elif (datasetx[j][k] > 800) and (datasetx[j][k + 1] <= 800) and datasetx[j][k + 2] <= 800 and datasetx[j][k + 3] <= 800 and \
                datasetx[j][k + 4] <= 800 and datasetx[j][k+5] == 0 and datasetx[j][k+6] == -1: #ㅂ
            datasety[j][6] = 1
        elif (datasetx[j][k] > 800) and (datasetx[j][k + 1] <= 800) and datasetx[j][k + 2] <= 800 and datasetx[j][k + 3] > 800 and \
                datasetx[j][k + 4] > 800 and datasetx[j][k+5] == 0 and datasetx[j][k+6] == 1: #ㅅ
            datasety[j][7] = 1
        elif (datasetx[j][k] > 800) and (datasetx[j][k + 1] > 800) and datasetx[j][k + 2] <= 800 and datasetx[j][k + 3] <= 800 and \
                datasetx[j][k + 4] <= 800 and datasetx[j][k+5] == 0 and datasetx[j][k+6] == -1: #ㅇ
            datasety[j][8] = 1
        elif (datasetx[j][k] <= 800) and (datasetx[j][k + 1] <= 800) and datasetx[j][k + 2] <= 800 and datasetx[j][k + 3] > 800 and \
                datasetx[j][k + 4] > 800 and datasetx[j][k+5] == 0 and datasetx[j][k+6] == 1: #ㅈ
            datasety[j][9] = 1
        elif (datasetx[j][k] >800) and (datasetx[j][k + 1] <= 800) and datasetx[j][k + 2] > 800 and datasetx[j][k + 3] > 800 and \
                datasetx[j][k + 4] > 800 and datasetx[j][k+5] == 0 and datasetx[j][k+6] == -1: #ㅏ
            datasety[j][10] = 1
        elif (datasetx[j][k] >800) and (datasetx[j][k + 1] <= 800) and datasetx[j][k + 2] > 800 and datasetx[j][k + 3] > 800 and \
                datasetx[j][k + 4] > 800 and datasetx[j][k+5] == 1 and datasetx[j][k+6] == 0: #ㅓ
            datasety[j][11] = 1
        elif (datasetx[j][k] >800) and (datasetx[j][k + 1] <= 800) and datasetx[j][k + 2] > 800 and datasetx[j][k + 3] > 800 and \
                datasetx[j][k + 4] > 800 and datasetx[j][k+5] == 0 and datasetx[j][k+6] == 1: #ㅜ
            datasety[j][12] = 1
        elif (datasetx[j][k] >800) and (datasetx[j][k + 1] > 800) and datasetx[j][k + 2] > 800 and datasetx[j][k + 3] > 800 and \
                datasetx[j][k + 4] <= 800 and datasetx[j][k+5] == 0 and datasetx[j][k+6] == -1: #ㅣ
            datasety[j][13] = 1
        else: #error
            datasety[j][14] = 1

    validation_rate = 0.20
    validation_num = int(datasetx.shape[0] * validation_rate)
    datasetx, datasety = shuffle_dataset(datasetx, datasety)
    x_test = datasetx[:validation_num]
    t_test = datasety[:validation_num]
    datasetx = datasetx[validation_num:]
    datasety = datasety[validation_num:]

    return ((datasetx, datasety),(x_test,t_test))

if __name__ == '__main__':
    loadData()