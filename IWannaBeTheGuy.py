# https://codeforces.com/problemset/problem/469/A
 
l = int(input())
x = list(map(int, input().split(' ')))
x.pop(0)
y = list(map(int, input().split(' ')))
y.pop(0)

count = 0
union = x + y

for i in range(1, l+1):
    if i in union:
        count += 1
    else:
        continue

if count == l:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')

'''
Right since I am dumb as fuck and didnt read the question properly this problem took me longer than
I am willing to admit.
The solution was easy in the end. We start by taking input of the number levels needed to be compleated.
We then take two more inputs for x and y, assign them to either a list or set and remove the first index
we then run through the range of i using a for loop ensuring i is in the union of our two inputs 
if the two inputs cover the range and thus equal the same total count which we have been incresing
by one with each itteration if right we print 'I become the guy, else we print Oh my Keyboard.
'''