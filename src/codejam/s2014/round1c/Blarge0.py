from collections import defaultdict


def valid(s):
    visited = defaultdict(lambda: -1)
    for i in range(len(s)):
        if visited[i] != -1 and visited[i] < i - 1:
            return False
    return True


def main():
    n = int(input())
    cars = [x for x in input().split()]
    g = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if set(cars[i]).intersection(set(cars[j])):
                if valid(cars[i] + cars[j]):
                    g[i][j] = 1
                if valid(cars[j] + cars[i]):
                    g[j][i] = 1
                if g[i][j] == 0 and g[j][i] == 0:
                    return 0

    visited = set()
    for i in range(n):
        pass


if __name__ == '__main__':
    t = int(input())
    for ti in range(1, t + 1):
        print("Case #" + str(ti) + ": " + str(main()))
