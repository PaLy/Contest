def solve():
    n = int(input())
    m = [list(map(int, input().split())) for _ in range(n)]

    k = sum([m[i][i] for i in range(n)])
    r = sum((0 if len(set(m[i])) == n else 1) for i in range(n))

    def columnCount(i):
        return len(set([m[j][i] for j in range(n)]))

    c = sum((0 if columnCount(i) == n else 1) for i in range(n))

    return str(k) + " " + str(r) + " " + str(c)


t = int(input())
for tt in range(1, t + 1):
    print("Case #" + str(tt) + ": " + str(solve()))
