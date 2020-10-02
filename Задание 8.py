a = input().split()
b = []
for n in a:
    if int(n) % 2 == 0:
        b.append(int(n))
print(b)