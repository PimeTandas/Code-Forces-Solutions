# https://codeforces.com/problemset/problem/4/A

x = int(input())
if x%2 == 0 and x != 2:
    print("YES")
else:
    print("NO")

'''
Pete and Billy sound autistic as fuck.
Weight of the watermellon is given via input. We then check the weight to see if it is an even 
number. (Even numbers will always return two even numbers when divided by 2, unless that 
number is 2). Thus we also check to ensure the weight is not 2. Returning YES and NO accordingly.
'''