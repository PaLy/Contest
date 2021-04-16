def main():
    r, c = map(int, input().split())

    def inmap(x, y):
        return 0 <= x < r and 0 <= y < c

    mapa = [input() for _ in range(r)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    cc = {'^': 3, '>': 0, 'v': 2, '<': 1}
    res = 0
    for i in range(r):
        for j in range(c):
            if mapa[i][j] != '.':
                smer = cc[mapa[i][j]]
                x = i
                y = j
                x += dx[smer]
                y += dy[smer]
                ok = False
                while inmap(x, y):
                    if mapa[x][y] != '.':
                        ok = True
                    x += dx[smer]
                    y += dy[smer]
                if ok:
                    continue
                else:
                    ok = False
                    for s in range(4):
                        x = i
                        y = j
                        x += dx[s]
                        y += dy[s]
                        while inmap(x, y):
                            if mapa[x][y] != '.':
                                ok = 1
                                break
                            x += dx[s]
                            y += dy[s]
                    if ok:
                        res += 1
                    else:
                        return "IMPOSSIBLE"
    return res


if __name__ == '__main__':
    t = int(input())
    for ti in range(1, t + 1):
        print("Case #" + str(ti) + ": " + str(main()))
