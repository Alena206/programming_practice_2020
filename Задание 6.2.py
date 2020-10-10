a = set()
b = [int(i) for i in input().split()]
for m in b:
    if m in a:
        print('YES')
    else:
        print('NO')
    a.add(m)
