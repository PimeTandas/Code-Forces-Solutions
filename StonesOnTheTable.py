x = int(input())
y = str(input().upper())
count = 0

for i in range(x-1):
    if y[i] == y[i+1]:
        count += 1
print(count)