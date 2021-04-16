def solve():
    n = int(input())
    p = [int(input()) for _ in range(n + 1)]

    if n % 2 == 1:
        print(1)
        print(0)
    else:
        print(0)


def main():
    for t in range(int(input())):
        print('Case #{}:'.format(t + 1), end=' ')
        solve()


if __name__ == '__main__':
    main()
