# https://codeforces.com/problemset/problem/677/A

x, y = map(int, input().split(' '))
h = map(int, input().split(' '))
width = 0

for height in h:
    if height > y:
        width += 2
    else:
        width += 1
print(width)

'''
The first input gives us the number of friends and the height of the fence. The next line we take 
in the height of each person.
Using a for loop we itterate over each of the 'friends' hights and check to see if the hight is 
greater than the height of the fence. If it is we have to increase the width of the group by 2. If
not then we can just keep with the increase of 1. And again as with most solutions we print the final
count of the width variable.
'''