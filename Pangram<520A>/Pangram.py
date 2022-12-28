# https://codeforces.com/problemset/problem/520/A

x = int(input())
y = set(input().lower())

if x >= 26 and len(y) == 26:
    print('YES')
else:
    print('NO')


'''
Learnt a new word: A Pangram is a sentance or word that includes every single letter in the alphabet.
This seemed an obvious task for a set seeing as they can only include distinct values.
Once the two inputs where assigned to a variable a if statement was used to check 1) That the 
first input was greater or equal to 26 as if not it surly couldnt contain every letter. And 2)
that the actual length of the set was equal to exactly 26.
'''