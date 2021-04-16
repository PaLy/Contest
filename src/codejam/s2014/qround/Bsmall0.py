def main():
    c, f, x = map(float, input().split())
    best_time = x / 2
    time = c / 2
    farms = 1
    while True:
        ptime = x / (2 + farms * f)
        if time + ptime < best_time:
            best_time = time + ptime
        else:
            break
        time += c / (2 + farms * f)
        farms += 1
    return "{:.7f}".format(best_time)


if __name__ == '__main__':
    t = int(input())
    for ti in range(1, t + 1):
        print("Case #" + str(ti) + ": " + main())
