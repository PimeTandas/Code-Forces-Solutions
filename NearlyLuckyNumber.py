x = list(map(int, input()))

luckCount = 0

for i in x:
    if i == 4 or i == 7:
        luckCount += 1
    else:
        continue

if luckCount == 4 or luckCount == 7:
    print('YES')
else:
    print('NO')
