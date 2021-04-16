def main():
    def contains(c):
        for row in mapa:
            if row.count(c) > 0:
                return True
        return False

    def cases():
        ss = [row for row in mapa]
        ss.append(''.join(mapa[i][i] for i in range(4)))
        ss.append(''.join(mapa[i][3 - i] for i in range(4)))
        ss.extend(''.join(mapa[row][col] for row in range(4)) for col in range(4))
        return ss

    def is_winner(c):
        for case in cases():
            if case.count(c) == 4 or (case.count(c) == 3 and case.count('T') == 1):
                return True
        return False


    mapa = [input() for _ in range(4)]
    if is_winner('X'):
        return "X won"
    elif is_winner('O'):
        return "O won"
    elif contains('.'):
        return "Game has not completed"
    else:
        return "Draw"


if __name__ == '__main__':
    t = int(input())
    for ti in range(1, t + 1):
        print("Case #" + str(ti) + ": " + main())
        input()
