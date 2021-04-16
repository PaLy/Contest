def solve():
    n, R, O, Y, G, B, V = map(int, input().split())
    IMPOS = "IMPOSSIBLE"

    if O > B or G > R or V > Y:
        return IMPOS
    if O == B and O > 0:
        if n == O + B:
            return 'OB' * O
        else:
            return IMPOS
    if G == R and G > 0:
        if n == G + R:
            return 'GR' * G
        else:
            return IMPOS
    if V == Y and V > 0:
        if n == V + Y:
            return 'VY' * Y
        else:
            return IMPOS

    resO = 'BO' * O + 'B'
    resG = 'RG' * G + 'R'
    resV = 'YV' * V + 'Y'
    B -= O
    R -= G
    Y -= V

    x = [(R, 'R'), (Y, 'Y'), (B, 'B')]
    x.sort(reverse=True)

    res = []
    if R + Y >= B and R + B >= Y and B + Y >= R:
        for _ in range(x[1][0]):
            res.append(x[0][1])
            res.append(x[1][1])
        x[0] = (x[0][0] - x[1][0], x[0][1])

        z = min(x[0][0], x[2][0])
        for _ in range(z):
            res.append(x[0][1])
            res.append(x[2][1])
        x[0] = (x[0][0] - z, x[0][1])
        x[2] = (x[2][0] - z, x[2][1])

        zz = x[2][0]
        for i in range(zz):
            res = res[:(i * 2) + 1] + [x[2][1]] + res[(i * 2) + 1:]

        for i in range(len(res)):
            if res[i] == 'B':
                res[i] = resO
                break
        for i in range(len(res)):
            if res[i] == 'R':
                res[i] = resG
                break
        for i in range(len(res)):
            if res[i] == 'Y':
                res[i] = resV
                break

        return ''.join(x for x in res)
    else:
        return "IMPOSSIBLE"


t = int(input())
for tt in range(1, t + 1):
    print("Case #" + str(tt) + ": " + str(solve()))
