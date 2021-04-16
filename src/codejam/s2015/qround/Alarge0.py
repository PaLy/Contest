def main():
    row = input().split()
    smax = int(row[0])
    s = 0
    res = 0
    for i in range(smax + 1):
        if s < i:
            res += i - s
            s = i
        s += int(row[1][i])
    return res


if __name__ == '__main__':
    t = int(input())
    for ti in range(1, t + 1):
        print("Case #" + str(ti) + ": " + str(main()))
