a1 = a2 = 0
b = int(input())
while b != 0:
    if b >= a1:
        a2, a1 = a1, b
    if a2 < b and b < a1:
        a2 = b
    b = int(input())
print('Второй максимум =', a2)







