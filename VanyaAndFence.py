# x = number of freinds
# y = height of fence
x, y = map(int, input().split(' '))

h = map(int, input().split(' '))

width = 0

for height in h:
    if height > y:
        width += 2
    else:
        width += 1

print(width)