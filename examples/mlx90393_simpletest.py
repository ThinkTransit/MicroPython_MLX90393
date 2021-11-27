# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
from machine import SoftI2C, Pin
import micropython_mlx90393

i2c = SoftI2C()
SENSOR = micropython_mlx90393.MLX90393(i2c, gain=micropython_mlx90393.GAIN_1X)

while True:
    MX, MY, MZ = SENSOR.magnetic
    print("[{}]".format(time.localtime()))
    print("X: {} uT".format(MX))
    print("Y: {} uT".format(MY))
    print("Z: {} uT".format(MZ))
    # Display the status field if an error occured, etc.
    if SENSOR.last_status > micropython_mlx90393.STATUS_OK:
        SENSOR.display_status()
    time.sleep(1.0)
