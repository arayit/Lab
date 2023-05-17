from zaber_motion import Units
from zaber_motion.ascii import Connection

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

    print("Starting position of x axis: ", x_axis.get_position(), "Starting position of y axis: ", y_axis.get_position())

    scanning_velocity = 0.2
    starting_position_x = 3
    starting_position_y = 3

    range = 10 #in millimeters
    step_size = 2 #in millimeters
    line_number = range/step_size
    #raster scan x-y axis

    x_axis.move_absolute(starting_position_x, Units.LENGTH_CENTIMETRES, wait_until_idle=True, velocity=scanning_velocity,
                        velocity_unit=Units.VELOCITY_CENTIMETRES_PER_SECOND)
    y_axis.move_absolute(starting_position_y, Units.LENGTH_CENTIMETRES, wait_until_idle=True, velocity=scanning_velocity,
                        velocity_unit=Units.VELOCITY_CENTIMETRES_PER_SECOND)

    print("Starting position of raster scan for x axis: ", x_axis.get_position(),
          "Starting position of raster scan for y axis: ", y_axis.get_position())
    current_step = 0
    while current_step < line_number:

        if current_step % 2 == 0:
            x_axis.move_relative(range, Units.LENGTH_MILLIMETRES, wait_until_idle=True, velocity= scanning_velocity,
                                velocity_unit=Units.VELOCITY_CENTIMETRES_PER_SECOND)
            y_axis.move_relative(step_size, Units.LENGTH_MILLIMETRES, wait_until_idle=True,
                            velocity=scanning_velocity,
                            velocity_unit=Units.VELOCITY_CENTIMETRES_PER_SECOND)

        else:
            x_axis.move_relative((-1*range), Units.LENGTH_MILLIMETRES, wait_until_idle=True, velocity=scanning_velocity,
                                velocity_unit=Units.VELOCITY_CENTIMETRES_PER_SECOND)
            y_axis.move_relative(step_size, Units.LENGTH_MILLIMETRES, wait_until_idle=True,
                                velocity=scanning_velocity,
                                velocity_unit=Units.VELOCITY_CENTIMETRES_PER_SECOND)
        current_step += 1
        print(current_step)


