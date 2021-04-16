def solve():
    n, m, k = map(int, input().split())
    g = [[-1] * n for _ in range(n)]
    for i in range(n):
        g[i][i] = 0
    for _ in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        g[a][b] = g[b][a] = c
    fam = [(0, 0)] + [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(k)]

    INF = 99999999999999999
    dp = [[INF] * 2 for _ in range(k + 1)]
    dp[0][0] = 0

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if g[i][k] != -1 and g[k][j] != -1:
                    g[i][j] = min(g[i][j], g[i][k] + g[k][j])

    def count(last_deli, loaded1, loaded2, was_loading):
        if loaded1 == 0:
            print("FUCK!")
            loaded1 = loaded2
            loaded2 = 0

        res = INF

        if was_loading:
            if loaded2 > 0:
                from_load1_to_load2 = g[fam[loaded1][0]][fam[loaded2][0]]
                if from_load1_to_load2 != -1:
                    res = min(res, count(last_deli, loaded1, 0, 1) + from_load1_to_load2)

                from_last_deli_to_load2 = g[fam[last_deli][1]][fam[loaded2][0]]
                if from_last_deli_to_load2 != -1:
                    res = min(res, count(last_deli, loaded1, 0, 0) + from_last_deli_to_load2)
            elif loaded1 > 0:
                from_last_deli_to_load1 = g[fam[last_deli][1]][fam[loaded1][0]]
                if from_last_deli_to_load1 != -1:
                    res = min(res, count(last_deli, 0, 0, 0) + from_last_deli_to_load1)
            else:
                print("FUCK!")
        else:
            if last_deli == 0:
                print("FUCK")
            else:
                if loaded2 > 0:
                    print("FUCK!")
                elif loaded1 > 0:
                    from_load1_to_last_deli = g[fam[loaded1][0]][fam[last_deli][1]]
                    if from_load1_to_last_deli != -1:
                        res = min(res, count(last_deli - 1, last_deli, loaded1, 1) + from_load1_to_last_deli)
                else:
                    from_last_deli_load_to_last_deli = g[fam[last_deli][0]][fam[last_deli][1]]
                    if from_last_deli_load_to_last_deli != -1:
                        res = min(res, count(last_deli - 1, last_deli, 0, 1) + from_last_deli_load_to_last_deli)

                    from_prev_deli_to_deli = g[fam[last_deli - 1][1]][fam[last_deli][1]]
                    if from_prev_deli_to_deli != -1:
                        res = min(res, count(last_deli - 1, last_deli, 0, 0) + from_prev_deli_to_deli)
        return res

    return count(k, 0, 0, 0)


def main():
    for t in range(int(input())):
        print('Case #{}:'.format(t + 1), solve())


if __name__ == '__main__':
    main()
