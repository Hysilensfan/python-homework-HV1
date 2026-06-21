# first method
def recurtion(w):
    t = 1
    if w != 0 and w!= 1:
        for i in range(1, w + 1):
            t *= i
        return t
    else:
        return 1
for _ in range(int(input())):
    c = int(input())
    print(recurtion(c))

#second method
recurtion = lambda w:  w * recurtion(w-1) if w != 0 else 1
for _ in range(int(input())):
    print(recurtion(int(input())))
