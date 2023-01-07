# https://codeforces.com/problemset/problem/61/A

x = list(map(int, input()))
y = list(map(int, input()))

a = []

for i in range(len(x)):
    if x[i] == y[i]:
        a.append(0)
    else:
        a.append(1)

print(''.join(str(i) for i in a))

'''
This is my second attempt this challenge where I have used list comprehension to join the resulting
list.
'''