# https://codeforces.com/problemset/problem/977/A

x, y = map(int, input().split(' '))

for i in range(y):
    if x % 10 != 0:
        x = x - 1
    elif x % 10 == 0:
        x = x // 10
print(x)

'''
Starts by taking input splitting it and mapping the values to two int variables.
Next uses a for loop to loop over the amount of subtractions we are going to be making.
Finally we check the two conditions stated in the breif and execute the subtraction accordingly.
Printing the end value after y amount of subtractions to our original number.
'''