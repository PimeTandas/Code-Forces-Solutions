x = int(input())
count = 0

for i in range(x):
    y = input().upper()
    if y == '--X' or y == 'X--':
        count = count - 1
    else:
        count = count + 1
print(count)