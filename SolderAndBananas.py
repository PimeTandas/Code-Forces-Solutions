#F = Cost of the first banana
#D = Dollars the solder has 
#N = Number of bananas he wants
f, d, n = map(int, input().split(' '))
cost = 0

for i in range(n+1):
    cost = cost + f*i
    
owes = cost - d
if owes < 0:
    print('0')
else:
    print(owes)
