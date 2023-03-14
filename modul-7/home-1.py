from datetime import date, datetime

# V1
today = date.today()
event = datetime.now()

formatted_date = today.strftime("%d/%m/%Y")
formatted_time = event.strftime("%H:%M:%S")
print(formatted_date, ",", formatted_time)

# V2
time_now = datetime.now()
print(time_now.strftime('%d/%m/%Y, %H:%M:%S'))

