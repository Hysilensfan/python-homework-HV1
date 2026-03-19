for _ in range(int(input())):
    a = input().split(" ")
    if len(a) < 22:
        for c in range(len(a)):a[c]= int(a[c])
        a = sorted(list(a));print(f"{int(a[-1])} {int(a[-2])}")
