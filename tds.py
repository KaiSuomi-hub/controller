import spidev
import time
 
# A0 = 0, A1 = 1, A2 = 2, A3 =3 
channel = 1
print ("\nKytke liittimeen A%1d\n" % channel)
#time.sleep(1)
 
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000

def readadc(adcnum):
# read SPI data from MCP3004 chip, 4 possible adc's (0 thru 3)
    if adcnum > 3 or adcnum < 0:
        return -1
    r = spi.xfer2([1,8+adcnum <<4,0])
    adcout = ((r[1] &3) <<8)+r[2]
    return adcout
 
value = readadc(channel) 
volts = value*5/1024
# volts = (value)
tds = ((133.42/volts*volts*volts-255.86*volts*volts+857.39*volts)*0.5) - 40
#temperature_F = (temperature_C * 9 / 5) + 32

print("Jannitetaso = %5.3f V" % volts )
print("%4.1f ppm" % tds)
#print("%4.1f  degrees F" % temperature_F)
print("-------------------------")
