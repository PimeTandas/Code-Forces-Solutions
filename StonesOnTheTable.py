x = int(input())
y = str(input().upper())
count = 0

for i in range(x):
    if y[i] == y[i+1] and i+1 < x:
        count = count + 1
print(count)