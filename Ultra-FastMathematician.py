# https://codeforces.com/problemset/problem/61/A

x = list(map(int, input()))
y = list(map(int, input()))

a = []

for i in range(len(x)):
    if x[i] == y[i]:
        a.append(0)
    else:
        a.append(1)

for i in a:
    print(i, end='')

'''
I belive changes can be made to this one maybe removal of the second for loop
'''