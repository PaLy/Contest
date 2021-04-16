def swap(a, i, j):
    pom = a[i]
    a[i] = a[j]
    a[j] = pom


def main():
    n = int(input())
    a = list(map(int, input().split()))
    pos = dict()
    for i in range(n):
        pos[a[i]] = i

    b = sorted(a)
    z = 0
    k = n - 1
    res = 0
    for i in range(n):
        mepos = pos[b[i]]
        if abs(mepos - z) < abs(mepos - k):
            for j in reversed(range(z, mepos)):
                pos[a[j]] += 1
                swap(a, j, j + 1)
            res += abs(mepos - z)
            z += 1
        else:
            for j in range(mepos + 1, k + 1):
                pos[a[j]] -= 1
                swap(a, j - 1, j)
            res += abs(mepos - k)
            k -= 1
    return res


if __name__ == '__main__':
    t = int(input())
    for ti in range(1, t + 1):
        print("Case #" + str(ti) + ": " + str(main()))
