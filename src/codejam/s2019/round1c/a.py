def solve():
    a = int(input())
    c = [input() for _ in range(a)]

    beat = {
        'R': 'S',
        'P': 'R',
        'S': 'P'
    }
    ibeat = {
        'R': 'P',
        'P': 'S',
        'S': 'R'
    }

    res = ""
    btn = set()
    for pos in range(243):
        x = set()
        for i in range(a):
            if i not in btn:
                opp = c[i]
                x.add(opp[pos % len(opp)])

        if len(x) == 1:
            res += ibeat[next(iter(x))]
            return res
        elif len(x) == 3:
            return "IMPOSSIBLE"
        else:
            it = iter(x)
            one = next(it)
            two = next(it)
            tor = []
            for k in x:
                tor.append(beat[k])
            x.discard(tor[0])
            x.discard(tor[1])
            res += next(iter(x))

            if one == res[-1]:
                other = two
            else:
                other = one

            for i in range(a):
                if i not in btn:
                    opp = c[i]
                    if other == opp[pos % len(opp)]:
                        btn.add(i)

    for lenme in range(1, len(res)):
        me = res[:lenme]
        ok = True
        beaten = set()
        for pos in range(243):
            for oi in range(len(c)):
                if oi not in beaten:
                    opp = c[oi]
                    oppc = opp[pos % len(opp)]
                    mec = me[pos % len(me)]
                    if beat[oppc] == mec:
                        ok = False
                        break
                    elif beat[mec] == oppc:
                        beaten.add(oi)
            if not ok:
                break
            if len(beaten) == len(c):
                return me

    return "IMPOSSIBLE"





t = int(input())
for tt in range(1, t + 1):
    print("Case #" + str(tt) + ": " + str(solve()))
