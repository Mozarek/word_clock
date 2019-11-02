import sys
import time
import pytz
from datetime import datetime
from display import *

timeZone = pytz.timezone('Europe/Warsaw')
currTime = datetime.now(tz = timeZone)
isOn = True

my_disp = Display(isDebug = False)
my_disp.updateDisplay(currTime.hour , currTime.minute)

while isOn:
    if currTime.minute != datetime.now().minute:
        currTime = datetime.now(tz = timeZone)
        h = currTime.hour
        m = currTime.minute
        my_disp.updateDisplay(h,m)
    time.sleep(0.1)

        
    
