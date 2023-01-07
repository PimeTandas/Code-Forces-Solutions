# https://codeforces.com/problemset/problem/231/A

x = int(input())
a = 0

for i in range(x):
    v = input()
    c = v.count('1')
    if c >= 2:
        a += 1
print(a)

'''
We first take the number of potential problems in the contest from input ensuring it is an int.
Using a for loop we loop over the number of problems, to get peoples desisions for each. For each 
iteration of the loop we accept one input, for which we will count the number of occarances of 1.
For each problem with 2 or more 1s increase a by 1. 
'''