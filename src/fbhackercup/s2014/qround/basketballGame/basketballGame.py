from collections import defaultdict
from operator import itemgetter


def makeTuple(list):
    return list[0], int(list[1]), int(list[2])


def removeLongest(cur, time):
    longest = 0
    for x in cur:
        if time[x] >= longest:
            rx = x
            longest = time[x]
    cur.remove(rx)


def addShortest(cur, time, n):
    shortest = -1
    for x in range(n):
        if x not in cur and (shortest == -1 or time[x] < shortest):
            ax = x
            shortest = time[x]
    cur.add(ax)


def solve():
    n, m, p = map(int, input().split())
    players = [makeTuple(input().split()) for _ in range(n)]
    players.sort(key=itemgetter(1, 2), reverse=True)

    res = []
    for i in range(2):
        team = [players[j][0] for j in range(n) if j % 2 == i]
        time = defaultdict(int)
        cur = set(range(p))
        for _ in range(m):
            for x in cur:
                time[x] += 1
            removeLongest(cur, time)
            addShortest(cur, time, len(team))
        res.extend(team[x] for x in cur)
    return ' '.join(sorted(res))


def main():
    for t in range(int(input())):
        print('Case #{}:'.format(t + 1), solve())


if __name__ == '__main__':
    main()