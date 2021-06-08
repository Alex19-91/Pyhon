s_time = input ("Please, enter your time in seconds:")
s_time = int(s_time)
h =0
m = 0
s = 0
n = ('0')
if s_time //3600 >0:
    h= s_time //3600
if s_time // 60 >0:
    m = (s_time //60) - (h*60)
s = s_time % 60
if h < 10:
    h = str(h)
    h = n + h
if m < 10:
    m = str(m)
    m = n + m
if s < 10:
    s = str(s)
    s = n + s

print (f"Your time is: {h}:{m}:{s}")