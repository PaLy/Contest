def solve():
    n = int(input())
    a = [list(map(int, input().split())) for i in range(n)]

    for i in range(n):
        a[i].append(i)

    a.sort(key=lambda se: se[1] * 100 * 100 + se[0])

    res = [""] * n
    e1 = 0
    e2 = 0
    for se in a:
        s, e, i = se
        if e1 > e2:
            if s >= e1:
                res[i] = "C"
                e1 = e
            elif s >= e2:
                res[i] = "J"
                e2 = e
            else:
                return "IMPOSSIBLE"
        else:
            if s >= e2:
                res[i] = "J"
                e2 = e
            elif s >= e1:
                res[i] = "C"
                e1 = e
            else:
                return "IMPOSSIBLE"
    return "".join(res)



t = int(input())
for tt in range(1, t + 1):
    print("Case #" + str(tt) + ": " + str(solve()))
