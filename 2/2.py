
horizontal = 0
depth = 0

aim = 0

with open('input.txt', 'r') as f:
#with open('input_test.txt', 'r') as f:
    for l in f:
        line = l.strip().split(' ')
        command = line[0]
        num = int(line[1])
        if command == 'forward':
            horizontal += num
            depth += (aim*num)
        if command == 'down':
            aim += num
        if command == 'up':
            aim -= num

print(horizontal*depth)
