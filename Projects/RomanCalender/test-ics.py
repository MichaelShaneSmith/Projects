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
