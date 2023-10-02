import time

tt = time.asctime((2023, 12, 2, 3, 4, 5, 6, 7, -1))
# Daylight Saving Time
print(tt)

t_epoch = time.ctime(1693501992)
# t_epoch = time.ctime(0000000000)
print(t_epoch)

time.sleep(0.5)
a = "05/06/2023T21:35:47"
b = "04/06/2023"
time_out_a = time.strptime(a, "%d/%m/%YT%H:%M:%S")
print(time_out_a)
time_out_b = time.strptime(b, "%d/%m/%Y")
print(time_out_a > time_out_b)
print(time.strftime("%a %b %d %H:%M:%S %Y", time_out_a))

