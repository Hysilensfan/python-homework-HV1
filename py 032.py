#first method
for _ in range(int(input())):
    a = input();y = 0
    if len(a) == 16:
        for i in range(len(a)):
            if i % 2 == 0:
                d= int(a[i]) * 2
                if d > 9:
                    d -= 9
                else:
                    d = d
            else:
                d= int(a[i])
            y += d
        if y % 10 == 0:
            print("T")
        else:
            print("F")
    else:
        print("F")
#second method
for _ in range(int(input())):
    a = input()
if (sum(map(int,str(int(a[0])*2))) + sum(map(int,str(int(a[1])*1))) + sum(map(int,str(int(a[2])*2))) + sum(map(int,str(int(a[3])*1))) + sum(map(int,str(int(a[4])*2))) + sum(map(int,str(int(a[5])*1))) + sum(map(int,str(int(a[6])*2))) + sum(map(int,str(int(a[7])*1))) + sum(map(int,str(int(a[8])*2))) + sum(map(int,str(int(a[9])*1))) + sum(map(int,str(int(a[10])*2))) + sum(map(int,str(int(a[11])*1))) + sum(map(int,str(int(a[12])*2))) + sum(map(int,str(int(a[13])*1))) + sum(map(int,str(int(a[14])*2))) + sum(map(int,str(int(a[15])*1))))%10==0 and len(a)==16:
    print("T")
else:
    print("F")
