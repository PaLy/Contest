IMPOSSIBLE = "Impossible"


def main():
    def full_of(ch):
        return [ch * c for _ in r]

    m, r, c = map(int, input())
    res = IMPOSSIBLE
    if min(r, c) == 1 or m == 0:
        res = full_of('.')
        for k in range(m):
            if r == 1:
                res[0][k] = '*'
            else:
                res[k][0] = '*'
        if r == 1:
            res[0][c - 1] = 'c'
        else:
            res[r - 1][0] = 'c'
    elif m == r * c - 1:
        res = full_of('*')
        res[0][0] = 'c'
    elif m >= r * c - 3:
        res = IMPOSSIBLE
    elif m % 2 == 1 and min(r, c) == 2:
        res = IMPOSSIBLE

    if res == IMPOSSIBLE:
        return res
    else:
        return '\n'.join(row for row in res)


if __name__ == '__main__':
    t = int(input())
    for ti in range(1, t + 1):
        print("Case #" + str(ti) + ": " + main())
