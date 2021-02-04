import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()

def make_noise_wave(data):
    # 現在描写されているグラフを消去
    plt.cla()                      
    rand = np.random.randn(50)
    # y軸固定
    plt.ylim(-4, 4)
    im = plt.plot(rand)

ani = animation.FuncAnimation(fig, make_noise_wave, interval=100)
plt.show()