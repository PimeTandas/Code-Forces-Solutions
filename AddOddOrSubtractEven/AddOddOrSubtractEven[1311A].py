# https://codeforces.com/problemset/problem/1311/A

x = int(input())
list = []

for i in range(x):
    a, b = map(int, input().split(' '))
    if a == b:
        list.append(0)
    elif (a > b) and (a - b) % 2 == 0 or (a < b) and (b - a) % 2 == 1:
        list.append(1)
    else:
        list.append(2)

for i in  list:
    print(i)

'''
After reading the breif for this problemset it was quite obvious that there where three possible test cases
'''

