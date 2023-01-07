# https://codeforces.com/problemset/problem/282/A

x = int(input())
count = 0

for i in range(x):
    y = input().upper()
    if y == '--X' or y == 'X--':
        count = count - 1
    else:
        count = count + 1
print(count)

'''
As with most answers this one starts by taking input in the form of a single int. This is the
amount of 'Bitland' commands the program will take.
A for loop is then used to take in each of these bitland commands.
A basic if statement checks to see if the bitland command is for subration if it is not it is
assumed it is a addition, and the count is updated, once all bitland comands have been dealt with
the final count is printed.
'''