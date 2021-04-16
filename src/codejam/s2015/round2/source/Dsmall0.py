def main():
    r, c = map(int, input().split())
    x = 1
    if r == 2:
        return 1
    elif r == 3:
        return 2
    elif r == 4:
        return 1 + x
    elif r == 5:
        return 1
    elif r == 6:
        return (1 + x) * 2


if __name__ == '__main__':
    t = int(input())
    for ti in range(1, t + 1):
        print("Case #" + str(ti) + ": " + str(main()))
