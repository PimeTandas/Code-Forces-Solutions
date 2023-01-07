# https://codeforces.com/problemset/problem/61/A

x = list(map(int, input()))
y = list(map(int, input()))

a = []

for i in range(len(x)):
    if x[i] == y[i]:
        a.append(0)
    else:
        a.append(1)

for i in a:
    print(i, end='')

'''
I belive changes can be made to this one maybe removal of the second for loop.
This solution begins by taking in inputs in the form of 2 lists of 0s and 1s, and storing them in 
variables x and y.
An empty list is also created, a.
Next a for loop itterates over every number in both inputs and compairs the two to each other in an
if statement. If the two match a 0 is appended to our empty list, else a 1 is appended.
Finally to print the final resulting string is printed through the use of another for loop.
'''