from datetime import datetime, timedelta, date
dt_now = datetime.now()
print(f'Сейчас: {dt_now}')
print(f'Вчера: {dt_now-timedelta(days=1)}')
print(f'Месяц назад: {dt_now-timedelta(days=30)}')
date_string="01/01/25 12:10:03.234567"
print(datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f'))