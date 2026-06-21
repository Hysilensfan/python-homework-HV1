for _ in range(int(input())):
    N = int(input())
    lk=[]
    if N == 1:
        print(1)
        continue
    for i in range (9,1,-1):
        while N % i == 0:
            N//=i
            lk.append(str(i))
    print(-1 if N != 1 else"".join(sorted(lk)))

