import datetime
date = datetime.datetime.now()
time = date.time()
def date_generator(date, delta):
  counter =0
  date = date - datetime.timedelta(days=delta)
  while counter <= delta:
    yield date
    date = date + datetime.timedelta(days=1)
    counter +=1

for date in date_generator(date, 30):
   if date.date() != datetime.datetime.now().date():
     start_date = date
     end_date = datetime.datetime.combine(date, datetime.time.max)
   else:
     start_date = date
     end_date = datetime.datetime.combine(date, time)
   print(start_date)