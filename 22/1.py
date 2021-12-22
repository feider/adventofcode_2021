from dataclasses import dataclass

@dataclass
class Command:
    com : str
    x : tuple
    y : tuple
    z : tuple

ip = 'input_test.txt'
ip = 'input_test2.txt'
ip = 'input.txt'


coms = []

with open (ip, "r") as f:
    for line in f:
        l = line.strip().split(' ')
        com = l[0]
        l = l[1].split(',')

        x = l[0].split('=')[1].split('..')
        x = [int(x[0]), int(x[1])]

        y = l[1].split('=')[1].split('..')
        y= [int(y[0]), int(y[1])]

        z = l[2].split('=')[1].split('..')
        z = [int(z[0]), int(z[1])]

        x[0] = max(x[0], -50)
        x[1] = min(x[1], 50)

        y[0] = max(y[0], -50)
        y[1] = min(y[1], 50)

        z[0] = max(z[0], -50)
        z[1] = min(z[1], 50)

        c = Command(com=com, x=tuple(x), y=tuple(y), z=tuple(z))
        coms.append(c)

cubes = set()

for i, c in enumerate(coms):
    print(i, c)
    for x in range(c.x[0], c.x[1]+1):
        for y in range(c.y[0], c.y[1]+1):
            for z in range(c.z[0], c.z[1]+1):
                t = (x, y, z)
                if c.com == "on":
                    cubes.add(t)
                else:
                    if t in cubes:
                        cubes.remove(t)
    print(i, len(cubes))

sum_on = 0
for c in cubes:
    x, y, z = c
    if x>=-50 and x <= 50 and y >= -50 and y <= 50 and z >= -50 and z <= 50:
        sum_on += 1

print(sum_on)

