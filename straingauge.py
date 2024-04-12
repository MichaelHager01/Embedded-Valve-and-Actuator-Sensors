import time
import busio
from cedargrove_nau7802 import NAU7802


# Define the SCL and SDA pins
SCL_PIN = 3
SDA_PIN = 2                             

# Initialize the I2C interface
i2c = busio.I2C(SCL_PIN, SDA_PIN)

# Instantiate 24-bit load sensor ADC
nau7802 = NAU7802(i2c, address=0x2a)

# Configure NAU7802 for strain gauge measurement
nau7802.gain = 128  # Adjust gain setting as needed
nau7802.calibrate()  # Perform calibration

# Read strain gauge measurement
while True:
    raw_data = nau7802.read()
    # Do something with raw_data, such as convert it to strain values
    print("Raw data:", raw_data)
    time.sleep(0.1)  # Wait for 0.1 second before the next reading
