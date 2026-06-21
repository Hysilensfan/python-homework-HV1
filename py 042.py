for _ in range(int(input())):
    A,B,N = map(int,input().split());tot=0
    for e in range(A,B+1):
        if str(N) in str(e):tot+=1
    print(tot)
