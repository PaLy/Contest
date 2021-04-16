# Read init information from standard input, if any
from collections import defaultdict, deque, namedtuple
from itertools import product
import random
import sys
import time

Position = namedtuple('Position', ['y', 'x'])


def move(position, direction):
    return Position(position.y + DIRECTIONS[direction].dy, position.x + DIRECTIONS[direction].dx)


class Map:
    def __init__(self, width, height, default_factory):
        self.width = width
        self.height = height
        self.default_factory = default_factory
        self.__nodes__ = defaultdict(default_factory)

    def get(self, pos):
        return self.__nodes__[pos]

    def is_empty(self, pos):
        return self.__nodes__[pos] == self.default_factory()

    def in_map(self, pos):
        return 0 <= pos.y < self.height and 0 <= pos.x < self.width

    def is_articulation(self, pos):
        n1 = move(pos, 0)
        n2 = move(pos, 1)
        n3 = move(pos, 2)
        n4 = move(pos, 3)
        if not self.is_empty(n1) and self.in_map(n1) and not self.is_empty(n2) and self.in_map(n2):
            return True
        elif not self.is_empty(n3) and self.in_map(n3) and not self.is_empty(n4) and self.in_map(
                n4):
            return True
        else:
            return False

    def __str__(self):
        return '\n'.join(
            ' '.join(str(self.__nodes__[Position(i, j)]).rjust(2) for j in range(self.width))
            for i in range(self.height))

    def clear(self, player):
        for i, j in product(range(self.height), range(self.width)):
            pos = Position(i, j)
            if self.__nodes__[pos] == player:
                self.__nodes__[pos] = self.default_factory()

    def set(self, pos, c):
        self.__nodes__[pos] = c

    def neibs(self, pos):
        res = []
        for d in range(len(DIRECTIONS)):
            npos = move(pos, d)
            if self.in_map(npos):
                res.append((npos, d))
        return res

    def count_empty_neib(self, pos):
        res = 0
        for neib in self.neibs(pos):
            if self.is_empty(neib[0]):
                res += 1
        return res


class Voronoi_map(Map):
    def __str__(self):
        return '\n'.join(
            ' '.join(str((self.__nodes__[Position(i, j)][0], self.__nodes__[Position(i, j)][1][0]
            if self.__nodes__[Position(i,
                                       j)][1]
            else 9)).rjust(7) for j in range(self.width)) for i in range(self.height))


class Component_map(Map):
    def __init__(self, map):
        Map.__init__(self, map.width, map.height, lambda: -1)
        self.map = map

        next_color = 0
        for i, j in product(range(self.height), range(self.width)):
            pos = Position(i,j)
            if self.map.in_map(pos) and self.map.is_empty(pos):
                colors = set()
                if i > 0:
                    colors.add(self.get(Position(i - 1, j)))
                if j > 0:
                    colors.add(self.get(Position(i, j - 1)))
                colors.discard(-1)
                if colors:
                    if len(colors) == 2:
                        color = min(colors)
                        self.set(pos, color)
                        self.recolor(color, colors)
                    elif len(colors) == 1:
                        self.set(pos, next(iter(colors)))
                    else:
                        self.set(pos, next_color)
                        next_color += 1
                else:
                    self.set(pos, next_color)
                    next_color += 1


    def recolor(self, new_color, colors):
        for i, j in product(range(self.height), range(self.width)):
            pos = Position(i, j)
            if self.get(pos) in colors:
                self.set(pos, new_color)


    def is_articulation(self, pos):
        neib_colors = set(filter(lambda x: x != self.default_factory(),
                                 [self.get(neib[0]) for neib in self.neibs(pos)]))
        return len(neib_colors) > 1


class Direction:
    def __init__(self, dy, dx, repr):
        self.dy = dy
        self.dx = dx
        self.repr = repr

    def __str__(self):
        return self.repr


