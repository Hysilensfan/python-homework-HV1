for i in range(int(input())):
    u = d = 0;input();z = input().split(",")
    for e in range(len(z)-1):
        if int(z[e])> int(z[e+1]) :
            d += int(z[e]) - int(z[e + 1])
        elif int(z[e])< int(z[e+1]):
            u += int(z[e+1]) -int(z[e])
    print((u * 20)+(d * 10))
