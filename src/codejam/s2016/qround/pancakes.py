import heapq


def flip(s, x):
    res = ''
    for i in reversed(range(x + 1)):
        res += '-' if s[i] == '+' else '+'
    res += s[x + 1:]
    return res


def solve():
    s = input()
    d = {s: 0}
    q = [(0, s)]
    while True:
        top = heapq.heappop(q)
        dist, ss = top
        if ss == '+' * len(s):
            return dist
        else:
            for i in range(len(s)):
                sss = flip(ss, i)
                if sss not in d or d[sss] > dist + 1:
                    d[sss] = dist + 1
                    heapq.heappush(q, (dist + 1, sss))


t = int(input())
for tt in range(1, t + 1):
    print("Case #" + str(tt) + ":", solve())
