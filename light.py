import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pinList = [2,3,4,17]

for i in pinList:
	GPIO.setup(i,GPIO.OUT)
	GPIO.output(i,GPIO.HIGH)

int_list = ['1','2','3','4','5','6','7','8','9','0']

class Light:
	def __init__(self):
		self.status = False
		self.alarms = []
	def __str__(self):
		return('Light status: ' + str(self.status) + '\n' + 'Current alarms: ' + str(self.alarms) + '\n')
	def add_alarm(self, alarm_time, ampm,alarm_day,recurring):
		self.alarms.append(alarm_time)
		#this_year = time.localtime().tm_year
		#this_month = time.localtime().tm_mon
		#if alarm_day == 'today':
		#	this_day = time.localtime().tm_mday
		#elif alarm_day == 'tomorrow':
		#	this_day = time.localtime().tm_mday+1
		#this_hour = int(alarm_time[0:alarm_time.index(':')])
		#this_minute = int(alarm_time[alarm_time.index(':')+1:])
		#this_second = 0
		#need to set recurring
		
	def clear_alarms(self):
		self.alarms = []
	def light_on(self):
		try:
			GPIO.output(2,GPIO.LOW)
			self.status = True
		except keyboardInterrupt:
			print('KeyboardInterrupt')
			GPIO.cleanup()
	def light_off(self):
		try:
			GPIO.output(2,GPIO.HIGH)
			self.status = False
		except KeyboardInterrupt:
			print('KeyboardInterrupt')
			GPIO.cleanup()

def light():
	raspi = Light()
	print(str(raspi))
	while True:
		try:
			user_input = str(input('On or off?\n')).lower()
			if 'on' in user_input:
				raspi.light_on()
			elif 'off' in user_input:
				raspi.light_off()
			elif ('set' in user_input) and ('alarm' in user_input):
				colon_at = user_input.index(':')
				if user_input[colon_at-2] in int_list:
					alarm_time = user_input[colon_at-2:colon_at+3]
				else:
					alarm_time = user_input[colon_at-1:colon_at+3]
				ampm = 'am'
				if ('pm' in user_input) or ('p.m' in user_input):
					ampm = 'pm'
				if 'today' in user_input:
					alarm_day = 'today'
				if ('recurring' in user_input) or ('repeat' in user_input):
					recurring = True
				else:
					recurring = False
				else:
					alarm_day = 'tomorrow'
				raspi.add_alarm(alarm_time,ampm,alarm_day,recurring)
			elif 'stop' in user_input:
				print('Stopping')
				return
			else:
				print('Unrecognized command')
		except KeyboardInterrupt:
			print('KeyboardInterrupt')
			GPIO.cleanup()

light()
