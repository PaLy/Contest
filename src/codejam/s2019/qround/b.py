def solve():
    n = int(input())
    s = input()
    res = ""
    for x in s:
        if x == 'S':
            res += 'E'
        else:
            res += 'S'
    return res


t = int(input())
for tt in range(1, t + 1):
    print("Case #" + str(tt) + ": " + str(solve()))
