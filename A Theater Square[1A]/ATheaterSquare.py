import math
n, m, a = map(int, input().split(' '))

vertical = math.ceil(n / a)
horizontal = math.ceil(m / a)

total = vertical * horizontal

print(total)