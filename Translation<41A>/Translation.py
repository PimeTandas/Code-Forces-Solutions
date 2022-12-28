# https://codeforces.com/problemset/problem/41/A

s = input()[::-1]
t = input()

if t == s:
    print('YES')
else:
    print('NO')

'''
So learnt something new with this challenge. Python does not have a built in method to handle
reversing string text. The easyst (first method I came accross) to acheive this is reverse slicing
The above input which is assigned to the variable is sliced in -1 increments.
That said we simply do that for one input, use a if statment to compare the two and print yes/ no
accordingly.
'''