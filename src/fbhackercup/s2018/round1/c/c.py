def parse(spell):
    x, zv = spell.split('d')
    if '+' in zv:
        y, z = zv.split('+')
    elif '-' in zv:
        y, z = zv.split('-')
        z = -int(z)
    else:
        y = zv
        z = 0
    return int(x), int(y), int(z)


def count(x, y, z, h):
    h -= z
    p = [[0 for _ in range(x + 1)] for _ in range(x * y + 1)]
    p[0][0] = 1
    for step in range(1, x + 1):
        for psum in range(0, x * y + 1):
            for hod in range(1, y + 1):
                if p[psum][step - 1] > 0:
                    p[psum + hod][step] += p[psum][step - 1] / y

    return sum(p[i][x] for i in range(max(0, h), x * y + 1))


def solve():
    h, s = map(int, input().split())
    res = 0.0
    for spell in input().split():
        x, y, z = parse(spell)
        res = max(res, count(x, y, z, h))
    return res


def main():
    for t in range(int(input())):
        print('Case #{}:'.format(t + 1), solve())


if __name__ == '__main__':
    main()
