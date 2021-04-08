"""
itbrainpower.net air quality utils library v0.3 / 20200218
        - convert temperature, humidity, pressure and length in/from various measurement units
        - 3 formulas to aquire altitude

Compatible with:
 		s-Sense HDC2010 I2C sensor breakout [PN: SS-HDC2010#I2C, SKU: ITBP-6005], info https://itbrainpower.net/sensors/HDC2010-TEMPERATURE-HUMIDITY-I2C-sensor-breakout 
		s-Sense CCS811 I2C sensor breakout [PN: SS-CCS811#I2C, SKU: ITBP-6004], info https://itbrainpower.net/sensors/CCS811-CO2-TVOC-I2C-sensor-breakout 
 		s-Sense CCS811 + HDC2010 I2C sensor breakout [PN: SS-HDC2010+CCS811#I2C, SKU: ITBP-6006], info https://itbrainpower.net/sensors/CCS811-HDC2010-CO2-TVOC-TEMPERATURE-HUMIDITY-I2C-sensor-breakout
                s-Sense BME680 I2C sensor breakout [PN: SS-BME680#I2C, SKU: ITBP-6003], info https://itbrainpower.net/sensors/BME680-BVOC-TEMPERATURE-HUMIDITY-PRESSURE-I2C-sensor-breakout
                s-Sense BME280 I2C temperature, pressure and humidity sensor breakout [PN: SS-BME280#I2C, SKU: ITBP-6002], info https://itbrainpower.net/sensors/BME280-TEMPERATURE-HUMIDITY-PRESSURE-I2C-sensor-breakout 
                s-Sense BMP280 I2C temperature and pressure sensor breakout [PN: SS-BMP280#I2C, SKU: ITBP-6001], info https://itbrainpower.net/sensors/BMP280-TEMPERATURE-PRESSURE-I2C-sensor-breakout 

		all Raspberry PI using Python 2.7


You are legaly entitled to use this SOFTWARE ONLY IN CONJUNCTION WITH s-Sense by itbrainpower.net I2C sensors DEVICES USAGE. Modifications, derivates
and redistribution of this software must include unmodified this COPYRIGHT NOTICE. You can redistribute this SOFTWARE and/or modify it under the terms 
of this COPYRIGHT NOTICE. Any other usage may be permited only after written notice of Dragos Iosub / R&D Software Solutions srl.

This SOFTWARE is distributed is provide "AS IS" in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY 
or FITNESS FOR A PARTICULAR PURPOSE.


itbrainpower.net invests significant time in design phase of our IoT products and in associated software and support resources.
Support us by purchasing our environmental and air quality sensors from here https://itbrainpower.net/order#s-Sense


Dragos Iosub, Bucharest 2020.
https://itbrainpower.net
"""


seaLevelPressure = 101325


'''
    wikipedia  altitude equation
        pressure is Pascals
        seaLevelPressure = 101325 #in Pascals

        return meters
'''
def altitude(pressure, seaLevelPressure):
    return 44330.0*(1.0-pow(pressure/seaLevelPressure,0.1903))
    
'''
    NOAA altitude equation
        pressure is Pascals
        seaLevelPressure = 101325 #in Pascals

        return meters
'''
def calculate_altitude(pressure, seaLevelPressure):
    return (1000.0 * ( seaLevelPressure - pressure ) / 3386.3752577878) * 0.3048


'''
    CASIO altitude equation
        pressure is Pascals
        seaLevelPressure = 101325 #in Pascals

        return meters
'''
def temperatureCompensatedAltitude(pressure, seaLevelPressure, temperature):
    return (pow((float(seaLevelPressure)/float(pressure)), (1/5.257))-1)*(float(temperature) + 273.15) / 0.0065 # Convert into altitude in meters


#print "wiki : %2F m" %altitude(91325.0, 101325.0) 
#print "NOAA : %2F m" %calculate_altitude(91325.0, 101325.0) 
#print "CASIO : %2F m" %temperatureCompensatedAltitude(91325.0, 101325.0, 15.0) 

'''
    distance conversion - reference: wikipedia
    
    international unit of measurement ==> m     meter
'''
def m2fe(m):                            #Feets
    return long(m) / 0.3048

def fe2m(fe):                           #inverse
    return long(fe) * 0.3048

def m2yd(m):                            #Yards
    return m2fe(m *3.0) 

def yd2m(yd):                           #inverse
    return fe2m(yd / 3.0)

'''
    temperature conversion - reference: wikipedia
    
    international unit of measurement ==> K     Kelvin degree - for convenience will use Celsius degree
'''
def C2K(Celsius):                       #Kelvin
    return Celsius + 273.15

