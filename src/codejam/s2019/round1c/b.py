import sys


def solve():
    d = [{'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0} for _ in range(5)]

    for p in range(118):
        for i in range(4):
            print(p * 5 + i + 1)
            x = input()
            d[i][x] += 1
    for i in range(3):
        print(118 * 5 + i + 1)
        x = input()
        d[i][x] += 1

    res = ""
    for i in range(4):
        dd = d[i]
        m = 1000
        mc = 'x'
        for c in 'ABCDE':
            if dd[c] < m:
                m = dd[c]
                mc = c
        res += mc

    for c in 'ABCDE':
        if c not in res:
            res += c

    # sys.stderr.write(res)
    # sys.stderr.write("\n")

    print(res)
    r = input()
    if r == 'N':
        exit(0)


t, f = map(int, input().split())
for tt in range(1, t + 1):
    solve()
