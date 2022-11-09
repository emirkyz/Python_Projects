import numpy as np
import matplotlib.pyplot as plt
import random
from mpl_toolkits import mplot3d

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


# B = np.random.randint(-80,80, size=(8,8))
data = np.random.randint(1, 80, size=8)

X = np.random.randint(-170, 170, size=8)
Y = np.random.randint(-170, 170, size=8)
Z = np.random.randint(-170, 170, size=8)

# X = np.sort(B[0,:])
# Y = np.sort(B[:,0])

tempX = np.array([])
tempY = np.array([])
data = np.sort(data)
i = 0

fig = plt.figure(figsize=(10,10))

ax = fig.add_subplot(111, projection='3d')





for i in range(8):
    for j in range(8):
        plt.plot((X[i],X[j]),(Y[i],Y[j]),(Z[i],Z[j]), alpha = 0.2,c = "grey",zorder = 0,linewidth=3)
ax.scatter(X,Y,Z,s=115,c="red",edgecolors="grey")

plt.xlim([-180, 180])
plt.ylim([-180, 180])
plt.axis("on")
plt.show()
