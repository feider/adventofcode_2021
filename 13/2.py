import numpy as np
dots = []
fold = []
#with open('input_test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    for l in f:
        if ',' in l:
            dots.append([int(d) for d in l.strip().split(',')])
        if 'fold' in l:
            e = l.strip().split(' ')[2]
            fold.append(e.split('='))

dots_a = np.asarray(dots)
m = np.max(dots_a+1, 0)
field = np.zeros(m)
print(field.shape)
for d in dots:
    field[d[0], d[1]] = 1
print(field)

for f in fold:
    fpos = int(f[1])
    fdir = f[0]

    ds = []
    for d in dots:
        if fdir =='y':
            if d[1]>fpos:
                d[1] = fpos-(d[1]-fpos)
        if fdir =='x':
            if d[0]>fpos:
                d[0] = fpos-(d[0]-fpos)
        ds.append(f"{d[0]},{d[1]}")
    ds = list(set(ds))
    dots = [ [int(d) for d in do.split(',')] for do in ds]
dots_a = np.asarray(dots)
m = np.max(dots_a+1, 0)
field = np.zeros(m)
print(field.shape)
for d in dots:
    field[d[0], d[1]] = 1
for l in field.transpose():
    line = [str(int(i)) for i in l.tolist()]
    s = "".join(line)
    
    print(s.replace('0', ' '))
