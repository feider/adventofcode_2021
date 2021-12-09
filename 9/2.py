import numpy as np

field = []
#with open('input_test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    for l in f:
        field.append([int(p) for p in l.strip()])
f = np.asarray(field)



def find_low(f):
    m = np.full_like(f, True)
    for x in range(f.shape[0]):
        for y in range(f.shape[1]):
            v = f[x][y]
            if x > 0:
                if f[x-1][y] <= v:
                    m[x][y] = False
            if x < f.shape[0]-1:
                if f[x+1][y] <= v:
                    m[x][y] = False
            if y > 0:
                if f[x][y-1] <= v:
                    m[x][y] = False
            if y < f.shape[1]-1:
                if f[x][y+1] <= v:
                    m[x][y] = False
    return m

def is_basin(f, x, y, x_s, y_s):
    print(x, y, x_s, y_s)
    if x < 0 or x == f.shape[0] or y < 0 or y == f.shape[1]:
        return False

    if x-1 != x_s and x > 0:
        print(1)
        if f[x-1][y] <= f[x][y]: return False
    if x+1 != x_s and x+1 < f.shape[0]:
        print(2)
        if f[x+1][y] <= f[x][y]: return False
    if y-1 != y_s and y > 0:
        print(3)
        if f[x][y-1] <= f[x][y]: return False
    if y+1 != y_s and y+1 < f.shape[1]:
        print(4)
        if f[x][y+1] <= f[x][y]: return False
    print("is basin")
    return True

def is_in(f, x, y):
    return x >= 0 and y >= 0 and x <f.shape[0] and y < f.shape[1]

def grow_basin(f, x0, y0):
    bm = np.max(f[:])
    basin = [(x0, y0)]
    for l in range(f[x0, y0], bm):
        op = [b for b in basin]
        for o in op:
            x, y= o[0]-1, o[1]
            if is_in(f, x, y) and f[x, y] == l and (x, y) not in basin:
                basin.append((x, y))
            x, y= o[0]+1, o[1]
            if is_in(f, x, y) and f[x, y] == l and (x, y) not in basin:
                basin.append((x, y))
            x, y= o[0], o[1]-1
            if is_in(f, x, y) and f[x, y] == l and (x, y) not in basin:
                basin.append((x, y))
            x, y= o[0], o[1]+1
            if is_in(f, x, y) and f[x, y] == l and (x, y) not in basin:
                basin.append((x, y))
    return basin


print("")
print(f)

m = find_low(f)

print("")
print(m)
print("")


print(np.where(m==1))
x, y = np.where(m==1)

basins = []
for _x, _y in zip(x, y):
    basins.append(grow_basin(f, _x, _y))
l = np.sort(np.asarray([len(b) for b in basins]))[::-1]
for b in basins:
    for x, y in b:
        m[x][y] = True

print("")
print(f)
print("")
print(m)

print("")
print(l)

print(l[0]*l[1]*l[2])
