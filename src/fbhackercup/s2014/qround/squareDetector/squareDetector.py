from itertools import product

t = int(input())

for tt in range(t):
    n = int(input())
    map = [input() for _ in range(n)]
    for si, sj in product(range(n), range(n)):
        if map[si][sj] == '#':
            break
    for ei, ej in reversed(list(product(range(n), range(n)))):
        if map[ei][ej] == '#':
            break
    if ei - si != ej - sj:
        res = 'NO'
    else:
        res = 'YES'
        for i, j in product(range(n), range(n)):
            if i < si or i > ei or j < sj or j > ej:
                if map[i][j] == '#':
                    res = 'NO'
                    break
            else:
                if map[i][j] == '.':
                    res = 'NO'
                    break
    print('Case #{}:'.format(tt + 1), res)