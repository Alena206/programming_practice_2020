a = [int(i) for i in input().split()]
c = 0
for i in range(0, len(a)):
    for n in range(1, len(a)):
        if a[n] == a[i]:
            c +=1
print(c)