from itertools import permutations as p
for i in range(int(input())):
    i,j,k = input().split(',');j,k=int(j),int(k)
    sort_that = sorted(int(''.join(p)) for p in list(p(i)))
    print(sort_that[j-1]+sort_that[k-1])
