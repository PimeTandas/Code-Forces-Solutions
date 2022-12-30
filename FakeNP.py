# https://codeforces.com/problemset/problem/805/A

x = list(map(int, input().split(' ')))
r = list(range(x[0], x[1]+1))
a = []

for c in range(1, 10):
        if i % c == 0:
            a.append(c)
        else:
            continue

print(a)
