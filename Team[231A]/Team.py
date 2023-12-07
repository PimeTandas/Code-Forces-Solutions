# https://codeforces.com/problemset/problem/231/A

x = int(input())
a = 0

for i in range(x):
    v = input()
    c = v.count('1')
    if c >= 2:
        a += 1
print(a)