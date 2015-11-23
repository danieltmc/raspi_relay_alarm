#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)

# pinList = [relay1,relay2,relay3,relay4]
pinList = [2, 3, 4, 17]

for i in pinList: 
    # setup each relay
    GPIO.setup(i, GPIO.OUT)
    # set each relay to off 
    GPIO.output(i, GPIO.HIGH)

def light():
  # False == light off, True == light on
  current_status = False
	while True:
		# take the user input as a string and convert to lowercase for easier use
		user_input = str(input('On or off?\n')).lower()
		# if the word 'on' appears in the input, turn the light on
		if 'on' in user_input:
		  try:
	      GPIO.output(2, GPIO.LOW)
	      current_status = True
      except KeyboardInterrupt:
	      print('KeyboardInterrupt')
	      GPIO.cleanup()
		# if the word 'off' appears in the input, turn the light off
		elif 'off' in user_input:
		  try:
	      GPIO.output(2, GPIO.HIGH)
	      current_status = False
      except KeyboardInterrupt:
	      print('KeyboardInterrupt')
	      GPIO.cleanup()
		# if the word 'stop' appears in the input, end the program
		elif 'stop' in user_input:
			print('Stopping')
			# return statement ends the function
			return
		else:
			# if an unrecognized word appears in the input, let the user know
			print('Unrecognized command')
# start the program
light()
# cleanup the GPIO pins after the program ends
GPIO.cleanup()

# try/except block for handling keyboard interrupt
# try:
# 	GPIO.output(*pin_number*, GPIO.LOW)
# except KeyboardInterrupt:
# 	print('KeyboardInterrupt')
# 	GPIO.cleanup()
