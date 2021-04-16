def solve():
    n, m = map(int, input().split())
    c = [sorted(list(map(int, input().split()))) for _ in range(n)]

    INF = 99999999999999999999999999
    dp = [[INF] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for day in range(1, n + 1):
        for total in range(n + 1):
            for p in range(m + 1):
                if total + p > n:
                    break
                else:
                    dp[day][total + p] = min(dp[day][total + p], dp[day - 1][total] + sum(c[day - 1][:p]) + p * p)

    return dp[n][n]


def main():
    for t in range(int(input())):
        print('Case #{}:'.format(t + 1), solve())


if __name__ == '__main__':
    main()
