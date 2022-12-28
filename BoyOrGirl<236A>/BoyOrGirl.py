# https://codeforces.com/problemset/problem/236/A

x = set(input())
if len(x) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')

'''
Nice simple challenge, if username contains an even number of distinct letters then the user is a 
girl, else (is odd) and user is a boy.
We take an input and make it a set, as sets contain only unique (distinct) values.
Then its simple find the length of the set, check if its even and print YES or NO depending.
'''