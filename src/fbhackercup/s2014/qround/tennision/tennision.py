def mapInput(line):
    return int(line[0]), map(float, line[1:])


def solve():
    K, (ps, pr, pi, pu, pw, pd, pl) = mapInput(input().split())
    cache = dict()

    def count(k1, k2, pi):
        if k1 == K:
            return 1
        elif k2 == K:
            return 0
        else:
            state = (k1, k2, int(pi * 1000))
            if state in cache:
                return cache[state]
            else:
                res = 0

                # win
                res += (ps * pi + pr * (1 - pi)) * (
                    pw * count(k1 + 1, k2, min(1, pi + pu)) + (1 - pw) * count(k1 + 1, k2, pi))

                # loose
                res += ((1 - ps) * pi + (1 - pr) * (1 - pi)) * (
                    pl * count(k1, k2 + 1, max(0, pi - pd)) + (1 - pl) * count(k1, k2 + 1, pi))

                cache[state] = res
                return res

    return '%.6f' % count(0, 0, pi)


def main():
    for t in range(int(input())):
        print('Case #{}:'.format(t + 1), solve())


if __name__ == '__main__':
    main()