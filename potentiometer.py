import time
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn


'''
LEFT 	----> 	RIGHT
RED 	ORANGE 	BLACK
GROUND 	GPIO 	5V
'''


# Define the SCL and SDA pins
SCL_PIN = 3
SDA_PIN = 2

# Define the range of degrees of rotation
MIN_DEGREES = 0
MAX_DEGREES = 230

# Define the maximum ADC value
MAX_ADC_VALUE = 2**15

# Initialize the I2C interface
i2c = busio.I2C(SCL_PIN, SDA_PIN)

# Create an ADS1115 object with 15-bit mode and data rate
ads = ADS.ADS1115(i2c, address=0x48)

# Define the analog input channel
channel = AnalogIn(ads, ADS.P2)

# Function to map ADC values to degrees of rotation
def map_to_degrees(value):
    return (value / MAX_ADC_VALUE) * (MAX_DEGREES - MIN_DEGREES)

# Loop to read the analog input continuously
while True:
    analog_value = channel.value
    degrees = map_to_degrees(analog_value)
    print("Analog Value:", analog_value, "Degrees of Rotation:", degrees)
    time.sleep(0.1)

