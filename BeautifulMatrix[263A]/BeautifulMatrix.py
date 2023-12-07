# https://codeforces.com/problemset/problem/263/A

a = []
x = 0
y = 0

for i in range(5):
    bm = input().split(' ')
    a.append(bm)
    for j in range(5):
        if a[i][j] == '1':
            x = i - 2
            y = j - 2
            print(abs(x) + abs(y))