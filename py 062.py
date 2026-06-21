gcd = lambda a, b: gcd(b, a % b) if a % b != 0 else b
lcm = lambda f, g: f * g // gcd(f, g)
for _ in range(int(input())):
    d = list(map(int, input().split(',')))
    c = l = d[0]
    for e in d[1:]:
        c = gcd(c, e)
        l = lcm(l, e)
    print(f"{c} {l}")
