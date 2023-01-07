# https://codeforces.com/problemset/problem/263/A

a = []
x = 0
y = 0

for i in range(5):
    bm = input().split(' ')
    a.append(bm)
    for j in range(5):
        if a[i][j] == '1':
            x = i - 2
            y = j - 2
            print(abs(x) + abs(y))

'''
This one was slightly difficult to begin with, till I realised I was going about it the wrong way, 
and needed to use nested for loops.
This solution seems to be the best I can think of. 
It starts by defining an empty list, and two empty int variables x and y.
We then use two nested for loops to first split and assign/ append the first list to the matrix list.
The second loop goes through the lists indexes looking for where the 1 is located.
Finally an if statement is used to check for the position of 1. Since the position we are looking for
is in index[2] we need to find the difference between where the 1 is and 2.
This is done by taking away to and using the absolute value to sort out any negitives we might have. 
'''



