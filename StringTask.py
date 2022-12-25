x = input().lower()
vowels = set(['a','e','i','o','u', 'y'])
output = ''
for letter in x:
    if letter not in vowels:
        output = output + "." + letter
print(output, sep='', end='')