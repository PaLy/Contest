from math import floor


def solve_easy():
    l, r = map(int, input().split())
    n = 0
    while l - (n + 1) >= 0 or r - (n + 1) >= 0:
        if l >= r:
            l -= n + 1
        else:
            r -= n + 1
        n += 1
    return str(n) + " " + str(l) + " " + str(r)


def solve():
    l, r = map(int, input().split())
    # l = 2
    # r = 2
    ma = max(l, r)
    mi = min(l, r)
    l_is_mi = mi == l and l != r

    lb = 1
    rb = 1000000000000000000
    while rb - lb > 1:
        n = floor((lb + rb) / 2)
        t = n * (n + 1) // 2
        if mi + t > ma:
            rb = n
        else:
            lb = n

    n = lb
    ma -= n * (n + 1) // 2

    while ma > mi and n + 1 <= ma:
        n += 1
        ma -= n

    lb = n + 1
    rb = 1000000000000000000
    mii = mi
    maa = ma
    while rb - lb > 1:
        nn = floor((lb + rb) / 2)

        lodd = nn if nn % 2 == 1 else nn - 1
        if (n + 1) % 2 == 1:
            fodd = n + 1
        else:
            fodd = n + 2
        if fodd > lodd:
            odd = 0
        else:
            odd = (fodd + lodd) * ((lodd - fodd) // 2 + 1) // 2

        leven = nn if nn % 2 == 0 else nn - 1
        if (n + 1) % 2 == 0:
            feven = n + 1
        else:
            feven = n + 2
        if feven > leven:
            even = 0
        else:
            even = (feven + leven) * ((leven - feven) // 2 + 1) // 2

        if (n + 1) % 2 == 1:
            mii = mi - odd
            maa = ma - even
        else:
            mii = mi - even
            maa = ma - odd
        if mii < 0 or maa < 0:
            rb = nn
        else:
            lb = nn

    nn = lb

    lodd = nn if nn % 2 == 1 else nn - 1
    if (n + 1) % 2 == 1:
        fodd = n + 1
    else:
        fodd = n + 2
    if fodd > lodd:
        odd = 0
    else:
        odd = (fodd + lodd) * ((lodd - fodd) // 2 + 1) // 2

    leven = nn if nn % 2 == 0 else nn - 1
    if (n + 1) % 2 == 0:
        feven = n + 1
    else:
        feven = n + 2
    if feven > leven:
        even = 0
    else:
        even = (feven + leven) * ((leven - feven) // 2 + 1) // 2

    if (n + 1) % 2 == 1:
        mii = mi - odd
        maa = ma - even
    else:
        mii = mi - even
        maa = ma - odd

    if mii < 0 or maa < 0:
        lb = n
        mii = mi
        maa = ma
    if l_is_mi:
        return str(lb) + " " + str(mii) + " " + str(maa)
    else:
        return str(lb) + " " + str(maa) + " " + str(mii)


t = int(input())
for tt in range(1, t + 1):
    print("Case #" + str(tt) + ": " + str(solve_easy()))
