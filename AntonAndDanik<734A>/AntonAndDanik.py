# https://codeforces.com/problemset/problem/734/A

x = int(input())
g = list(input())

if g.count('A') > g.count('D'):
    print('Anton')
elif g.count('A') < g.count('D'):
    print('Danik')
else:
    print('Friendship')

'''
We start by taking our two inputs, the first being the number of games, the second being the outcome 
of said games.
We ensure that the second input of games outcomes is in a list format.
Lists have a handy count function that we use along with a if statement to check who won the most 
games. The out come of each part of the if statement prints the corresponding output.
'''