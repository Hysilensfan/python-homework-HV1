for _ in range(int(input())):
    a=input().replace(" ","");b=input().replace(" ","")
    print("0" if set(a[1:]).isdisjoint(b[1:]) else len(set(b[1:]).intersection(a[1:])))
