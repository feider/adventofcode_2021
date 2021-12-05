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
    _s = s [i, :]
    _e = e [i, :]

    
    if _s[0] == _e[0]:
        if(_s[1] <= _e[1]):
            st = _s[1]
            en = _e[1]+1
        else:
            st = _e[1]
            en = _s[1]+1

        f[_s[0], st:en] += 1

    if _s[1] == _e[1]:
        if(_s[0] <= _e[0]):
            st = _s[0]
            en = _e[0]+1
        else:
            st = _e[0]
            en = _s[0]+1
        f[st:en, _s[1]] += 1
    



o = f>1
print(f)
print(o)
print(np.sum(o[:]))



