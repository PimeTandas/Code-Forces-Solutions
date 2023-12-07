num = int(input())
count = 0
for i in range(num):
    x, y, z = map(int, input().split(' '))
    count += x + y + z

if count == num:
    print("YES")
else:
    print("NO")