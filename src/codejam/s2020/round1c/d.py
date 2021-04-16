def solve_easy():
    r, c = map(int, input().split())
    df = [list(map(int, input().split())) for _ in range(r)]

    ilr = sum(sum(x for x in row) for row in df)
    il = ilr

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while True:
        el = [[0] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if df[i][j] != 0:
                    ns = []
                    for d in range(4):
                        ci = i
                        cj = j
                        ci += dx[d]
                        cj += dy[d]
                        while 0 <= ci < r and 0 <= cj < c:
                            if df[ci][cj] != 0:
                                ns.append(df[ci][cj])
                                break
                            else:
                                ci += dx[d]
                                cj += dy[d]
                    if len(ns) > 0 and df[i][j] < sum(ns) / len(ns):
                        el[i][j] = 1
        for i in range(r):
            for j in range(c):
                if el[i][j]:
                    df[i][j] = 0

        cilr = sum(sum(x for x in row) for row in df)
        if cilr == ilr:
            break
        else:
            il += cilr
            ilr = cilr
    return il


def solve_hard():
    r, c = map(int, input().split())
    df = [list(map(int, input().split())) for _ in range(r)]

    e = [[col - 1 for col in range(c)] for row in range(r)]
    w = [[col + 1 for col in range(c)] for row in range(r)]
    n = [[row - 1 for col in range(c)] for row in range(r)]
    s = [[row + 1 for col in range(c)] for row in range(r)]

    ilr = sum(sum(x for x in row) for row in df)
    il = 0

    elim = set()
    check = [[row, col] for row in range(r) for col in range(c)]

    while len(check) > 0:
        il += ilr
        # print(ilr)
        e2 = [x.copy() for x in e]
        w2 = [x.copy() for x in w]
        n2 = [x.copy() for x in n]
        s2 = [x.copy() for x in s]

        next_check = set()
        for row, col in check:
            en = e[row][col]
            wn = w[row][col]
            nn = n[row][col]
            sn = s[row][col]
            n_count = 0
            n_sum = 0
            if 0 <= en:
                n_count += 1
                n_sum += df[row][en]
            if wn < c:
                n_count += 1
                n_sum += df[row][wn]
            if 0 <= nn:
                n_count += 1
                n_sum += df[nn][col]
            if sn < r:
                n_count += 1
                n_sum += df[sn][col]

            if n_count > 0 and n_sum / n_count > df[row][col]:
                if (row, col) in next_check:
                    next_check.remove((row, col))

                ilr -= df[row][col]
                en = e2[row][col]
                wn = w2[row][col]
                nn = n2[row][col]
                sn = s2[row][col]
                if 0 <= en:
                    w2[row][en] = wn
                    next_check.add((row, en))
                if wn < c:
                    e2[row][wn] = en
                    next_check.add((row, wn))
                if 0 <= nn:
                    s2[nn][col] = sn
                    next_check.add((nn, col))
                if sn < r:
                    n2[sn][col] = nn
                    next_check.add((sn, col))

        e = e2
        w = w2
        n = n2
        s = s2
        check = list(next_check)

    return il


t = int(input())
for tt in range(1, t + 1):
    print("Case #" + str(tt) + ": " + str(solve_hard()))
