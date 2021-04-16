def solve():
    s = input()
    n = len(s)
    p = [s]
    for i in range(n):
        for j in range(i + 1, n):
            if i > 0 or s[j] > '0':
                p.append(s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:])
    p.sort()
    return p[0] + ' ' + p[-1]


def main():
    for t in range(int(input())):
        print('Case #{}:'.format(t + 1), solve())


if __name__ == '__main__':
    main()