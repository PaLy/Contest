def check(first, second, m):
    for b in range(m):
        if ((first >> b) & 1 == 1) and ((second >> b) & 1 == 1):
            return False
    return True


cache = dict()


def count(mask, s, m):
    tup = (mask, m)
    if tup in cache:
        return cache[tup]
    else:
        trie = set()
        for i in range(m):
            if ((mask >> i) & 1) == 1:
                for j in range(len(s[i]) + 1):
                    trie.add(s[i][:j])
        cache[tup] = len(trie)
        return len(trie)


res = -1
y = 0


def solve(s, m, n, a, used):
    if n == 1:
        last = ((1 << m) - 1) ^ used
        r = sum(count(x, s, m) for x in a) + count(last, s, m)
        global res, y
        if res == -1 or r > res:
            res = r
            y = 1
        elif res == r:
            y += 1
    else:
        for x in range(1 << m):
            if check(used, x, m):
                a.append(x)
                solve(s, m, n - 1, a, used | x)
                a.remove(x)


def main():
    m, n = map(int, input().split())
    s = [input() for _ in range(m)]
    global res, y, cache
    res = -1
    y = 0
    cache = dict()
    solve(s, m, n, [], 0)
    return str(res) + " " + str(y)


if __name__ == '__main__':
    t = int(input())
    for ti in range(1, t + 1):
        print("Case #" + str(ti) + ": " + main())
