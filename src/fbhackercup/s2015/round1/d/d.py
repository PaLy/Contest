import random

t = 100
print(t)


def myrand(i):
    if i == t - 1:
        return random.randint(i, i)
    elif i > t - 10:
        return random.randint(max(1, i - 5), i)
    else:
        return random.randint(1, i)


for _ in range(t):
    n = 200000
    print(n)
    p = [0]
    for i in range(1, n):
        p.append(myrand(i))
    print(' '.join(str(x) for x in p))
