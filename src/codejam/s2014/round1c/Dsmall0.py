import bisect


def play_war(naomi, ken):
    score = 0
    naomi.sort()
    ken.sort()
    ken_lo = 0
    for naomi_w in naomi:
        pos = bisect.bisect(ken, naomi_w, lo=ken_lo)
        if pos == len(ken):
            score += 1
            ken_lo += 1
        else:
            ken.remove(ken[pos])
    return score


def play_deceitful_war(naomi, ken):
    score = 0
    naomi.sort()
    ken.sort()
    for ken_w in ken:
        pos = bisect.bisect(naomi, ken_w)
        if pos < len(naomi):
            score += 1
            naomi.remove(naomi[pos])
    return score


def main():
    input()
    naomi = list(map(float, input().split()))
    ken = list(map(float, input().split()))

    war_result = play_war(list(naomi), list(ken))
    deceitful_war_result = play_deceitful_war(list(naomi), list(ken))
    return str(deceitful_war_result) + ' ' + str(war_result)


if __name__ == '__main__':
    t = int(input())
    for ti in range(1, t + 1):
        print("Case #" + str(ti) + ": " + main())
