import sys
sys.setrecursionlimit(1000047)

def solve():
    n = int(input())
    p = [input() for _ in range(3)]

    dp = [[-1 for _ in range(n + 1)] for _ in range(3)]

    def solve(f, c):
        if dp[f][c] != -1:
            return dp[f][c]
        elif c == n:
            if f == 2:
                return 1
            else:
                return 0
        else:
            res = 0
            if f == 0:
                if p[0][c] == '.' and p[1][c] == '.':
                    res += solve(1, c + 1)
            elif f == 1:
                if p[0][c] == '.' and p[1][c] == '.':
                    res += solve(0, c + 1)
                if p[2][c] == '.' and p[1][c] == '.':
                    res += solve(2, c + 1)
            else:
                if p[2][c] == '.' and p[1][c] == '.':
                    res += solve(1, c + 1)
            res %= 1000000007
            dp[f][c] = res
            return res

    return solve(0, 0)


def main():
    for t in range(int(input())):
        print('Case #{}:'.format(t + 1), solve())


if __name__ == '__main__':
    main()
