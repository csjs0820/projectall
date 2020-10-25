import serial
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation
from numpy import argmax
from playsound import playsound

arduino = serial.Serial('COM4', 9600)

idxcode = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'error'}

init = arduino.readline()

datanum = input("입력 받을 센서 값 개수 : ")
datanum = int(datanum)

def getdata():
    value = []
    for i in range(0,datanum):
        res = arduino.readline()  # 시리얼 통신으로 받은 값 중에 첫번째줄 읽기(=엄지 value)
        res = int(res.decode()[:len(res) - 1])  # value 뒤에 붙은 줄바꿈표(\n) 제거하고 실수형으로 변환
        value.append(res)  # value1 리스트에 값 추가
        #print("value:", value1)

    value = np.reshape(value,(int(datanum/5),5))
    return value

def use_model(data):
    num = len(data)

    # 2. 모델 불러오기
    from keras.models import load_model

    model = load_model('test_model_addaction.h5')

    seq_out = []
    temp = np.zeros((10, 1))
    # 3. 모델 사용하기
    for i in range(0, num):
        pred_out = model.predict(data)
        idx = np.argmax(pred_out[i])  # one-hot 인코딩을 인덱스 값으로 변환
        # seq_out.append(idx2code[idx])  # seq_out는 최종 악보이므로 인덱스 값을 코드로 변환하여 저장
        temp[idx] += 1  # seq_out는 최종 악보이므로 인덱스 값을 코드로 변환하여 저장

    action = idxcode[np.argmax(temp)]

    print('Predict : ' + action)
    return action

def wav_sound(action):
    if action == 'zero':
        playsound("./sound/zero.wav")
    elif action == 'one':
        playsound("./sound/one.wav")
    elif action == 'two':
        playsound("./sound/two.wav")
    elif action == 'three':
        playsound("./sound/three.wav")
    elif action == 'four':
        playsound("./sound/four.wav")
    elif action == 'five':
        playsound("./sound/five.wav")
    elif action == 'error':
        playsound("./sound/error.wav")

while True:

    wav_sound(use_model(getdata()))


