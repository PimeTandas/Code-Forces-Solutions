# https://codeforces.com/problemset/problem/112/A

x = input().upper()
y = input().upper()

if x < y:
    print('-1')
elif x > y:
    print('1')
else: 
    print('0')

'''
As with most solutions this one starts by taking two inputs as case does not matter we had to make 
each input either all upper case or all lower case (it does not matter which).
The next step is just a simple if statement that prints -1 if the first input is less than the second
1 if the first is greater than the second and 0 if they are equal.
'''