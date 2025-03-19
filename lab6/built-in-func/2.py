txt="AbsDEfg"

a=0
b=0

for i in txt:
    if i.islower():
        a=a+1
    else:
        b=b+1

print(a)
print(b)