MOD = 10 ** 9 + 7

cache_bc = dict()
cache_fac = dict()


def factorial(x):
    if x in cache_fac:
        return cache_fac[x]
    res = 1
    for i in range(x):
        res *= i + 1
        res %= MOD
    cache_fac[x] = res
    return res


def bc(n, k):
    tup = (n, k)
    if tup in cache_bc:
        return cache_bc[tup]
    nf = 1
    for i in range(k):
        nf *= n - i
        nf %= MOD
    kf = factorial(k)
    pkf = pow(kf, MOD - 2, MOD)
    res = (nf * pkf) % MOD
    cache_bc[tup] = res
    # print(n, k, res, "bc")
    return res


def solve():
    n, m = map(int, input().split())
    r = [int(input()) for _ in range(n)]
    sum_r = 2 * sum(r)

    def count(first, last):
        other_sum = sum_r - 2 * r[first] - 2 * r[last]
        places = m - 1 - r[first] - r[last]
        spaces = places - other_sum
        if spaces < 0:
            return 0
        else:
            divs = n - 2
            print(other_sum, places, spaces, divs)
            x = bc(spaces + divs, divs) * factorial(n - 2)
            return x

    res = 0
    for first in range(n):
        for last in range(n):
            if first != last:
                c = count(first, last)
                # print(first, last, c)
                res += c
                res %= MOD
    return res


def main():
    for t in range(int(input())):
        print('Case #{}:'.format(t + 1), solve())


if __name__ == '__main__':
    main()
