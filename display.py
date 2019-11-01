from parseLayout import *
import RPi.GPIO as GPIO

import Adafruit_WS2801 as AF
import Adafruit_GPIO.SPI as SPI

class Display:
    def __init__(self , isDebug):
        self.compressedLayouts , self.rows , self.cols , self.lastCols = parseLayoutsCompressed("compressed_layouts.txt")
        self.layoutLetters = parseLayoutLetters("layout_letters.txt")
        if isDebug:
            self.displayFun = self.displayCmd
        else:
            self.pixelCount = 126
            self.pixels = AF.WS2801Pixels(self.pixelCount, spi=SPI.SpiDev(0,0) , gpio = GPIO)
            self.brightness = 0.5
            self.color = [255.0,255.0,255.0]
            self.displayFun = self.displayLED


    def displayCmd(self , layoutId):
        layoutCompressed = self.compressedLayouts[layoutId]
        layout = decompressLayout(layoutCompressed)
        for r in range(12):
            for c in range(11):
                if layout[r][c] == 1:
                    print(self.layoutLetters[r][c] , end='')
                else:
                    print(" " , end='')
            print("")

    def getPixelIndex(self , row, col):
        if row<11:
            if row%2 == 0:
                return self.pixelCount-1 -(row*11+ 11-1-col)
            else:
                return self.pixelCount-1 -(row*11+ col)
        else:
            if col< 2:
                return self.pixelCount-1 -(row*11 + col)
            else:
                return self.pixelCount-1 -(row*11 + col+1)

    def displayLED(self , layoutId):
        layoutCompressed = self.compressedLayouts[layoutId]
        layout = decompressLayout(layoutCompressed)

        self.pixels.clear()
        for r in range(12):
            for c in range(11):
                if layout[r][c] == 1:
                    self.pixels.set_pixel(self.getPixelIndex(r,c), AF.RGB_to_color(*[100,100,100]))
        self.pixels.show()



    def updateDisplay(self , hours , minutes):
        hours = hours%12
        self.displayFun(hours*60+minutes)


        
