a = []
b = []
c = []
d = []
e = []
f = []

def remainder_x ():
    for x in range(0,1000,7):
        if x % 6 == 1:
            a.append(x)
        for y in (a):
            if  y % 5 == 1:
                b.append(y)
        for z in (b):
            if z % 4 == 1:
                c.append(z)
        for v in (c):
            if v % 3 == 1:
                d.append(v)
        for g in (d):
            if g % 3 == 1:
                e.append(g)
        for h in (e):
            if h % 2 == 1:
                f.append(h)
        if len(f) == 1:
            break
    print(f)
remainder_x()
