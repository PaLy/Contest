def solve():
    d, p = input().split()
    d = int(d)

    def lastCS(s):
        for i in reversed(range(len(s) - 1)):
            if s[i] == 'C' and s[i + 1] == 'S':
                return i
        return None

    def count(s):
        res = 0
        v = 1
        for i in range(len(s)):
            if s[i] == 'S':
                res += v
            else:
                v *= 2
        return res

    res = 0
    while True:
        c = count(p)
        if c <= d:
            return res
        l = lastCS(p)
        if l is None:
            return "IMPOSSIBLE"
        else:
            p = p[:l] + p[l + 1] + p[l] + p[l + 2:]
        res += 1


t = int(input())
for tt in range(1, t + 1):
    print("Case #" + str(tt) + ": " + str(solve()))
