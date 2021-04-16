import random

t = 1
print(t)
for _ in range(t):
    n = 100
    print(n)
    print(*(random.randint(1, 1000) for _ in range(n)))