def solve():
    s = input()
    s = list(s)

    changed = True
    while changed:
        changed = False

        n = len(s)
        for i in range(n - 1):
            if s[i] > s[i + 1]:
                s[i] = str(int(s[i]) - 1)
                changed = True
                for j in range(i + 1, n):
                    s[j] = '9'
        if s[0] == '0':
            s = s[1:]

    return ''.join(x for x in s)


t = int(input())
for tt in range(1, t + 1):
    print("Case #" + str(tt) + ": " + str(solve()))
