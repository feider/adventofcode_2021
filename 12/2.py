
import numpy as np

c = {}

#fn = 'input_test.txt'
#fn = 'input_sl.txt'
fn = 'input.txt'

ls = []

with open(fn, 'r') as f:
    for l in f:
        _l = l.strip().split('-')
        ls.append((_l[0], _l[1]))
        if not _l[0] in c:
            c[_l[0]] = []
        c[_l[0]].append(_l[1])
        if not _l[1] in c:
            c[_l[1]] = []
        c[_l[1]].append(_l[0])



ps = [[]]
o = ['start']
vs = [False]

ct = 0

while len(o) > 0:
    n = o.pop()
    p = ps.pop()
    v = vs.pop()
    if n == 'end':
        print(p)
        ct += 1
        continue
    try:
        ts = c[n]
    except:
        ts = []
    for t in ts:
        vc = v
        #print(n, '-', t)
        if t == 'start':
            continue
        if t.islower() and t in p:
            if vc:
                continue
            else:
                vc = True
        pc = p.copy()
        pc.append(n)
        ps.append(pc)
        o.append(t)
        vs.append(vc)
    #print(len(o), ct)
print(ct)

    
