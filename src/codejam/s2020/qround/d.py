def solve10():
    array = [0] * b

    for i in range(b):
        print(i + 1)
        sbit = input()
        if sbit == "N":
            exit(0)
        else:
            array[i] = int(sbit)

    print("".join(str(x) for x in array))
    result = input()
    if result == "N":
        exit(0)


def solve20():
    array = [0] * b

    for i in range(b):
        print(i + 1)
        sbit = input()
        if sbit == "N":
            exit(0)
        else:
            array[i] = int(sbit)

    print("".join(str(x) for x in array))
    result = input()
    if result == "N":
        exit(0)


def solve():
    pass


t, b = map(int, input().split())
for tt in range(1, t + 1):
    if b == 10:
        solve10()
    elif b == 20:
        solve20()
    else:
        solve()
