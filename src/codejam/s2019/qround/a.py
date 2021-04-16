def solve():
    n = input()
    a = ""
    b = ""
    for x in n:
        if x == '4':
            a += '2'
            b += '2'
        else:
            a += x
            if len(b) > 0:
                b += '0'
    return a + " " + b


t = int(input())
for tt in range(1, t + 1):
    print("Case #" + str(tt) + ": " + str(solve()))
