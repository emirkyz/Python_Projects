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
        alpha = 0.35
    return alpha


def width_finder(value):
    if (value > 2) and (value <= 5):
        width = 4.5
    elif 6 < value <= 8:
        width = 1
    elif 9 < value <= 12:
        width = 0.75
    else:
        width = 0.65
    return width


# B = np.random.randint(-100,100, size=(10,10))
data = np.random.randint(1, 100, size=10)
# print(B)

X = np.random.randint(-170, 170, size=10)
Y = np.random.randint(-170, 170, size=10)

# X = np.sort(B[0,:])
# Y = np.sort(B[:,0])

tempX = np.array([])
tempY = np.array([])
data = np.sort(data)

i = 0
plt.figure(figsize=(8, 5))
for i in range(10):
    if i + 1 == 10:
        break
    else:

        for j in range(0,10):
            if (i!= j) and abs((data[i] - data[j])) <= 20:
                tempX = np.append(tempX, (X[i], X[j]))
                tempY = np.append(tempY, (Y[i], Y[j]))
                plt.plot(tempX, tempY, linewidth=width_finder(abs((data[i] - data[j]))), color=random.choice(colors),
                         alpha=alpha_finder(abs((data[i] - data[j]))),zorder = 0)
            tempX = np.array([])
            tempY = np.array([])


plt.scatter(X, Y, s=120)
plt.xlim([-200, 200])
plt.ylim([-200, 200])

for i, txt in enumerate(data):
    plt.annotate(f"{txt:4}", (X[i], Y[i]),fontsize = 15)

plt.show()
