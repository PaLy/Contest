from collections import defaultdict


def solve():
    n, k = map(int, input().split())

    d = defaultdict(int)
    d[n] = 1

    while True:
        key = sorted(d.keys(), reverse=True)[0]
        a = d[key]
        if a < k:
            k -= a
            d.pop(key)

            nkey = key // 2
            if key % 2 == 1:
                if nkey > 0:
                    d[nkey] = d[nkey] + 2 * a
            else:
                if nkey > 0:
                    d[nkey] = d[nkey] + a
                if nkey > 1:
                    d[nkey - 1] = d[nkey - 1] + a
        else:
            break

    lastKey = sorted(d.keys(), reverse=True)[0]
    ma = lastKey // 2
    mi = ma if lastKey % 2 == 1 else ma - 1
    return str(ma) + " " + str(mi)


t = int(input())
for tt in range(1, t + 1):
    print("Case #" + str(tt) + ": " + str(solve()))
