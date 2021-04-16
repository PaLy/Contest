import math


def solve():
    n, p = input().split()
    n = int(n)
    p = float(p)
    w = []
    h = []
    for _ in range(n):
        x, y = map(int, input().split())
        w.append(x)
        h.append(y)

    d = []
    for i in range(n):
        x1 = 2 * math.sqrt(h[i] * h[i] / 4)
        x2 = 2 * math.sqrt(h[i] * h[i] / 4 + w[i] * w[i] / 4)
        x3 = 2 * math.sqrt(w[i] * w[i] / 4 + h[i] * h[i] / 4)
        x4 = 2 * math.sqrt(w[i] * w[i] / 4)
        d.append((min(x1, x2, x3, x4), max(x1, x2, x3, x4)))

    s = sum(2 * w[i] + 2 * h[i] for i in range(n))
    p -= s

    mi = d[0][0]
    ma = d[0][1]

    if p < mi:
        return s
    elif p > n * 2 * ma:
        return s + n * 2 * ma
    else:
        pok = [(0, 0)]
        for i in range(n):
            pok.append((2 * mi * (i + 1), 2 * ma * (i + 1)))
        pok.append((2 * ma * n, 2 * ma * n))
        for i in range(1, n + 2):
            if p < pok[i][0]:
                return s + min(p, pok[i - 1][1])


t = int(input())
for tt in range(1, t + 1):
    print("Case #" + str(tt) + ": " + str(solve()))
