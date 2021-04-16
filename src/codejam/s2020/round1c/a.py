def solve():
    xs, ys, m = input().split()
    x = int(xs)
    y = int(ys)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    ds = ['N', 'S', 'E', 'W']
    for i in range(len(m)):
        x = x + dx[ds.index(m[i])]
        y = y + dy[ds.index(m[i])]
        if abs(x) + abs(y) <= i + 1:
            return i + 1
    return "IMPOSSIBLE"


t = int(input())
for tt in range(1, t + 1):
    print("Case #" + str(tt) + ": " + str(solve()))
