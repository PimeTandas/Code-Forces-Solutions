# https://codeforces.com/problemset/problem/158/A

# n = number of partisipants 
# k = place


n, k = map(int, input().split(' '))
a = input().split(' ')
num = sorted(a)[k]
print(a)

count = 0

for i in range(len(a)):
    print(i)
    if i > a[k]:
        count += 1
print(count)

'''
need to get the value at a[k]
'''