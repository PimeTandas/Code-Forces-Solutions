w = input()
cap = 0
low = 0
for i in w:
    if i.islower():
        low += 1
    else:
        cap += 1

if low < cap:
    w = w.upper()
elif low > cap:
    w = w.lower()
else:
    w = w.lower()
print(w)
