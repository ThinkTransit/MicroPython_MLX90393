Introduction
============

MicroPython driver for the MLX90393 3-axis magnetometer.

Forked from https://github.com/adafruit/Adafruit_CircuitPython_MLX90393

Dependencies
=============
This driver depends on:

* `MicropythonPython <https://github.com/micropython/micropython>`_


Usage Example
=============

.. code-block:: python3

    import time
    from machine import SoftI2C, Pin
    import micropython_mlx90393 import MLX90393

    i2c = SoftI2C.I2C()  # uses board.SCL and board.SDA
    SENSOR = MLX90393(i2c, gain=micropython_mlx90393.GAIN_1X)

    while True:
        MX, MY, MZ = SENSOR.magnetic
        print("[{}]".format(time.time()))
        print("X: {} uT".format(MX))
        print("Y: {} uT".format(MY))
        print("Z: {} uT".format(MZ))
        # Display the status field if an error occured, etc.
        if SENSOR.last_status > micropython_mlx90393.STATUS_OK:
            SENSOR.display_status()
        time.sleep(1.0)

Documentation
=============

API documentation for this library can be found on `Read the Docs <https://circuitpython.readthedocs.io/projects/mlx90393/en/latest/>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/ThinkTransit/MicroPython_MLX90393/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
