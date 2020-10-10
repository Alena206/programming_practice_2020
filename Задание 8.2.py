n = int(input())
dict = {}
for i in range(n):
    k, v = input().split()
    dict[k] = v
c = input()
print(dict.get(c) or ''.join([k for k, v in dict.items() if v == c]))