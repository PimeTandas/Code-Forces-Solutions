# https://codeforces.com/problemset/problem/158/A

n, k = map(int, input().split(' '))
a = list(map(int, input().split(' ')))
count = 0

for i in range(len(a)):
    if a[i] >= a[k-1] and a[i] != 0:
        count += 1
print(count)   

'''
This one was a bit of a ball ache at first.
Firstly we deal with the first two inputs mapping the split of the input values to two variables.
The second input on the next line is mapped to a list variable again split by spaces.
What can be considered the main part of our program begins with a for loop, that iterates over the
length of a.
An if statement then checks to see each item in a is greater than or equal to the element in 
position k.
As long as the value of a[i] is not 0 the program will increase the count by 1.
'''