a = input().split()
b = [int(i) for i in a]
c = 0
for m in range (1, len(b) - 1):
  if b[m] > b[m - 1] and b[m] > b[m + 1]:
    c += 1
print(c)
