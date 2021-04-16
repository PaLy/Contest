def solve():
    n = int(input())
    v = list(map(int, input().split()))
    v = [(v[i], i % 2) for i in range(n)]
    v.sort()

    i = 0
    while i < n:
        si = i
        num = v[i][0]
        enums = 0
        onums = 0
        for j in range(i, n):
            if v[j][0] != num:
                break
            else:
                if v[j][1] == 0:
                    enums += 1
                else:
                    onums += 1
                i += 1
        for k in range(si, i):
            if k % 2 == 0:
                if enums > 0:
                    enums -= 1
                else:
                    return k
            else:
                if onums > 0:
                    onums -= 1
                else:
                    return k
    return "OK"


t = int(input())
for tt in range(1, t + 1):
    print("Case #" + str(tt) + ": " + str(solve()))
