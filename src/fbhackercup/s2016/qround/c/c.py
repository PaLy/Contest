def solve():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    i = 1
    j = 1
    res = 0
    while i <= n:
        while j < n and s[j] - s[i - 1] <= p:
            j += 1
        if s[j] - s[i - 1] > p:
            j -= 1
        if i <= j and s[j] - s[i - 1] <= p:
            res += j - i + 1
        i += 1
    return res


def main():
    for t in range(int(input())):
        print('Case #{}:'.format(t + 1), solve())


if __name__ == '__main__':
    main()
