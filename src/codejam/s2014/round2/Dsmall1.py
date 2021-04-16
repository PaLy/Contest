def check(first, second, m):
    for b in range(m):
        if ((first >> b) & 1 == 1) and ((second >> b) & 1 == 1):
            return False
    return True


def count(mask, s, m):
    trie = set()
    for i in range(m):
        if ((mask >> i) & 1) == 1:
            for j in range(len(s[i]) + 1):
                trie.add(s[i][:j])
    return len(trie)


def main():
    m, n = map(int, input().split())
    s = [input() for _ in range(m)]
    res = -1
    y = -1
    for first in range(1 << m):
        if n > 1:
            for second in range(1 << m):
                if check(first, second, m):
                    if n > 2:
                        for third in range(1 << m):
                            if check(first | second, third, m):
                                if n > 3:
                                    for fourth in range(1 << m):
                                        if check(first | second | third, fourth, m):
                                            if first | second | third | fourth == (1 << m) - 1:
                                                r = count(first, s, m)
                                                r += count(second, s, m)
                                                r += count(third, s, m)
                                                r += count(fourth, s, m)
                                                if res == -1 or r > res:
                                                    res = r
                                                    y = 1
                                                elif res == r:
                                                    y += 1
                                else:
                                    if first | second | third == (1 << m) - 1:
                                        r = count(first, s, m)
                                        r += count(second, s, m)
                                        r += count(third, s, m)
                                        if res == -1 or r > res:
                                            res = r
                                            y = 1
                                        elif res == r:
                                            y += 1
                    else:
                        if first | second == (1 << m) - 1:
                            r = count(first, s, m)
                            r += count(second, s, m)
                            if res == -1 or r > res:
                                res = r
                                y = 1
                            elif res == r:
                                y += 1
        else:
            if first == (1 << m) - 1:
                r = count(first, s, m)
                if res == -1 or r > res:
                    res = r
                    y = 1
                elif res == r:
                    y += 1
    return str(res) + " " + str(y)


if __name__ == '__main__':
    t = int(input())
    for ti in range(1, t + 1):
        print("Case #" + str(ti) + ": " + main())