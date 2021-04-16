def solve():
    n, k, v = map(int, input().split())
    a = [(0, i, input()) for i in range(n)]

    kn = k * n
    v %= kn
    if v == 0:
        v = kn

    for i in range(v):
        a.sort()
        for j in range(k):
            a[j] = (a[j][0] + 1, a[j][1], a[j][2])

    r = a[:k]
    r.sort(key=lambda x: x[1])
    return " ".join(x[2] for x in r)


def main():
    for t in range(int(input())):
        print('Case #{}:'.format(t + 1), solve())


if __name__ == '__main__':
    main()
