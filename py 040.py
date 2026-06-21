for e in range(int(input())):
    n = input();tot = 0;count_O=0
    for c in n:
        if c == "O":
            tot = tot + 1 + count_O
            count_O += 1
        else:
            count_O = 0
    print(tot)
