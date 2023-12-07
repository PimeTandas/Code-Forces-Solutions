# https://codeforces.com/problemset/problem/71/A

x = int(input())

for i in range(x):
    w = int(input())
    if len(w) > 10:
        print(w[0] + str(len(w)-2) + w[-1], sep='')
    else: 
        print(w)