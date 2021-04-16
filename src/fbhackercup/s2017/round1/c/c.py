import sys

sys.setrecursionlimit(1000000000)
# ulimit -s 16384


def solve():
    INF = 99999999999999999

    n, m, kk = map(int, input().split())
    g = [[INF] * n for _ in range(n)]
    for i in range(n):
        g[i][i] = 0
    for _ in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        g[a][b] = g[b][a] = c
    fam = [(0, 0)] + [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(kk)]

    dp = [[INF] * 2 for _ in range(kk + 1)]
    dp[0][0] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])

    cache = dict()
    path = dict()

    def print_path(x):
        y = path[x] if x in path else None
        print(x, "->", y)
        if y:
            print_path(y)

    def count(where, delivered, loaded1, loaded2):
        if delivered == kk:
            return 0

        tup = (where, delivered, loaded1, loaded2)
        if tup in cache:
            return cache[tup]
        else:
            res = INF

            if loaded2 > 0:
                res = deliver(tup, loaded1, loaded2, res, where)
            elif loaded1 > 0:
                res = deliver(tup, loaded1, loaded2, res, where)
                res = pick(tup, delivered, loaded1, res, where)
            else:
                res = pick(tup, delivered, loaded1, res, where)

            cache[tup] = res
            return res

    def pick(tup, delivered, loaded1, res, where):
        next_pick = max(delivered, loaded1) + 1
        if next_pick <= kk:
            next_to = fam[next_pick][0]
            dist = g[where][next_to]
            if dist != INF:
                if loaded1 == 0:
                    loaded1 = next_pick
                    loaded2 = 0
                else:
                    loaded2 = next_pick
                next_res = min(res, count(next_to, delivered, loaded1, loaded2) + dist)
                if next_res < res:
                    res = next_res
                    # path[tup] = (next_to, delivered, loaded1, loaded2)
        return res

    def deliver(tup, loaded1, loaded2, res, where):
        del_to = fam[loaded1][1]
        dist = g[where][del_to]
        if dist != INF:
            next_res = min(res, count(del_to, loaded1, loaded2, 0) + dist)
            if next_res < res:
                res = next_res
                # path[tup] = (del_to, loaded1, loaded2, 0)
        return res

    res = count(0, 0, 0, 0)
    # print_path((0, 0, 0, 0))
    return -1 if res == INF else res


def main():
    for t in range(int(input())):
        print('Case #{}:'.format(t + 1), solve())


if __name__ == '__main__':
    main()
