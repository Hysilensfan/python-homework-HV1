for i in range(int(input())):
    list_digit = [0,0,0,0,0,0,0,0,0,0]
    h = ""
    for j in range(1,int(input())+1):
        h +=str(j)
    for w in range(len(list_digit)):
        for k in h:
            if k == str(w):
                list_digit[w]+=1
    print(*list_digit,sep = " ")
