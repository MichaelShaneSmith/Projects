import pytz
import tempfile
import arrow
import os
import dateutil


from icalendar import Calendar, Event
from datetime import datetime
from pytz import timezone


def display(cal):
    print cal.to_ical().replace('\r\n', '\n').strip()


def makeCalender(Name, Start_time, End_time, Date):
	cal = Calendar()
	cal['summary'] = 'Python Calendaring'

	tz = timezone('US/Eastern')

	event = Event()
	event.add('summary', 'Python meeting about calendaring')
	event.add('dtstart', datetime(tz.localize(datetime(2016, 9, 30, 1, 0, 0))))
	event.add('dtend', datetime(tz.localize(datetime(2016, 9, 30, 1, 50, 0))))

	cal.add_component(event)

	with open('example.ics', 'w') as f:
		f.write(cal.to_ical())

	display(cal)

makeCalender('', '13:00:00', '13:50:00', '2016-09-30')