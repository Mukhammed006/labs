#1
import datetime

a=datetime.datetime.now()
b=a-datetime.timedelta(days=5)
print(b)

#2
import datetime

a=datetime.datetime.now()
b=a-datetime.timedelta(days=1)
c=a+datetime.timedelta(days=1)

print(b)
print(a)
print(c)
