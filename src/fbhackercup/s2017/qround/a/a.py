import math


def dotp(x, y):
    return sum(i * j for i, j in zip(x, y))


def vlen(x):
    return math.sqrt(sum(i * i for i in x))


def det(x, y):
    return x[0] * y[1] - x[1] * y[0]


def inCircle(x):
    return vlen(x) <= 50


def solve():
    p, x, y = map(int, input().split())
    x -= 50
    y -= 50

    if x == 0 and y >= 0:
        if p == 0:
            return "white"
        else:
            return "black"

    x2 = (x, y)

    angleRad = math.atan2(y, x)
    angleDeg = math.degrees(angleRad)

    if angleDeg > 0:
        angleDeg = (180 - angleDeg - 90 + 360) % 360
    else:
        angleDeg = abs(angleDeg) + 90


    pAngle = 360 / 100 * p
    # print(angleRad)
    # print(angleDeg)

    if angleDeg <= pAngle and inCircle(x2):
        return "black"
    else:
        return "white"


def main():
    for t in range(int(input())):
        print('Case #{}:'.format(t + 1), solve())


if __name__ == '__main__':
    main()
