d=100
nd = 0

def get_d():
    global d
    global nd
    d+=1
    nd+=1
    if d > 100: d=1
    return d

p1 = 4-1
p2 = 8-1
#p1 = 10-1
#p2 = 2-1

sp1 = 0
sp2 = 0

while True:
    #p1
    ds = 0
    for i in range(3):
        ds += get_d()
    p1 += ds
    p1 %= 10
    sp1 += (p1+1)
    if sp1 >= 1000:
        print(sp2*nd)
        exit()

    #p1
    ds = 0
    for i in range(3):
        ds += get_d()
    p2 += ds
    p2 %= 10
    sp2 += (p2+1)
    if sp2 >= 1000:
        print(sp1*nd)
        exit()

