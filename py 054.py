while True:
    a,b = map(int,input().split())
    if a == 0 and b == 0:break
    tot = plus = 0;length = max(len(str(a)), len(str(b)));a, b = str(a).zfill(length), str(b).zfill(length)
    for i in range(length):
        if ((int(a[i]) + int(b[i]))+plus)>=10:plus=1;tot += 1
        else:plus=0
    if 2 > tot > 0:
        print(f"{tot} carry operation.")
    elif tot > 1:
        print(f"{tot} carry operations.")
    else:
        print("No carry operation.")
