# https://codeforces.com/problemset/problem/486/A

x = int(input())
y = list(range(1, (x + 1)))
s = 0
i = 0
while i <= 4:
    i += 1
    if i%2 != 0:
        s = s - i
    else:
        s = s + i
    i += 1
print(s)






'''
for i in range(1,x):
    if i%2 != 0:
        s -= i
    else:
        s += i
print(s)
'''
