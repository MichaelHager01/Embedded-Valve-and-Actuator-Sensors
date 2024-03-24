import time
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn


'''
DC MOTOR
LEFT 	----> 	RIGHT
WHITE 	        BLACK
5V 	            GROUND
'''


# Define the SCL and SDA pins
SCL_PIN = 3
SDA_PIN = 2

# Initialize the I2C interface
i2c = busio.I2C(SCL_PIN, SDA_PIN)

# Create an ADS1115 object with 15-bit mode and data rate
ads = ADS.ADS1115(i2c, address=0x48)

# Define the analog input channel
channel = AnalogIn(ads, ADS.P3)

# Loop to read the analog input continuously
while True:
    analog_value = channel.value
    print("Analog Value:", analog_value)
    time.sleep(0.1)

