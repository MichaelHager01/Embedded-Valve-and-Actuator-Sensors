# Embedded valve and actuator sensors

Senior capstone for Bray International: measure valve rotation and actuator torque on a pneumatic valve, independent of the other operating parameters.

## What it does

- The sensing rig uses a Raspberry Pi 4, an ADS1115 16-bit ADC, a potentiometer, a Hall-effect angle sensor, a strain gauge on an NAU7802, and a DC motor.
- On the validation set, valve rotation was measured within ±1.4% error against a target of under 2%, from 40 to 80 psi.
- The Python scripts in `src/` are the acquisition programs. They talk to the hardware and write a CSV in the current working directory. They do not read the archived CSVs.
- Logged trials, course reports, presentations, photos, and purchase records are kept under `data/`, `docs/`, and `assets/`.

## Layout

- `src/potentiometer.py` — logs potentiometer angle versus time
- `src/halleffect.py` — reads the angle sensor over I2C
- `src/dcmotor.py` — logs DC motor voltage versus time
- `src/straingauge.py` — prints raw NAU7802 strain readings
- `data/` — potentiometer, motor, and Hall-effect trials, including the earlier `data/` CSVs
- `docs/fall-2023/` — fall design reviews, meeting notes, and weekly presentations
- `docs/spring-2024/` — spring reports, photos, validation workbooks, and purchase records
- `assets/` — figures that used to sit at the repository root

## Run

Run the acquisition scripts on the Raspberry Pi that has the ADC and sensors wired:

```bash
python src/potentiometer.py
```

`src/halleffect.py` needs the sensor's I2C address, and `src/straingauge.py` needs the NAU7802 library used on the Pi. Archived plots and CSVs can be read without the hardware.

## Stack

Python on a Raspberry Pi 4, with an ADS1115 and an NAU7802. Team of six, September 2023 through April 2024.
