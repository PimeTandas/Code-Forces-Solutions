# https://codeforces.com/problemset/problem/281/A

x = input()
y, z = x[0], x[1:]
r = y.upper() + z
print(r)

'''
Input is assigned to x. Upper is a command that exists but that makes the whole thing uppercase, 
capitalise I think also exisits but that makes everything but the first character lowercase.
So what I had to do was split the string into its first character x[0] and the rest of the string
x[1:].
The first indexed character is capitalized then joined with the rest of the string and then printed.
'''