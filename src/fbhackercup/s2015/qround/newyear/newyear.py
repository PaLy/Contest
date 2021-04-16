import multiprocessing


def solve():
    g = [int(x) for x in input().split()]
    n = int(input())
    pcf = []
    for _ in range(n):
        pcf.append(tuple(int(x) for x in input().split()))
    for mask in range(1 << n):
        s = [0, 0, 0]
        for i in range(n):
            if (mask >> i) & 1 == 1:
                for k in range(3):
                    s[k] += pcf[i][k]
        if g == s:
            return 'yes'
    return 'no'


def main():
    for t in range(int(input())):
        print('Case #{}:'.format(t + 1), solve())


if __name__ == '__main__':
    main()