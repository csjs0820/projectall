import serial
import numpy as np
from unicode import *
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from keras.models import load_model
#print("임포트 완료")

#print("serial 통신 준비완료")
idxcode = {0: '0', 1: 'ㄱ', 2: 'ㄴ', 3: 'ㄷ', 4: 'ㄹ', 5: 'ㅁ', 6: 'ㅂ',7:'ㅅ',8:'ㅇ',9:'ㅈ',10:'ㅏ',11:'ㅓ',12:'ㅜ',13:'ㅣ',14:'error'}

cred = credentials.Certificate("capstone-b68d8-firebase-adminsdk-lf2yy-0c12699124.json")
firebase_admin.initialize_app(cred,{'databaseURL':'https://capstone-b68d8.firebaseio.com/'})
#print("DB 준비 완료")

datanum = 63
result = []
plus = []

arduino = serial.Serial('COM4', 9600)
for i in range(0,71):
    init = arduino.readline()

def writeDB_word(action):
    dir = db.reference()
    dir.update({'predict_word': action})

def writeDB_spell(spell):
    dir = db.reference()
    dir.update({'predict_spell': spell})

def getdata():
    value = np.zeros((int(datanum/7),7))
    for i in range(0,int(datanum/7)):
        for j in range(0,7):
            while True:
                try:
                    res = arduino.readline()  # 시리얼 통신으로 받은 값 중에 첫번째줄 읽기(=엄지 value)
                    res = int(res.decode()[:len(res) - 1])  # value 뒤에 붙은 줄바꿈표(\n) 제거하고 실수형으로 변환
                    if j >= 5 and res <= 1:
                        value[i][j] = res  # value1 리스트에 값 추가
                    elif j < 5 and res > 600:
                        value[i][j] = res  # value1 리스트에 값 추가
                    else:
                        #print("error 발생")
                        continue
                    #print(rescode[i],":",value)
                except ValueError:
                    print("error 좌표 x :",i+1,"y : ",j+1)
                    continue
                break

    #value = np.reshape(value,(int(datanum/7),7))
    print(value)
    return value

def use_model(data):
    num = len(data)

    model = load_model('ㄱ~ㅈ_ㅏㅓㅜㅣ_upgrade.h5')

    seq_out = []
    temp = np.zeros((15, 1))
    # 3. 모델 사용하기
    for i in range(0, num):
        pred_out = model.predict(data)
        idx = np.argmax(pred_out[i])  # one-hot 인코딩을 인덱스 값으로 변환
        temp[idx] += 1  #

    action = idxcode[np.argmax(temp)]

    print('예측 결과 : ' + action)
    return action

while True:
    res = use_model(getdata())

    if (res != 'error'):
        if (res == '0'):
            #writeDB_spell(res)
            if (len(result) != 0):
                word = join_jamos(result)
                print("조합 결과 : ", word)
                writeDB_word(word)
                writeDB_spell(res)
                result.clear()
                plus.clear()
            else:
                if (len(plus) == 0):
                    print("==============================")
                    # plus.append(res)
        else:
            if (len(result) == 0 or result[len(result) - 1] != res):
                result.append(res)
                print(result)
                writeDB_spell(res)
