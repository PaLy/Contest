def solve20(h=5, w=4):
    a = [[0 for _ in range(w)] for _ in range(h)]
    while True:
        breakFors = False
        for i in range(h):
            for j in range(w):
                if a[i][j] == 0:
                    pi = max(i, 1)
                    pi = min(pi, h - 2)
                    pj = max(j, 1)
                    pj = min(pj, w - 2)
                    print(pi + 1, pj + 1)
                    breakFors = True
                    break
            if breakFors:
                break

        i, j = map(int, input().split())
        if i == -1 and j == -1 or i == 0 and j == 0:
            break
        else:
            i -= 1
            j -= 1
            a[i][j] = 1


def solve200():
    solve20(14, 15)


t = int(input())
for tt in range(1, t + 1):
    a = int(input())
    if a == 20:
        solve20()
    else:
        solve200()
