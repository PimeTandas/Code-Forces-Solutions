# https://codeforces.com/problemset/problem/510/A

y, x = map(int, input().split(' ')) # x Represents the x direction and y obviously represents the y direction
s = 'r'

for i in range(y):
    if (i % 2 == 0) and (i != 1):
        print('#' * x)
    elif s == 'r':
        print('.' * (x-1) + '#')
        s = 'l'
    else:
        print('#' + ((x-1) * '.'))
        s = 'r'

'''
This solution begins by taking input in the form of the height y and width of the snake x. We split the input to achieve this. Next I have defiend s which is ment to represent which side the next turn or kink of the snake appears on, this will be explained later.
A for loop is used as the main body of this solution, it itterated through the length of the snake (height). For each itteration we work out if the itteration is even or one if it is that is to be one of our flat sides to the snake so we just print '#' * the width (x).
If it is not then we check if the side that the kink is ment to be on is left or right and then print accordingly in a similar mannor. We also use this to update the s varaible changing the side of the next kink, this works for both left and right.
I belive there might be another way of acheiving the same thing so I will most likely come back to try this challenge again.
'''