# https://codeforces.com/problemset/problem/200/B

x = int(input()) # Number of drinks
y = list(map(int, input().split(' '))) 
c = 1
ov = 0

for i in range(x):
    ov += (y[i] / 100) * c
print(ov/(c*x)*100)