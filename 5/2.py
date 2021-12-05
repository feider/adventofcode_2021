import numpy as np

start = []
end = []
with open('input.txt', 'r') as f:
#with open('input_test.txt', 'r') as f:
    for l in f:
        line = l.strip().split(' -> ')
        start.append([int(i) for i in line[0].split(',')])
        end.append([int(i) for i in line[1].split(',')])

n = len(start)

a = start+end

s = np.asarray(start)
e = np.asarray(end)
a = np.asarray(a)
f = np.zeros([np.max(a)+1, np.max(a)+1])


for i in range(n):
    print("")
    print(i)
    _s = s [i, :]
    _e = e [i, :]

    print(_s)
    print(_e)

    
    if _s[0] == _e[0]:
        st = np.min([_s[1], _e[1]])
        en = np.max([_s[1], _e[1]])+1
        f[_s[0], st:en] += 1

    elif _s[1] == _e[1]:
        st = np.min([_s[0], _e[0]])
        en = np.max([_s[0], _e[0]])+1
        f[st:en, _s[1]] += 1

    elif _s[0] < _e[0] and _s[1] < _e[1]:
        x = list(range(_s[0], _e[0]+1))
        y = list(range(_s[1], _e[1]+1))
        for _x, _y in zip(x, y):
            f[_x, _y] += 1

    elif _s[0] > _e[0] and _s[1] < _e[1]:
        x = list(range(_s[0], _e[0]-1, -1))
        y = list(range(_s[1], _e[1]+1))
        for _x, _y in zip(x, y):
            f[_x, _y] += 1

    elif _s[0] > _e[0] and _s[1] > _e[1]:
        x = list(range(_s[0], _e[0]-1, -1))
        y = list(range(_s[1], _e[1]-1, -1))
        for _x, _y in zip(x, y):
            f[_x, _y] += 1

    elif _s[0] < _e[0] and _s[1] > _e[1]:
        x = list(range(_s[0], _e[0]+1))
        y = list(range(_s[1], _e[1]-1, -1))
        for _x, _y in zip(x, y):
            f[_x, _y] += 1
    
    print(np.transpose(f))
    



o = f>1
print(np.transpose(f))
print(np.transpose(o))
print(np.sum(o[:]))
