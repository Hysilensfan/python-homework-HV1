for _ in range(int(input())):
    a, b = [list(map(int,input().split())) for i in range(2)]
    print(len(set(a[1:]).intersection(b[1:])))
