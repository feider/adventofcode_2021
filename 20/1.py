#ip = 'input_test.txt'
ip = 'input.txt'

padding = "."

lines = []
with open(ip, 'r') as f:
    input_lines = [l.strip() for l in f]

code = input_lines[0]
lines = input_lines[2:]

def expand(lines, padding):
    dots = padding*len(lines[0])
    lines = [dots]+lines+[dots]
    for i in range(len(lines)):
        lines[i] = padding+lines[i]+padding
    return lines

def get_point(lines, i, j, padding):
    if i<0 or j<0 or i>=len(lines) or j>=len(lines[0]): return padding
    return lines[i][j]

def get_new_padding(padding):
    padding = '0' if padding=='.' else '1'
    return code[int(padding*9, 2)]

for i in range(2):
    lines = expand(lines, padding)

for l in lines:
    print(l)
print()


for repetition in range(1, 2+1):
    print(repetition)
    lines = expand(lines, padding)

    lines_new = lines.copy()

    for i in range(len(lines)):
        l = lines[i]
        for j in range(len(l)):
            b = ''
            for mi in range(i-1, i+2):
                for mj in range(j-1, j+2):
                    c = get_point(lines, mi, mj, padding)
                    if c =='.': b+= "0"
                    else: b+= "1"
            if b == '000100010' and False:
                print()
                print(lines[i-1][j-1:j+2])
                print(lines[i][j-1:j+2])
                print(lines[i+1][j-1:j+2])
                print()
                exit()
            num = int(b, 2)
            lines_new[i] = lines_new[i][:j]+code[num]+lines_new[i][j+1:]
    padding = get_new_padding(padding)
    lines = lines_new
    for l in lines:
        print(l)
    print()

# cut off border

s = sum([l.count('#') for l in lines])
print(s)

