from itertools import product
from math import sqrt, ceil
from sys import stderr


def solve():
    n, j = map(int, input().split())
    for inner in product('01', repeat=n - 2):
        if j == 0:
            break

        x = '1' + ''.join(inner) + '1'
        divs = []
        for base in range(2, 11):
            xx = int(x, base)
            for d in range(2, ceil(sqrt(xx)) + 1):
                if xx % d == 0:
                    divs.append(d)
                    break
        if len(divs) == 9:
            j -= 1
            print(x, ' '.join(str(x) for x in divs))
        print(int(x, 2), file=stderr)


t = int(input())
for tt in range(1, t + 1):
    print("Case #" + str(tt) + ":")
    solve()
