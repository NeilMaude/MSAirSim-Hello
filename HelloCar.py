from AirSimClient import *

# connect to the AirSim simulator
client = CarClient()
client.confirmConnection()
client.enableApiControl(True)
car_controls = CarControls()

while True:
    # get state of the car
    car_state = client.getCarState()
    print("Speed %d, Gear %d" % (car_state.speed, car_state.gear))

    # set the controls for car
    car_controls.throttle = 1
    car_controls.steering = 0   #1
    client.setCarControls(car_controls)

    # let car drive a bit
    time.sleep(1)

    # get camera images from the car
    # responses = client.simGetImages([
    #     ImageRequest(0, AirSimImageType.DepthVis),
    #     ImageRequest(1, AirSimImageType.DepthPlanner, True)])
    # responses = client.simGetImages([
    #     ImageRequest(0, AirSimImageType.Scene)    ])
    responses = client.simGetImages([
        ImageRequest(0, AirSimImageType.Scene),
        ImageRequest(1, AirSimImageType.Scene),
        ImageRequest(2, AirSimImageType.Scene)
        ])
    print('Retrieved images: %d', len(responses))

    image_num = 0
    for response in responses:
        if response.pixels_as_float:
            print("Type %d, size %d" % (response.image_type, len(response.image_data_float)))
            CarClient.write_pfm(os.path.normpath('D:/SDCND/MSAirSim/TempImages/py1.pfm'), CarClient.getPfmArray(response))
        else:
            print("Type %d, size %d" % (response.image_type, len(response.image_data_uint8)))
            CarClient.write_file(os.path.normpath('D:/SDCND/MSAirSim/TempImages/py' + str(image_num) + '.png'), response.image_data_uint8)
            image_num += 1