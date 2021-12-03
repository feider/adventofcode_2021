numbers = [0]*12
with open('input.txt', 'r') as f:
    for l in f:
        for i, bit in enumerate(l.strip()):
            if bit == '1':
                numbers[i] += 1
            else:
                numbers[i] -= 1

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
