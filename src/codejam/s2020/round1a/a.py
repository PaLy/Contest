def longest_pr(s):
    res = ""
    for x in s:
        if x.startswith(res):
            res = x
        elif res.startswith(x):
            pass
        else:
            return -1
    return res


def longest_su(s):
    res = ""
    for x in s:
        if x.endswith(res):
            res = x
        elif res.endswith(x):
            pass
        else:
            return -1
    return res


def solve():
    n = int(input())
    p = [input() for _ in range(n)]

    prefixes = {""}
    suffixes = {""}
    middles = {""}
    for pi in p:
        parts = pi.split("*")
        prefixes.add(parts[0])
        suffixes.add(parts[-1])
        middles.add("".join(parts[i] for i in range(1, len(parts) - 1)))
    prefixes.remove("")
    suffixes.remove("")
    middles.remove("")

    prefix = longest_pr(prefixes)
    suffix = longest_su(suffixes)

    # print(prefix)
    # print(suffix)

    if prefix == -1 or suffix == -1:
        return "*"
    else:
        return prefix + "".join(x for x in middles) + suffix


t = int(input())
for tt in range(1, t + 1):
    print("Case #" + str(tt) + ": " + str(solve()))
