a = 0
b = 1
n = int(input())
for i in range(1, n + 1):
    b = b * i
    a = a + b
print(a)