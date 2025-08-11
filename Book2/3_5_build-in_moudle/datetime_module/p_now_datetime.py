from datetime import datetime
now = datetime.now()
print(now)

old = datetime(2019, 1, 1,12, 0, 0)
print(old)

year = old.year
print( year)

# 将日期转化为时间戳
timestamp = datetime.timestamp(old)
print(timestamp)

# 如果用户输入的日期字符串,怎么变成datetime对象?
date = '2002-08-25'
date = datetime.strptime(date, '%Y-%m-%d')
print(type(date))

# 把日期格式化为字符串显示给用户
date = datetime.now()
# 参数标识你要显示的时间格式
date = date.strftime('%Y-%m-%d %H:%M:%S')
print( date)

# 计算时间的差值 timeDelta
from datetime import timedelta
now = datetime.now()
date = now - timedelta(days=3)
print(date)

list_date = ['2002-08-25','2002-08-26']
date1 = datetime.strptime(list_date[0], '%Y-%m-%d')
date2 = datetime.strptime(list_date[1], '%Y-%m-%d')
new_date = date2 - date1
print(new_date)