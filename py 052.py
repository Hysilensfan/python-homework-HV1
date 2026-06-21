from sys import stdin as s

prime_check = lambda n: n > 1 and all(n % i != 0 for i in range(2,int(n**0.5)+1))

for i in s:
    i = int(i.strip("\n"))
    if i == 0:
        pass
    else:
        tot = 0
        for c in range(2,int(i/2)+1):
            if prime_check(c) and prime_check(i - c):
                if c + (i - c) == i:
                    tot += 1
        print(tot)
