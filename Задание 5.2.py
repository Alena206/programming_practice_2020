a = set(input().split())
b = set(input().split())
c = set()
for i in a.intersection(b):
    c.add(i)
    print(c)