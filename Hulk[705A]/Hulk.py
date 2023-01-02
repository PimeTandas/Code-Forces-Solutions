# https://codeforces.com/problemset/problem/705/A

x = int(input())
a = []

for i in range(x):
    if i%2 == 0:
        a.append('I hate')
    else:
        a.append('I love')

    if i != (x-1):
        a.append('that')

a.append('it')
print(' '.join(a))

'''
Quite a cool Challenge I really enjoyed this one, good way to start the year :D
Starts by taking an input and creates an empty list variable a. We then use a for loop to itterate
over a range which is supplied x.
The first if statement in this for loop basicly just checks to see if the currect itteration is 
odd or even, if its odd and for each will append I hate or I love to the list.
After each of the first if statements another if statement runs checking to see if this is the last
itteration, if it is it will not add another 'that' to the list. Finally after the for loop as finished
we append 'it' to the list which marks it as compleated. Finally we join and print the list as 
required par the brief.
'''

