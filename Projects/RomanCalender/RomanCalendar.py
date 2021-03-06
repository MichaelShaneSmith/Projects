""" TODO:
        Handle not found classes(ex. ValueError:No JSON object could be decoded)
        Cleanse user input
        Account for multi section classes (ex. 101-0, 101-1)
        Holidays
        Reading week
"""

import os
import json
import argparse
from datetime import datetime

import prep
from icalendar import Calendar, Event
from pytz import timezone
import requests

API_KEY = os.environ['CAESAR_APIKEY']

def parse_meeting_days(week):
    dates = []

    if 'Su' in week:
        dates.append('SU')
    if 'Mo' in week:
        dates.append('MO')
    if 'Tu' in week:
        dates.append('TU')
    if 'We' in week:
        dates.append('WE')
    if 'Th' in week:
        dates.append('TH')
    if 'Fr' in week:
        dates.append('FR')
    if 'Sa' in week:
        dates.append('SA')
    print dates
    return dates

def display(cal):
    print cal.to_ical().replace('\r\n', '\n').strip()

def make_event(course):
    day_dict = {'SU' : [2016, 9, 18],
                'MO' : [2016, 9, 19],
                'TU' : [2016, 9, 20],
                'WE' : [2016, 9, 21],
                'TH' : [2016, 9, 22],
                'FR' : [2016, 9, 23],
                'SA' : [2016, 9, 24]}

    end_of_classes = datetime(2016, 11, 27, 0, 0, 0)

    start = map(int, course['start_time'].split(':'))
    end = map(int, course['end_time'].split(':'))

    dates = parse_meeting_days(course['meeting_days'])
    date = day_dict[dates[0]]

    tz = timezone('US/Central')

    event = Event()
    event.add('summary', course['title'])
    event.add('dtstart', tz.localize(datetime(date[0], date[1], date[2], start[0], start[1], 00)))
    event.add('dtend', tz.localize(datetime(date[0], date[1], date[2], end[0], end[1], 00)))

    event.add('rrule', {'FREQ':'WEEKLY', 'UNTIL': end_of_classes, 'WKST':'SU', 'BYDAY': dates})

    return event

def main(department_code, class_number, mycal, to_file=False):
    params = {
        'key': API_KEY,
        'term': '4640',
        'subject': department_code,
        'catalog_num': '{}'.format(class_number)
    }

    response = requests.get('http://api.asg.northwestern.edu/courses/details/', params=params)
    text = response.text
    print response.text
    course_dict = json.loads(text[1:len(text)-1])

    event = make_event(course_dict)

    mycal.add_component(event)

    if to_file:
        with open('schedule.ics', 'w') as file:
            file.write(mycal.to_ical())

    display(mycal)
    return mycal

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='The inputs')
    parser.add_argument('department_code', type=str, help='(ex. EECS, AFAM, MATH)')
    parser.add_argument('class_number', type=str, help='(ex. 101-0, 201-1)')
    parser.add_argument('-t', '--to_file', action='store_true')
    args = parser.parse_args()

    cal = Calendar()
    main(args.department_code.upper(), args.class_number, cal, args.to_file)