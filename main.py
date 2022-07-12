import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

def animate(i):

    data = open('stock.txt', 'r').read()
    lines = data.split('\n')
    xs = []
    ys = []

    for line in lines:
        x, y = line.split(',')
        xs.append(float(x))
        ys.append(float(y))

    ax.clear()
    ax.plot(xs, ys)

    plt.xlabel('Дфта')
    plt.ylabel('Цена')
    plt.title('График обновлений в режиме реального времени')

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()