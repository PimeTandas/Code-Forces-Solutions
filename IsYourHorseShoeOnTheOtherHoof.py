# https://codeforces.com/problemset/problem/228/A

x = set(map(int,input().split(' ')))
i = 0

if len(x) == 4:
    i = 0
else:
    i = 4-len(x)
print(i)

'''

'''