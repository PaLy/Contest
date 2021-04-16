def solve():
    n = int(input())
    n = 1000000000
    if n < 500:
        for i in range(1, n + 1):
            print(i, 1)
    # elif n <= 997:
    #     x = n - 500 + 2
    #     for i in range(1, x):
    #         print(i, 1)
    #     print(x, 2)
    #     for i in range(x, 500):
    #         print(i, 1)
    # elif n == 998:
    #     print(1, 1)
    #     print(2, 1)
    #     print(3, 1)
    #     print(4, 2)
    #     for i in range(4, 498):
    #         print(i, 1)
    #     print(498, 2)
    #     print(498, 1)
    # elif n == 999:
    #     print(1, 1)
    #     print(2, 1)
    #     print(3, 1)
    #     print(4, 1)
    #     print(5, 2)
    #     for i in range(5, 498):
    #         print(i, 1)
    #     print(498, 2)
    #     print(498, 1)
    # elif n == 1000:
    #     print(1, 1)
    #     print(2, 1)
    #     print(3, 1)
    #     print(4, 1)
    #     print(5, 1)
    #     print(6, 2)
    #     for i in range(6, 498):
    #         print(i, 1)
    #     print(498, 2)
    #     print(498, 1)
    else:
        nn = n
        xs = []
        while nn > 0:
            x = 0
            while 2 ** x <= nn:
                x += 1
            x -= 1
            xs.append(x)
            nn -= 2 ** x

        # print(xs)

        td = 0
        while len(xs) > 0:
            s = xs[0] - len(xs) + 1 - td
            if s > 0:
                td += 2 ** xs[-1]
                xs = xs[:-1]
            else:
                break
        # print(xs)
        # print(td)

        if len(xs) > 0:
            td -= xs[0] - len(xs) + 1

        # print(td)
        cr = 0
        left = True
        xs.reverse()
        for x in xs:
            while cr < x:
                if left:
                    print(cr + 1, 1)
                else:
                    print(cr + 1, cr + 1)
                cr += 1
            if left:
                for c in range(1, x + 2):
                    print(x + 1, c)
            else:
                for c in range(x + 1, 0, -1):
                    print(x + 1, c)
            left = not left
            cr += 1

        while td > 0:
            nl = cr
            if nl <= td:
                if left:
                    print(cr + 1, 2)
                else:
                    print(cr + 1, cr)
                td -= nl
                cr += 1
            else:
                break
        for i in range(td):
            if left:
                print(cr + i + 1, 1)
            else:
                print(cr + i + 1, cr + i + 1)



t = int(input())
for tt in range(1, t + 1):
    print("Case #" + str(tt) + ": ")
    solve()
