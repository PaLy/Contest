from itertools import permutations

print(1)
print(475)

xs = []
for x in permutations('ABCDE'):
    xs.append(x)

for i in range(len(xs)-1):
    for j in range(3):
        print(xs[i][j])

print(xs[-1][4])