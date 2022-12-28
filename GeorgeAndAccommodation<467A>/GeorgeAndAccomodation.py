# https://codeforces.com/problemset?order=BY_RATING_ASC

x = int(input())
n = 0

for i in range(x):
    y, x = map(int, input().split(' '))
    if (x - y) >= 2:
        n += 1
    else: 
        n = n
print(n)

'''
Start by taking the inital int input stating how many rooms our code will be checking. Then take in
said amount of inputs, this is done using a for loop. The values are split and mapped to two 
variables. These are then used in a if statement to check if the difference in the two is greater than
2. If it is then this accommodation is suitable for our pair and we increase the count by 1.
'''