def solve():
    n, k, c = map(int, input().split())
    res = k * n
    z = 0
    while c > (k // n) * n:
        r = k % n
        res = min(res, n - r + c + z)
        n -= 1
        z += 1
    res = min(res, z + c)
    return res


def main():
    for t in range(int(input())):
        print('Case #{}:'.format(t + 1), solve())


if __name__ == '__main__':
    main()