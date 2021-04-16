def to_bin(x):
    return bin(x)[2:].rjust(50, '0')


def solve(a, b, k, distinct, not_first_a, not_first_b):
    end = len(a) - 1
    if end == 0:
        if k[0] == '0':
            if distinct:
                return 2
            else:
                return 1
    else:
        if k[0] == '1':
            if a[0] == '0' and b[0] == '0':
                return solve(a[1:], b[1:], k[1:], distinct, not_first_a, not_first_b)
            elif a[0] == '1' and b[0] == '1':
                res = solve(a[1:], b[1:], k[1:], True, True, not_first_b)
                res += solve(a[1:], b[1:], k[1:], True, not_first_a, True)
                res += solve(a[1:], b[1:], k[1:], distinct, not_first_a, not_first_b)  # 0,0
                return res
            elif a[0] == '1':
                return solve(a[1:], b[1:], k[1:], True, True, not_first_b)
            elif b[0] == '1':
                return solve(a[1:], b[1:], k[1:], True, not_first_a, True)
        else:
            if a[0] == '0' and b[0] == '0':
                res = solve(a[1:], b[1:], k[1:], distinct, not_first_a, not_first_b)
                if not_first_a and not_first_b:
                    res += solve(a[1:], b[1:], k[1:], distinct, not_first_a, not_first_b)
                return res
            elif a[0] == '1' and b[0] == '1':
                return solve(a[1:], b[1:], k[1:], distinct, True, True)
            elif a[0] == '1':
                return solve(a[1:], b[1:], k[1:], True, True, not_first_b)
            elif b[0] == '1':
                return solve(a[1:], b[1:], k[1:], True, not_first_a, True)


def main():
    A, B, K = map(int, input().split())
    a = to_bin(A - 1)
    b = to_bin(B - 1)
    k = to_bin(K - 1)
    for i in range(len(a)):
        if a[i] == '0' and b[i] == '0':
            if k[i] == '1':
                return str(2 * A * B)
        else:
            a = a[i:]
            b = b[i:]
            k = k[i:]
            return
    return str(solve(a, b, k, False, False, False))


if __name__ == '__main__':
    t = int(input())
    for ti in range(1, t + 1):
        print("Case #" + str(ti) + ": " + main())
