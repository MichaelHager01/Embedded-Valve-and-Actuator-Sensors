import time
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import csv


'''
DC MOTOR
LEFT 	----> 	RIGHT
WHITE 	        BLACK
GPIO 	        GROUND
'''


# Define the SCL and SDA pins
SCL_PIN = 3
SDA_PIN = 2                             

# Initialize the I2C interface
i2c = busio.I2C(SCL_PIN, SDA_PIN)

# Create an ADS1115 object with 15-bit mode and data rate
ads = ADS.ADS1115(i2c, address=0x48)

# Configure the ADC settings for 5V reference voltage
ads.gain = 1
ads.mode = ADS.Mode.CONTINUOUS

# Define the analog input channel
channel = AnalogIn(ads, ADS.P3)

# Define time variables for csv file
time_pass = 0
time_increment = 0.004

# Create csv to write data into
with open("dcmotor_data_test.csv", 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Time(s)", "Volts"])
    
    # Loop to read the analog input continuously
    while True:
        analog_value = channel.value
        voltage_output = (analog_value * 4.096) / (2**15)
        print(f"Voltage Output: {voltage_output:.8f}")
        csvwriter.writerow([f"{time_pass:.2f}", voltage_output])
        time.sleep(time_increment)
        time_pass += time_increment

