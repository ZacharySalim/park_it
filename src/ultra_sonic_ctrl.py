# Hardware control file
# This file controls the operation of the ultra sonic sensor

import RPi.GPIO as gpio
import time
import config

gpio.setwarnings(False)

gpio.setmode(gpio.BOARD)

TRIG = config.ultra_sonic_trig
ECHO = config.ultra_sonic_echo
max_distance_cm = config.max_distance_cm
min_distance_cm = config.min_distance_cm

################################################################################
# Function Name: get_distance
#   Description: Sends a pulse for .0001 seconds and calculate the distance based on the pulse.
################################################################################
def get_distance():
        pulse_start = 0
        pulse_end = 0
        gpio.setmode(gpio.BOARD)

        print("Distance Measurement In Progress")

        gpio.setup(TRIG, gpio.OUT)
        gpio.setup(ECHO, gpio.IN)

        gpio.output(TRIG, False)

        print("Waiting For Sensor To Settle")

        time.sleep(2)

        gpio.output(TRIG, True)
        time.sleep(0.00001)
        gpio.output(TRIG, False)

        while gpio.input(ECHO) == 0:
                pulse_start = time.time()

        while gpio.input(ECHO) == 1:
                pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150

        distance = round(distance, 2)
        print("Distance: ", distance, "cm")

        return distance

################################################################################
# Function Name: object_in_range
#   Description: Detect if the distance detected is within the specified distance
################################################################################
def object_in_range(min_distance, max_distance):
        car_in_range = False
        distance = get_distance()
        if distance > min_distance and distance < max_distance:
	        car_in_range = True
        else:
                car_in_range = False

        if car_in_range == True:
                print("Car is detected")
        else:
	        print("Car not present")
        return(car_in_range)

#def main():
#	object_in_range(min_distance_cm, max_distance_cm)

#main()
