import calendar
year=1901
month=1
day=1
c=0
while year<2001:
    while month<13:
        if calendar.weekday(year,month,day)==6:
            print(year,month,day)
            c+=1
        month+=1
    month=1
    year+=1
print(c)




