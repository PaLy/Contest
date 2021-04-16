def main():
    n, x = map(int, input().split())
    s = list(map(int, input().split()))
    s.sort(reverse=True)
    l = n - 1
    res = 0
    for i in range(n):
        if i > l:
            break
        if i == l:
            res += 1
        else:
            if s[i] + s[l] <= x:
                l -= 1
            res += 1
    return res


if __name__ == '__main__':
    t = int(input())
    for ti in range(1, t + 1):
        print("Case #" + str(ti) + ": " + str(main()))
