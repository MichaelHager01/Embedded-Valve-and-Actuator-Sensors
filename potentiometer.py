import time
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import csv


'''
POTENTIOMETER
LEFT 	----> 	RIGHT
RED 	ORANGE 	BLACK
GROUND 	GPIO 	5V
'''


# Define the SCL and SDA pins
SCL_PIN = 3
SDA_PIN = 2

# Define the range of degrees of rotation
MIN_DEGREES = 0
MAX_DEGREES = 270

# Define the maximum ADC value
MAX_ADC_VALUE = 2**15

# Initialize the I2C interface
i2c = busio.I2C(SCL_PIN, SDA_PIN)

# Create an ADS1115 object with 15-bit mode and data rate
ads = ADS.ADS1115(i2c, address=0x48)

# Define the analog input channel
channel = AnalogIn(ads, ADS.P3)

# Function to map ADC values to degrees of rotation
def map_to_degrees(value):
    return (value / MAX_ADC_VALUE) * (MAX_DEGREES - MIN_DEGREES)

# Define time variables for csv file
time_pass = 0
time_increment = 0.1

# Create csv to write data into
with open("potentiometer_data_40.csv", 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Time(s)", "Degrees of Rotation"])
    
    # Loop to read the analog input continuously
    while True:
        analog_value = channel.value
        degrees = map_to_degrees(analog_value)
        print("Degrees of Rotation:", degrees)
        csvwriter.writerow([f"{time_pass:.1f}", degrees])
        time.sleep(time_increment)
        time_pass += time_increment

