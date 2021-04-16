import math


def solve():
    n, k = map(int, input().split())
    a = [int(x) for x in input().split()]
    a.sort()
    res = 0
    if a[0] == 0:
        a = a[1:]
    for i in range(len(a)):
        if a[i] < k:
            res += k - a[i]
            a[i] = k
    while a and a[0] == k:
        a = a[1:]

    if not a:
        return res
    else:  # every > k
        n = len(a)
        cache = {}
        biggest = a[-1]
        for i in range(len(primes)):
            if primes[i] > biggest:
                bi = i
                break

        def best(cond, mask, floor):
            tup = (cond, mask, floor)
            if tup in cache:
                return cache[tup]
            elif cond == n:
                # return (), 0
                return 0
            else:
                res = INF
                # resT = ()
                # for x in range(math.ceil(max(a[cond], floor) / k), len(fact)):
                mm = len(fact)
                if bi + cond < len(primes):
                    mm = primes[bi + cond]
                for x in range(math.ceil(max(a[cond], floor) / k), mm):
                    ok = True
                    nmask = mask
                    for p in fact[x]:
                        if (1 << mp[p]) & mask != 0:
                            ok = False
                            break
                        nmask |= 1 << mp[p]
                    if ok:
                        r = best(cond + 1, nmask, k * x + 1)
                        # rec = r[1]
                        rec = r
                        inc = k * x - a[cond]
                        if rec + inc < res:
                            # resT = (x * k,) + r[0]
                            res = rec + inc

                # cache[tup] = resT, res
                cache[tup] = res
                return cache[tup]

        r = best(0, 0, 0)
        # print(r[0])
        # return res + r[1]
        return res + r


def main():
    for t in range(int(input())):
        print('Case #{}:'.format(t + 1), solve())
        # break

    # t = 20
    # print(t)
    # for _ in range(t):
    #     n = random.randint(2, 20)
    #     k = random.randint(1, 20)
    #     print(n, k)
    #     print(' '.join(str(random.randint(0, 50)) for _ in range(n)))


if __name__ == '__main__':
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
              103, 107, 109, 113, 127]
    mp = {primes[i]: i for i in range(len(primes))}
    INF = 1000000000000000000
    fact = [(), ()]
    tt = set()
    for i in range(2, 128):
        t = ()
        t2 = set()
        x = i
        for k in range(2, i + 1):
            while x % k == 0:
                t += (k, )
                t2.add(k)
                x //= k
        fact.append(t)
        tt.add(tuple(sorted(t2)))

    # print('\n'.join(str(x) for x in fact))
    # print('\n'.join(str(x) for x in tt))
    # print(len(tt))

    main()