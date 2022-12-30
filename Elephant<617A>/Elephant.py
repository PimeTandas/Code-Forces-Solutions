# https://codeforces.com/problemset/problem/617/A

x = int(input())
count = 0

while x != 0:
    if x > 4:
        x -= 5
        count += 1
    elif x > 3:
        x -= 4
        count += 1
    elif x > 2:
        x -= 3
        count += 1
    elif x > 1:
        x -= 2
        count += 1
    elif x > 0:
        x -=1
        count += 1
print(count)

'''
This solution begins with taking an int input and assigning it to a variable.
We use a while loop to reduce x (the target) before we make a reduction we want to check what
the largest reduction we can make is luckily there are only 5 values we need to check for so we 
just used 5 for loops increasing the count, which represents steps to get to zero. Prining it at
the end.
'''