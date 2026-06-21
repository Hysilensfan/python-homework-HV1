from sys import stdin as std
from collections import Counter as Cou

Iie = []
for k in std:
    Iie.append(k.strip())
    if len(Iie) == 2:
        c = Cou(Iie[0]) & Cou(Iie[1])
        print(*sorted(''.join(k * c[k] for k in c)), sep="")
        Iie.clear()
