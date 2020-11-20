import serial
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import pandas as pd
from pandas import DataFrame
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score

arduino = serial.Serial('COM4', 9600)

for i in range(0,3):
    init = arduino.readline()

value1 = []  # 엄지 굽힘 값 저장 리스트
value2 = []  # 검지 굽힘 값 저장 리스트
value3 = []  # 중지 굽힘 값 저장 리스트

def data1():
    res1 = arduino.readline()
    res1 = float(res1.decode()[:len(res1) - 1])

    if (res1 != 0):
        if ((len(value1)) == 10):
            value1.clear()
        value1.append(res1)
        print("엄지:", value1)
    else:
        value1.clear()

def data2():
    res2 = arduino.readline()
    res2 = float(res2.decode()[:len(res2) - 1])

    if (res2 != 0):
        if ((len(value2)) == 10):
            value2.clear()
        value2.append(res2)
        print("검지:", value2)
    else:
        value2.clear()


def data3():
    res3 = arduino.readline()
    res3 = float(res3.decode()[:len(res3) - 1])

    if (res3 != 0):
        if ((len(value3)) == 10):
            value3.clear()
        value3.append(res3)
        print("중지:", value3)
    else:
        value3.clear()

    if(len(value3)==10):
        return print_Data()


def print_Data():
    if(len(value1)==9):
        value1.append(value1[8])
    if(len(value2)==9):
        value2.append(value2[8])
    datas = {'v1': value1,
             'v2': value2,
             'v3': value3,
             'res':['?','?','?','?','?','?','?','?','?','?']}
    df = pd.DataFrame(datas)
    print(df)

    df.to_csv('data_test.csv',
              sep=',',
              index=False)
    return train()

def train():
    train = pd.read_csv('data_train.csv')
    test = pd.read_csv('data_test.csv')

    max_k_range = train.shape[0] // 2
    k_list = []
    for i in range(3, max_k_range, 2):
        k_list.append(i)

    cross_validation_scores = []
    x_train = train[['v1', 'v2', 'v3']]
    y_train = train[['res']]

    for k in k_list:
        knn = KNeighborsClassifier(n_neighbors=k)
        scores = cross_val_score(knn, x_train, y_train.values.ravel(),
                                 cv=10, scoring='accuracy')
        cross_validation_scores.append(scores.mean())

    # print(cross_validation_scores)

    # plt.plot(k_list,cross_validation_scores)
    # plt.show()

    cvs = cross_validation_scores
    k = k_list[cvs.index(max(cross_validation_scores))]
    print("The best number of k : " + str(k) )

    knn = KNeighborsClassifier(n_neighbors=k)

    x_train = train[['v1', 'v2', 'v3']]
    y_train = train[['res']]

    knn.fit(x_train, y_train.values.ravel())

    x_test = test[['v1', 'v2', 'v3']]
    y_test = test[['res']]

    pred = knn.predict(x_test)

    comparison = pd.DataFrame({'prediction': pred})
    print(comparison)

    # print("accuracy : " + str(accuracy_score(y_test.values.ravel(), pred)) )
    return first_do()

def first_do():
    data1()
    data2()
    data3()

while True:
    first_do()