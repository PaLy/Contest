def solve():
    s = map(int, input())
    res = ""
    opened = 0
    for x in s:
        if x != opened:
            while x < opened:
                res += ")"
                opened -= 1
            while x > opened:
                res += "("
                opened += 1
        res += str(x)
    for _ in range(opened):
        res += ")"
    return res


t = int(input())
for tt in range(1, t + 1):
    print("Case #" + str(tt) + ": " + str(solve()))
