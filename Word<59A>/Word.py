# https://codeforces.com/problemset/problem/59/A

w = input()
cap = 0
low = 0
for i in w:
    if i.islower():
        low += 1
    else:
        cap += 1

if low < cap:
    w = w.upper()
elif low > cap:
    w = w.lower()
else:
    w = w.lower()
print(w)

'''
We start by assigning input to w, and creating two variables set to 0 which will function as a count
of weather letter is lower case or upper case.
A for loop with a nested if statment is used to get a count of upper and lower case occarances.
The second part of the solution compares the two counts, and prints according to the breif.
'''