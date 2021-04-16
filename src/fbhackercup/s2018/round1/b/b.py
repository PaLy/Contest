import sys

sys.setrecursionlimit(1000047)


def solve():
    n, k = map(int, input().split())
    l = [-1] * n
    r = [-1] * n
    for i in range(n):
        l[i], r[i] = map(int, input().split())
        l[i] -= 1
        r[i] -= 1

    def preorder(root):
        if root == -1:
            return []
        else:
            return [root] + preorder(l[root]) + preorder(r[root])

    def postorder(root):
        if root == -1:
            return []
        else:
            return postorder(l[root]) + postorder(r[root]) + [root]

    pre = preorder(0)
    post = postorder(0)

    p = [i for i in range(n)]

    def par(x):
        if p[x] == x:
            return x
        else:
            return par(p[x])

    for i in range(n):
        x = pre[i]
        y = post[i]

        px = par(x)
        py = par(y)
        p[py] = p[y] = p[x] = px

    for i in range(n):
        p[i] = par(i)

    pars = set(p)

    if len(pars) >= k:
        pn = [-1] * n
        i = 1
        for pp in pars:
            pn[pp] = i
            i += 1

        r = [-1] * n
        for i in range(n):
            r[i] = pn[p[i]]

        return ' '.join(str(x) for x in r)
    else:
        return "Impossible"


def main():
    for t in range(int(input())):
        print('Case #{}: {}'.format(t + 1, solve()))


if __name__ == '__main__':
    main()
