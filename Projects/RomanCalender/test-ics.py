"""
{"id": 144513, 
"title": "An Introduction to Computer Science for Everyone", 
"term": "2016 Fall", 
"instructor": "Jason D Hartline", 
"subject": "EECS", 
"catalog_num": "101-0", 
"section": "20", 
"room": "Annenberg Hall G15", 
"meeting_days": "MoWeFr", 
"start_time": "11:00", 
"end_time": "11:50", 
"seats": 102, 
"topic": null, 
"component": "LEC", 
"class_num": 16794, 
"course_id": 8093
"""

import arrow
import dateutil

from ics import Calendar, Event

def makeCalender(Name, Start_time, End_time, Date):
	"""Creates a .ics file based on the inputs"""
	c = Calendar()
	e = Event()

	tz = 'US/Central'
	DATETIMEFORMAT = 'YYYY-MM-DD HH:mm:ss'
	
	e.name = Name
	e.begin = arrow.get('{} {}'.format(Date, Start_time), DATETIMEFORMAT).replace(tzinfo=dateutil.tz.gettz(tz))
	e.end = arrow.get('{} {}'.format(Date, End_time), DATETIMEFORMAT).replace(tzinfo=dateutil.tz.gettz(tz))
	c.events.append(e)

	print c.events

	with open('my_schedule.ics', 'w') as f:
		f.writelines(c)

makeCalender('My cool event', '13:00:00', '13:50:00', '2016-09-09')
