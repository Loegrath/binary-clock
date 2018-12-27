"""Binary Clock"""
from bin_clock_display import clock_display, datetime

clock = clock_display()

time = datetime.now()
clock.cols_update(time)
print(clock)
while True:
    if time.minute is not datetime.now().minute:
        time = datetime.now()
        clock.cols_update(time)
        print(clock)
