nbits = 12
#nbits = 5
numbers = [0]*nbits

b = []
with open('input.txt', 'r') as f:
#with open('input_test.txt', 'r') as f:
    for l in f:
        for i, bit in enumerate(l.strip()):
            if bit == '1':
                numbers[i] += 1
            else:
                numbers[i] -= 1
        b.append(l.strip())

gam = ''
eps = ''


for n in numbers:
    if n > 0:
        gam += '1'
        eps += '0' 
    else:
        gam += '0'
        eps += '1'

print(int(gam, 2)*int(eps, 2))


o = [bn for bn in b]
i = 0
while(len(o) > 1):
    numbers = [0]*nbits
    for bn in o:
        for j, bit in enumerate(bn):
            if bit == '1':
                numbers[j] += 1
            else:
                numbers[j] -= 1
    onew = []
    for bn in o:
        if numbers[i] >= 0:
            bit = '1'
        else:
            bit = '0'
        if bn[i] == bit:
            onew.append(bn)
    o = onew
    i+= 1
print(numbers)
o = o[0]
print(o)
print(int(o, 2))

g = [bn for bn in b]
i = 0
while(len(g) > 1):
    numbers = [0]*nbits
    for bn in g:
        for j, bit in enumerate(bn):
            if bit == '1':
                numbers[j] += 1
            else:
                numbers[j] -= 1
    onew = []
    for bn in g:
        if numbers[i] >= 0:
            bit = '0'
        if numbers[i] < 0:
            bit = '1'
        if bn[i] == bit:
            onew.append(bn)
    g = onew
    i+= 1

g = g[0]
print(int(g, 2))

print(int(o, 2)*int(g, 2))
