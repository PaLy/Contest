from collections import deque
from itertools import permutations


def get_reachable(s, done, edge, n):
    d = deque()
    d.append(s)
    reachable = set()
    visited = set()
    visited.add(s)
    while len(d) > 0:
        x = d.popleft()
        for i in range(n):
            if edge[x][i] and i not in visited:
                visited.add(i)
                if i in done:
                    d.append(i)
                else:
                    reachable.add(i)
    return reachable


def is_ok(p, edge, n):
    done = set()
    done.add(p[0])
    for i in range(1, n):
        reachable = get_reachable(p[i - 1], done, edge, n)
        if p == (4, 1, 3, 0, 2):
            print(reachable)
        if p[i] not in reachable:
            return False
        done.add(p[i])
    return True


def main():
    n, m = map(int, input().split())
    zips = [input() for _ in range(n)]
    edge = [[False for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        edge[x][y] = edge[y][x] = True

    res = None
    for p in permutations(range(n)):
        if is_ok(p, edge, n):
            s = ''.join(zips[x] for x in p)
            if res is None or s < res:
                res = s

    return res


if __name__ == '__main__':
    t = int(input())
    for ti in range(1, t + 1):
        print("Case #" + str(ti) + ": " + main())
