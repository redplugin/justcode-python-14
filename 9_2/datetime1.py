from datetime import datetime

# a = datetime.utcnow()
a = datetime.now()
print(type(a))
print(a)

# a = datetime.strftime(a, '%Y/%m/%d %H:%M:%S')

# a = a.strftime('%Y год, %m месяц %d день! \n%H часов %M минут %S секунд!')
# a = a.strftime('%d %h %H:%M')
a = a.strftime('%Y/%m/%d %H:%M:%S')

print(type(a))
print(a)





