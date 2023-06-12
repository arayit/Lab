from zaber_motion import Units
from zaber_motion.ascii import Connection
import time
##geri sayım ekleme tarama sürerken, user inputla kontrol etme

with Connection.open_serial_port("COM5") as connection:
    connection.enable_alerts()

    device_list = connection.detect_devices()
    print("Found {} devices".format(len(device_list)))

    #device listing
    device1 = device_list[0]
    device2 = device_list[1]
    device3 = device_list[2]
    device4 = device_list[3]

    x_axis = device1.get_axis(1) #x axis
    y_axis = device2.get_axis(1) #y axis
    z_axis = device3.get_axis(1) #z axis
    rot_axis = device4.get_axis(1) #rotational axis

    #print("Starting position of x axis: ", x_axis.get_position(), "Starting position of y axis: ", y_axis.get_position())

    scanning_velocity = 50
    starting_position_x = 20.059
    waiting_time = 30 #in seconds
    starting_position_y = 11.894
    range = 2.5
    #scanning



    #move to origin
    x_axis.move_absolute(starting_position_x, Units.LENGTH_MILLIMETRES, wait_until_idle=True, velocity=scanning_velocity,
                        velocity_unit=Units.VELOCITY_MILLIMETRES_PER_SECOND)
    y_axis.move_absolute(starting_position_y, Units.LENGTH_MILLIMETRES, wait_until_idle=True,
                         velocity=scanning_velocity,
                         velocity_unit=Units.VELOCITY_MILLIMETRES_PER_SECOND)

    print("Waiting for ", waiting_time, " seconds.")
    time.sleep(waiting_time)
    print("Wait is over.")

    rot_axis.move_absolute(0, Units.ANGLE_DEGREES, wait_until_idle=False, velocity=1800,
                           velocity_unit=Units.ANGULAR_VELOCITY_DEGREES_PER_SECOND)


    #first step
    x_axis.move_relative(range, Units.LENGTH_MILLIMETRES, wait_until_idle=True, velocity=scanning_velocity,
                         velocity_unit=Units.VELOCITY_MICROMETRES_PER_SECOND)
    rot_axis.stop()
    print("Waiting for ", waiting_time, " seconds.")
    time.sleep(waiting_time)
    print("Wait is over.")
    rot_axis.move_absolute(0, Units.ANGLE_DEGREES, wait_until_idle=False, velocity=1800,
                           velocity_unit=Units.ANGULAR_VELOCITY_DEGREES_PER_SECOND)
    # second step
    x_axis.move_relative(range, Units.LENGTH_MILLIMETRES, wait_until_idle=True, velocity=scanning_velocity,
                         velocity_unit=Units.VELOCITY_MICROMETRES_PER_SECOND)
    rot_axis.stop()

    print("Waiting for ",waiting_time," seconds.")
    time.sleep(waiting_time)
    print("Wait is over.")

    # third step
    x_axis.move_relative(range, Units.LENGTH_MILLIMETRES, wait_until_idle=True, velocity=scanning_velocity,
                         velocity_unit=Units.VELOCITY_MICROMETRES_PER_SECOND)

    rot_axis.stop()

