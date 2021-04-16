def solve():
    n = int(input())
    if n == 0:
        res = "INSOMNIA"
    else:
        s = set()
        x = n
        res = x
        while len(s) < 10:
            s.update((c for c in str(x)))
            res = x
            x += n
    return res


t = int(input())
for tt in range(1, t + 1):
    print("Case #" + str(tt) + ":", solve())
