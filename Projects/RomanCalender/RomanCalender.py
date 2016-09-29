""" TODO: 
		Handle not found classes
		Cleanse user input
"""

import requests
import arrow
import dateutil
import json
import ast

from ics import Calendar, Event  

def parseMeetingDays(week):
	dates = []

	if 'Su' in week:
		dates.append('2016-09-18')
	if 'Mo' in week:
		dates.append('2016-09-19')
	if 'Tu' in week:
		dates.append('2016-09-20')
	if 'We' in week:
		dates.append('2016-09-21')
	if 'Th' in week:
		dates.append('2016-09-22')
	if 'Fr' in week:
		dates.append('2016-09-23')
	if 'Sa' in week:
		dates.append('2016-09-24')

	return dates

def makeCalender(Course):
	"""Creates a .ics file based on the inputs"""
	c = Calendar()

	tz = 'US/Central'
	DATETIMEFORMAT = 'YYYY-MM-DD HH:mm:ss'

	date_lst = parseMeetingDays(Course['meeting_days'])

	for ii in range(len(date_lst)):
		e = Event()
		e.name = Course['title']
		e.begin = arrow.get('{} {}:00'.format(date_lst[ii], Course['start_time']), DATETIMEFORMAT).replace(tzinfo=dateutil.tz.gettz(tz))

		e.end = arrow.get('{} {}:00'.format(date_lst[ii], Course['end_time']), DATETIMEFORMAT).replace(tzinfo=dateutil.tz.gettz(tz))

		c.events.append(e)
		print c.events

	with open('my_schedule.ics', 'w') as f:
		f.writelines(c)

def main():

	subject = raw_input('Enter the Department Code. (ex. EECS, AFAM, MATH): ')
	number = raw_input('Enter Class Number. (ex. 101-0, 201-1):' )
	print '\n'

	params = {
	  'key': '<apikey>',
	  'term': '4640',

	  # 'subject': 'EECS',
	  # 'catalog_num': '101-0'
	  'subject': subject,
	  'catalog_num': number
	}

	response = requests.get('http://api.asg.northwestern.edu/courses/details/', params=params)
	text = response.text
	print response.text
	course_dict = json.loads(text[1:len(text)-1])
	print course_dict['meeting_days']

	makeCalender(course_dict)

if __name__ == '__main__':
	main()


#makeCalender('My cool event', '13:00:00', '13:50:00', '2016-09-09')














