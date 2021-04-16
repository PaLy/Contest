tab = {'1': {'1': '1', 'i': 'i', 'j': 'j', 'k': 'k'},
       'i': {'1': 'i', 'i': '-1', 'j': 'k', 'k': '-j'},
       'j': {'1': 'j', 'i': '-k', 'j': '-1', 'k': 'i'},
       'k': {'1': 'k', 'i': 'j', 'j': '-i', 'k': '-1'},
       }


def mul(x, y):
    z = 1
    if x[0] == '-':
        z *= -1
        x = x[1]
    if y[0] == '-':
        z *= -1
        y = y[1]
    res = tab[x][y]
    if z == -1:
        if res[0] == '-':
            res = res[1:]
        else:
            res = '-' + res
    return res


def ldiv(c, a):
    z = -1
    if a[0] == '-':
        z *= -1
        a = a[1]
    if c[0] == '-':
        z *= -1
        c = c[1]
    res = tab[a][c]
    if z == -1:
        if res[0] == '-':
            res = res[1:]
        else:
            res = '-' + res
    return res


def main():
    l, x = map(int, input().split())
    s = input() * x
    n = len(s)
    p = ['1']
    for i in range(n):
        p.append(mul(p[-1], s[i]))
    for i in range(1, n - 1):
        if p[i] == 'i':
            for j in range(i + 1, n):
                if ldiv(p[j], p[i]) == 'j' and ldiv(p[n], p[j]) == 'k':
                    return 'YES'
    return 'NO'


if __name__ == '__main__':
    t = int(input())
    for ti in range(1, t + 1):
        print("Case #" + str(ti) + ": " + str(main()))
