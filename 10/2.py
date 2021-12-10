import numpy as np

ls = []
#with open('input_test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    for line in f:
        ls.append(line.strip())

chars = {
        "[": "]",
        "(": ")",
        "<": ">",
        "{": "}"
        }

scores = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
        }

def get_score(l):
    k = list(chars.keys())
    m = []
    s = 0
    for c in l:
        if c in k:
            m.append(chars[c])
        elif m[-1] == c:
            del m[-1]
        else: 
            return 0
    m = m[::-1]
    for c in m:
        s *= 5
        s += scores[c]
    return s


for l in ls:
    print(l, get_score(l))
s = [get_score(l) for l in ls if get_score(l) > 0]
print(s)
print(np.median(s))
