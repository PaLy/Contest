import math


def solve():
    a = float(input())
    dx = math.sqrt(2 - a * a)
    x = dx / 2
    dy = math.sqrt(2 - dx * dx)
    y = dy / 2
    print(0, 0, 0.5)
    print((x + y) / 2, (y - x) / 2, 0)
    print((x - y) / 2, (x + y) / 2, 0)


t = int(input())
for tt in range(1, t + 1):
    print("Case #" + str(tt) + ":")
    solve()
