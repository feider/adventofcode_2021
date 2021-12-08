lines = []
u = set.union
#with open('input_test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    for l in f:
        lines.append(l.strip())

def get_key(d, v):
    for k in list(d.keys()):
        if d[k] == v:
            return k

def stos(s):
    return "".join(sorted(list(s)))

out = 0

for line in lines:
    nums, res = line.split('|')
    nums = [set(n) for n in nums.strip().split()]
    res = [set(r) for r in res.strip().split()]

    num = {}

    num[1] = [n for n in nums if len(n)==2]
    assert(len(num[1]) == 1)
    num[1] = num[1][0]

    num[4] = [n for n in nums if len(n)==4]
    assert(len(num[4]) == 1)
    num[4] = num[4][0]

    num[7] = [n for n in nums if len(n)==3]
    assert(len(num[7]) == 1)
    num[7] = num[7][0]

    num[8] = [n for n in nums if len(n)==7]
    assert(len(num[8]) == 1)
    num[8] = num[8][0]
    # 1 4 7 8
    num[9] = [n for n in nums if len(n)==6 and len(n - u(num[4], num[7])) == 1]
    assert(len(num[9]) == 1)
    num[9] = num[9][0]
    # 1 4 7 8 9
    num[0] = [n for n in nums if len(n)==6 and all(_n in n for _n in num[7]) and not n == num[9]]
    assert(len(num[0]) == 1)
    num[0] = num[0][0]
    # 0 1 4 7 8 9
    num[3] = [n for n in nums if len(n)==5 and all(_n in n for _n in num[7])]
    assert(len(num[3]) == 1)
    num[3] = num[3][0]
    # 0 1 3 4 7 8 9
    num[6] = [n for n in nums if len(n)==6 and not n==num[9] and not n==num[0]]
    assert(len(num[6]) == 1)
    num[6] = num[6][0]
    # 0 1 3 4 6 7 8 9
    num[2] = [n for n in nums if len(n) == 5 and next(iter(num[8]-num[9])) in n]
    assert(len(num[2]) == 1)
    num[2] = num[2][0]
    # 0 1 2 3 4 6 7 8 9 only 5 missing now :)
    num[5] = [n for n in nums if len(n) == 5 and not n == num[3] and not n == num[2]]
    assert(len(num[5]) == 1)
    num[5] = num[5][0]

    rstr = ''
    for r in res:
        rstr += str(get_key(num, r))

    out += int(rstr)
print(out)

