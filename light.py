import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pinList = [2,3,4,17]

for i in pinList:
	GPIO.setup(i,GPIO.OUT)
	GPIO.output(i,GPIO.HIGH)

int_str = '1234567890'

class Light:
	def __init__(self):
		self.status = False
		self.alarms = []
		self.nonrecurring_alarms = []
		self.daily_alarms = []
		self.weekly_alarms = []
		self.monthly_alarms = []
		self.yearly_alarms = []
	def __str__(self):
		return('Light status: ' + str(self.status) + '\nCurrent alarms: ' + str(self.alarms) + '\n')
	def add_alarm(self, alarm_time):
		self.alarms.append(alarm_time)
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

raspi = Light()

def my_py():
	print(str(raspi))
	while True:
		print(str(time.localtime().tm_hour) + ':' + str(time.localtime().tm_min) + '\n')
		try:
			user_input = str(input('What would you like to work with?\n')).lower()
			if 'light' in user_input:
				lighting(user_input)
			elif ('alarm' in user_input) and ('help' in user_input):
				print('I can set an alarm for you, please include:\n\tTime (Include AM/PM)\n\tDate (I will assume you mean the soonest possible date)\n\tHow often you want the alarm to go off (I will assume only once)')
			if 'help' in user_input:
				print('I can turn the light on or off and I can set an alarm for you.  If you need help with one of those, please let me know')
'''			elif ('alarm' in user_input):
				user_input = str(input('Would you like to set an alarm or delete the existing alarms?')).lower()
				alarm_input = str(input('Okay, we\'ll make an alarm.  What date would you like the alarm?')).lower()
				alarm_year = time.localtime().tm_year
				alarm_month = int(alarm_input[:alarm_input.index('/')])
				alarm_day = int(alarm_input[alarm_input.index('/')+1:])
				alarm_input = str(input('Great, what time would you like the alarm? Please include AM/PM')).lower()
				alarm_hour = int(alarm_input[:alarm_input.index(':')])
				alarm_minute = int(alarm_input[alarm_input.index(':')+1:])
				alarm_second = 0
				alarm_weekday = 0
				alarm_yearday = 0
				alarm_dst = time.localtime().tm_isdst
				alarm_tuple = (alarm_year,alarm_month,alarm_day,alarm_hour,alarm_minute,alarm_second,alarm_weekday,alarm_yearday,alarm_dst)
				raspi.add_alarm(time.mktime(alarm_tuple))
			if (('clear' or 'delete') in user_input) and ('alarm' in user_input):
				raspi.clear_alarms()
				print('All alarms cleared')'''
			elif 'stop' in user_input:
				print('Stopping')
				return
			else:
				print('Unrecognized command')
		except KeyboardInterrupt:
			print('KeyboardInterrupt')
			GPIO.cleanup()

def lighting(user_input):
	if ('help' in user_input):
		print('I can turn the light on or off for you, even for a given amount of time.')
	elif ('on' in user_input):
		if 'for' in user_input:
			if 'minute' in user_input:
				int_minutes = ''
				for i in user_input:
					if user_input[i].isdigit():
						int_minutes += user_input[i]
				int_minutes = int(int_minutes)
				raspi.light_on()
				time.sleep(int_minutes * 60)
				raspi.light_off()
			elif 'hour' in user_input:
				int_hours = ''
				for i in user_input:
					if user_input[i].isdigit():
						int_hours += user_input[i]
				int_hours = int(int_hours)
				raspi.light_on()
				time.sleep(int_hours * 60 * 60)
				raspi.light_off()
			else:
				print('Please pick a number of minutes or hours to turn the light on for.')
		else:
			raspi.light_on()
	elif ('off' in user_input):
		if 'for' in user_input:
			if 'minute' in user_input:
				int_minutes = ''
				for i in user_input:
					if user_input[i].isdigit():
						int_minutes += user_input[i]
				int_minutes = int(int_minutes)
				raspi.light_off()
				time.sleep(int_minutes * 60)
				raspi.light_on()
			elif 'hour' in user_input:
				int_hours = ''
				for i in user_input:
					if user_input[i].isdigit():
						int_hours += user_input[i]
				int_hours = int(int_hours)
				raspi.light_off()
				time.sleep(int_hours * 60 * 60)
				raspi.light_on()
			else:
				print('Please pick a number of minutes or hours to turn the light off for.')
		else:
			raspi.light_off()

my_py()
