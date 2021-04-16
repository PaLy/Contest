# Read init information from standard input, if any
from collections import deque
from itertools import product
from random import randrange
import sys

DIRS = [(0, 1, "RIGHT"), (0, -1, "LEFT"), (-1, 0, "UP"), (1, 0, "DOWN")]

rows, cols, a = map(int, input().split())
cx = None
cy = None
tx = None
ty = None


def update_maze():
    global cx, cy, tx, ty
    for i, j in product(range(rows), range(cols)):
        if maze[i][j] == 'C':
            cx = i
            cy = j
        elif maze[i][j] == 'T':
            tx = i
            ty = j


def max_quot():
    resc = -1
    res = DIRS
    for d in DIRS:
        nr = kr + d[0]
        nc = kc + d[1]
        if valid(nr, nc):
            c = 0
            for i, j in product(range(max(0, nr - 2), min(rows, nr + 3)),
                                range(max(0, nc - 2), min(cols, nc + 3))):
                if maze[i][j] == '?':
                    c += 1
            if c > resc:
                resc = c
                res = [d]
            elif c == resc:
                res.append(d)
    if resc > 0:
        return [res[randrange(0, len(res))][2]]
    else:
        return shortest_path(kr, kc, -1, -1, True)


def is_in(x, y):
    return 0 <= x < rows and 0 <= y < cols


def valid(x, y):
    return is_in(x, y) and maze[x][y] not in ['?', '#']


def shortest_path(sx, sy, ex, ey, first_quot=False):
    dist = {(sx, sy): 0}
    fr = {(sx, sy): -1}
    pr = {(sx, sy): -1}
    queue = deque([(sx, sy)])
    not_found = True
    while queue and not_found:
        pos = queue.popleft()
        for d in DIRS:
            nx = pos[0] + d[0]
            ny = pos[1] + d[1]
            npos = (nx, ny)
            if (valid(nx, ny) and npos not in dist) or (first_quot and is_in(nx, ny) and maze[nx][ny] == '?'):
                dist[npos] = dist[pos] + 1
                fr[npos] = pos
                pr[npos] = d[2]
                queue.append(npos)

                if first_quot and maze[nx][ny] == '?':
                    ex = nx
                    ey = ny
                if nx == ex and ny == ey:
                    not_found = False
                    break
    cur_pos = (ex, ey)
    if cur_pos in dist:
        path = []
        while cur_pos != (sx, sy):
            path.append(pr[cur_pos])
            cur_pos = fr[cur_pos]

        path = list(reversed(path))
        print(path, file=sys.stderr)
        return path
    else:
        return None


path_to_iter = iter([])
found = False

while 1:
    # Read information from standard input
    kr, kc = map(int, input().split())
    if kr == cx and kc == cy:
        found =True
    maze = [input() for _ in range(rows)]
    update_maze()
    print(kr, kc, file=sys.stderr)
    print('\n'.join(x for x in maze), file=sys.stderr)

    if cx is not None:
        if found:
            path = shortest_path(kr, kc, tx, ty)
            path_to_iter = iter(path)
            print(next(path_to_iter))
        else:
            path_to_c = shortest_path(kr, kc, cx, cy)
            return_path = shortest_path(cx, cy, tx, ty)
            if path_to_c is None or len(return_path) > a:
                path_to_iter = iter(max_quot())
                print(next(path_to_iter))
            else:
                path_to_iter = iter(path_to_c)
                print(next(path_to_iter))                
    else:
        path_to_iter = iter(max_quot())
        print(next(path_to_iter))