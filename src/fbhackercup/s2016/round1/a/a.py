def solve():
    n = int(input())
    d = list(map(int, input().split()))

    res = 0
    c = 0
    for i in range(0, n):
        if c == 0:
            c = 1
            continue
        else:
            dd = d[i] - d[i - 1]
            if dd <= 0:
                res += 4 - c
                c = 1
            else:
                k = (dd - 1) // 10
                need = 4 - c
                if k >= need:
                    res += need
                    c = 1
                elif k == need - 1:
                    res += k
                    c = 0
                else:
                    res += k
                    c += k + 1
                    if c == 4:
                        c = 0
    if c > 0:
        res += 4 - c
    return res


def main():
    for t in range(int(input())):
        print('Case #{}:'.format(t + 1), solve())


if __name__ == '__main__':
    main()