def calc_voronoi(mapa, my_head):
    def bfs(player, start_pos):
        voronoi_map.set(start_pos, (0, []))
        to_process = deque([start_pos])
        while to_process:
            cur_pos = to_process.popleft()
            ndist = voronoi_map.get(cur_pos)[0] + 1

            for neib_dir in voronoi_map.neibs(cur_pos):
                neib = neib_dir[0]
                if mapa.is_empty(neib):
                    dist = voronoi_map.get(neib)[0]
                    owners = voronoi_map.get(neib)[1]
                    if dist == -1 or dist > ndist:
                        voronoi_map.set(neib, (ndist, [player]))
                        to_process.append(neib)
                    elif dist == ndist and player not in owners:
                        owners.append(player)
                        to_process.append(neib)

    voronoi_map = Voronoi_map(mapa.width, mapa.height, lambda: (-1, []))
    for player in range(n):
        if player == p:
            start_pos = my_head
        else:
            start_pos = heads[player]
        bfs(player, start_pos)

    return voronoi_map


def count_space(voronoi_map, player):
    res = 0
    for i, j in product(range(voronoi_map.height), range(voronoi_map.width)):
        pos = Position(i, j)
        owners = voronoi_map.get(pos)[1]
        if len(owners) == 1 and player in owners:
            res += 1
    return res


class Strategies:
    @staticmethod
    def random_valid_move():
        len_dir = len(DIRECTIONS)
        move = random.randrange(0, len_dir)
        for d in range(len_dir):
            if MAP.is_empty(heads[p].move(move)):
                return move
            else:
                move += 1
                move %= len_dir

    @staticmethod
    def __count_empty_neighbors__():
        pos = heads[p]
        moves = [[] for _ in range(len(DIRECTIONS))]

        for d in range(len(DIRECTIONS)):
            npos = move(pos, d)
            if MAP.is_empty(npos):
                cen = MAP.count_empty_neib(npos)
                moves[cen].append(d)

        priority = [1, 2, 3, 0]
        for pr in priority:
            if moves[pr]:
                return moves[pr]


    @staticmethod
    def random_count_empty_neighbors():
        moves = Strategies.__count_empty_neighbors__()
        return moves[random.randrange(0, len(moves))]


    @staticmethod
    def first_count_empty_neighbors():
        return Strategies.__count_empty_neighbors__()[-1]

    @staticmethod
    def max_space_voronoi():
        pos = heads[p]
        spaces = []
        articulation = dict()
        # not_articulation = False
        for neib_dir in MAP.neibs(pos):
            neib = neib_dir[0]
            dir = neib_dir[1]
            if MAP.is_empty(neib):
                # not_articulation = not_articulation or not MAP.is_articulation(neib)
                MAP.set(neib, p)
                voronoi_map = calc_voronoi(MAP, neib)
                space = count_space(voronoi_map, p)
                # print(component_map, file=sys.stderr)
                # print(dir, neib, space, file=sys.stderr)
                # print(voronoi_map, file=sys.stderr)
                spaces.append((space, neib_dir))
                component_map = Component_map(MAP)
                # print(dir, file=sys.stderr)
                # print(component_map, file=sys.stderr)
                articulation[neib] = component_map.is_articulation(neib)
                MAP.set(neib, MAP.default_factory())

        spaces.sort(reverse=True)
        print(spaces, file=sys.stderr)
        for n in spaces:
            if not articulation[n[1][0]]:
                return n[1][1]
        return spaces[0][1][1]


WIDTH = 30
HEIGHT = 20
MAP = Map(WIDTH, HEIGHT, lambda: -1)
DIRECTIONS = (
    Direction(0, -1, 'LEFT'), Direction(0, 1, 'RIGHT'), Direction(-1, 0, 'UP'),
    Direction(1, 0, 'DOWN'))

while 1:
    start_time = time.time()
    # Read information from standard input
    n, p = map(int, input().split())
    tails = []
    heads = []
    for i in range(n):
        tailX, tailY, headX, headY = map(int, input().split())
        tail_pos = Position(tailY, tailX)
        head_pos = Position(headY, headX)
        tails.append(tail_pos)
        heads.append(head_pos)

        if headX == -1:
            MAP.clear(i)
        else:
            MAP.set(tail_pos, i)
            MAP.set(head_pos, i)

    # print(MAP, file=sys.stderr)

    # next_move = Strategies.random_valid_move()
    # next_move = Strategies.first_count_empty_neighbors()
    next_move = Strategies.max_space_voronoi()

    print(next_move, file=sys.stderr)
    # Write action to standard output
    print(DIRECTIONS[next_move])
    print(time.time()-start_time, file=sys.stderr)