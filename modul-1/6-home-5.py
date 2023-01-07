# time_start = 23400
time_start = int(input("Time in seconds: "))
time_min = time_start/60
time_h = int(time_min // 60)
time_sec = int(time_min % 60)

# print(time_min)
# print(time_h)
# print(time_sec)

print(f"{time_h}:{time_sec}")