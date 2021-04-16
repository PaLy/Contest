def solve():
    n = int(input())
    w = [int(input()) for _ in range(n)]
    w = sorted(w, reverse=True)

    res = 0
    while True:
        if len(w) < 1 or w[0] * len(w) < 50:
            break
        else:
            res += 1
            q = (50 + w[0] - 1) // w[0] - 1
            if q > 0:
                w = w[1:-q]
            else:
                w = w[1:]
    return res


def main():
    for t in range(int(input())):
        print('Case #{}:'.format(t + 1), solve())


if __name__ == '__main__':
    main()
