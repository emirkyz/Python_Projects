import numpy as np
import matplotlib.pyplot as plt
import random


colors = ["b", "g", "r", "c", "m", "y", "k"]

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

print(data)
i = 0
plt.figure(figsize=(10, 5))
for i in range(10):
    if i + 1 == 10:
        break
    else:
        if abs((data[i] - data[i + 1])) <= 5:
            print(f"i sayisi = {i}")
            # print(f"j sayisi = {j}")
            print((data[i] - data[i+1]))
            tempX = np.append(tempX, (X[i], X[i+1]))
            tempY = np.append(tempY, (Y[i], Y[i+1]))

            plt.plot(tempX, tempY, color=random.choice(colors))
    tempX = np.array([])
    tempY = np.array([])



plt.scatter(X, Y, s=data)
plt.xlim([-200, 200])
plt.ylim([-200, 200])

for i, txt in enumerate(data):
    plt.annotate(f"{txt:4}", (X[i], Y[i]))

plt.show()
