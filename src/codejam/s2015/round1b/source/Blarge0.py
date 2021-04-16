def main():
    d = int(input())
    p = list(map(int, input().split()))
    p.sort()
    res = p[-1]
    for i in range(res):
        last = p[-1]
        if last > 1:
            p[-1] = last // 2
            p.append(last - p[-1])
            p.sort()
            res = min(p[-1] + i + 1, res)
        else:
            break
    return res


cache = dict()


def f(p):
    tp = tuple(p)
    if tp in cache:
        return cache[tp]
    if p[-1] == 0:
        return 0
    res = p[-1]
    for k in range(1, p[-1]):
        p2 = list(p)
        p2[-1] = k
        p2.append(p[-1] - p2[-1])
        p2.sort()
        res = min(res, f(p2) + 1)
    cache[tp] = res
    return cache[tp]


def main2():
    d = int(input())
    p = list(map(int, input().split()))
    return f(sorted(p))


if __name__ == '__main__':
    t = int(input())
    for ti in range(1, t + 1):
        print("Case #" + str(ti) + ": " + str(main2()))
