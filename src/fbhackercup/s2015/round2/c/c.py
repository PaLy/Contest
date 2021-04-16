import random

t = 20
print(t)


def randomstring(n):
    s = ""
    for _ in range(n):
        s += chr(ord('a') + random.randint(0, 25))
    return s


for _ in range(t):
    n = 2000
    k = 100
    print(str(n) + " " + str(k))
    p = set()
    for i in range(n):
        while True:
            s = randomstring(10)
            if s not in p:
                p.add(s)
                break
    for x in p:
        print(x)
