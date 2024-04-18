'''
Attempt at making a python script that will read the MIKROE Hall Effect Sensor
Avery - 4/7/2024

 * CONNECTION NOTES:
 * ON HALL EFFECT SENSOR:
 * ORANGE WIRE ----> SCL PORT
 * WHITE WIRE ----> SDA PORT
 * BLACK WIRE ---> GND PORT
 * GREEN WIRE ---> 5V PORT

'''

import smbus
import time

# Define the I2C address of the Angle Click Hall Effect Sensor
SENSOR_ADDRESS = 0x0c

# Register addresses for angle data
ANGLE_MSB_REG = 0x20
ANGLE_LSB_REG = 0x14

# Function to read the angle data from the sensor
def read_angle(sensor):
    # Read 2 bytes of data from the specified registers
    msb = sensor.read_byte_data(SENSOR_ADDRESS, ANGLE_MSB_REG)
    lsb = sensor.read_byte_data(SENSOR_ADDRESS, ANGLE_LSB_REG)
    print(msb, lsb)
    
    # Combine the MSB and LSB to get the angle value
    angle_raw = (msb << 8) | lsb
    
    # Convert the raw angle value to degrees (0-360)
    angle_degrees = (angle_raw / 4096) * 360
    
    return angle_degrees

def main():
    # Initialize I2C bus
    bus = smbus.SMBus(1)  # For Raspberry Pi 4, use bus 1
    
    try:
        while True:
            # Read angle data
            angle = read_angle(bus)
            print("Degrees of Rotation:", angle)
            
            # Wait for some time before reading again
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        # Clean up
        bus.close()

if __name__ == "__main__":
    main()
