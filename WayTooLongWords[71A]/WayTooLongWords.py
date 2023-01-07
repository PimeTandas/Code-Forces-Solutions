# https://codeforces.com/problemset/problem/71/A

x = int(input())

for i in range(x):
    w = int(input())
    if len(w) > 10:
        print(w[0] + str(len(w)-2) + w[-1], sep='')
    else: 
        print(w)

'''
Here a for loop is used to take in the correct amount of words, as provided by the user.
The length of each provided word is then checked. If its length is greater than 10 the abbreviated 
version of the word is printed as stated in the challenge. Else the the original word is printed.
'''