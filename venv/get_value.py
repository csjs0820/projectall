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

fig = plt.figure()
ax = plt.subplot(321,xlim=(0, 50), ylim=(650, 900))
ax2 = plt.subplot(322,xlim=(0, 50), ylim=(650, 900))
ax3 = plt.subplot(323,xlim=(0, 50), ylim=(650, 900))
ax4 = plt.subplot(324,xlim=(0, 50), ylim=(650, 900))
ax5 = plt.subplot(325,xlim=(0, 50), ylim=(650, 900))
#line, = ax.plot([], [], lw=2)

max_points = 50

line, = ax.plot(np.arange(max_points),np.ones(max_points, dtype=np.float)*np.nan, lw=2)
line2, = ax.plot(np.arange(max_points),np.ones(max_points, dtype=np.float)*np.nan, lw=2)
line3, = ax.plot(np.arange(max_points),np.ones(max_points, dtype=np.float)*np.nan, lw=2)
line4, = ax.plot(np.arange(max_points),np.ones(max_points, dtype=np.float)*np.nan, lw=2)
line5, = ax.plot(np.arange(max_points),np.ones(max_points, dtype=np.float)*np.nan, lw=2)


def init():
    return line,


def animate1(i):
    global j
    for j in range(5):
        res = arduino.readline()
        res = float(res.decode()[:len(res) - 1])
        if j == 0:
            value1.append(res)
            print("엄지:", value1)

            y = res
            y = float(y)
            old_y = line.get_ydata()
            new_y = np.r_[old_y[1:], y]
            line.set_ydata(new_y)
            return line,
        elif j == 1:
            value2.append(res)
            print("검지:", value2)

            y = res
            y = float(y)
            old_y = line.get_ydata()
            new_y = np.r_[old_y[1:], y]
            line.set_ydata(new_y)
            return line2,
        elif j == 2:
            value3.append(res)
            print("중지:", value3)

            y = res
            y = float(y)
            old_y = line.get_ydata()
            new_y = np.r_[old_y[1:], y]
            line.set_ydata(new_y)
            return line3,
        elif j == 3:
            value4.append(res)
            print("약지:", value4)

            y = res
            y = float(y)
            old_y = line.get_ydata()
            new_y = np.r_[old_y[1:], y]
            line.set_ydata(new_y)
            return line4,
        elif j == 4:
            value5.append(res)
            print("새끼:", value5)

            y = res
            y = float(y)
            old_y = line.get_ydata()
            new_y = np.r_[old_y[1:], y]
            line.set_ydata(new_y)

            j = 0
            return line5,


while True:
    anim = animation.FuncAnimation(fig, animate1, init_func=init, frames=200, interval=20, blit=False)
    anim2 = animation.FuncAnimation(fig, animate1, init_func=init, frames=200, interval=20, blit=False)
    anim3 = animation.FuncAnimation(fig, animate1, init_func=init, frames=200, interval=20, blit=False)
    anim4 = animation.FuncAnimation(fig, animate1, init_func=init, frames=200, interval=20, blit=False)
    anim5 = animation.FuncAnimation(fig, animate1, init_func=init, frames=200, interval=20, blit=False)
    plt.show()