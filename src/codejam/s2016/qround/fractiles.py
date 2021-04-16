def solve():
    k, c, s = map(int, input().split())
    return ' '.join(str(x + 1) for x in range(s))


t = int(input())
for tt in range(1, t + 1):
    print("Case #" + str(tt) + ":", solve())
