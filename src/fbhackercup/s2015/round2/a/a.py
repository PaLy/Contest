from collections import deque


def solve():
    n = int(input())
    p = list(map(int, input().split()))

    i = 1
    j = n - 1
    pole = deque()
    pole.appendleft(p[0])
    ok = True
    while i != j:
        if p[i] == pole[-1] + 1:
            pole.append(p[i])
            i += 1
        elif p[i] == pole[0] - 1:
            pole.appendleft(p[i])
            i += 1
        elif p[j] == pole[-1] + 1:
            pole.append(p[j])
            j -= 1
        elif p[j] == pole[0] - 1:
            pole.appendleft(p[j])
            j -= 1
        else:
            ok = False
            break
    if ok:
        return "yes"

    i = 0
    j = n - 2
    pole = deque()
    pole.append(p[-1])
    ok = True
    while i != j:
        if p[i] == pole[-1] + 1:
            pole.append(p[i])
            i += 1
        elif p[i] == pole[0] - 1:
            pole.appendleft(p[i])
            i += 1
        elif p[j] == pole[-1] + 1:
            pole.append(p[j])
            j -= 1
        elif p[j] == pole[0] - 1:
            pole.appendleft(p[j])
            j -= 1
        else:
            ok = False
            break
    if ok:
        return "yes"

    return "no"


def main():
    for t in range(int(input())):
        print('Case #{}:'.format(t + 1), solve())


if __name__ == '__main__':
    main()