# https://codeforces.com/problemset/problem/705/A

x = int(input())
a =[]

for i in range(x):
    if i%2 == 0:
        a.append('I hate')
    else:
        a.append('I love')

    if i != (x-1):
        a.append('that')

a.append('it')
print(' '.join(a))

'''

'''