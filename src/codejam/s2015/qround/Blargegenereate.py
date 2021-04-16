import random

t = 1
print(t)
for _ in range(t):
    d = 1000
    p = [random.randint(1, 1000) for _ in  range(d)]
    print(d)
    print(' '.join(str(x) for x in p))
