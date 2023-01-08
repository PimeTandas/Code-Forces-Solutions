# https://codeforces.com/problemset/problem/1030/A

x = input()
o = map(int, input().split(' '))

if sum(o) >= 1:
    print('HARD')
else:
    print('EASY')

'''
We start by taking an input x which represents the number of people who where asked to give their
opinion.
The second input o represents their opinions 1 means they though hard and 0 means they though it 
was easy. We map this second input to a list of values. It will be made up of 0s and 1s so we can 
simpliy check if their are any 1s present in said list. If there is then we print hard, else easy.
'''