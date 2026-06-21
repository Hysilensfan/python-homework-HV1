def gcd(a, b):
    r = a % b
    return gcd(b, r) if r != 0 else b

for _ in range(int(input())):
    d = list(map(int, input().split(',')))
    c = d[0]
    for e in d[1:]:
        c = gcd(c, e)
    print(c)
