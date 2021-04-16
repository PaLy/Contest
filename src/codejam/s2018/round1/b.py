def solve():
    r, b, c = map(int, input().split())
    msp = [tuple(map(int, input().split())) for _ in range(c)]

    max_time = max(msp[i][0] * msp[i][1] + msp[i][2] for i in range(c)) + 1
    min_time = 0

    def check(time):
        items = [max(0, min(msp[i][0], (time - msp[i][2]) // msp[i][1])) for i in range(c)]
        items.sort(reverse=True)
        return sum(items[:r])

    while min_time + 2 < max_time:
        mid_time = (min_time + max_time) // 2
        total_items = check(mid_time)
        if total_items >= b:
            max_time = mid_time
        else:
            min_time = mid_time + 1

    t1 = check(min_time)
    t2 = check(min_time + 1)
    t3 = check(min_time + 2)
    if t1 >= b:
        return min_time
    if t2 >= b:
        return min_time + 1
    if t3 >= b:
        return min_time + 2


t = int(input())
for tt in range(1, t + 1):
    print("Case #" + str(tt) + ": " + str(solve()))
