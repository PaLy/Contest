IMPOS = "IMPOSSIBLE"
POS = "POSSIBLE"


def solve():
    r, c, h, v = map(int, input().split())
    m = [input() for _ in range(r)]
    s = sum([1 for i in range(r) for j in range(c) if m[i][j] == '@'])

    if s == 0:
        return POS
    elif s % ((h + 1) * (v + 1)) > 0:
        return IMPOS
    else:
        s1 = s / ((h + 1) * (v + 1))
        cc = 0
        dv = 0
        ver_cuts = [0]
        for i in range(c):
            for j in range(r):
                if m[j][i] == '@':
                    cc += 1
            if cc == s1 * (h + 1):
                cc = 0
                dv += 1
                ver_cuts.append(i + 1)

        if dv != v + 1 or cc > 0:
            return IMPOS

        cc = 0
        dv = 0
        hor_cuts = [0]
        for i in range(r):
            for j in range(c):
                if m[i][j] == '@':
                    cc += 1
            if cc == s1 * (v + 1):
                cc = 0
                dv += 1
                hor_cuts.append(i + 1)
        if dv != h + 1 or cc > 0:
            return IMPOS

        for i in range(h + 1):
            for j in range(v + 1):
                ss = 0
                for k in range(hor_cuts[i], hor_cuts[i + 1]):
                    for l in range(ver_cuts[i], ver_cuts[i + 1]):
                        if m[k][l] == '@':
                            ss += 1
                if ss != s1:
                    return IMPOS

        return POS


t = int(input())
for tt in range(1, t + 1):
    print("Case #" + str(tt) + ": " + str(solve()))
