n, k = map(int, input().split(' '))
a = map(int, input().split(' '))
count = 0

for i in a:
    if a[-1] > k:
        count =  n
print(count)    
