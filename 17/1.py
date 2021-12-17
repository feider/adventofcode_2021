from tqdm import tqdm
#ta = [143,177,-106,-71]
ta = [143,177,-106,-71]
#ta = [20,30,-10,-5]
xmin = min(ta[:2])
xmax = max(ta[:2])
ymin = min(ta[2:])
ymax = max(ta[2:])
print(xmin, xmax, ymin, ymax)

def check_if_in(dx, dy):
    ym = 0
    x=0
    y=0
    while(y >= ymin and x<=xmax):
        x+=dx
        y+=dy
        if dx > 0: dx-= 1
        if dx < 0: dx+= 1
        #if dy > 0: dy-= 1
        #if dy < 0: dy+= 1
        dy -= 1
        if ym < y: ym=y

#        print(x, y, dx, dy)

        if x >= xmin and x <= xmax and y>=ymin and y <= ymax:
            return True, ym
    return False, None


ys = []
xm = max(abs(xmin),abs(xmax))
for x in tqdm(range(xm)):
    for y in range(ymin, 1000):
        r, ym = check_if_in(x,y)
        if r:
            ys.append(ym)
print(max(ys))


