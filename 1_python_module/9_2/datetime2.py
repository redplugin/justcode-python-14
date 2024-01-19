from datetime import datetime

# str_dtime = "2023/01/01 00:00:00"
str_dtime = "01.01 00:00"
print(type(str_dtime))
print(str_dtime)

# str_to_datetime = datetime.strptime(str_dtime, "%Y/%m/%d %H:%M:%S")
str_to_datetime = datetime.strptime(str_dtime, "%d.%m %H:%M")

print(type(str_to_datetime))
print(str_to_datetime)





