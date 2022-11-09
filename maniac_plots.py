import numpy as np
import matplotlib.pyplot as plt
import random

colors = ["b", "g", "r", "c", "m", "y", "k"]


def alpha_finder(value):
    if 0<= value <= 5:
        alpha = 1
    elif 6 < value <= 8:
        alpha = 0.65
    elif 9 < value <= 12:
        alpha = 0.45
    else:
        alpha = 0.30
    return alpha


def width_finder(value):
    if (value > 2) and (value <= 5):
        width = 1.6
    elif 6 < value <= 8:
        width = 1
    elif 9 < value <= 12:
        width = 0.75
    else:
        width = 0
    return width


# B = np.random.randint(-100,100, size=(10,10))
data = np.random.randint(1, 100, size=10)

X = np.random.randint(-170, 170, size=10)
Y = np.random.randint(-170, 170, size=10)

# X = np.sort(B[0,:])
# Y = np.sort(B[:,0])

tempX = np.array([])
tempY = np.array([])
data = np.sort(data)
i = 0

plt.figure(figsize=(10, 5))

for i in range(10):
    if i + 1 == 10:
        break
    else:
        for j in range(1,10):
            print([X[i],X[j]])
            print([Y[i], Y[j]])
            plt.plot((X[i],X[j]),(Y[i], Y[j]), linewidth=width_finder(abs((data[i] - data[j]))), color=random.choice(colors),
                        alpha=alpha_finder(abs((data[i] - data[j]))))


plt.scatter(X, Y,s=data)
plt.xlim([-200, 200])
plt.ylim([-200, 200])

for i, txt in enumerate(data):
    plt.annotate(f"{txt:4}", (X[i], Y[i]))

plt.show()
