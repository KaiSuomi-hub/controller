from time import sleep
from ccs811 import *


ccs811Begin(CCS811_driveMode_1sec)                                      #start CCS811, data update rate at 1sec

while(1):
        ccs811SetEnvironmentalData(21.102, 57.73)                       #replace with temperature and humidity values from HDC2010 sensor

        if ccs811CheckDataAndUpdate():
                CO2 = ccs811GetCO2()
                tVOC = ccs811GetTVOC()
                print "CO2 : %d ppm" %CO2
                print "tVOC : %d ppb" %tVOC
        elif ccs811CheckForError():
                ccs811PrintError()

        sleep(2)