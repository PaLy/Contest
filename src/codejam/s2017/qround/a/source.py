def flip(s, i, k):
    for j in range(i, i + k):
        s[j] = '+' if s[j] == '-' else '-'


def solve():
    s, k = input().split()
    s = list(s)
    k = int(k)
    n = len(s)
    res = 0
    for i in range(n - k + 1):
        if s[i] == "-":
            flip(s, i, k)
            res += 1

    for i in range(n):
        if s[i] == '-':
            return 'IMPOSSIBLE'
    return res


t = int(input())
for tt in range(1, t + 1):
    print("Case #" + str(tt) + ": " + str(solve()))
