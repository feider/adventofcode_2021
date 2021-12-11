from PIL import Image
import numpy as np
import cv2

mi = 100
#mi = 3
p = True
p = False

m = []
with open('input.txt', 'r') as f:
#ith open('input_test.txt', 'r') as f:
#with open('input_test_mini.txt', 'r') as f:
    for l in f:
        m.append([int(n) for n in l.strip()])

m = np.asarray(m)

def is_in(x, y, m):
    return x >= 0 and x < m.shape[0] and y >= 0 and y < m.shape[1]

def inc(x, y, m):
    if is_in(x, y, m):
        m[x, y] += 1
        return m[x, y]
    return -1

flashes = 0
if p:
    print(m)


for i in range(500):
    m+=1

    x, y = np.where(m==10)

    while x.size > 0:
        _x, x = x[-1], x[:-1]
        _y, y = y[-1], y[:-1]
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                if inc(_x+dx, _y+dy, m) == 10:
                    x = np.append(x, _x+dx)
                    y = np.append(y, _y+dy)

    x, y = np.where(m>9)
    for _x, _y in zip(x, y):
        m[_x, _y] = 0
    if p:
        print(m)
    img = Image.fromarray(cv2.resize(src = m*255/10.0, dsize=[s * 10 for s in m.shape], interpolation = cv2.INTER_NEAREST))
    img = img.convert('RGB')
    img.save(f"{i:03}.png")

