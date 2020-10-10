d = {}
for i in range(int(input())):
    for m in input().split():
        d[m] = d.get(m, 0) + 1
for i in sorted(d.items(), key=lambda x: (x[0])):
    if i[1] == max(d.values()):
        print(i[0])
        break