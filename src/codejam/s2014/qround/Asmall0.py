def main():
    r1 = int(input()) - 1
    r1_cards = [set(map(int, input().split())) for _ in range(4)]
    r2 = int(input()) - 1
    r2_cards = [set(map(int, input().split())) for _ in range(4)]
    inter = r1_cards[r1].intersection(r2_cards[r2])
    if len(inter) == 0:
        return "Volunteer cheated!"
    elif len(inter) == 1:
        return str(next(iter(inter)))
    else:
        return "Bad magician!"


if __name__ == '__main__':
    t = int(input())
    for ti in range(1, t + 1):
        print("Case #" + str(ti) + ": " + main())
