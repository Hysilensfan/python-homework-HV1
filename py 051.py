from collections import Counter as C
dict_ = []
for i in range(int(input())):
    dict_.append(input().split(' ')[0])
k = list(sorted(C(dict_).items()))
for c in range(len(k)):
    print(f"{k[c][0]} {k[c][1]}" )
