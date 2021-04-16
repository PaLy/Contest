def solve():
    x, y = map(int, input().split())
    res = ''
    while x != 0 or y != 0:
        if x % 2 == y % 2:
            return "IMPOSSIBLE"
        elif x % 2 == 1:
            if y == 0 and abs(x) == 1:
                if x > 0:
                    res += 'E'
                    x -= 1
                else:
                    res += 'W'
                    x += 1
            else:
                if ((x + 1) // 2) % 2 != (y // 2) % 2:
                    res += 'W'
                    x += 1
                elif ((x - 1) // 2) % 2 != (y // 2) % 2:
                    res += 'E'
                    x -= 1
                else:
                    return "IMPOSSIBLE"
        elif y % 2 == 1:
            if x == 0 and abs(y) == 1:
                if y > 0:
                    res += 'N'
                    y -= 1
                else:
                    res += 'S'
                    y += 1
            else:
                if (x // 2) % 2 != ((y + 1) // 2) % 2:
                    res += 'S'
                    y += 1
                elif (x // 2) % 2 != ((y - 1) // 2) % 2:
                    res += 'N'
                    y -= 1
                else:
                    return "IMPOSSIBLE"
        x //= 2
        y //= 2

    return res


t = int(input())
for tt in range(1, t + 1):
    print("Case #" + str(tt) + ": " + str(solve()))
