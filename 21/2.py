d=100
nd = 0


p1 = 4-1
p2 = 8-1
#p1 = 10-1
#p2 = 2-1

sp1 = 0
sp2 = 0

outcomes = []
for a in range(1, 4):
    for b in range(1, 4):
        for c in range(1,4):
            outcomes.append(a+b+c)


results = {}

def play(p1, p2, sp1, sp2, player):

    p = (p1, p2, sp1, sp2, player)
    if p in results:
        return results[p]

    wp1 =0
    wp2 =0


    for ds in outcomes:
        if player == 1:
            _p1 = p1+ds
            _p1 %= 10
            _sp1 = sp1+(_p1+1)
            if _sp1 >= 21:
                wp1 += 1
            else:
                _wp1, _wp2 = play(_p1, p2, _sp1, sp2, 2)
                wp1 += _wp1
                wp2 += _wp2
        elif player == 2:
            _p2 = p2+ds
            _p2 %= 10
            _sp2 = sp2+(_p2+1)
            if _sp2 >= 21:
                wp2 += 1
            else:
                _wp1, _wp2 = play(p1, _p2, sp1, _sp2, 1)
                wp1 += _wp1
                wp2 += _wp2
        else:
            print("🤡")
            exit()

    results[p] = [wp1, wp2]
    return wp1, wp2

#wp1, wp2 = play(4-1, 8-1, 0, 0, 1)
wp1, wp2 = play(10-1, 2-1, 0, 0, 1)

print(max(wp1, wp2))
