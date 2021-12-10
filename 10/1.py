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
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
        }

def get_score(l):
    k = list(chars.keys())
    v = list(chars.values())
    m = []
    s = 0
    for c in l:
        if c in k:
            m.append(chars[c])
        elif m[-1] == c:
            del m[-1]
        else:
            return scores[c]
    return 0


print(np.sum([get_score(l) for l in ls]))
