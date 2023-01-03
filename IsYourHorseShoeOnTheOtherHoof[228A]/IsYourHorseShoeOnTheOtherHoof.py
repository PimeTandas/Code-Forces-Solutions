# https://codeforces.com/problemset/problem/228/A

x = set(map(int,input().split(' ')))
i = 0

if len(x) == 4:
    i = 0
else:
    i = 4-len(x)
print(i)

'''
We start by taking the input to a set as sets only allow one of each value which is perfect for this
problem. We check to see if any horse shoes need purchasing in the first place. If they do we take 
four way from the result to find out how many need to be purchased then print the result.
'''