dic = {
    "A":(1,0),"B":(1,1),"C":(1,2),"D":(1,3),"E":(1,4),
    "F":(1,5),"G":(1,6),"H":(1,7),"I":(3,4),"J":(1,8),
    "K":(1,9),"L":(2,0),"M":(2,1),"N":(2,2),"O":(3,5),
    "P":(2,3),"Q":(2,4),"R":(2,5),"S":(2,6),"T":(2,7),
    "U":(2,8),"V":(2,9),"W":(3,2),"X":(3,0),"Y":(3,1),
    "Z":(3,3),
}
wei = "1987654321"
for i in range(int(input())):
    t = input();tot=0
    if len(t) != 10:
        print("0");continue
    if t[0] not in dic:
        print("0");continue
    if not t[2:].isdigit():
        print("0");continue
    if t[1] not in "12":
        print("F");continue
    n1,n2 =dic[t[0]];n3,n4,n5,n6,n7,n8,n9,n10,n11 = [int(i) for i in t[1:]];l = [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11]
    for c in range(10):
        tot+=l[c] * int(wei[c])
    tot+=l[10]
    print("0" if tot %10 != 0 else "1")
