def solve():
    l, n = input().split()
    n = int(n)
    e = len(l)
    c = 0
    ll = 1
    while c + e < n:
        ll += 1
        c += e
        e *= len(l)
    n -= c
    e //= len(l)
    res = ''
    while e > 1:
        x = n // e
        res += l[x]
        n %= e
        e //= len(l)
    res += l[n // e - 1]
    k = len(res)
    for i in range(ll - k):
        res = l[0] + res
    return res


def main():
    for t in range(int(input())):
        print('Case #{}:'.format(t + 1), solve())


if __name__ == '__main__':
    main()