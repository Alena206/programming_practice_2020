a = input().split()
b = [int(i) for i in a]
z = g = 0
for n in range(0, len(b)):
    if b[n] > b[z]:
        z = n
    if b[n] < b[g]:
        g = n
b[z], b[g] = b[g], b[z]
print(' '.join([str(n) for n in b]))






