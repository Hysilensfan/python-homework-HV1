def report(v):
    r, k = '', 1
    for i in range(1, len(v)):
        if v[i] == v[i - 1]:
            k += 1
        else:
            r += v[i - 1] + str(k)
            k = 1
    r += v[-1] + str(k)
    return r

for _ in range(int(input())):
    print(report(input()))
