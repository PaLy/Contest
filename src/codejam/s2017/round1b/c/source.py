def solve():
    n, q = map(int, input().split())
    e = [-1] * n
    s = [-1] * n
    for i in range(n):
        x, y = map(int, input().split())
        e[i] = x
        s[i] = y

    d = [list(map(int, input().split())) for _ in range(n)]
    u = [-1] * q
    v = [-1] * q
    for i in range(q):
        x, y = map(int, input().split())
        u[i] = x
        v[i] = y

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if (d[j][k] == -1 or d[j][k] > d[j][i] + d[i][k]) and d[j][i] > - 1 and d[i][k] > - 1:
                    d[j][k] = d[j][i] + d[i][k]

    t = [[-1 for _ in range(n)] for _ in range(n)]

    for st in range(n):
        for i in range(n):
            if e[st] >= d[st][i] and d[st][i] > - 1:
                t[st][i] = d[st][i] * 1.0 / s[st]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if (t[j][k] == -1 or t[j][k] > t[j][i] + t[i][k]) and t[j][i] > - 1 and t[i][k] > - 1:
                    t[j][k] = t[j][i] + t[i][k]

    res = [-1] * q
    for qi in range(q):
        res[qi] = t[u[qi] - 1][v[qi] - 1]
    return ' '.join(str(x) for x in res)


t = int(input())
for tt in range(1, t + 1):
    print("Case #" + str(tt) + ": " + str(solve()))
