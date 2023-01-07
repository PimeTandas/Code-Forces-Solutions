# https://codeforces.com/problemset/problem/116/A

x = int(input())
p = 0
count = []

for i in range(x):
    d, e = map(int, input().split(' '))
    p -= d
    p += e
    count.append(p)
print(max(count))

'''
Challenge solution begins by taking input in the form of an int variable representing the number of
tram stops. This is used to iterate through the rest of the code using a for loop. We basicly 
subtract any leaving and add any passangers boarding the train, appending the count to a list
after each itteration, finally we get the max load along the journy using the max function applied
to our list, printing the outcome.  
'''