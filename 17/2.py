from tqdm import tqdm
#ta = [143,177,-106,-71]
ta = [143,177,-106,-71]
#ta = [20,30,-10,-5]
xmin = min(ta[:2])
xmax = max(ta[:2])
ymin = min(ta[2:])
ymax = max(ta[2:])
print(xmin, xmax, ymin, ymax)
debug = False
#debug = True

def check_if_in(dx, dy):
    ym = 0
    x=0
    y=0
    if debug: print("enter with", dx, dy)
    while(y >= ymin and x<=xmax):
        x+=dx
        y+=dy
        if dx > 0: dx-= 1
        if dx < 0: dx+= 1
        #if dy > 0: dy-= 1
        #if dy < 0: dy+= 1
        dy -= 1
        if ym < y: ym=y
        if(debug):
            print(x, y, dx, dy)

        if x >= xmin and x <= xmax and y>=ymin and y <= ymax:
            return True, ym
    return False, None


if debug:
    x=30
    y=-9
    print(check_if_in(x,y))
    exit()

ys = []
xm = max(abs(xmin),abs(xmax))
ni = 0
for x in tqdm(range(xm*2)):
    for y in range(ymin*2, 250):
        r, ym = check_if_in(x,y)
        if r: 
            ni+=1
print(ni)


