# https://codeforces.com/problemset/problem/50/A

x, y = map(int, input().split(' '))

area = x*y
number = area // 2
print(number)

'''
First line takes an input of two numbers splits them by spaces. This corasponds to the board size/
We then use the two ints to workout the board size first input * second input.
Next work out how many 1*2 dominos will fit into this space, and finally print said number.
'''