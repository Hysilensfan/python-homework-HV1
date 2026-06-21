for _ in range(int(input())):
    N = (bin(int(input()))).replace("0b","");tot = 0
    for c in range(len(N)):
        if N[c] == '1':tot+=1
    print(tot)
