e = []
for s in range(int(input())):
    e.append(tuple(map(int, input().split())))
for i in sorted(e, key=lambda g: (-g[1], -g[2], g[0])):
    print(i[0], i[1], i[2])
