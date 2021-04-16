from collections import Counter


def solve():
    n = int(input())
    xy = [tuple(map(int, input().split())) for _ in range(n)]

    res = 0
    for s1 in xy:
        c = Counter()
        for s2 in xy:
            if s1 != s2:
                dist = (s1[0] - s2[0]) ** 2 + (s1[1] - s2[1]) ** 2
                c[dist] += 1
        for k, v in c.items():
            res += v * (v - 1) // 2
    return res


def main():
    for t in range(int(input())):
        print('Case #{}:'.format(t + 1), solve())


if __name__ == '__main__':
    main()
