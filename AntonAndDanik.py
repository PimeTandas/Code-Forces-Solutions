# https://codeforces.com/problemset/problem/734/A

x = int(input())
g = input()
l = []

for i in range(x):
    l.append(g[i])

a = l.count('A')
d = l.count('D')

if a > d:
    print('Anton')
elif a < d:
    print('Danik')
else:
    print('Friendship')

'''

'''