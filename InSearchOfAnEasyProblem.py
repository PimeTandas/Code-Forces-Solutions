x = input()
o = map(int, input().split(' '))

if sum(o) >= 1:
    print('HARD')
else:
    print('EASY')