
#ip = 'input_test.txt'
ip = 'input.txt'


l = []
with open(ip, 'r') as f:
    for lines in f:
        l.append(lines.strip())

com = l[2:]
s = l[0].strip()

print(0, s)
print(0, len(s))

test_cases = [
'NCNBCHB',
'NBCCNBBBCBHCB',
'NBBBCNCCNBBNBNBBCHBHHBCHB',
'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB']
for i in range(1,11):
    for c in com:
        a,b=c.split(' -> ')
        b = a[0]+'_'+b.strip()+'_'+a[1]
        s_old = s
        while True:
            s = s.replace(a, b)
            if s == s_old: break
            s_old = s
            

    s = s.replace('_', '')
    

n = []
for e in set(s):
    n.append(s.count(e))
print(max(n))
print(min(n))
print(max(n)-min(n))
