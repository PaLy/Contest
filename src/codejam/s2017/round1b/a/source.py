def solve():
    d, n = map(int, input().split())
    x = [tuple(map(int, input().split())) for _ in range(n)]
    x.sort(reverse=True)

    t = 0

    for ks in x:
        k, s = ks
        t = max(t, (d - k) * 1.0 / s)

    return d * 1.0 / t


t = int(input())
for tt in range(1, t + 1):
    print("Case #" + str(tt) + ": " + str(solve()))
