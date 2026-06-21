dic = {
    "A":(1,0),"B":(1,1),"C":(1,2),"D":(1,3),"E":(1,4),
    "F":(1,5),"G":(1,6),"H":(1,7),"I":(3,4),"J":(1,8),
    "K":(1,9),"L":(2,0),"M":(2,1),"N":(2,2),"O":(3,5),
    "P":(2,3),"Q":(2,4),"R":(2,5),"S":(2,6),"T":(2,7),
    "U":(2,8),"V":(2,9),"W":(3,2),"X":(3,0),"Y":(3,1),
    "Z":(3,3)
}
l = "1987654321"
def ope():
    c= list(dic.keys());l2 = [n3, n4, n5, n6, n7, n8, n9, n10, n11]
    for p in range(26):
        tot = 0
        m = c[p];n1,n2= dic[m];w= [n1,n2];l2 = w + l2
        for k in range(10):
            tot += l2[k] * int(l[k])
        tot += int(l2[10])
        if tot % 10 == 0:
            print(m,end="")
        del l2[0:2]
    print()
for _ in range(int(input())):
    s = list(input())
    n3, n4, n5, n6, n7, n8, n9, n10, n11 = [int(j) for j in s]
    ope()
