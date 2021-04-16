# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# width: width of the firewall grid
# height: height of the firewall grid

width, height = [int(i) for i in input().split()]
mapa = []
for i in range(height):
    mapRow = [x for x in input()]  # one line of the firewall grid
    mapa.append(mapRow)


def left(x, y):
    return [(i, y) for i in range(x - 1, max(-1, x - 4), -1)]


def right(x, y):
    return [(i, y) for i in range(x + 1, min(height, x + 4))]


def up(x, y):
    return [(x, j) for j in range(y - 1, max(-1, y - 4), -1)]


def down(x, y):
    return [(x, j) for j in range(y + 1, min(width, y + 4))]


def how_many_to_destroy(x, y):
    def fff(blocks):
        res = 0
        for block in blocks:
            x, y = block
            if mapa[x][y] == '@' and die_time[x][y] < 1:
                res += 1
            if mapa[x][y] == '#':
                break
        return res

    res = 0
    res += fff(left(x,y))
    res += fff(right(x,y))
    res += fff(up(x,y))
    res += fff(down(x,y))
    return res


def update_map(x, y, d_time):
    mapa[x][y] = 'B'
    die_time[x][y] = d_time

    def fff(blocks):
        res = 0
        for b in blocks:
            x, y = b
            if mapa[x][y] == '@':
                die_time[x][y] = max(die_time[x][y], d_time)
            if mapa[x][y] == '#':
                break
        return res

    fff(left(x,y))
    fff(right(x,y))
    fff(up(x,y))
    fff(down(x,y))


die_time = [[-1] * width for _ in range(height)]


def explode_time(cur_time, x, y):
    def fff(blocks):
        res = 0
        for b in blocks:
            x, y = b
            if mapa[x][y] == 'B':
                time = die_time[x][y]
                res = max(time, res)
            if mapa[x][y] == '#':
                break
        return res

    res = cur_time - 3
    res = max(res, fff(left(x,y)))
    res = max(res, fff(right(x,y)))
    res = max(res, fff(up(x,y)))
    res = max(res, fff(down(x,y)))
    return res


def choose_by_explode_time(cur_time, X, Y):
    n = len(X)
    res = []
    for i in range(n):
        t = explode_time(cur_time, X[i], Y[i])
        res.append((t, X[i], Y[i]))
    res.sort(reverse=True)
    return res


def remove_exploded_bombs(time):
    for i in range(height):
        for j in range(width):
            if mapa[i][j] == 'B' and die_time[i][j] >= time:
                mapa[i][j] = '.'
                die_time[i][j] = -1


while 1:
    # rounds: number of rounds left before the end of the game
    # bombs: number of bombs left
    rounds, bombs = [int(i) for i in input().split()]
    remove_exploded_bombs(rounds)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    ma = 0
    ri = []
    rj = []
    for i in range(height):
        for j in range(width):
            if mapa[i][j] == '.':
                x = how_many_to_destroy(i, j)
                if x > ma:
                    ri = [i]
                    rj = [j]
                    ma = x
                elif x == ma:
                    ri.append(i)
                    rj.append(j)
    if ma == 0:
        print('WAIT')
    else:
        sorted_vals = choose_by_explode_time(rounds, ri, rj)
        d_time, ri, rj = sorted_vals[0]
        update_map(ri, rj, d_time)
        print(rj, ri)
