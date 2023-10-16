import time
def make_readable(seconds):
    times = time.gmtime(seconds)
    sec = times[5]
    min = times[4]
    hour = times[3] + (times[7] - 1) * 24
    return f'%02i:%02i:%02i' % (hour, min, sec)

print(make_readable(0), "00:00:00")
print(make_readable(5), "00:00:05")
print(make_readable(60), "00:01:00")
print(make_readable(86399), "23:59:59")
print(make_readable(359999), "99:59:59")