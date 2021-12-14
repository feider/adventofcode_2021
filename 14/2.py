from collections import Counter

#ip = 'input_test.txt'
ip = 'input.txt'

l = []
with open(ip, 'r') as f:
    for lines in f:
        l.append(lines.strip())

com = l[2:]
s = l[0].strip()

assignments = {}
for c in com:
    a,b=c.strip().split(' -> ')
    assignments[a]=b

pc = Counter()
for i in range(len(s)-1):
    pc[s[i]+s[i+1]]+=1

for i in range(40):
    cnew = Counter()
    for pair in pc:
        a=assignments[pair]
        cnew[pair[0]+a] += pc[pair]
        cnew[a+pair[1]] += pc[pair]
    pc = cnew

char_c = Counter()
for pair in pc:
    char_c[pair[0]] += pc[pair]
char_c[s[-1]]+=1

print(char_c)

print(max(char_c.values())-min(char_c.values()))
