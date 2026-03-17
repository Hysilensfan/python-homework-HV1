for _ in range(int(input())):
    a = input();b = input();print("N" if set(a).isdisjoint(b) else"".join(sorted(set(b).intersection(a))))