def K2C(Kelvin):                        #inverse
    return Kelvin - 273.15

def C2R(Celsius):                       #Rankine
    return Celsius*9.0/5.0 + 491.67

def R2C(Rankine):                       #inverse
    return (Rankine - 491.67)*5.0/9.0

def C2F(Celsius):                       #Fahrenheit
    return Celsius*9.0/5.0 + 32.0

def F2C(Fahrenheit):                    #inverse
    return (Fahrenheit - 32.0)*5.0/9.0


'''
    pressure conversion - reference: CASIO, wikipedia and other
    international unit of measurement ==> Pa    Pascal - N / square m
'''

def Pa2HPa(Pascals):                    #hectoPascal - 100 Pascals = 1 HPascal
    return Pascals / 100.0

def HPa2Pa(hPascals):                   #inverse
    return hPascals * 100.0


def Pa2KPa(Pascals):                    #KiloPascal - 1000 Pascals = 1 KPascal
    return Pascals / 1000.0

def KPa2Pa(kPascals):                   #inverse
    return kPascals * 1000.0


def Pa2MPa(Pascals):                    #MegaPascal - 1000000 Pascals = 1 MPascal
    return Pascals / 1000000.0

def MPa2Pa(MPascals):                   #inverse
    return MPascals * 1000000.0


def Pa2Bar(Pascals):                    #bar
    return Pascals / 100000.0

def Bar2Pa(Bars):                       #inverse
    return Bars * 100000.0


def Pa2mBar(Pascals):                   #milibar - 1 milibar = 1bar / 1000
    return Pa2Bars(Pascals * 1000.0) 

def Bar2mPa(mBars):                     #inverse
    return mBars * 1000.0


def Pa2Torr(Pascals):                   #torr
    return 101325.0 * Pascals / 760.0

def Torr2Pa(Torrs):                     #inverse
    return 760.0 * Torrs / 101325.0


def Pa2mmHg(Pascals):                   #mmHg, same as torr
    return Pa2Torr(Pascals)

def mmHg2Pa(mmHgs):                     #inverse
    return Torr2Pa(mmHgs)


def Pa2inHg(Pascals):                   #inHg
    return Pa2Torr(25.4 * Pascals)

def inHg2Pa(inHgs):                     #inverse
    return Torr2Pa(inHg) / 25.4


def Pa2mmH2O(Pascals):                  #mm H2O @ 4C [water density 999.9720kg/m3 at 4C, standard acceleration of gravity 9.80665 m/s2] 
    return Pascals / 9.8063754138

def mmH2O2PA(mmH2Os):                   #inverse
    return mmH2Os * 9.8063754138


def Pa2Atm(Pascals):                    #standard atmosphere
    return Pascals / 101325.0

def Atm2Pa(Atms):                       #inverse
    return Atms * 101325.0


def Pa2At(Pascals):                     #technical atmosphere
    return Pascals / 98066.5

def At2Pa(Ats):                         #inverse
    return Ats * 98066.5


def Pa2Psi(Pascals):                    #pounds per square inch
    return Pascals / 6894.757293

def Psi2Pa(Psis):                       #inverse
    return Psis * 6894.757293






#pascal = 100000.0
#print ("Pascal %2F" %pascal)

#atms = Pa2Atm(pascal)
#print ("Atm %2F" %atms)
#print ("Pascal %2F" %Atm2Pa(atms))


#pascal = 10.0
#psi = Pa2Psi(pascal)
#print ("Psi %2F" %psi)
#print ("Pascal %2F" %Psi2Pa(psi))

#torr = Pa2Torr(pascal)
#print ("Torr %2F" %torr)

#print ("Pascal %2F" %Torr2Pa(torr))



#tempCelsius = -17.78

#tempRankine = C2R(tempCelsius)
#print ("Rankine %2F" %tempRankine)

#tempCelsius = R2C(tempRankine)
#print ("Celsius %2F" %tempCelsius)

#tempFehrenheit = C2F(tempCelsius)
#print ("Fehrenheit %2F" %tempFehrenheit)

#tempKelvin = C2K(tempCelsius)
#print ("Kelvin %2F" %tempKelvin)

#tempCelsius = F2C(tempFehrenheit)
#print ("Celsius %2F" %tempCelsius)

#tempKelvin = C2K(tempCelsius)
#print ("Kelvin %2F" %tempKelvin)

#tempFehrenheit = C2F(tempCelsius)
#print ("Fehrenheit %2F" %tempFehrenheit)

#tempCelsius = F2C(tempFehrenheit)
#print ("Celsius %2F" %tempCelsius)
