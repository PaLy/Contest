import random

t = 100
print(t)
for _ in range(t):
    n = 100
    m = 5000
    k = 5000
    print(n, m, k)
    for _ in range(m):
        a = b = random.randint(1, n)
        while b == a:
            b = random.randint(1, n)
        g = random.randint(1, 1000)
        print(a, b, g)
    for _ in range(k):
        s = d = random.randint(1, n)
        while s == d:
            d = random.randint(1, n)
        print(s, d)

