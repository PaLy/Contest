def solve():
    n, a, b = map(int, input().split())
    c = list(map(int, input().split()))
    s = sum(c)
    I = b - a
    rc = I // s

    res = 0

    if rc >= 1:
        i = 0
        aa = a
        aa %= s
        while aa - c[i] > 0:
            aa -= c[i]
            i += 1
        interval = min(c[i] - aa, b - a)
        if interval > 0:
            res += interval / I * avg(aa, aa + interval)
        a += interval

        if interval > 0:
            i += 1
        for j in range(i, n):
            interval = min(c[j], b - a)
            a += interval
            res += interval / I * avg(0, interval)

    zr = (b - a) // s
    if zr >= 1:
        rr = 0
        for j in range(n):
            interval = c[j]
            a += interval
            rr += interval / I * avg(0, interval)
        res += zr * rr
        a += (zr - 1) * s

    i = 0
    zc = b - a
    xa = a % s
    while zc > 0:
        interval = min(zc, c[i])
        res += interval / I * avg(xa, xa + interval)
        xa = 0
        zc -= interval
        i += 1

    return res


def avg(a, b):
    return (a + b) / 2


def main():
    for t in range(int(input())):
        print('Case #{}:'.format(t + 1), solve())


if __name__ == '__main__':
    main()
