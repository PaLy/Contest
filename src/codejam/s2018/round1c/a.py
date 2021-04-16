import itertools
import random


def find(chars, n, l, words):
    counter = 0
    for w in itertools.product(*(c for c in chars)):
        w = ''.join(x for x in w)
        if w not in words:
            return w
        counter += 1
        if counter == 10000:
            break

    chars = [list(c) for c in chars]

    while True:
        w = "".join(c[random.randint(0, len(c) - 1)] for c in chars)
        if w not in words:
            return w


def solve():
    n, l = map(int, input().split())
    words = set(input() for _ in range(n))

    chars = [set() for _ in range(l)]
    for w in words:
        for i in range(l):
            chars[i].add(w[i])

    all = 1
    for i in range(l):
        all *= len(chars[i])

    if len(words) == all:
        return "-"
    else:
        return find(chars, n, l, words)


t = int(input())
for tt in range(1, t + 1):
    print("Case #" + str(tt) + ": " + str(solve()))
