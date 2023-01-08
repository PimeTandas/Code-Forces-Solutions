# https://codeforces.com/problemset/problem/996/A

d = int(input())
b = [100, 20, 10, 5, 1]
c = 0

for i in b:
    c += d//i
    d = d%i
print(c)

'''
We start by taking the variable d as input which represents dollars in an account. B is a list we 
create to represent the allowable bills. We also create a counter variable c and set it to zero.
A for loop is used to itterate through each of the bills starting with the highest continuing down to 
lowest. 
For each itteration we do two things. 1. We find how many times that bill goes in to the amount of 
dollars using floored division and setting c to be this plus what ever it was before.
2. We then find what is remaining of our dollars after we preform this division and update the 
account value accordinly before the next itteration can begin.
Finally as always we print the resulting count.
'''