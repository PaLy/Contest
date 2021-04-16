import random


def solve():
    n = int(input())
    s = [0]*n
    used = set()
    for _ in range(n):
        l = list(map(int, input().split()))[1:]
        for x in l:
            s[x] += 1
        toUse = list()
        m = 0
        for i in range(n):
            if i in l and s[i] > m and i not in used:
                m = s[i]
                toUse = [i]
            elif i in l and s[i] == m and i not in used:
                toUse.append(i)
        if len(toUse) == 0:
            print(-1)
        else:
            u = toUse[random.randint(0, len(toUse) - 1)]
            used.add(u)
            print(u)


t = int(input())
for tt in range(1, t + 1):
    solve()
