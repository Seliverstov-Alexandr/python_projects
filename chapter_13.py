# Запишите текущие дату и время как строку в текстовый файл today.txt. 
print('exercise_1\n')

from datetime import datetime, date, time, timedelta
import time
print(datetime.now())
with open('today.txt','w') as today:
    today.write(datetime.strftime(datetime.today(),'%Y-%m-%d-%I-%M-%S%p'))


# Прочтите текстовый файл today.txt и разместите данные в строке today_string.
print('\nexersice_2\n')
with open('today.txt','r') as file:
    today_string = file.read()
    print(file.read())
    
print((today_string +'     ') *3)


# Проанализируйте дату из строки today_string. 
print('\nexersice_3\n')

day = datetime.now() 
print(day.isoformat(), day.year, day.minute)
now_time = time.time()
print(day.date())
print(time.ctime(now_time))
print(time.localtime(now_time))
print(time.gmtime(now_time)[:8])
print(time.mktime(time.localtime(now_time)))
print('year is ' + str(datetime.strptime(today_string,'%Y-%m-%d-%H-%M-%S%p').year))
# Создайте объект date с датой вашего рождения.
print('\nexersice_4\n') 
date = date(1993,7,16)
print(date)
date_2 = time.localtime(time.time())
# В какой день недели вы родились? 
print('\nexersice_5\n')
print(datetime.weekday(date))
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(week_days[datetime.weekday(date)])
print(date_2.tm_wday)


# Когда вам будет (или уже было) 10 000 дней от роду?
print('\nexersice_6\n')

print(date + timedelta(days=10000))