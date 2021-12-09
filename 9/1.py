import numpy as np

field = []

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

            

        

#with open('input_test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    for l in f:
        field.append([int(p) for p in l.strip()])

f = np.asarray(field)

print(f)

m = find_low(f)

print(m)

risk = np.sum(m[:]) + np.sum(f[m==1][:])

print(risk)
