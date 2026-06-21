for _ in range(int(input())):
    b,c = input().split(', ');A=B=0
    for e in range(len(b)):
        if b[e] == c[e]:
            A+=1
        elif b[e] in c:
            B+=1
    print(f"{A}A{B}B")
