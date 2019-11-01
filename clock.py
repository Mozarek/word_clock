import sys
import time
from datetime import datetime
from display import *

currTime = datetime.now()
isOn = True

my_disp = Display(isDebug = False)
my_disp.updateDisplay(currTime.hour , currTime.minute)

while isOn:
    if currTime.minute != datetime.now().minute:
        currTime = datetime.now()
        h = currTime.hour
        m = currTime.minute
        my_disp.updateDisplay(h,m)
    time.sleep(0.1)

        
    
