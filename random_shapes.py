import numpy as np
import matplotlib.pyplot as plt
import random

floor_x = np.array([1, 2, 3, 4, 5, 6])
floor_y = np.repeat(40, 6)

ceil_x = np.array([1, 2, 3, 4, 5, 6])
ceil_y = np.repeat(20, 6)

colors = ["b", "g", "r", "c", "m", "y", "k"]


def kare_ciz():
    possible_pos_X = []

    for j in range(6):
        possible_pos_X.append([floor_x[j], floor_y[1]])
    print(possible_pos_X)
    print("""""")
    possible_pos_Y = []
    for i in range(6):
        possible_pos_Y.append([ceil_x[i], ceil_y[1]])
    print(possible_pos_Y)
    selected_x = random.sample(possible_pos_X, 2)
    selected_x2 = random.choice(possible_pos_X)

    selected_y = random.sample(possible_pos_Y, 2)
    selected_y2 = random.choice(possible_pos_Y)
    print([selected_x], [selected_y])

    draw_x = (selected_x[0], selected_x[1], selected_y[0], selected_y[1], selected_x[0])
    draw_y = ([40, 40, 20, 20, 40])
    plt.fill(draw_x, draw_y, color=random.choice(colors), alpha=0.1)
    plt.plot(draw_x, draw_y)


def altUcgen_ciz():
    possible_pos_X = []

    for j in range(6):
        possible_pos_X.append([floor_x[j], floor_y[1]])
    print(possible_pos_X)
    print("""""")
    possible_pos_Y = []
    for i in range(6):
        possible_pos_Y.append([ceil_x[i], ceil_y[1]])
    print(possible_pos_Y)
    selected_x = random.sample(possible_pos_X, 1)
    selected_x2 = random.choice(possible_pos_X)

    selected_y = random.sample(possible_pos_Y, 2)
    selected_y2 = random.choice(possible_pos_Y)

    print([selected_x], [selected_y])

    draw_x = (selected_x[0], selected_y[0], selected_y[1], selected_x[0])
    draw_y = ([40, 20, 20, 40])
    plt.fill(draw_x, draw_y, color=random.choice(colors), alpha=0.1)
    plt.plot(draw_x, draw_y)


def ustUcgen_ciz():
    possible_pos_X = []

    for j in range(6):
        possible_pos_X.append([floor_x[j], floor_y[1]])
    print(possible_pos_X)
    print("""""")
    possible_pos_Y = []
    for i in range(6):
        possible_pos_Y.append([ceil_x[i], ceil_y[1]])
    print(possible_pos_Y)
    selected_x = random.sample(possible_pos_X, 2)
    selected_x2 = random.choice(possible_pos_X)

    selected_y = random.sample(possible_pos_Y, 1)
    selected_y2 = random.choice(possible_pos_Y)
    print([selected_x], [selected_y])

    draw_x = (selected_x[0], selected_x[1], selected_y[0], selected_x[0])
    draw_y = ([40, 40, 20, 40])
    plt.fill(draw_x, draw_y, color=random.choice(colors), alpha=0.1)
    plt.plot(draw_x, draw_y)


def dikdortgen_ciz():
    print("4")


# plt.scatter(floor_x,floor_y)
# plt.scatter(ceil_x,ceil_y)

shapes = ["kare", "ustUcgen", "altUcgen"]

choice = random.choice(shapes)
print(choice)
if (choice == "kare"):
    kare_ciz()

if (choice == "ustUcgen"):
    ustUcgen_ciz()
if (choice == "altUcgen"):
    altUcgen_ciz()
if (choice == "dikdortgen"):
    dikdortgen_ciz()

plt.ylim(19, 41)
plt.xlim(1, 6)
plt.axis('off')
plt.show()