#x = starting number 
#y = number of subtractions
x, y = map(int, input(). split(' '))

for i in range(y):
    if x[-1] == 0:
        x = x//10
        y -= 1
    else:
        x -= 1
        y -= 1
print(y)

