import pulp
from collections import Counter


def solve():
    n, p = map(int, input().split())
    g = list(map(int, input().split()))
    for i in range(n):
        g[i] = g[i] % p
    counter = Counter(g)

    if p == 4:
        model = pulp.LpProblem('a', pulp.LpMaximize)
        ing = ['1111', '121', '13', '22', '233', '3333']
        x = pulp.LpVariable.dict('a_%s', ing, lowBound=0, upBound=100, cat=pulp.LpInteger)
        cost = dict(zip(ing, [1] * 6))
        model += sum([cost[i] * x[i] for i in ing])
        jj = dict(zip(ing, [4, 2, 1, 0, 0, 0]))
        dd = dict(zip(ing, [0, 1, 0, 2, 1, 0]))
        tt = dict(zip(ing, [0, 0, 1, 0, 2, 4]))
        model += sum([jj[i] * x[i] for i in ing]) <= counter[1]
        model += sum([dd[i] * x[i] for i in ing]) <= counter[2]
        model += sum([tt[i] * x[i] for i in ing]) <= counter[3]
        model.solve()
        gg = sum(x[i].value() for i in ing)
        pj = 4 * x['1111'].value() + 2 * x['121'].value() + x['13'].value()
        pd = x['121'].value() + 2 * x['22'].value() + x['233'].value()
        pt = x['13'].value() + 2 * x['233'].value() + 4 * x['3333'].value()
        zv = 0
        if n - pj - pd - pt - counter[0] > 0:
            zv = 1
        return counter[0] + gg + zv
    elif p == 3:
        model = pulp.LpProblem('a', pulp.LpMaximize)
        ing = ['12', '111', '222']
        x = pulp.LpVariable.dict('a_%s', ing, lowBound=0, upBound=100, cat=pulp.LpInteger)
        cost = dict(zip(ing, [1] * 3))
        model += sum([cost[i] * x[i] for i in ing])
        jj = dict(zip(ing, [1, 3, 0]))
        dd = dict(zip(ing, [1, 0, 3]))
        model += sum([jj[i] * x[i] for i in ing]) <= counter[1]
        model += sum([dd[i] * x[i] for i in ing]) <= counter[2]
        model.solve()
        gg = sum(x[i].value() for i in ing)
        pj = x['12'].value() + 3 * x['111'].value()
        pd = x['12'].value() + 3 * x['222'].value()
        zv = 0
        if n - pj - pd - counter[0] > 0:
            zv = 1
        return counter[0] + gg + zv
    elif p == 2:
        jj = counter[1] // 2 + counter[1] % 2
        return counter[0] + jj


t = int(input())
for tt in range(1, t + 1):
    print("Case #" + str(tt) + ": " + str(int(solve())))
