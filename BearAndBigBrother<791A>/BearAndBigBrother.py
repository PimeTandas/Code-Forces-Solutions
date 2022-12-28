# https://codeforces.com/problemset/problem/791/A

l, b = map(int, input().split(' '))
y = 0

while l <= b:
    l = l*3
    b = b*2
    y += 1
print(y)

'''
Starts by splitting the input and mapping the results to two integer variables, and create and set
the timer variable to 0.
Since we are looking for ls weight to be larger not just equal we use a while loop for this condition
and with each loop we tripple ls weight and double bs weight, once the loop exits we print the
time taken as required. 
'''