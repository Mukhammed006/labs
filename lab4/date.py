#1
import datetime

a=datetime.datetime.now()
b=a-datetime.timedelta(days=5)
print(b)

#2
import datetime

tdy=datetime.datetime.now()
ytdy=tdy-datetime.timedelta(days=1)
tmrw=tdy+datetime.timedelta(days=1)

print(ytdy)
print(tdy)
print(tmrw)

#3
import datetime

a=datetime.datetime.now()
b=a.replace(microsecond=0)

print(a)
print(b)

#4
import datetime

date_format="%Y-%m-%d %H:%M:%S"

date1_str=input("First date (YYYY-MM-DD HH:MM:SS): ")
date2_str=input("Second date (YYYY-MM-DD HH:MM:SS): ")

date1=datetime.datetime.strptime(date1_str, date_format)
date2=datetime.datetime.strptime(date1_str, date_format)

difference = abs(date2-date1)

print("Difference in seconds:", int(difference.total_seconds()))

