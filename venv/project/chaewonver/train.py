import serial
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import pandas as pd
from pandas import DataFrame

arduino = serial.Serial('COM4', 9600)

value1 = []  # 엄지 굽힘 값 저장 리스트
value2 = []  # 검지 굽힘 값 저장 리스트
value3 = []  # 중지 굽힘 값 저장 리스트

for i in range(0,3):
    init = arduino.readline()

def data1():
    res1 = arduino.readline()
    res1 = float(res1.decode()[:len(res1) - 1])

    if (res1 != 0):
        if ((len(value1)) == 20):
            value1.clear()
        value1.append(res1)
        print("엄지:", value1)
    else:
        value1.clear()

def data2():
    res2 = arduino.readline()
    res2 = float(res2.decode()[:len(res2) - 1])

    if (res2 != 0):
        if ((len(value2)) == 20):
            value2.clear()
        value2.append(res2)
        print("검지:", value2)
    else:
        value2.clear()


def data3():
    res3 = arduino.readline()
    res3 = float(res3.decode()[:len(res3) - 1])

    if (res3 != 0):
        if ((len(value3)) == 20):
            value3.clear()
        value3.append(res3)
        print("중지:", value3)
    else:
        value3.clear()

    if (len(value3) == 20):
        return print_Data()

def print_Data():
    if(len(value1)==19):
        value1.append(value1[18])
    if(len(value2)==19):
        value2.append(value2[18])
    datas = {'v1': value1,
             'v2': value2,
             'v3': value3,
             'res':[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]}
    df = pd.DataFrame(datas)
    print(df)

    df.to_csv('data_train.csv',
              sep=',',
              index=False)



while True:
    data1()
    data2()
    data3()
