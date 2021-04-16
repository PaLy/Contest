def h(tup):
    x = 0
    y = 0
    for i in range(0, len(tup), 2):
        x += (10 ** i) * (tup[i] + 1)
    for i in range(1, len(tup), 2):
        y += (10 ** i) * (tup[i] + 1)
    return x, y


def dh(xy, r, s):
    x, y = xy
    tup = [-1] * 2 * r * s
    i = 0
    while x > 0:
        rm = x % 10
        if rm > 0:
            tup[i] = rm - 1
        x //= 10
        i += 1
    i = 0
    while y > 0:
        rm = y % 10
        if rm > 0:
            tup[i] = rm - 1
        y //= 10
        i += 1
    return tuple(tup)


def solve():
    r, s = map(int, input().split())
    initial = ()
    for i in range(s):
        for j in range(r):
            initial += (j, i)

    distFrom = {}
    distFrom[h(initial)] = (0, -1, -1, -1)

    todo = [h(initial)]
    while len(todo) > 0:
        todo2 = []
        for t in todo:
            d, _, _, _ = distFrom[t]
            tt = dh(t, r, s)

            ok = True
            for i in range(2, 2 * r * s, 2):
                if tt[i] < tt[i - 2]:
                    ok = False
                    break
            if ok:
                cur = t
                path = []
                while True:
                    _, pcur, a, b = distFrom[cur]
                    if pcur == -1:
                        break
                    path.append((a, b))
                    cur = pcur
                path.reverse()

                return d, path

            for a in range(1, r * s):
                for b in range(1, r * s - a):
                    ad = tt[:2 * a]
                    bd = tt[2 * a:2 * (a + b)]
                    rd = tt[2 * (a + b):]
                    nd = bd + ad + rd
                    hnd = h(nd)
                    ndist = d + 1
                    if hnd not in distFrom:
                        distFrom[hnd] = (ndist, t, a, b)
                        todo2.append(hnd)
        todo = todo2


t = int(input())
for tt in range(1, t + 1):
    d, p = solve()
    print("Case #" + str(tt) + ": " + str(d))
    print('\n'.join(str(a) + " " + str(b) for a, b in p))
