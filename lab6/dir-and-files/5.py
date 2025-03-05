number = int(input())
milsec = int(input())
sec = milsec / 1000

start = int(str((10**10) * sec).split('.')[0])
while start > 0:
    start -= 1

sqrt = number ** 0.5
txt = 'Square root of {fnum} after {fsec} is {fsqrt}'.format(fnum=number, fsec=milsec, fsqrt=sqrt)
print(txt)