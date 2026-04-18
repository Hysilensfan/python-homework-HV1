# first method
for _ in range(int(input())):
    a=input().replace(" ","");b=input().replace(" ","")
    print("0" if set(a[1:]).isdisjoint(b[1:]) else len(set(b[1:]).intersection(a[1:])))
# second method
for _ in range(int(input())):
    a = list(map(int,input().split(' ')));b = list(map(int,input().split(' ')))
    print(len(set(a[1:]).intersection(b[1:])))
