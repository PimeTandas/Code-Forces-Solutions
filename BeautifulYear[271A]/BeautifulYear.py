# https://codeforces.com/problemset/problem/271/A

x = int(input()) + 1

while len(set(str(x))) < 4:
    x +=1

print(x)

'''
This solution begins by takin gin the year as an integer, we add one to it to ensure that we are not
returned the year we are given.
We then check the a set made up of the numbers from each year, sets do not allow for duplicates so the
set will only be made up of unique values. As soon as the length of the set is nolonger less than 4
we print the year.
'''