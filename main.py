################################################
#
# Pomodoro timer for TiLDA mk Pi
#
# Default time is 5 minutes
# Press button B to add additional time
# Press button A to exit
# 
#
################################################

import ugfx
import buttons
import pyb
import dialogs
 
# BUTTONS 
buttons.init()

# SCREEN
ugfx.init()
ugfx.clear(ugfx.BLACK)
ugfx.set_default_font(ugfx.FONT_NAME)
ugfx.orientation(0)

# CLOCK
rtc = pyb.RTC()
rtc.init()

# WINDOWS
window = ugfx.Container(0,25,320,240-25-60, style=dialogs.default_style_badge)

# SETUP THE TIME
syear, smonth, sday, sweekday, shours, sminutes, sseconds, sss = rtc.datetime()
session_mins = 5

# DISPLAY TIME REMAINING AND ACCEPT INSTRUCTIONS
while True:

    if buttons.is_pressed("BTN_B"):
        session_mins += 5

    year, month, day, weekday, hours, minutes, seconds, ss = rtc.datetime()

    been_mins = (minutes - sminutes)%60
    been_secs = (seconds - sseconds)%60

    left_mins = session_mins - been_mins - 1
    left_secs = 60 - been_secs - 1

    msg = "%s : %s" % (left_mins, left_secs)

    l=ugfx.Label(5,20,310,window.height()-20,msg,parent=window)
    window.show()

    if buttons.is_pressed("BTN_A"):
        break

    if been_mins >= session_mins:
        break

    pyb.delay(1000)
    l.destroy()


# PLAY SOUND WHEN FINISHED
t4 = pyb.Timer(4, freq=100, mode=pyb.Timer.CENTER)
for x in range(10,30):
    t4.freq(x*100)
    ch1 = t4.channel(1, pyb.Timer.PWM, pin=pyb.Pin("BUZZ"), pulse_width=(t4.period() + 1) // 2)
    pyb.delay(100)

pyb.Pin("BUZZ",pyb.Pin.OUT).low()


