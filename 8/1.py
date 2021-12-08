lines = []
#with open('input_test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    for l in f:
        lines.append(l.strip())

counts = {}
for line in lines:
    l = line.split('|')[1].strip().split()
    for p in l:
        n = len(p)
        if not n in counts:
            counts[n] = 0
        counts[n] += 1

for k in counts.keys():
    print(f"{k}: {counts[k]}")

li = [2, 3, 4, 7]
s = 0
for l in li:
    s += counts[l]
print(s)
