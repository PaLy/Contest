import sys

sys.setrecursionlimit(100000000)


def solve():
    n, m = map(int, input().split())
    mapa = [input() for _ in range(n)]

    cache = {}

    def best(i, j, s, f):
        tup = (i, j, s, f)
        if mapa[i][j] == '#':
            return -1
        elif tup in cache:
            return cache[tup]
        else:
            res = 1 if i == n - 1 and j == m - 1 else -1
            if i < n - 1 and f != 3:
                x = best(i + 1, j, s, 1)
                res = max(res, x + 1)
            if j < m - 1 and f != 2:
                x = best(i, j + 1, s, 4)
                if x != - 1:
                    res = max(res, x + 1)
            if s == 0:
                if f != 1:
                    iii = i
                    while iii >= 0 and mapa[iii][j] == '.':
                        iii -= 1
                    iii = max(iii, 0)
                    for ii in range(iii, i):
                        x = best(ii, j, 1, 3)
                        if x > -1:
                            res = max(res, x + i - ii)
                if f != 4:
                    jjj = j
                    while jjj >= 0 and mapa[i][jjj] == '.':
                        jjj -= 1
                    jjj = max(jjj, 0)
                    for jj in range(jjj, j):
                        x = best(i, jj, 1, 2)
                        if x > -1:
                            res = max(res, x + j - jj)
            cache[tup] = res
            return cache[tup]

    res = best(0, 0, 0, 0)
    return res


def main():
    for t in range(int(input())):
        print('Case #{}:'.format(t + 1), solve())


if __name__ == '__main__':
    main()