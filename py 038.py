for _ in range(int(input())):
    N = input();t = 4;A=B=''
    for i in range(len(N)):
        if N[i] == '4':A+='3';B+='1'
        else:A+=N[i];B+='0'
    print(f"{A} {int(B)}")
