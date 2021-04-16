# Read init information from standard input, if any

while 1:
    # Read information from standard input
    sx, sy = map(int, input().split())
    mountains = [(int(input()), i) for i in range(8)]
    mountains.sort()
    ma_pos = mountains[-1][1]

    if sx == ma_pos:
        print("FIRE")
    else:
        print("HOLD")
    
    # print("Debug messages...", file=sys.stderr)