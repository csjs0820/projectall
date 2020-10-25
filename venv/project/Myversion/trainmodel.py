# 0. 사용할 패키지 불러오기
import keras
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.utils import np_utils
from keras.models import load_model
from dataset import loadData

# 손실 이력 클래스 정의
class LossHistory(keras.callbacks.Callback):
    def init(self):
        self.losses = []

    def on_epoch_end(self, batch, logs={}):
        self.losses.append(logs.get('loss'))

# 1. 데이터 준비하기

# 코드 사전 정의
code2idx = {'bend': 0, 'unfold': 1}
idx2code = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'error'}

# 2. 데이터셋 생성하기
(x_train, t_train), (x_test, t_test) = loadData()

max_idx_value = 6

one_hot_vec_size = t_train.shape[1]

print("one hot encoding vector size is ", one_hot_vec_size)

# 3. 모델 구성하기
model = Sequential()
model.add(Dense(128, input_dim=5, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(one_hot_vec_size, activation='softmax'))

# 4. 모델 학습과정 설정하기
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

history = LossHistory()  # 손실 이력 객체 생성
history.init()

# 5. 모델 학습시키기
model.fit(x_train, t_train, epochs=800, batch_size=100, verbose=2, callbacks=[history])

# 6. 학습과정 살펴보기
import matplotlib.pyplot as plt

plt.plot(history.losses)
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train'], loc='upper left')
plt.show()

# 7. 모델 평가하기
score, acc = model.evaluate(x_test, t_test, batch_size=10)
print('Test performance: accuracy={0}, loss={1}'.format(acc, score))

model.save('test_model_addaction.h5') #test_model(0,1,2,3,4,5,6) test_model2(0,1,2,2,3,3,4,5,6)