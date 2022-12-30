# https://codeforces.com/problemset/problem/344/A

x = int(input())
a = []
g = 1

for i in range(x):
    m = input()
    a.append(m)
    if m == '10' and a[i-1] == '01' and i != 0:
        g += 1
    elif m == '01' and a[i-1] == '10'  and i != 0:
        g += 1

print(g)

'''

'''