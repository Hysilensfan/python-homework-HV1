for _ in range(int(input())):
    s, p, tot = int(input()), input().split(","), 0  # Record the number of stops, the floors where the elevator stops, and the total cost. The cost is initialized to 0 by default
    if len(p) == s:  # Check whether the test data fully conforms to the requirements (optional)
        fst_p, p = int(p[0]), list(map(int,p[1:]))
        for a in p:
            a = int(a)
            if fst_p > a:
                tot += (fst_p - a) * 10
            elif fst_p < a:
                tot += (a - fst_p) * 20
            fst_p = a
        print(tot)
