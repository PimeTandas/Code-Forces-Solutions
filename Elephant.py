x = int(input())
count = 0

while x != 0:
    if x > 4:
        x -= 5
        count += 1
    elif x > 3:
        x -= 4
        count += 1
    elif x > 2:
        x -= 3
        count += 1
    elif x > 1:
        x -= 2
        count += 1
    elif x > 0:
        x -=1
        count += 1

print(count)