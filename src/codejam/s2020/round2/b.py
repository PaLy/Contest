from heapq import heappop, heappush


def solve_easy():
    c, d = map(int, input().split())
    dist = [0] + list(map(lambda x: -int(x), input().split()))

    edges = []
    fedges = [[] for _ in range(c)]
    for _ in range(d):
        edge = tuple(map(lambda x: int(x) - 1, input().split()))
        edges.append(edge)
        fedges[edge[0]].append(edge[1])
        fedges[edge[1]].append(edge[0])

    res = [1000000] * len(edges)
    time_at = [0] * c

    done = set()

    heap = [(0, 0, -1)]
    time = 0
    while len(heap) > 0:
        time += 1
        dnf = heappop(heap)
        dnfs = [dnf]

        if dnf[2] != -1:
            mint = max(time_at[dnf[2]] + 1, time)
            while len(heap) > 0:
                dnf2 = heappop(heap)
                if dnf2[0] == dnf[0]:
                    dnfs.append(dnf2)
                    mint = max(mint, dnf2[2])
                else:
                    heappush(heap, dnf2)
                    break

            for di, node, fr in dnfs:
                time_at[node] = time
                if fr != -1:
                    for i in range(len(edges)):
                        edge = edges[i]
                        if edge == (node, fr) or edge == (fr, node):
                            res[i] = mint - time_at[fr]

        for _, node, _ in dnfs:
            done.add(node)

        for _, node, _ in dnfs:
            for next in fedges[node]:
                if next not in done:
                    heappush(heap, (dist[next], next, node))

    return " ".join(str(x) for x in res)


t = int(input())
for tt in range(1, t + 1):
    print("Case #" + str(tt) + ": " + str(solve_easy()))
