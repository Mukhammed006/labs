#1
def squares(n):
    for i in range(1,n+1):
        yield i*i

n=int(input())
for num in squares(n):
    print(num)

#2
def even(n):
    for i in range(1,n+1):
        if i%2==0:
            yield i

n=int(input())
result=even(n)

print(",".join(map(str,result)))

#3
def divisible(n):
    for i in range(0,n):
        if i%3==0 and i%4==0:
            yield i

n=int(input())

for num in divisible(n):
    print(num)

#4
def squares1(a,b):
    for i in range(a,b):
        yield i*i

a=int(input())
b=int(input())

for num in squares1(a,b):
    print(num)

#5
def down(n):
    for i in range(0,n+1):
        yield n-i

n=int(input())

for num in down(n):
    print(num)