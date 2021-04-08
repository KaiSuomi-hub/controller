import spidev
import time
 
# A0 = 0, A1 = 1, A2 = 2, A3 =3 
temp_channel = 0
print ("\nKytke liittimeen A%1d\n" % temp_channel)
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
 
while True:
	value = readadc(temp_channel) 
	volts = (value * 3.3) / 1024
	temperature_C = (volts - 0.5) * 100
	#temperature_F = (temperature_C * 9 / 5) + 32
 
	print("Jannitetaso = %5.3f V" % volts )
	print("%4.1f Celsiusastetta C" % temperature_C)
	#print("%4.1f  degrees F" % temperature_F)
	print("-------------------------")
	time.sleep(5)