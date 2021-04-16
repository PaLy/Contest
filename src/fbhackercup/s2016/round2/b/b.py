import math

import sys

sys.setrecursionlimit(1000000)


def solve():
    n, k, p = input().split()
    n = int(n)
    k = int(k)
    p = float(p)

    cache = dict()

    def best(n):
        if n in cache:
            return cache[n]
        elif n < k:
            return 0
        else:
            res = 0
            for m in range(1, n + 1):
                res = max(res, hod(m) + best(n - m))
            cache[n] = res
            return res

    cacheh = dict()

    def hod(m):
        if m in cacheh:
            return cacheh[m]
        res = 0
        for i in range(k, m + 1):
            res += math.pow(p, i) * math.pow(1 - p, m - i)
        cacheh[m] = res
        return res

    return best(n)


def main():
    for t in range(int(input())):
        print('Case #{}:'.format(t + 1), solve())


if __name__ == '__main__':
    main()
