def operation(f):
    f = f.replace("-", "+-").split("+");k=  0
    for n in f:
        if n!= "":
            k+=int(n.strip(" "))
    return k
for i in range(4):
    a,c = input().split("==")
    print("TRUE"if operation(a) == operation(c)else"FALSE")
