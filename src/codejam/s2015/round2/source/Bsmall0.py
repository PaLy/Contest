from fractions import Fraction


def main():
    def to_fraction(x):
        return Fraction.from_decimal(int(float(x) * 10000))

    n, v, x = input().split()
    n = int(n)
    v = to_fraction(v)
    x = to_fraction(x)
    r1, c1 = map(to_fraction, input().split())
    if n == 1:
        if c1 == x:
            return float(v / r1)
        else:
            return "IMPOSSIBLE"
    else:
        r2, c2 = map(to_fraction, input().split())
        if c1 == c2:
            if c1 == x:
                return float(v / (r1 + r2))
            else:
                return "IMPOSSIBLE"
        else:
            v1 = (v * x - v * c2) / (c1 - c2)
            v2 = v - v1
            if v1 < 0 or v2 < 0:
                return "IMPOSSIBLE"
            else:
                return float(max(v1 / r1, v2 / r2))


if __name__ == '__main__':
    t = int(input())
    for ti in range(1, t + 1):
        res = main()
        if res == "IMPOSSIBLE":
            print("Case #" + str(ti) + ": " + res)
        else:
            print("Case #" + str(ti) + ": " + "{0:.8f}".format(res))
