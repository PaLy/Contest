def solve():
    n, k = map(int, input().split())
    n = 4
    k = 7

    def remap(rmp, rows):
        for i in range(n):
            for j in range(n):
                for (a, b) in rmp:
                    if rows[i][j] == a:
                        rows[i][j] = b
                        break
                    elif rows[i][j] == b:
                        rows[i][j] = a
                        break

    def prnt(rows):
        print("\n".join("".join(str(x) for x in row) for row in rows))

    def same_diag(rmp):
        rows = []
        for i in range(n):
            row0 = list(range(1, n + 1))
            row = row0[-i:] + row0[:-i]
            rows.append(row)
        remap(rmp, rows)
        return rows

    if k == n + 1 or k == n * n - 1 or (n == 3 and (k == 5 or k == 7)):
        print("IMPOSSIBLE")
    else:
        print("POSSIBLE")
        if k == n:
            prnt(same_diag([]))
        elif k == n * n:
            prnt(same_diag([(1, n)]))
        else:
            d = k // (n - 1)
            rm = k - (n - 1) * d
            if rm == 0:
                d -= 1
                rm = k - (n - 1) * d
            if rm == d:
                prnt(same_diag([(1, d)]))
            else:
                if rm == d - 1:
                    a = d - 2
                    b = d + 1
                elif rm > d:
                    a = d + 1
                    b = rm - 1
                else:
                    a = rm + 1
                    b = d - 1

                if a == b:
                    square = [[0] * n for _ in range(n)]

                    other = list(range(3, n + 1))
                    ois = 0
                    for row in range(n):
                        oi = ois
                        for col in range(n):
                            if row == 0 and col == 1 or row == 1 and col == 0:
                                square[row][col] = 1
                            elif row == n - 1 and col == n - 2 or row == n - 2 and col == n - 1:
                                square[row][col] = 2
                            elif row == col:
                                if row == 0 or row == 1:
                                    square[row][col] = 2
                                else:
                                    square[row][col] = 1
                            else:
                                square[row][col] = other[oi]
                                oi = (oi + 1) % len(other)
                        ois = (ois + 1) % len(other)
                    remap([(1, d), (2, a)], square)
                    prnt(square)
                else:
                    rows = same_diag([(1, d)])
                    tmp = rows[-1]
                    rows[-1] = rows[-2]
                    rows[-2] = tmp
                    remap([(2, a), (5, b)], rows)
                    prnt(rows)


t = int(input())
for tt in range(1, t + 1):
    print("Case #" + str(tt) + ":")
    solve()
