import serial
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

arduino = serial.Serial('COM5', 9600)

value1 = []  # 엄지 굽힘 값 저장 리스트
value2 = []  # 검지 굽힘 값 저장 리스트
value3 = []  # 중지 굽힘 값 저장 리스트
value4 = []  # 약지 굽힘 값 저장 리스트
value5 = []  # 새끼 굽힘 값 저장 리스트

fig = plt.figure(figsize=(12,12)) #그래프 그릴 창 생성 size = 12*12(inch)

ax = plt.subplot(321,xlim=(0, 50), ylim=(100, 400)) #엄지 그래프 x축 범위 0 ~ 50, y축 범위 100 ~ 400
ax2 = plt.subplot(322,xlim=(0, 50), ylim=(100, 400)) #검지 그래프
ax3 = plt.subplot(323,xlim=(0, 50), ylim=(100, 400)) #중지 그래프
ax4 = plt.subplot(324,xlim=(0, 50), ylim=(100, 400)) #약지 그래프
ax5 = plt.subplot(325,xlim=(0, 50), ylim=(100, 400)) #새끼 그래프


max_points = 50 #x축 max 값 50

line, = ax.plot(np.arange(max_points),np.ones(max_points, dtype=np.float)*np.nan, lw=2) #엄지그래프 line 그리기
line2, = ax2.plot(np.arange(max_points),np.ones(max_points, dtype=np.float)*np.nan, lw=2)
line3, = ax3.plot(np.arange(max_points),np.ones(max_points, dtype=np.float)*np.nan, lw=2)
line4, = ax4.plot(np.arange(max_points),np.ones(max_points, dtype=np.float)*np.nan, lw=2)
line5, = ax5.plot(np.arange(max_points),np.ones(max_points, dtype=np.float)*np.nan, lw=2)

#animation 사용 위한 초기화 정의
def init():
    return line,
def init2():
    return line2,
def init3():
    return line3,
def init4():
    return line4,
def init5():
    return line5,

#엄지 실시간 그래프 그리기 위한 함수
def animate1(i):
    res1 = arduino.readline() #시리얼 통신으로 받은 값 중에 첫번째줄 읽기(=엄지 value)
    res1 = float(res1.decode()[:len(res1) - 1]) #value 뒤에 붙은 줄바꿈표(\n) 제거하고 실수형으로 변환
    value1.append(res1) #value1 리스트에 값 추가
    print("엄지:", value1)

    y = res1
    old_y = line.get_ydata() #업데이트 하기 이전의 그래프의 y값 old_y에 저장
    new_y = np.r_[old_y[1:], y] #np.r_[]은 y를 old_y[1:]에 이어 붙이는 함수
    line.set_ydata(new_y) #새로 추가된 값이 들어간 line으로 설정 후 반환
    return line,


def animate2(i):
    res2 = arduino.readline()
    res2 = float(res2.decode()[:len(res2) - 1])
    value2.append(res2)
    print("검지:", value2)

    y = res2st
    old_y = line2.get_ydata()
    new_y = np.r_[old_y[1:], y]
    line2.set_ydata(new_y)
    return line2,


def animate3(i):
    res3 = arduino.readline()
    res3 = float(res3.decode()[:len(res3) - 1])
    value3.append(res3)
    print("중지:", value3)

    y = res3
    old_y = line3.get_ydata()
    new_y = np.r_[old_y[1:], y]
    line3.set_ydata(new_y)
    return line3,

def animate4(i):
    res4 = arduino.readline()
    res4 = float(res4.decode()[:len(res4) - 1])
    value4.append(res4)
    print("약지:", value4)

    y = res4
    old_y = line4.get_ydata()
    new_y = np.r_[old_y[1:], y]
    line4.set_ydata(new_y)
    return line4,


def animate5(i):
    res5 = arduino.readline()
    res5 = float(res5.decode()[:len(res5) - 1])

    value5.append(res5)
    print("새끼:", value5)

    y = res5
    old_y = line5.get_ydata()
    new_y = np.r_[old_y[1:], y]
    line5.set_ydata(new_y)
    return line5,



while True:
    # func인 animate1을 반복 호출하여 애니메이션 생성하는 함수 animation.FuncAnimation 이용
    print("insert op :", end=' ')
    op = input()
    arduino.write(op.encode())
    anim = animation.FuncAnimation(fig, animate1, init_func=init, frames=100, interval=20, blit=False)
    anim2 = animation.FuncAnimation(fig, animate2, init_func=init2, frames=100, interval=20, blit=False)
    anim3 = animation.FuncAnimation(fig, animate3, init_func=init3, frames=100, interval=20, blit=False)
    anim4 = animation.FuncAnimation(fig, animate4, init_func=init4, frames=100, interval=20, blit=False)
    anim5 = animation.FuncAnimation(fig, animate5, init_func=init5, frames=100, interval=20, blit=False)
    plt.show()