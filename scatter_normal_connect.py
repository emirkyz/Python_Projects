import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import random

colors = ["b", "g", "r", "c", "m", "y", "k"]

# B = np.random.randint(-100,100, size=(10,10))
# data = np.random.randint(1, 100, size=10)
# print(B)

# X = np.random.randint(-170, 170, size=10)
#Y = np.random.randint(-170, 170, size=10)

X = np.array([325,215,185,332,406,522,412,614,544,421,445,408])
Y = np.array([16.4,14.2,11.9,15.2,18.5,22.1,19.4,25.1,23.4,18.1,22.6,17.2])

XX = np.sort(X)
YY = np.sort(Y)
last_X = np.array([])
last_Y = np.array([])

for i in range(len(X)):
    index = np.where(X == XX[i])
    last_X = np.append(last_X, X[index])
    last_Y = np.append(last_Y, Y[index])

tempX = np.array([])
tempY = np.array([])

plt.figure(figsize=(15,5))
plt.plot(last_X,last_Y)
plt.scatter(X, Y, s=50)
plt.title("Ice cream sales / Temperature")
plt.xlabel("Ice cream sales")
plt.ylabel("Temperature")
for i, txt in enumerate(Y):
    plt.annotate(f"{txt:6}", (X[i], Y[i]))

plt.show()